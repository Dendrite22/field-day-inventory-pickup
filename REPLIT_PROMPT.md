You are working inside the **Field Day** pnpm monorepo. I need you to implement a new module called **Data Collection: P&E** following the exact same conventions as the existing `am-data-collection-buildings` module, which is your reference for every pattern used below.

---

**MODULE IDENTITY**

- Slug: `am-data-collection-pe`
- Module key: `amDataCollectionPe`
- OpenAPI tag prefix: `pe`
- Frontend base route: `/module/am-data-collection-pe` (singular "module")
- Backend mount: `/api/modules/am-data-collection-pe` (plural "modules")
- DB table prefix: `pe_`
- Job type label: `"Data Collection: P&E"`

The frontend/backend path asymmetry (singular vs plural) is intentional. Never hard-code either path — always import `MODULE_BASE` from the module's `lib/constants.ts`.

---

**PURPOSE**

This module is a mobile-first site inspection tool for capturing a Plant & Equipment (Contents) inventory. The output is an insurance and financial reporting valuation of loose-contents assets — furniture, IT equipment, AV, appliances, and office equipment. Each item captures physical attributes, condition, two photos, and replacement cost / indemnity valuation. This module does NOT record defects, works costs, repair priorities, or works photos. GPS coordinates belong to the parent building record (`am_buildings`) only — individual items do not carry GPS.

---

**STEP 1 — REGISTRATION**

Add to `SEED_JOB_TYPES` in `artifacts/api-server/src/lib/seed.ts`:
```ts
{
  slug: "am-data-collection-pe",
  label: "Data Collection: P&E",
  moduleKey: "amDataCollectionPe",
  description: "Plant & Equipment contents inventory for insurance and financial reporting valuation.",
}
```

Add to `artifacts/api-server/src/modules/index.ts`:
```ts
import peDataCollection from "./am-data-collection-pe";
router.use("/modules/am-data-collection-pe", peDataCollection);
```

Add to `artifacts/field-day/src/modules/registry.ts`:
```ts
import AmDataCollectionPePage from "./am-data-collection-pe";
// add to moduleRegistry:
amDataCollectionPe: AmDataCollectionPePage,
```

---

**STEP 2 — DATABASE TABLE**

Create `lib/db/src/schema/am-data-collection-pe.ts` and export `peItems` from `lib/db/src/index.ts`.

```ts
import { pgTable, serial, integer, varchar, text, numeric, timestamp } from "drizzle-orm/pg-core";
import { amBuildings } from "./am-data-collection-buildings";
import { users } from "./auth";

export const peItems = pgTable("pe_items", {
  id:              serial("id").primaryKey(),
  version:         integer("version").default(1).notNull(),

  uniqueId:        varchar("unique_id", { length: 20 }).notNull(),
  assetIdClient:   varchar("asset_id_client", { length: 50 }),
  buildingId:      integer("building_id").notNull().references(() => amBuildings.id),

  level:           varchar("level", { length: 100 }),
  subLocation:     varchar("sub_location", { length: 200 }),

  categoryL1:      varchar("category_l1", { length: 100 }).notNull(),
  categoryL2:      varchar("category_l2", { length: 100 }),
  categoryL3:      varchar("category_l3", { length: 100 }),
  categoryL4:      varchar("category_l4", { length: 100 }),

  itemDescription: text("item_description"),
  make:            varchar("make", { length: 100 }),
  model:           varchar("model", { length: 100 }),
  serialNumber:    varchar("serial_number", { length: 200 }),
  assetTag:        varchar("asset_tag", { length: 100 }),
  colourFinish:    varchar("colour_finish", { length: 100 }),

  quantity:        integer("quantity").notNull().default(1),
  uom:             varchar("uom", { length: 10 }).notNull().default("ea"),

  widthMm:         integer("width_mm"),
  depthMm:         integer("depth_mm"),
  heightMm:        integer("height_mm"),
  screenSizeIn:    numeric("screen_size_in", { precision: 5, scale: 1 }),
  weightKg:        numeric("weight_kg", { precision: 8, scale: 2 }),

  conditionRating: integer("condition_rating").notNull(),
  conditionLabel:  varchar("condition_label", { length: 30 }).notNull(),

  photo1Url:       text("photo1_url"),
  photo2Url:       text("photo2_url"),

  commentsRecs:    text("comments_recs"),

  unitRateRcn:        numeric("unit_rate_rcn", { precision: 12, scale: 2 }),
  estReplacementCost: numeric("est_replacement_cost", { precision: 12, scale: 2 }),
  remainingUsefulLifePct: integer("remaining_useful_life_pct"),
  indemnityValue:     numeric("indemnity_value", { precision: 12, scale: 2 }),
  effectiveLifeYears: integer("effective_life_years"),
  insuranceCategory:  varchar("insurance_category", { length: 30 }).default("Contents"),

  inspectedBy: integer("inspected_by").references(() => users.id),
  createdAt:   timestamp("created_at").defaultNow().notNull(),
  updatedAt:   timestamp("updated_at").defaultNow().notNull(),
});
```

