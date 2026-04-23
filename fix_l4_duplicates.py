"""
fix_l4_duplicates.py
Resolves the 17 (L1,L2,L3,L4) paths that have multiple unit rates
by appending a type/material/grade descriptor to L4.

Rule:
  - If current L4 == "--"  → replace with descriptor
  - If current L4 != "--"  → append " / <descriptor>"

Reads  Asset_Library_AU.csv  (cp1252)
Writes Asset_Library_AU_fixed.csv  (utf-8)
"""
import csv
from pathlib import Path

# Map UID -> new L4 descriptor to append/replace
# Format: {uid_str: "descriptor"}
L4_UPDATES = {
    # ── Furniture > Desks > Corner Desk > 1800mm ────────────────────────────
    "200043": "Laminate",
    "200044": "Veneer",

    # ── Furniture > Desks > Straight Desk > 1500mm ──────────────────────────
    "200038": "Laminate",
    "200040": "Veneer",

    # ── Furniture > Desks > Straight Desk > 1800mm ──────────────────────────
    "200039": "Laminate",
    "200041": "Veneer",

    # ── Furniture > Desks > Height-Adjustable Desk > 1500mm ─────────────────
    "200046": "Electric",
    "200048": "Manual Crank",

    # ── Furniture > Desks > Height-Adjustable Desk > 1800mm ─────────────────
    "200047": "Electric Dual Motor",
    "200049": "Electric Single Motor",

    # ── Furniture > Seating > Bar Stool > -- ────────────────────────────────
    "200029": "Adjustable / Vinyl",
    "200030": "Fixed / Timber",
    "200031": "Swivel / Upholstered",
    "200485": "Fixed / Metal",
    "200532": "Swivel / Velvet",

    # ── Furniture > Seating > Bench Seat > -- ───────────────────────────────
    "200032": "2-Seat / Upholstered",
    "200033": "Backless / Timber",
    "200486": "3-Seat / Upholstered",

    # ── Furniture > Seating > Drafting Chair > -- ────────────────────────────
    "200034": "Fabric Seat",
    "200731": "Mesh Back",

    # ── Furniture > Seating > Lounge Chair / Sofa > 2-seater ────────────────
    "200025": "Fabric",
    "200026": "Vinyl",

    # ── Furniture > Seating > Lounge Chair / Sofa > 3-seater ────────────────
    "200027": "Fabric",
    "200028": "Vinyl",

    # ── Furniture > Seating > Lounge Chair / Sofa > Single ──────────────────
    "200022": "Fabric",
    "200023": "Vinyl Tub",
    "200024": "Leather",
    "200481": "Shell Pod",

    # ── Furniture > Seating > Meeting Chair > -- ─────────────────────────────
    "200014": "Mesh / 4-Star Base",
    "200015": "Fabric / Chrome Legs",
    "200016": "Leather / Castors",
    "200017": "Mesh / 5-Star Castors",
    "200483": "Fabric Armchair",
    "200523": "Stackable / Padded",
    "200700": "Ergonomic Mesh",

    # ── Furniture > Seating > Stacking Chair > -- ────────────────────────────
    "200018": "Polypropylene / Indoor",
    "200019": "Padded / Link Arms",
    "200020": "Steel Frame / Upholstered",
    "200021": "Polypropylene / Heavy Duty",
    "200484": "Polypropylene / Bistro",
    "200701": "Polypropylene / Outdoor",

    # ── Furniture > Seating > Task Chair > -- ───────────────────────────────
    "200001": "Mesh / Mid-Back Ergonomic",
    "200002": "Mesh / Mid-Back Fixed Arms",
    "200003": "Leather / High-Back",
    "200004": "Fabric / Budget",
    "200005": "Mesh / Premium Herman Miller",
    "200006": "Mesh / Premium Humanscale",
    "200007": "Mesh / Contoured Nylon Base",
    "200008": "Fabric Seat Mesh Back",
    "200009": "Fabric / Heavy Duty 150kg",
    "200479": "Fabric / Lumbar Support",
    "200487": "Fabric / Posture Wide Seat",
    "200488": "Fabric / 24hr Operator",
    "200524": "Mesh / With Headrest",
    "200697": "Leather / High-Back Star Base",
    "200718": "ESD Anti-Static",
    "200719": "Saddle Stool",

    # ── Furniture > Seating > Visitor Chair > -- ─────────────────────────────
    "200010": "4-Leg / Upholstered",
    "200011": "Cantilever / Chrome",
    "200012": "Upholstered / Timber Legs",
    "200013": "Stackable / Link Arms",
    "200480": "4-Star Base / Fabric",
    "200698": "Timber Legs / Guest",
    "200725": "Sled Base / Plastic Shell",

    # ── Furniture > Storage > Filing Cabinet (Lateral) > 2-drawer ───────────
    "200073": "900mm W",
    "200076": "1200mm W",

    # ── Furniture > Storage > Filing Cabinet (Pedestal) > 3-drawer ──────────
    "200077": "Mobile",
    "200078": "Fixed",
}

def apply_l4(current_l4: str, descriptor: str) -> str:
    if current_l4.strip() == "--":
        return descriptor
    else:
        return f"{current_l4.strip()} / {descriptor}"

src = Path("Asset_Library_AU.csv")
dst = Path("Asset_Library_AU_fixed.csv")

changed = 0
with open(src, encoding="utf-8", newline="") as fin, \
     open(dst, "w", encoding="utf-8", newline="") as fout:

    reader = csv.reader(fin)
    writer = csv.writer(fout)

    headers = next(reader)
    writer.writerow(headers)

    for row in reader:
        uid = str(row[0]).strip()
        if uid in L4_UPDATES:
            old_l4 = row[9]
            row[9] = apply_l4(old_l4, L4_UPDATES[uid])
            changed += 1
        writer.writerow(row)

print(f"Updated {changed} rows  ({len(L4_UPDATES)} UIDs targeted)")
print(f"Output: {dst}")

# ── Verify no duplicates remain ───────────────────────────────────────────────
from collections import defaultdict
with open(dst, encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))
paths = defaultdict(list)
for r in rows[1:]:
    key = (r[6], r[7], r[8], r[9])
    paths[key].append(r[27])   # unit rate

conflicts = {k: v for k, v in paths.items() if len(set(v)) > 1}
print(f"\nRemaining unit-rate conflicts: {len(conflicts)}")
if conflicts:
    for k, rates in conflicts.items():
        print(f"  {' > '.join(k)}  rates: {sorted(set(rates))}")
else:
    print("  None — all (L1,L2,L3,L4) paths are now unique by unit rate.")

print(f"\nTotal records: {len(rows)-1}")
print(f"Unique taxonomy paths: {len(paths)}")
