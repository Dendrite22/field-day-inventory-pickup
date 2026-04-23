# Field Day — Module Authoring Guide

This guide is for any contributor (human or AI) adding a new **inspection module** to Field Day. Field Day is a pnpm monorepo where the backend, the API contract, the typed React client, and the mobile-first PWA frontend all live together. New work belongs inside a module so it can grow without entangling other modules.

If you read only one section, read **"Create a new module — checklist"** at the bottom.

---

## 1. Repo layout

```
artifacts/
  api-server/      Express API (TypeScript, esbuild bundle, runs on $PORT)
  field-day/       React + Vite PWA (mobile-first, IndexedDB offline, Leaflet map)
  mockup-sandbox/  Isolated component preview server (design only, ignore for modules)

lib/
  api-spec/        Single source of truth: openapi.yaml + orval codegen config
  api-client-react/ GENERATED React Query hooks + types (do not hand-edit src/generated)
  api-zod/         GENERATED zod schemas (do not hand-edit src/generated)
  db/              Drizzle schema, db client, table exports
```

The frontend talks to the backend at `/api`. The dev server proxies it. Each artifact runs as its own workflow on its own `$PORT`.

---

## 2. The module pattern

A module is a *vertical slice* of the product: backend routes + DB tables + frontend pages + offline cache + UI components. There are two registration points (one backend, one frontend) and they use **slightly different paths** — this is the single most common source of bugs.

### 2.1 Backend module mount point

Every module router lives at:

```
artifacts/api-server/src/modules/<slug>/index.ts
```

…and is mounted in:

```
artifacts/api-server/src/modules/index.ts
```

Example:

```ts
// artifacts/api-server/src/modules/index.ts
router.use("/modules/<slug>", myModule);
```

So backend URLs end up at **`/api/modules/<slug>/...`** (note: plural `modules`).

Inside the module's `index.ts`, sub-routers are composed:

```ts
// artifacts/api-server/src/modules/<slug>/index.ts
import { Router, type IRouter } from "express";
import buildings from "./routes/buildings";
import components from "./routes/components";

const router: IRouter = Router();
router.use(buildings);
router.use(components);
export default router;
```

### 2.2 Frontend module mount point

Every module's UI lives at:

```
artifacts/field-day/src/modules/<slug>/
  ModulePage.tsx       // entry component (renders a wouter <Switch>)
  index.ts             // re-exports ModulePage
  pages/               // route components
  components/          // module-only components
  lib/constants.ts     // export const MODULE_BASE = "/module/<slug>";
  offline/             // optional: IndexedDB cache + sync queue
  services/            // optional: client-side business logic
```

Register the page in:

```ts
// artifacts/field-day/src/modules/registry.ts
export const moduleRegistry = {
  "<slug>": MyModulePage,
  // ...
};
```

So frontend URLs are **`/module/<slug>/...`** (note: **singular** `module`). The asymmetry is intentional but easy to mix up — always import `MODULE_BASE` from the module's `lib/constants.ts` instead of hard-coding paths.

### 2.3 Job-type seeding

A module isn't visible to users until a row exists in the `job_types` table pointing at the module key. Add an entry in:

```
artifacts/api-server/src/lib/seed.ts  → SEED_JOB_TYPES
```

with `slug` matching the URL slug and `moduleKey` matching the registry key.

---

## 3. The API contract (OpenAPI → codegen → hooks)

Field Day is **OpenAPI-first**. The flow is:

1. Edit `lib/api-spec/openapi.yaml` (paths + schemas).
2. Run `pnpm --filter @workspace/api-spec run codegen`.
3. orval regenerates:
   - `lib/api-client-react/src/generated/api.ts` — typed fetch fns + `useFooBar` React Query hooks.
   - `lib/api-client-react/src/generated/api.schemas.ts` — TypeScript types.
   - `lib/api-zod/src/generated/...` — zod runtime validators.
4. Use the generated hooks on the frontend: `import { useAmListBuildings } from "@workspace/api-client-react"`.

**Do not hand-write fetch calls** on the frontend, and do not edit anything under `src/generated`. If a hook is missing, the spec is missing it.

### Conventions for new operations

- `operationId`: camelCase, prefixed with the module's tag (e.g. `amListBuildings`, `amCreateCostLibrary`). The prefix becomes the React hook name.
- `tags`: one tag per module (e.g. `amBuildings`). Add to the top-level `tags:` list.
- Schemas: `PascalCase`. Module-scoped types are prefixed (e.g. `AmCostLibraryRow`, `AmCostLibraryInput`).
- Use `$ref: "#/components/responses/Error"` for `401`, `403`, `404`, `409`, `400` responses where appropriate.
- Always declare the role-gating in the summary so it's discoverable: `summary: Create a cost library entry (admin/reviewer)`.

