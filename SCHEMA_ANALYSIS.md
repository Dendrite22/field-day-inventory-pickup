# Field Day: Inventory Pickup — Schema Analysis & P&E Reconfiguration

## 1. Original "First Pass.xlsx" — What It Does

The source document is a **Building Asset Register** designed for infrastructure/building component condition assessment and capital expenditure planning. Its purpose is:
- Track building fabric and services (Finishes, Electrical, Fire, Hydraulic)
- Rate condition (1–5 scale) for capital replacement forecasting
- Record defects and associated maintenance works costs
- Generate Estimated Replacement Cost per asset line

### Original Data Hierarchy
```
Parent Asset → Address → Level → Sub Location
  → L1 (Services / Finishes / Fitouts)
    → L2 (Electrical / Fire / Internal Floor etc.)
      → L3 (Lighting / Smoke Alarm / Carpet etc.)
        → L4 (Exit Light / Painted / --)
```

### Original Measurement Approach
Units used: `ea`, `m2`, `m`, `m3`  
Focus: area-based (m2 of carpet, painted walls) or count-based (ea fire extinguisher)  
No dimensional capture (no W × D × H)  
No serial numbers or asset tags  
No purchase history  

---

## 2. What Needs to Change for Plant & Equipment (Contents) Valuation

### Purpose Shift
| Original | New (P&E Contents) |
|---|---|
| Building fabric & services | Loose contents, furniture, equipment |
| Capital replacement planning | Insurance valuation (Replacement Cost New + Indemnity) |
| Maintenance defect tracking | Condition for depreciation rate |
| Unit rates from cost library | Market replacement values (insurance schedules) |
| m2 / linear metre measurements | Physical dimensions (W × D × H) + count |

### What Stays
- Unique ID system (auto-generated from 100001)
- Parent Asset / Address / Level / Sub Location hierarchy
- Condition Rating 1–5 + Label
- Photo 1 / Photo 2 capture
- Defect (yes/no) → Works Photos
- GPS functionality
- Autofill from existing entries
- Make / Model fields

---

## 3. Reconfigured P&E Contents Schema

### 3.1 Identity & Location Fields (unchanged logic, same autofill rules)

| Field | Type | Notes |
|---|---|---|
| Unique ID | Auto-generated | System assigns from 100001, increments across portfolio |
| Asset ID (Client) | Text | Imported from client records or input on inspection |
| Parent Asset | Text (autofill) | Building / facility name |
| Address | Text (autofill) | Imported from client list |
| Level | Text (autofill) | Ground Floor, Level 1, Basement, etc. |
| Sub Location | Text (autofill) | Room / area name (e.g. Board Room, Reception, Open Plan) |

### 3.2 Asset Category Hierarchy — P&E Contents

Replace the original building-component L1–L4 with:

```
L1: Contents Category
  L2: Sub-Category
    L3: Item Type
      L4: Variant / Specification
```

#### Full P&E Category Library

**L1: Furniture**
- L2: Seating → L3: Task Chair, Visitor Chair, Meeting Chair, Lounge Chair / Sofa, Bar Stool, Bench Seat, Chair (Other)
- L2: Tables → L3: Meeting Table, Dining Table, Coffee Table, Side Table, Boardroom Table
- L2: Desks & Workstations → L3: Straight Desk, Corner Desk, Height-Adjustable Desk, Workstation Pod, Reception Desk / Counter
- L2: Storage & Filing → L3: Filing Cabinet (Lateral), Filing Cabinet (Pedestal), Bookcase / Shelf Unit, Storage Cabinet, Credenza / Buffet, Locker
- L2: Screens & Partitions → L3: Acoustic Screen, Desk Divider, Freestanding Partition
- L2: Soft Furnishings → L3: Rug / Mat, Curtain / Blind, Cushion Set, Artwork / Print

**L1: Information Technology**
- L2: Computing → L3: Desktop Computer (Tower), All-in-One Computer, Laptop / Notebook, Tablet / iPad, Server, Docking Station, UPS
- L2: Display & Peripherals → L3: Monitor / Screen, Keyboard & Mouse (Set), Printer (Multifunction), Printer (Desktop), Scanner, Webcam
- L2: Networking → L3: Switch, Router, Wireless Access Point, Patch Panel, Network Rack
- L2: Telephony → L3: Desk Phone (IP), PABX / Phone System, Conference Phone, Handset

