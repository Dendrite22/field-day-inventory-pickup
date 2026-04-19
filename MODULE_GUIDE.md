# Field Day — Module Seed: Data Collection: P&E

## Hierarchy context

```
Field Day (parent app — pnpm monorepo)
└── Modules
    ├── am-data-collection-buildings   ← existing reference implementation
    └── am-data-collection-pe          ← THIS MODULE (new)
```

This document seeds the **Data Collection: P&E** module. It follows the conventions
established in the Field Day Module Authoring Guide verbatim. Read that guide first
if anything here is unclear — the reference implementation for every pattern is
`am-data-collection-buildings`.

**Purpose:** Mobile-first site inspection tool for capturing a Plant & Equipment
(Contents) inventory. The output is an Insurance and Financial Reporting Valuation
of loose-contents assets (furniture, IT equipment, AV, appliances, office equipment).
Each item record captures physical attributes, condition, photos, defect details,
and replacement cost / indemnity valuation.

---

## 1. Module identity

| Property | Value |
|---|---|
| Slug (kebab-case) | `am-data-collection-pe` |
| Module key (registry) | `amDataCollectionPe` |
| OpenAPI tag prefix | `pe` |
| Frontend base route | `/module/am-data-collection-pe` |
| Backend mount point | `/api/modules/am-data-collection-pe` |
| DB table prefix | `pe_` |
| Job type label | `"Data Collection: P&E"` |
| Seed entry module key | `amDataCollectionPe` |

The asymmetry between frontend (`/module/`) and backend (`/api/modules/`) is
intentional — see section 2.2 of the parent guide. Always import `MODULE_BASE`
from `lib/constants.ts`, never hard-code the path.

---

## 2. Registration checklist (fill these in first)

### 2.1 Job-type seed entry

In `artifacts/api-server/src/lib/seed.ts`, add to `SEED_JOB_TYPES`:

```ts
{
  slug: "am-data-collection-pe",
  label: "Data Collection: P&E",
  moduleKey: "amDataCollectionPe",
  description: "Plant & Equipment contents inventory for insurance and financial reporting valuation.",
}
```

### 2.2 Backend mount

In `artifacts/api-server/src/modules/index.ts`:

```ts
import peDataCollection from "./am-data-collection-pe";
router.use("/modules/am-data-collection-pe", peDataCollection);
```

### 2.3 Frontend registry

In `artifacts/field-day/src/modules/registry.ts`:

```ts
import AmDataCollectionPePage from "./am-data-collection-pe";
export const moduleRegistry = {
  // ...existing entries
  amDataCollectionPe: AmDataCollectionPePage,
};
```

---

## 3. Database schema (Drizzle)

Create `lib/db/src/schema/am-data-collection-pe.ts` and export from
`lib/db/src/index.ts`.

The module uses one primary table. It references `am_buildings` (from the existing
buildings module) for the building identity — do **not** duplicate building data.