---

## 4. Auth & roles

- **Cookie sessions, not bearer tokens.** Login is `POST /api/auth/login {email, password}` and sets an httpOnly cookie. Whoami is `GET /api/auth/me`.
- Roles are: `admin`, `reviewer`, `user` (a.k.a. inspector).
- Middleware (in `artifacts/api-server/src/lib/auth.ts`):
  - `requireAuth` — any signed-in user.
  - `requireAdmin` — admin only.
  - `requireRole(["admin","reviewer"], async (userId) => {...})` — flexible role gate; the second arg is an optional resolver if the role check needs DB lookups.
- Default for reads: `requireAuth`. Default for writes that touch shared/admin data: `requireRole(["admin","reviewer"], ...)`.
- On the frontend, gate UI with `useGetCurrentUser()` and an `ADMIN_ROLES = new Set(["admin","reviewer"])` check. **Always render a friendly "Restricted" fallback inside the page** so a direct URL hit doesn't 404 silently.

Demo accounts (seeded):

- `admin@test.com` / `admin123`
- `inspector@test.com` / `inspector123`

---

## 5. Database (Drizzle)

- Schema lives in `lib/db/src/schema/...`. Tables are exported from `lib/db/src/index.ts`.
- **Never change a primary key column type.** If it's `serial` keep it `serial`; if it's `varchar`/UUID keep it that way. Migrations are auto-applied.
- New module tables: prefix with the module name when there's any chance of collision (e.g. `am_buildings`, `am_components`, `am_cost_library`).
- For optimistic concurrency, add an integer `version` column with default `1`. Bump it on every write.

---

## 6. Optimistic concurrency (for any multi-writer resource)

The buildings module is the reference implementation. Pattern:

- `PATCH /resource/:id` body **must include `version`** (the value the client read).
- Server compares `existing.version !== body.version` → returns `409` with `{ error: "Version conflict", currentVersion: <n> }`.
- On success, server updates with `where(eq(table.id, id), eq(table.version, body.version))`, sets `version = existing.version + 1`, returns the new row.
- The frontend handles 409 by re-fetching the current row, surfacing a conflict resolver, and retrying with the fresh `version`.

If your resource will ever be edited by two people, use this pattern.

---

## 7. Validation style

`api-server` does **not** depend on `zod`. Keep handlers self-contained with a small `parseInput()` function (see `routes/costLibrary.ts` for the canonical example). It returns a discriminated union:

```ts
type InputResult = { ok: true; value: T } | { ok: false; error: string };
```

If you genuinely need zod, add it to `artifacts/api-server/package.json` deliberately — don't import from `@workspace/api-zod` in handlers (those are for the codegen path).

---

## 8. Frontend conventions (mobile-first)

Field Day is a **PWA installed on phones in the field**. Treat 375 × 812 as your primary canvas.

- **Tap targets ≥ 44px.** Use `h-11` (44px) for buttons. Avoid the shadcn `size="sm"` for any interactive control.
- **Form layouts:** `grid-cols-1 sm:grid-cols-2 gap-3`. Single-column on mobile, two-column from `sm:` up. Read-only summary cards can stay 2-col.
- **No horizontal scroll** at 375px. Use `min-w-0`, `truncate`, `flex-wrap` liberally.
- **Every interactive element gets a `data-testid`.** Tests rely on these.
- **Toasts** for all user feedback: `import { useToast } from "@/hooks/use-toast"`.
- **Routing:** `wouter`. Inside a module, always use `MODULE_BASE` from `lib/constants.ts`.
- **Dark mode:** components from `@/components/ui` already handle it; avoid hard-coded colors.

### Offline-capable queries

Modules that must work offline wrap their `useFooBar` hook in `useCachedQuery` and provide IndexedDB read/write helpers (see `am-data-collection-buildings/offline/`). New modules can opt out — it's not free.

### Autofill / vocabulary

Free-text fields use the `AutofillInput` component, backed by an HTML `<datalist>` populated from a `/vocabulary` endpoint (frequency-ranked, building-scoped first then portfolio). Note: `<datalist>` options are real DOM but native browser UI shows them — Playwright tests need to read options via `page.evaluate`, not look for an ARIA listbox.

---

## 9. Workflows & ports

- Every artifact runs as its own workflow defined by `artifact.toml`. **Never edit `artifact.toml` directly** — use the artifact tooling.
- Each artifact binds to `$PORT` (assigned per artifact). Hard-coding `3000` etc. will collide.
- Restart a workflow after backend code changes: the api-server uses `build && start`, not watch mode.

---

## 10. Testing