No GPS columns on `pe_items`. GPS comes from `am_buildings`.

---

**STEP 3 — BACKEND FILES**

Create this folder structure:
```
artifacts/api-server/src/modules/am-data-collection-pe/
  index.ts
  routes/buildings.ts
  routes/items.ts
  routes/vocabulary.ts
  routes/export.ts
  services/valuation.ts
  services/uniqueId.ts
```

**`services/valuation.ts`** — condition rating to RUL, ERC, and indemnity derivation:
```ts
const RUL_MAP: Record<number, number | null> = { 0: null, 1: 100, 2: 75, 3: 50, 4: 25, 5: 0 };

export function deriveRul(conditionRating: number): number | null {
  return RUL_MAP[conditionRating] ?? null;
}
export function deriveErc(unitRateRcn: number, quantity: number): number {
  return unitRateRcn * quantity;
}
export function deriveIndemnity(erc: number, rulPct: number | null): number {
  if (rulPct === null) return 0;
  return erc * (rulPct / 100);
}
export function deriveConditionLabel(rating: number): string {
  const map: Record<number, string> = { 0: "Not Present", 1: "As New", 2: "Good", 3: "Fair", 4: "Poor", 5: "Very Poor" };
  return map[rating] ?? "";
}
```

**`services/uniqueId.ts`** — auto-incrementing unique ID starting at 100001 across the portfolio:
```ts
import { db } from "@workspace/db";
import { peItems } from "@workspace/db";
import { sql } from "drizzle-orm";

export async function nextUniqueId(): Promise<string> {
  const result = await db.select({ maxId: sql<string>`max(unique_id::bigint)` }).from(peItems);
  const max = result[0]?.maxId ? parseInt(result[0].maxId, 10) : 100000;
  return String(max + 1);
}
```

**`routes/items.ts`** — full CRUD. All writes require `requireAuth`. DELETE requires `requireRole(["admin","reviewer"])`. PATCH uses optimistic concurrency: body must include `version`; if `existing.version !== body.version` return 409 with `{ error: "Version conflict", currentVersion: existing.version }`. On every write, server derives and stores `conditionLabel`, `remainingUsefulLifePct`, `estReplacementCost`, and `indemnityValue` — never trust the client to send these.

**`routes/buildings.ts`** — GET `/buildings` returns the list of buildings from `am_buildings` scoped to this module's job type.

**`routes/vocabulary.ts`** — GET `/buildings/:buildingId/vocabulary?field=<fieldName>` returns frequency-ranked distinct values for `level`, `subLocation`, `make`, `colourFinish`, or `model` from existing `pe_items` for that building.

**`routes/export.ts`** — GET `/buildings/:buildingId/export?format=csv` returns a CSV of all items. Requires `requireRole(["admin","reviewer"])`.

**`index.ts`** composes all four routers.

Use a hand-rolled `parseInput()` function for body validation (no zod in api-server). Follow the pattern in `am-data-collection-buildings/routes/costLibrary.ts`.

---

**STEP 4 — OPENAPI SPEC**

Add four tags to the top-level `tags:` list in `lib/api-spec/openapi.yaml`: `peItems`, `peBuildings`, `peVocabulary`, `peExport`.

Add schemas `PeItemBase`, `PeItem`, and `PeItemInput` to `components/schemas`. `PeItemBase` contains all writable fields. `PeItem` extends it with `id`, `version`, `uniqueId`, `buildingId`, `conditionLabel`, `remainingUsefulLifePct`, `estReplacementCost`, `indemnityValue`, `createdAt`, `updatedAt`. Required fields on input: `categoryL1`, `conditionRating`, `quantity`, `uom`.