**L1: Audio Visual**
- L2: Display Systems → L3: Flat Screen TV, Interactive Whiteboard, Digital Signage Screen, Projection Screen
- L2: Projection → L3: Data Projector, Laser Projector
- L2: Audio → L3: Speaker System, Amplifier, Microphone System, Hearing Loop
- L2: Video Conferencing → L3: Video Conferencing Unit, Camera (PTZ), Video Bar (All-in-One)
- L2: Control Systems → L3: AV Control Panel, HDMI Switch / Matrix

**L1: Appliances & White Goods**
- L2: Kitchen Appliances → L3: Refrigerator / Fridge, Bar Fridge, Dishwasher, Microwave Oven, Oven / Stove, Coffee Machine (Auto), Coffee Machine (Manual), Toaster, Kettle, Water Cooler / Dispenser
- L2: Laundry → L3: Washing Machine, Dryer
- L2: Cleaning → L3: Vacuum Cleaner, Steam Cleaner, Floor Polisher

**L1: Office Equipment**
- L2: Mail & Document → L3: Postage Meter, Guillotine / Trimmer, Laminator, Shredder, Binding Machine
- L2: Security → L3: Safe, Cash Register, Key Cabinet
- L2: Material Handling → L3: Trolley, Hand Truck, Pallet Jack

**L1: Fitness & Recreation**
- L2: Cardio Equipment → L3: Treadmill, Stationary Bike, Rowing Machine, Elliptical
- L2: Strength Equipment → L3: Weight Bench, Dumbbell Set, Barbell / Rack, Gym Machine
- L2: Recreation → L3: Pool / Billiards Table, Table Tennis Table, Foosball Table

**L1: Medical & First Aid**
- L2: First Aid → L3: Defibrillator (AED), First Aid Cabinet, Stretcher
- L2: Medical Equipment → L3: Blood Pressure Monitor, Examination Table

**L1: Vehicles & Motorised Plant**
- L2: Vehicles → L3: Car / Sedan, Van / Ute, Bus / Minibus, Forklift, Golf Cart / Buggy
- L2: Grounds → L3: Ride-On Mower, Walk-Behind Mower, Generator, Pressure Washer, Chainsaw

**L1: Other / Miscellaneous**
- L2: Fixtures → L3: Wall Clock, Flag Pole, Noticeboard / Whiteboard (non-interactive), Letterbox
- L2: Uncategorised → L3: Other (describe in Comments)

---

### 3.3 Item Attributes & Measurements

These replace the original minimal Make/Model/Qty/UoM fields with a richer set:

| Field | Type | Description |
|---|---|---|
| Item Description | Text | Free-text description of the specific item |
| Make / Brand | Text (autofill) | Manufacturer name |
| Model | Text | Model name or number |
| Serial Number | Text | Manufacturer serial (critical for insurance) |
| Asset Tag / Label | Text | Client's own tag or label number |
| Colour / Finish | Text | e.g. Black, White, Timber veneer, Chrome |
| Quantity | Number | Count of identical items in this entry |
| Unit of Measurement | Selection | `ea`, `set`, `pair`, `lot` |

#### Dimensional Capture (Furniture & Equipment)

| Field | Type | Unit | Applies To |
|---|---|---|---|
| Width | Number | mm | Furniture, screens, appliances |
| Depth | Number | mm | Furniture, equipment |
| Height | Number | mm | All items |
| Seating Capacity | Number | persons | Tables, sofas, benches |
| Screen Size | Number | inches | TVs, monitors, projectors |
| Storage Capacity | Number | GB / TB | Computers, servers (note unit in Comments) |
| Weight | Number | kg | Plant, heavy equipment |

> **Rule**: Width/Depth/Height always captured for furniture. Screen Size captured for AV/IT displays. Other dimensional fields optional based on L1 category.

---

### 3.4 Condition Rating (unchanged from original)