- After any feature, run an end-to-end test via the testing tooling. Tests run against the **same dev database** as you — generate unique values (nanoid) for emails/titles to avoid collisions.
- Don't assert exact row counts; the DB is dirty.
- For role-gated routes, always add a test for `inspector → 403` in addition to the happy path.

---

## 11. Create a new module — checklist

> Replace `<slug>` with kebab-case, e.g. `pavement-survey`. Replace `<Pfx>` with the OpenAPI tag prefix, e.g. `pv` (for `pvListInspections`).

### Backend

- [ ] `mkdir artifacts/api-server/src/modules/<slug>/{routes,services}`
- [ ] Create `routes/<resource>.ts` exporting an Express `Router`.
- [ ] Create `index.ts` that composes those sub-routers.
- [ ] Mount in `artifacts/api-server/src/modules/index.ts`: `router.use("/modules/<slug>", myModule);`
- [ ] Add tables in `lib/db/src/schema/<slug>.ts` and export from `lib/db/src/index.ts`. Include a `version` column if multi-writer.
- [ ] Gate writes with `requireRole(["admin","reviewer"], ...)`; reads with `requireAuth`.
- [ ] Use a hand-rolled `parseInput()` for body validation.
- [ ] Add a row to `SEED_JOB_TYPES` in `artifacts/api-server/src/lib/seed.ts`.

### API contract

- [ ] Add operations + schemas to `lib/api-spec/openapi.yaml`. Tag them under a new module-specific tag (`<Pfx>...`).
- [ ] Run `pnpm --filter @workspace/api-spec run codegen`.
- [ ] Confirm hooks appear in `lib/api-client-react/src/generated/api.ts`.

### Frontend

- [ ] `mkdir artifacts/field-day/src/modules/<slug>/{pages,components,lib}`
- [ ] `lib/constants.ts`: `export const MODULE_BASE = "/module/<slug>";`
- [ ] `ModulePage.tsx`: a wouter `<Switch>` listing the module's routes. Export it from `index.ts`.
- [ ] Register in `artifacts/field-day/src/modules/registry.ts`.
- [ ] Build pages using generated hooks from `@workspace/api-client-react`.
- [ ] Gate admin-only pages with `useGetCurrentUser()` + a `Restricted` fallback inside the page.
- [ ] Use `h-11` tap targets, `grid-cols-1 sm:grid-cols-2`, `data-testid` everywhere.
- [ ] If multi-writer, handle the 409 retry path.
- [ ] If offline-required, wrap reads in `useCachedQuery` and writes through the sync queue.

### Verify

- [ ] Restart the api-server workflow (`build && start`).
- [ ] curl the new endpoints as admin (expect 200/201) and as inspector (expect 403 on writes if gated).
- [ ] Run an end-to-end test covering: visible to allowed role, hidden/restricted for others, primary CRUD path, mobile viewport (375×812) with no horizontal scroll.

---

## 12. Common pitfalls (read this twice)

1. **Path asymmetry.** Backend mount is `/api/modules/<slug>/...` (plural). Frontend route is `/module/<slug>/...` (singular). Always use `MODULE_BASE` on the frontend.
2. **Forgetting codegen.** Editing `openapi.yaml` without running codegen → frontend hooks are stale → silent type drift.
3. **Hand-writing fetch.** Skipping the generated hook means you also skip `customFetch` (which handles cookies, base path, error shape). Always use the generated hook.
4. **Hard-coding port.** Read `$PORT`. Never `3000`.
5. **`size="sm"` on interactive controls.** Falls below the 44px tap target.
6. **`grid-cols-2` without an `sm:` prefix.** Cramps inputs at 375px.
7. **No `Restricted` fallback in admin pages.** Direct URL navigation 404s instead of explaining.
8. **Bearer tokens in auth tests.** Login is cookie-based; use a cookie jar.
9. **Running api-server tests against the wrong port.** It listens on `$PORT` (typically not 3000/5000) — check the workflow logs.
10. **Changing primary-key column types.** Will destroy data on next push. Don't do it.

---

## 13. Where to look for a reference implementation

The `am-data-collection-buildings` module exercises every pattern in this guide:

- Backend: `artifacts/api-server/src/modules/am-data-collection-buildings/`
- Frontend: `artifacts/field-day/src/modules/am-data-collection-buildings/`
- Spec: search `lib/api-spec/openapi.yaml` for `amBuildings` tag.
- Optimistic concurrency: `routes/components.ts`.
- Role-gated CRUD: `routes/costLibrary.ts` + frontend `pages/CostLibraryAdminPage.tsx`.
- Offline cache: `offline/db.ts`, `offline/useCachedQuery.ts`, `offline/sync.ts`.
- Autofill: `components/AutofillInput.tsx` + backend `routes/vocabulary.ts`.

When in doubt, copy from there and adapt.