Add these paths:
- `GET /modules/am-data-collection-pe/buildings` → `peListBuildings`
- `GET /modules/am-data-collection-pe/buildings/{buildingId}/items` → `peListItems`
- `POST /modules/am-data-collection-pe/buildings/{buildingId}/items` → `peCreateItem`
- `GET /modules/am-data-collection-pe/items/{id}` → `peGetItem`
- `PATCH /modules/am-data-collection-pe/items/{id}` → `peUpdateItem` (body includes `version`)
- `DELETE /modules/am-data-collection-pe/items/{id}` → `peDeleteItem`
- `GET /modules/am-data-collection-pe/buildings/{buildingId}/vocabulary` → `peGetVocabulary`
- `GET /modules/am-data-collection-pe/buildings/{buildingId}/export` → `peExportBuilding`

Then run: `pnpm --filter @workspace/api-spec run codegen`

Confirm these hooks exist in `lib/api-client-react/src/generated/api.ts`: `usePeListItems`, `usePeCreateItem`, `usePeUpdateItem`, `usePeDeleteItem`, `usePeGetVocabulary`, `usePeExportBuilding`.

---

**STEP 5 — FRONTEND**

Create this folder structure:
```
artifacts/field-day/src/modules/am-data-collection-pe/
  index.ts
  ModulePage.tsx
  lib/constants.ts
  lib/categoryLibrary.ts
  lib/dimensionRules.ts
  pages/BuildingSelectPage.tsx
  pages/LocationDrillPage.tsx
  pages/ItemListPage.tsx
  pages/ItemFormPage.tsx
  pages/SummaryPage.tsx
  pages/ExportPage.tsx
  components/ConditionBadge.tsx
  components/ValuationCard.tsx
  components/DimensionFields.tsx
  components/PhotoCapture.tsx
  components/CategoryDrilldown.tsx
```

**`lib/constants.ts`:**
```ts
export const MODULE_BASE = "/module/am-data-collection-pe";
export const MODULE_KEY  = "amDataCollectionPe";
```

**`ModulePage.tsx`** — wouter `<Switch>` with these routes:
- `MODULE_BASE` → `BuildingSelectPage`
- `MODULE_BASE/buildings/:buildingId` → `LocationDrillPage`
- `MODULE_BASE/buildings/:buildingId/items` → `ItemListPage`
- `MODULE_BASE/buildings/:buildingId/items/new` → `ItemFormPage`
- `MODULE_BASE/buildings/:buildingId/items/:itemId/edit` → `ItemFormPage`
- `MODULE_BASE/buildings/:buildingId/summary` → `SummaryPage`
- `MODULE_BASE/buildings/:buildingId/export` → `ExportPage`

**`lib/dimensionRules.ts`** — controls which dimension inputs render based on category:
```ts
export function getDimensionRules(l1: string, l2: string) {
  const full    = { width: true,  depth: true,  height: true,  screenSize: false, weight: false };
  const screens = { width: false, depth: false, height: false, screenSize: true,  weight: false };
  const heavy   = { width: true,  depth: true,  height: true,  screenSize: false, weight: true  };
  const none    = { width: false, depth: false, height: false, screenSize: false, weight: false };

  if (l1 === "Information Technology") return l2 === "Display & Peripherals" ? screens : full;
  if (l1 === "Audio Visual") return (l2 === "Display Systems" || l2 === "Projection") ? screens : full;
  if (l1 === "Vehicles & Motorised Plant" || l1 === "Fitness & Recreation") return heavy;
  if (l1 === "Other / Miscellaneous") return none;
  return full;
}
```

**`lib/categoryLibrary.ts`** — the full L1→L2→L3→L4 category tree is already defined in `schema.json` at the repo root. Import it and expose `getL2Options(l1)`, `getL3Options(l1, l2)`, `getL4Options(l1, l2, l3)` helper functions.

---

**STEP 6 — PAGE BEHAVIOUR**

**BuildingSelectPage:** Calls `usePeListBuildings()`. Shows buildings as tappable cards with name, address, and a Leaflet map thumbnail using the building's GPS coordinates from `am_buildings`. GPS is on the building record only — items have no GPS. Tapping navigates to the location drill page. Mobile: full-width cards, `h-11` tap targets, search bar.

**LocationDrillPage:** Shows building name as breadcrumb. Tile grid for Level selection (distinct values from existing items, plus "Add new level"). Tapping a level shows Sub Location tiles the same way. A floating "+ New Item" FAB is always visible and opens the item form pre-filled with the selected level and sub location.