| Rating | Label |
|---|---|
| 0 | Not Present (asset recorded previously, no longer on site) |
| 1 | As New |
| 2 | Good |
| 3 | Fair |
| 4 | Poor |
| 5 | Very Poor / End of Life |

> Blank not accepted. Rating 0 → all valuation fields auto-set to $0 / N/A.

---

### 3.5 Valuation Fields (Insurance / Financial Reporting)

| Field | Type | Description |
|---|---|---|
| Year of Manufacture | Number | Year item was made (if known) |
| Year Purchased / Installed | Number | Year client acquired item |
| Purchase Price | Currency | Original cost if known (optional) |
| Unit Rate (RCN) | Currency | Replacement Cost New per unit — system library or manual override |
| Estimated Replacement Cost | Currency | Formula: Unit Rate × Quantity |
| Effective Life (years) | Number | Total expected useful life from system library |
| Remaining Useful Life (%) | Number | Derived from Condition Rating (Rating 1 = 100%, Rating 5 = 0%, linear interpolation) |
| Indemnity Value | Currency | Formula: Replacement Cost × (Remaining Useful Life %) |
| Insurance Schedule Category | Selection | Contents / Plant & Equipment / Motor Vehicle / Other |

> **Replacement Cost vs Indemnity**: RCN is used for new-for-old insurance. Indemnity is the depreciated market value — required for financial reporting (AASB 116, AASB 13).

---

### 3.6 Defect & Works Fields (unchanged logic)

| Field | Type | Notes |
|---|---|---|
| Defect (yes/no) | Selection | Yes/No only |
| Works Description | Text | Only active if Defect = Yes |
| Defect Priority | Selection | Low / Moderate / High / Immediate |
| Probable Repair Cost | Currency | Manual entry |
| Works Photo 1 | Photo | Only enabled if Defect = Yes |
| Works Photo 2 | Photo | Only enabled if Defect = Yes |

---

### 3.7 Photo & GPS Fields

| Field | Type | Notes |
|---|---|---|
| Photo 1 | Camera capture | Primary item photo |
| Photo 2 | Camera capture | Secondary / detail photo |
| GPS Coordinates | Auto (device) | Latitude / Longitude captured on entry creation |
| Map View | Hybrid (Google Maps aerial + street names) | Displayed per building, not per item |

---

## 4. Data Entry Form Flow (App Logic)

```
[Select Building / Parent Asset]
  → [Select or Create Address]
    → [Select Level]
      → [Select Sub Location]
        → [Select L1 Category]
          → [Select L2 → L3 → L4]
            → [Item Detail Form]
              - Core attributes (Description, Make, Model, Serial No., Asset Tag)
              - Dimensions (context-sensitive based on L1/L2)
              - Condition Rating (mandatory — no blank)
              - Photos (1 & 2)
              - Defect toggle → if Yes, Works fields + Works Photos unlock
              - Valuation (Unit Rate auto-suggest, manual override allowed)
              → [Save & Next Item] or [Save & Change Location]
```

**Autofill rules** (as per original spec):
- Any non-measurement / non-condition field should offer autofill from existing entries at the same building
- Make / Sub Location / Address / Level are prime autofill candidates

---

## 5. Key Schema Differences Summary

| Aspect | Original (Building Assets) | New (P&E Contents) |
|---|---|---|
| L1 Categories | Services, Finishes, Fitouts | Furniture, IT, AV, Appliances, Office Equip, Fitness, Medical, Vehicles |
| Primary UoM | m2, m, ea | ea (predominantly), set, pair, lot |
| Dimensions | None | Width × Depth × Height (mm); Screen Size (in) |
| Serial / Asset Tag | Not present | Required fields |
| Valuation basis | Unit rate × area | RCN per unit × quantity |
| Financial output | Estimated Replacement Cost | RCN + Indemnity Value (depreciated) |
| Depreciation | Maintenance Year only | Remaining Useful Life (%) + Indemnity Value |
| Insurance fields | Not present | Insurance Schedule Category |
| Year fields | Maintenance Year (future) | Year Manufactured + Year Purchased |
| Purchase Price | Not present | Optional capture field |