```ts
import {
  pgTable, serial, integer, varchar, text, boolean,
  numeric, timestamp
} from "drizzle-orm/pg-core";
import { amBuildings } from "./am-data-collection-buildings";
import { users } from "./auth";

export const peItems = pgTable("pe_items", {
  // ── Primary key + optimistic concurrency ─────────────────────────────────
  id:              serial("id").primaryKey(),
  version:         integer("version").default(1).notNull(),

  // ── Portfolio identity ────────────────────────────────────────────────────
  uniqueId:        varchar("unique_id", { length: 20 }).notNull(),
  assetIdClient:   varchar("asset_id_client", { length: 50 }),
  buildingId:      integer("building_id")
                     .notNull()
                     .references(() => amBuildings.id),

  // ── Location ──────────────────────────────────────────────────────────────
  level:           varchar("level",        { length: 100 }),
  subLocation:     varchar("sub_location", { length: 200 }),

  // ── Category hierarchy (L1–L4) ────────────────────────────────────────────
  // L1 values: Furniture | Information Technology | Audio Visual |
  //            Appliances & White Goods | Office Equipment |
  //            Fitness & Recreation | Medical & First Aid |
  //            Vehicles & Motorised Plant | Other / Miscellaneous
  categoryL1:      varchar("category_l1", { length: 100 }).notNull(),
  categoryL2:      varchar("category_l2", { length: 100 }),
  categoryL3:      varchar("category_l3", { length: 100 }),
  categoryL4:      varchar("category_l4", { length: 100 }),  // "--" when n/a

  // ── Item description & identity ───────────────────────────────────────────
  itemDescription: text("item_description"),
  make:            varchar("make",          { length: 100 }),
  model:           varchar("model",         { length: 100 }),
  serialNumber:    varchar("serial_number", { length: 200 }),
  assetTag:        varchar("asset_tag",     { length: 100 }),
  colourFinish:    varchar("colour_finish", { length: 100 }),

  // ── Quantity ──────────────────────────────────────────────────────────────
  // uom values: ea | set | pair | lot
  quantity:        integer("quantity").notNull().default(1),
  uom:             varchar("uom", { length: 10 }).notNull().default("ea"),

  // ── Dimensions (context-sensitive — see §7) ───────────────────────────────
  widthMm:         integer("width_mm"),
  depthMm:         integer("depth_mm"),
  heightMm:        integer("height_mm"),
  screenSizeIn:    numeric("screen_size_in", { precision: 5, scale: 1 }),
  weightKg:        numeric("weight_kg",      { precision: 8, scale: 2 }),

  // ── Condition ─────────────────────────────────────────────────────────────
  // 0=Not Present 1=As New 2=Good 3=Fair 4=Poor 5=Very Poor — never null
  conditionRating: integer("condition_rating").notNull(),
  conditionLabel:  varchar("condition_label", { length: 30 }).notNull(),

  // ── Photos ────────────────────────────────────────────────────────────────
  photo1Url:       text("photo1_url"),
  photo2Url:       text("photo2_url"),
  worksPhoto1Url:  text("works_photo1_url"),   // only when defect = true
  worksPhoto2Url:  text("works_photo2_url"),   // only when defect = true

  // ── Defect & works ────────────────────────────────────────────────────────
  // defect_priority values: Immediate (High) | High | Moderate | Low
  commentsRecs:    text("comments_recs"),
  defect:          boolean("defect").notNull().default(false),
  worksDescription: text("works_description"),
  defectPriority:  varchar("defect_priority", { length: 30 }),
  probableRepairCost: numeric("probable_repair_cost", { precision: 10, scale: 2 }),

  // ── Valuation ─────────────────────────────────────────────────────────────
  // insurance_category values: Contents | Plant & Equipment | Motor Vehicle | Other
  yearManufactured:   integer("year_manufactured"),
  yearPurchased:      integer("year_purchased"),
  purchasePrice:      numeric("purchase_price",    { precision: 12, scale: 2 }),
  unitRateRcn:        numeric("unit_rate_rcn",      { precision: 12, scale: 2 }),
  estReplacementCost: numeric("est_replacement_cost",{ precision: 12, scale: 2 }),
  // RUL stored as integer 0–100. Derived: rating 1→100 2→75 3→50 4→25 5→0 0→null
  remainingUsefulLifePct: integer("remaining_useful_life_pct"),
  indemnityValue:     numeric("indemnity_value",    { precision: 12, scale: 2 }),
  // effective_life in years, from cost library or manual entry
  effectiveLifeYears: integer("effective_life_years"),
  insuranceCategory:  varchar("insurance_category", { length: 30 }).default("Contents"),

  // ── GPS ───────────────────────────────────────────────────────────────────
  gpsLat:   numeric("gps_lat", { precision: 10, scale: 7 }),
  gpsLng:   numeric("gps_lng", { precision: 10, scale: 7 }),

  // ── Audit ─────────────────────────────────────────────────────────────────
  inspectedBy: integer("inspected_by").references(() => users.id),
  createdAt:   timestamp("created_at").defaultNow().notNull(),
  updatedAt:   timestamp("updated_at").defaultNow().notNull(),
});
```

Export from `lib/db/src/index.ts`:

```ts
export { peItems } from "./schema/am-data-collection-pe";
```

---

## 4. Backend file layout