**ItemListPage:** Calls `usePeListItems({ buildingId })`. Groups items by Level → Sub Location → L1 category using collapsible sections. Each row shows the L3 item type, Qty × UoM, and a colour-coded condition badge: As New=green, Good=teal, Fair=amber, Poor=orange, Very Poor=red, Not Present=grey. Right-arrow opens the edit form.

**ItemFormPage** — the main data entry form, used for both create and edit. Sections in order:

1. **Location** — Level and Sub Location, both using `<AutofillInput>` backed by the vocabulary endpoint.
2. **Category** — `<CategoryDrilldown>` with cascading selects: L1 → L2 → L3 → L4. L1 is required. Selecting L1 clears L2/L3/L4. Selecting L2 clears L3/L4. L4 only shows when that L3 has variants other than "--".
3. **Item Details** — Item Description (free text), Make (autofill), Model, Serial Number, Asset Tag, Colour / Finish (autofill).
4. **Quantity & Unit** — Quantity (integer, min 1), UoM select: `ea / set / pair / lot`.
5. **Dimensions** — `<DimensionFields>` renders only the inputs relevant to the selected L1/L2 per `dimensionRules.ts`. Furniture shows Width, Depth, Height. AV displays show Screen Size only. Vehicles/Fitness shows all plus Weight.
6. **Condition** — Six tile buttons labelled 0–5 (Not Present through Very Poor). Required — form cannot submit without a selection. Rating 0 disables valuation fields.
7. **Photos** — `<PhotoCapture>` with exactly two slots: Photo 1 (primary) and Photo 2 (secondary detail). Both are always visible regardless of any other field state. There are no works photos in this module.
8. **Comments / Recommendations** — optional text area.
9. **Valuation** — Unit Rate (editable, manual override allowed), then read-only display of Estimated Replacement Cost (Unit Rate × Qty), Remaining Useful Life % (derived from condition rating: 1=100%, 2=75%, 3=50%, 4=25%, 5=0%, 0=N/A), and Indemnity Value (ERC × RUL%). Also: Insurance Category select (Contents / Plant & Equipment / Motor Vehicle / Other) and Effective Life in years (optional).

On save: POST for new items, PATCH with `version` for edits. Handle 409 conflict by re-fetching and showing a conflict toast. On success: toast "Item saved" and return to ItemListPage.

**SummaryPage:** Client-side aggregation of `usePeListItems`. Table grouped by L1 showing item count, total quantity, total Estimated Replacement Cost, and total Indemnity Value. Footer row totals the valuation columns. Export button visible to admin/reviewer only.

**ExportPage:** Gate with `useGetCurrentUser()` + `ADMIN_ROLES = new Set(["admin","reviewer"])`. Show a `<Restricted>` fallback component for inspectors — never 404 on a direct URL. Triggers `usePeExportBuilding` CSV download on button click.

---

**STEP 7 — RULES TO FOLLOW THROUGHOUT**

- All tap targets `h-11` (44px minimum). Never use `size="sm"` on interactive controls.
- Form layouts: `grid-cols-1 sm:grid-cols-2 gap-3`. No horizontal scroll at 375px viewport width.
- Every interactive element needs a `data-testid`.
- Use `useToast` for all user feedback.
- Never hand-write fetch calls — use only the generated hooks from `@workspace/api-client-react`.
- Never edit anything under `src/generated`.
- After backend changes, restart the api-server workflow (`build && start`).
- Read `$PORT` from the environment — never hard-code a port number.
- Backend URL pattern: `/api/modules/am-data-collection-pe/...` (plural). Frontend URL pattern: `/module/am-data-collection-pe/...` (singular). Always use `MODULE_BASE` on the frontend.

---

**STEP 8 — VERIFY**

After implementation, confirm:
- Inspector can create an item (201) but cannot delete one (403).
- PATCH with a stale `version` returns 409.
- Export returns 403 for inspector, 200 CSV for admin.
- Condition rating 0 results in `estReplacementCost`, `indemnityValue`, and `remainingUsefulLifePct` all null/zero.
- Category drilldown clears child selections when a parent changes.
- Dimension fields for Furniture/Seating show Width, Depth, Height — not Screen Size.
- Dimension fields for Audio Visual/Display Systems show Screen Size only.
- Photo 1 and Photo 2 are always visible. No defect, works, or GPS fields exist anywhere.
- No horizontal scroll at 375×812 on ItemFormPage.