```
artifacts/api-server/src/modules/am-data-collection-pe/
  index.ts              ← compose sub-routers (see §2.1 of parent guide)
  routes/
    buildings.ts        ← GET /buildings (scoped list — reuse am_buildings)
    items.ts            ← CRUD on pe_items
    vocabulary.ts       ← GET /buildings/:id/vocabulary (autofill)
    export.ts           ← GET /buildings/:id/export (CSV/XLSX, admin+reviewer)
  services/
    valuation.ts        ← RUL derivation, ERC and indemnity formula helpers
    uniqueId.ts         ← portfolio-wide auto-increment from 100001
```

### index.ts

```ts
import { Router, type IRouter } from "express";
import buildings  from "./routes/buildings";
import items      from "./routes/items";
import vocabulary from "./routes/vocabulary";
import exportRoute from "./routes/export";

const router: IRouter = Router();
router.use(buildings);
router.use(items);
router.use(vocabulary);
router.use(exportRoute);
export default router;
```

### services/valuation.ts

```ts
// RUL derivation (linear scale from condition rating)
const RUL_MAP: Record<number, number | null> = {
  0: null,   // Not Present — indemnity = 0
  1: 100,
  2: 75,
  3: 50,
  4: 25,
  5: 0,
};

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
  const map: Record<number, string> = {
    0: "Not Present", 1: "As New", 2: "Good",
    3: "Fair", 4: "Poor", 5: "Very Poor",
  };
  return map[rating] ?? "";
}
```

### services/uniqueId.ts

```ts
// Returns the next unique ID across all pe_items for the portfolio.
// Starts at 100001 if no rows exist.
import { db } from "@workspace/db";
import { peItems } from "@workspace/db";
import { sql } from "drizzle-orm";

export async function nextUniqueId(): Promise<string> {
  const result = await db
    .select({ maxId: sql<string>`max(unique_id::bigint)` })
    .from(peItems);
  const max = result[0]?.maxId ? parseInt(result[0].maxId, 10) : 100000;
  return String(max + 1);
}
```

### routes/items.ts (key patterns)

```ts
import { Router } from "express";
import { requireAuth, requireRole } from "../../lib/auth";
import { db } from "@workspace/db";
import { peItems } from "@workspace/db";
import { eq, and } from "drizzle-orm";
import { deriveRul, deriveErc, deriveIndemnity, deriveConditionLabel } from "../services/valuation";
import { nextUniqueId } from "../services/uniqueId";

const router = Router();

// ── List items for a building ─────────────────────────────────────────────────
router.get("/buildings/:buildingId/items", requireAuth, async (req, res) => {
  const items = await db
    .select()
    .from(peItems)
    .where(eq(peItems.buildingId, Number(req.params.buildingId)));
  res.json(items);
});

// ── Create item ───────────────────────────────────────────────────────────────
router.post("/buildings/:buildingId/items", requireAuth, async (req, res) => {
  const parsed = parseItemInput(req.body);
  if (!parsed.ok) return res.status(400).json({ error: parsed.error });

  const { conditionRating, unitRateRcn, quantity } = parsed.value;
  const rul = deriveRul(conditionRating);
  const erc = unitRateRcn != null && quantity != null
    ? deriveErc(unitRateRcn, quantity) : null;
  const indemnity = erc != null ? deriveIndemnity(erc, rul) : null;

  const [created] = await db.insert(peItems).values({
    ...parsed.value,
    buildingId:          Number(req.params.buildingId),
    uniqueId:            await nextUniqueId(),
    conditionLabel:      deriveConditionLabel(conditionRating),
    remainingUsefulLifePct: rul,
    estReplacementCost:  erc != null ? String(erc) : null,
    indemnityValue:      indemnity != null ? String(indemnity) : null,
    inspectedBy:         req.user!.id,
  }).returning();

  res.status(201).json(created);
});

// ── PATCH item (optimistic concurrency — see §6 of parent guide) ──────────────
router.patch("/items/:id", requireAuth, async (req, res) => {
  const parsed = parseItemInput(req.body, { partial: true });
  if (!parsed.ok) return res.status(400).json({ error: parsed.error });
  if (req.body.version == null)
    return res.status(400).json({ error: "version is required" });

  const [existing] = await db.select().from(peItems)
    .where(eq(peItems.id, Number(req.params.id)));
  if (!existing) return res.status(404).json({ error: "Not found" });
  if (existing.version !== req.body.version)
    return res.status(409).json({
      error: "Version conflict", currentVersion: existing.version
    });

  const merged = { ...existing, ...parsed.value };
  const rul = deriveRul(merged.conditionRating);
  const erc = merged.unitRateRcn != null && merged.quantity != null
    ? deriveErc(Number(merged.unitRateRcn), merged.quantity) : null;
  const indemnity = erc != null ? deriveIndemnity(erc, rul) : null;

  const [updated] = await db.update(peItems)
    .set({
      ...parsed.value,
      conditionLabel:         deriveConditionLabel(merged.conditionRating),
      remainingUsefulLifePct: rul,
      estReplacementCost:     erc != null ? String(erc) : null,
      indemnityValue:         indemnity != null ? String(indemnity) : null,
      version:                existing.version + 1,
      updatedAt:              new Date(),
    })
    .where(and(eq(peItems.id, Number(req.params.id)), eq(peItems.version, req.body.version)))
    .returning();

  res.json(updated);
});

// ── DELETE item (admin/reviewer only) ─────────────────────────────────────────
router.delete("/items/:id", requireRole(["admin", "reviewer"], async () => true), async (req, res) => {
  await db.delete(peItems).where(eq(peItems.id, Number(req.params.id)));
  res.status(204).end();
});

export default router;
```

---

## 5. OpenAPI spec additions

Add the following to `lib/api-spec/openapi.yaml`.

### Tags (add to top-level `tags:` list)

```yaml
- name: peItems
  description: P&E Contents inventory items
- name: peBuildings
  description: Buildings in scope for P&E inspection (read via am_buildings)
- name: peVocabulary
  description: Autofill vocabulary for P&E item fields
- name: peExport
  description: Export P&E inventory to CSV/Excel
```

### Schemas (add to `components/schemas:`)

```yaml
PeItemBase:
  type: object
  required: [categoryL1, conditionRating, quantity, uom]
  properties:
    assetIdClient:        { type: string }
    level:                { type: string }
    subLocation:          { type: string }
    categoryL1:           { type: string }
    categoryL2:           { type: string }
    categoryL3:           { type: string }
    categoryL4:           { type: string }
    itemDescription:      { type: string }
    make:                 { type: string }
    model:                { type: string }
    serialNumber:         { type: string }
    assetTag:             { type: string }
    colourFinish:         { type: string }
    quantity:             { type: integer, minimum: 1 }
    uom:
      type: string
      enum: [ea, set, pair, lot]
    widthMm:              { type: integer }
    depthMm:              { type: integer }
    heightMm:             { type: integer }
    screenSizeIn:         { type: number }
    weightKg:             { type: number }
    conditionRating:
      type: integer
      minimum: 0
      maximum: 5
    photo1Url:            { type: string }
    photo2Url:            { type: string }
    worksPhoto1Url:       { type: string }
    worksPhoto2Url:       { type: string }
    commentsRecs:         { type: string }
    defect:               { type: boolean }
    worksDescription:     { type: string }
    defectPriority:
      type: string
      enum: ["Immediate (High)", "High", "Moderate", "Low"]
    probableRepairCost:   { type: number }
    yearManufactured:     { type: integer }
    yearPurchased:        { type: integer }
    purchasePrice:        { type: number }
    unitRateRcn:          { type: number }
    effectiveLifeYears:   { type: integer }
    insuranceCategory:
      type: string
      enum: [Contents, "Plant & Equipment", "Motor Vehicle", Other]
    gpsLat:               { type: number }
    gpsLng:               { type: number }

PeItem:
  allOf:
    - $ref: "#/components/schemas/PeItemBase"
    - type: object
      required: [id, version, uniqueId, buildingId, conditionLabel,
                 remainingUsefulLifePct, estReplacementCost, indemnityValue,
                 createdAt, updatedAt]
      properties:
        id:                       { type: integer }
        version:                  { type: integer }
        uniqueId:                 { type: string }
        buildingId:               { type: integer }
        conditionLabel:           { type: string }
        remainingUsefulLifePct:   { type: integer, nullable: true }
        estReplacementCost:       { type: number, nullable: true }
        indemnityValue:           { type: number, nullable: true }
        createdAt:                { type: string, format: date-time }
        updatedAt:                { type: string, format: date-time }

PeItemInput:
  $ref: "#/components/schemas/PeItemBase"
```

### Paths (add to `paths:`)

```yaml
/modules/am-data-collection-pe/buildings:
  get:
    summary: List buildings available for P&E inspection
    operationId: peListBuildings
    tags: [peBuildings]
    responses:
      "200":
        description: Array of buildings
        content:
          application/json:
            schema:
              type: array
              items: { $ref: "#/components/schemas/AmBuilding" }
      "401": { $ref: "#/components/responses/Error" }

/modules/am-data-collection-pe/buildings/{buildingId}/items:
  get:
    summary: List all P&E items for a building
    operationId: peListItems
    tags: [peItems]
    parameters:
      - { name: buildingId, in: path, required: true, schema: { type: integer } }
    responses:
      "200":
        description: Array of PeItem
        content:
          application/json:
            schema: { type: array, items: { $ref: "#/components/schemas/PeItem" } }
      "401": { $ref: "#/components/responses/Error" }
  post:
    summary: Create a new P&E item
    operationId: peCreateItem
    tags: [peItems]
    parameters:
      - { name: buildingId, in: path, required: true, schema: { type: integer } }
    requestBody:
      required: true
      content:
        application/json:
          schema: { $ref: "#/components/schemas/PeItemInput" }
    responses:
      "201":
        description: Created PeItem
        content:
          application/json:
            schema: { $ref: "#/components/schemas/PeItem" }
      "400": { $ref: "#/components/responses/Error" }
      "401": { $ref: "#/components/responses/Error" }

/modules/am-data-collection-pe/items/{id}:
  get:
    summary: Get a single P&E item
    operationId: peGetItem
    tags: [peItems]
    parameters:
      - { name: id, in: path, required: true, schema: { type: integer } }
    responses:
      "200":
        content:
          application/json:
            schema: { $ref: "#/components/schemas/PeItem" }
      "401": { $ref: "#/components/responses/Error" }
      "404": { $ref: "#/components/responses/Error" }
  patch:
    summary: Update a P&E item (optimistic concurrency — version required)
    operationId: peUpdateItem
    tags: [peItems]
    parameters:
      - { name: id, in: path, required: true, schema: { type: integer } }
    requestBody:
      required: true
      content:
        application/json:
          schema:
            allOf:
              - $ref: "#/components/schemas/PeItemInput"
              - type: object
                required: [version]
                properties:
                  version: { type: integer }
    responses:
      "200":
        content:
          application/json:
            schema: { $ref: "#/components/schemas/PeItem" }
      "400": { $ref: "#/components/responses/Error" }
      "401": { $ref: "#/components/responses/Error" }
      "404": { $ref: "#/components/responses/Error" }
      "409": { $ref: "#/components/responses/Error" }
  delete:
    summary: Delete a P&E item (admin/reviewer)
    operationId: peDeleteItem
    tags: [peItems]
    parameters:
      - { name: id, in: path, required: true, schema: { type: integer } }
    responses:
      "204": { description: Deleted }
      "401": { $ref: "#/components/responses/Error" }
      "403": { $ref: "#/components/responses/Error" }
      "404": { $ref: "#/components/responses/Error" }

/modules/am-data-collection-pe/buildings/{buildingId}/vocabulary:
  get:
    summary: Vocabulary for autofill fields within a building (frequency-ranked)
    operationId: peGetVocabulary
    tags: [peVocabulary]
    parameters:
      - { name: buildingId, in: path, required: true, schema: { type: integer } }
      - { name: field, in: query, required: true, schema: { type: string },
          description: "Field name: level | subLocation | make | colourFinish | model" }
    responses:
      "200":
        content:
          application/json:
            schema: { type: array, items: { type: string } }
      "401": { $ref: "#/components/responses/Error" }

/modules/am-data-collection-pe/buildings/{buildingId}/export:
  get:
    summary: Export P&E inventory to CSV (admin/reviewer)
    operationId: peExportBuilding
    tags: [peExport]
    parameters:
      - { name: buildingId, in: path, required: true, schema: { type: integer } }
      - { name: format, in: query, schema: { type: string, enum: [csv] }, default: csv }
    responses:
      "200":
        description: CSV file download
        content:
          text/csv:
            schema: { type: string }
      "401": { $ref: "#/components/responses/Error" }
      "403": { $ref: "#/components/responses/Error" }
```

After editing the spec, run:

```bash
pnpm --filter @workspace/api-spec run codegen
```

Verify that hooks appear in `lib/api-client-react/src/generated/api.ts`:
`usePeListItems`, `usePeCreateItem`, `usePeUpdateItem`, `usePeDeleteItem`,
`usePeGetVocabulary`, `usePeExportBuilding`.

---

## 6. Frontend file layout

```
artifacts/field-day/src/modules/am-data-collection-pe/
  index.ts
  ModulePage.tsx
  lib/
    constants.ts
    categoryLibrary.ts     ← L1→L2→L3→L4 lookup tree (see §7)
    dimensionRules.ts      ← which dimension fields show for each L1/L2
  pages/
    BuildingSelectPage.tsx
    LocationDrillPage.tsx
    ItemListPage.tsx
    ItemFormPage.tsx
    SummaryPage.tsx
    ExportPage.tsx         ← admin/reviewer only
  components/
    ConditionBadge.tsx
    ValuationCard.tsx
    DimensionFields.tsx    ← context-sensitive W/D/H/Screen/Weight inputs
    DefectSection.tsx      ← hidden until defect toggled on
    PhotoCapture.tsx       ← camera capture + preview strip
    CategoryDrilldown.tsx  ← cascading L1→L2→L3→L4 selects
```

### lib/constants.ts

```ts
export const MODULE_BASE = "/module/am-data-collection-pe";
export const MODULE_KEY  = "amDataCollectionPe";
```

### ModulePage.tsx (wouter routing)

```tsx
import { Switch, Route, Redirect } from "wouter";
import { MODULE_BASE } from "./lib/constants";
import BuildingSelectPage  from "./pages/BuildingSelectPage";
import LocationDrillPage   from "./pages/LocationDrillPage";
import ItemListPage         from "./pages/ItemListPage";
import ItemFormPage         from "./pages/ItemFormPage";
import SummaryPage          from "./pages/SummaryPage";
import ExportPage           from "./pages/ExportPage";

export default function AmDataCollectionPePage() {
  return (
    <Switch>
      <Route path={MODULE_BASE}
        component={BuildingSelectPage} />
      <Route path={`${MODULE_BASE}/buildings/:buildingId`}
        component={LocationDrillPage} />
      <Route path={`${MODULE_BASE}/buildings/:buildingId/items`}
        component={ItemListPage} />
      <Route path={`${MODULE_BASE}/buildings/:buildingId/items/new`}
        component={ItemFormPage} />
      <Route path={`${MODULE_BASE}/buildings/:buildingId/items/:itemId/edit`}
        component={ItemFormPage} />
      <Route path={`${MODULE_BASE}/buildings/:buildingId/summary`}
        component={SummaryPage} />
      <Route path={`${MODULE_BASE}/buildings/:buildingId/export`}
        component={ExportPage} />
      <Redirect to={MODULE_BASE} />
    </Switch>
  );
}
```

---

## 7. Frontend page specifications

### BuildingSelectPage
- Calls `usePeListBuildings()`.
- Lists buildings as tappable cards (name + address).
- Tapping navigates to `${MODULE_BASE}/buildings/:buildingId`.
- Mobile: full-width list, `h-11` touch targets, search/filter bar.

### LocationDrillPage
- Shows the breadcrumb for the selected building.
- Presents a tile grid for **Level** selection (from distinct `level` values already
  on record for that building, plus an "Add new level" option).
- Navigating through Level → Sub Location pre-populates the new-item form.
- A floating "+ New Item" button at bottom-right is always visible.

### ItemListPage
- Calls `usePeListItems({ buildingId })`.
- Groups items by `level` → `subLocation` → `categoryL1` using collapsible sections.
- Each item row shows: `categoryL3` name, Qty × UoM, `conditionLabel` badge
  (colour coded: As New=green, Good=teal, Fair=amber, Poor=orange, Very Poor=red,
  Not Present=grey), and a right-arrow to edit.
- Defect rows show a red dot indicator.
- Floating "+ Add Item" button links to the item form pre-seeded with the current
  level/subLocation context.

### ItemFormPage (create and edit)
This is the most complex page. It has two modes: **create** (POST) and **edit** (PATCH
with `version`). On edit, handle `409` by re-fetching and showing a conflict toast.

**Section order:**

1. **Location** — Level (autofill), Sub Location (autofill). Both autofill via
   `usePeGetVocabulary({ field: "level" | "subLocation" })`.

2. **Category** — `<CategoryDrilldown>` component: cascading selects L1 → L2 → L3 → L4.
   L1 is required. L2/L3 cascade from `categoryLibrary.ts`. L4 shows only if that L3
   has variants other than `"--"`.

3. **Item Details** — Item Description (text), Make (autofill), Model, Serial Number,
   Asset Tag, Colour / Finish (autofill).

4. **Quantity & Unit** — Quantity (number, min 1), UoM select (`ea` / `set` / `pair` / `lot`).

5. **Dimensions** — `<DimensionFields categoryL1={...} categoryL2={...} />`. Shows
   only the fields relevant to the selected category (see `dimensionRules.ts` below).

6. **Condition** — `<ConditionRatingSelect>`: tile buttons 0–5, each labelled.
   Required — cannot submit with blank. Rating 0 = "Not Present" disables valuation
   fields and forces `insuranceCategory` to "N/A".

7. **Photos** — `<PhotoCapture>` for Photo 1 and Photo 2.

8. **Comments / Recommendations** — text area.

9. **Defect** — Yes/No toggle. When toggled **Yes**, `<DefectSection>` slides in:
   Works Description (text), Defect Priority (select), Probable Repair Cost ($),
   Works Photo 1, Works Photo 2.

10. **Valuation** — Read-only computed display (Estimated Replacement Cost, RUL %,
    Indemnity Value) driven by condition rating and Unit Rate. Unit Rate field is
    editable (manual override). Insurance Category select. Effective Life (years).

**Form behaviour:**
- All non-measurement / non-condition fields use `<AutofillInput>` backed by the
  vocabulary endpoint (same component as `am-data-collection-buildings`).
- `estReplacementCost = unitRateRcn × quantity` — update on any change to either field.
- `remainingUsefulLifePct` — update on condition rating change.
- `indemnityValue = estReplacementCost × (rulPct / 100)` — update reactively.
- On submit: POST or PATCH. On success: toast "Item saved" and navigate back to
  `ItemListPage`.

### SummaryPage
- Calls `usePeListItems({ buildingId })`, client-side aggregates.
- Shows a table grouped by L1 category with:
  - Item count, Total Quantity
  - Total Estimated Replacement Cost (RCN)
  - Total Indemnity Value
- A footer row totals all three valuation columns.
- Export button (visible to admin/reviewer only) links to ExportPage.

### ExportPage (admin/reviewer)
- Gate with `useGetCurrentUser()` + `ADMIN_ROLES` check. Show `<Restricted>` fallback
  for inspectors — never 404.
- Calls `usePeExportBuilding({ buildingId, format: "csv" })`.
- Download triggers on button click.

---

## 8. lib/dimensionRules.ts — context-sensitive dimension fields

```ts
type DimensionSet = {
  width: boolean;
  depth: boolean;
  height: boolean;
  screenSize: boolean;
  weight: boolean;
};

export function getDimensionRules(l1: string, l2: string): DimensionSet {
  const always   = { width: true,  depth: true,  height: true,  screenSize: false, weight: false };
  const screens  = { width: false, depth: false,  height: false, screenSize: true,  weight: false };
  const heavy    = { width: true,  depth: true,  height: true,  screenSize: false, weight: true  };
  const none     = { width: false, depth: false, height: false, screenSize: false, weight: false };

  if (l1 === "Information Technology") {
    if (l2 === "Display & Peripherals") return screens;
    return { width: true, depth: true, height: true, screenSize: false, weight: false };
  }
  if (l1 === "Audio Visual") {
    if (l2 === "Display Systems" || l2 === "Projection") return screens;
    return always;
  }
  if (l1 === "Vehicles & Motorised Plant") return heavy;
  if (l1 === "Fitness & Recreation")       return heavy;
  if (l1 === "Other / Miscellaneous")      return none;
  return always; // Furniture, Appliances, Office Equipment, Medical
}
```

---

## 9. lib/categoryLibrary.ts

Import directly from the project's `schema.json` (already committed at the repo root).
The `categoryLibrary` key contains the full L1 → L2 → L3 → L4 tree. At runtime, build
a lookup:

```ts
import schema from "../../../../../schema.json";

export type CategoryTree = typeof schema.categoryLibrary;
export const CATEGORY_TREE = schema.categoryLibrary as CategoryTree;

export function getL2Options(l1: string): string[] {
  return Object.keys(CATEGORY_TREE[l1 as keyof CategoryTree] ?? {});
}
export function getL3Options(l1: string, l2: string): string[] {
  const sub = CATEGORY_TREE[l1 as keyof CategoryTree];
  return Object.keys((sub as any)?.[l2] ?? {});
}
export function getL4Options(l1: string, l2: string, l3: string): string[] {
  const sub = CATEGORY_TREE[l1 as keyof CategoryTree];
  return ((sub as any)?.[l2]?.[l3] ?? []) as string[];
}
```

---

## 10. Offline support (optional — opt in if required)

Follow the pattern in `am-data-collection-buildings/offline/`. The three files needed:

- `offline/db.ts` — IndexedDB store for `pe_items` keyed by `id`.
- `offline/useCachedQuery.ts` — wraps `usePeListItems`, serves IndexedDB on network fail.
- `offline/sync.ts` — queues POST/PATCH when offline, drains on reconnect.

If offline is not required for the initial release, skip this directory. An inspector
in the field will need it; gate the decision on connectivity assumptions.

---

## 11. GPS / Map

The location hierarchy page (`LocationDrillPage`) shows a Leaflet map with Google
hybrid layer (aerial + street names), centred on the building's GPS coordinates from
`am_buildings`. Individual items capture `gpsLat`/`gpsLng` at creation time via
`navigator.geolocation.getCurrentPosition()` — fire-and-forget, no blocking.

---

## 12. Module-specific test checklist

In addition to the standard module verify steps:

- [ ] Condition rating 0 ("Not Present"): `estReplacementCost`, `indemnityValue`
  and `remainingUsefulLifePct` all resolve to `0` / `null` on the server.
- [ ] Defect toggle OFF → `worksDescription`, `defectPriority`, `probableRepairCost`,
  `worksPhoto1Url`, `worksPhoto2Url` are all null in the saved record.
- [ ] Defect toggle ON → works fields and works photo capture are visible and saved.
- [ ] Creating an item as **inspector** returns 201.
- [ ] Deleting an item as **inspector** returns 403.
- [ ] PATCH with a stale `version` returns 409 with `currentVersion`.
- [ ] Export endpoint as **inspector** returns 403.
- [ ] Export endpoint as **admin** returns a 200 `text/csv` response.
- [ ] Category drilldown: selecting L1 clears L2/L3/L4. Selecting L2 clears L3/L4.
- [ ] Dimension fields shown for `Furniture / Seating`: Width, Depth, Height (no screen).
- [ ] Dimension fields shown for `Audio Visual / Display Systems`: Screen Size only.
- [ ] Mobile viewport (375×812): no horizontal scroll on ItemFormPage.
- [ ] All interactive controls have `data-testid`.

---

## 13. Path asymmetry reminder

| Layer | Pattern |
|---|---|
| Backend route | `/api/modules/am-data-collection-pe/...` |
| Frontend route | `/module/am-data-collection-pe/...` |
| `MODULE_BASE` constant | `"/module/am-data-collection-pe"` |
| DB table prefix | `pe_` |
| OpenAPI operationId prefix | `pe` (e.g. `peListItems`) |

Always import `MODULE_BASE` — never hard-code either URL form.

---

## 14. Reference implementation

Copy patterns from `am-data-collection-buildings` for:

| Pattern | Source file |
|---|---|
| Optimistic concurrency | `routes/components.ts` |
| Role-gated CRUD + Restricted fallback | `routes/costLibrary.ts` + `pages/CostLibraryAdminPage.tsx` |
| Vocabulary / autofill | `routes/vocabulary.ts` + `components/AutofillInput.tsx` |
| Offline cache | `offline/db.ts`, `offline/useCachedQuery.ts`, `offline/sync.ts` |
| Photo capture | `components/PhotoCapture.tsx` (if exists) or implement fresh |
| Summary / totals card | `pages/SummaryPage.tsx` |
