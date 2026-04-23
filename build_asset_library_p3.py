"""
Asset Library AU – Part 3
Appends additional records to reach 3× the original counts.
Run AFTER Parts 1 & 2.
"""
import csv
from pathlib import Path

COND_LABELS = {0:'Not Present',1:'As New',2:'Good',3:'Fair',4:'Poor',5:'Very Poor'}
RUL_MAP     = {0:None,1:1.00,2:0.75,3:0.50,4:0.25,5:0.00}

def row(l1,l2,l3,l4,desc,make,model,colour,w,d,h,scr,qty,uom,rate,eff,ins,src,cond=2):
    rul = RUL_MAP[cond]
    erc = round(rate * qty, 2)
    iv  = round(erc * rul, 2) if rul is not None else 0.00
    return [
        '',
        '','','','','',
        l1,l2,l3,l4,desc,
        cond,COND_LABELS[cond],
        '','',
        qty,uom,
        w or '',d or '',h or '',scr or '',
        make,model,
        '','',
        colour,
        f'Source: {src}',
        rate,erc,
        rul if rul is not None else '',
        iv,
        ins,eff
    ]

R = row
CONT = 'Contents'
PE   = 'Plant & Equipment'
MV   = 'Motor Vehicle'

# =============================================================================
# FURNITURE – additional ~90 records
# =============================================================================
F = 'Furniture'

furniture_p3 = [
    # Seating extras
    R(F,'Seating','Task Chair','--','Ergonomic chair, lumbar support, fabric seat, castors','Buro','Sprint','Blue Fabric',660,640,1050,None,1,'ea',520,12,CONT,'Buro.com.au, approx AUD $519, 2025'),
    R(F,'Seating','Visitor Chair','--','Visitor chair, chrome 4-star base, fabric','Buro','Sprint V','Black Fabric',545,545,820,None,1,'ea',300,10,CONT,'Buro.com.au, approx AUD $299, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Single','Tub/pod chair, shell design, metal legs','Instyle','Pod','White',750,760,760,None,1,'ea',1100,12,CONT,'Instyle.com.au, approx AUD $1099, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Corner modular','Modular corner sofa, 4-seat, fabric','Instyle','Modular 4S','Light Grey Fabric',2500,2500,760,None,1,'ea',4500,12,CONT,'Instyle.com.au, approx AUD $4499, 2025'),
    R(F,'Seating','Meeting Chair','--','Meeting armchair, upholstered, 4-leg','Buro','York HC','Black Leather',560,550,870,None,1,'ea',750,12,CONT,'Buro.com.au, approx AUD $749, 2025'),
    R(F,'Seating','Stacking Chair','--','Bistro-style polypropylene stacking chair','Kartell','Louis Ghost','Transparent',380,380,870,None,1,'ea',200,10,CONT,'Stylecraft AU, approx AUD $199, 2025'),
    R(F,'Seating','Bar Stool','--','Metal bar stool, powder coat, 65cm height','Generic','Industrial Stool','Matte Black',400,400,650,None,1,'ea',220,10,CONT,'Officeworks, approx AUD $219, 2025'),
    R(F,'Seating','Bench Seat','--','Upholstered bench seat with backrest, 3-seat','Rapidline','Banquet 3S','Charcoal Fabric',1600,500,800,None,1,'ea',900,12,CONT,'Epic Office Furniture, approx AUD $899, 2025'),
    R(F,'Seating','Task Chair','--','Posture chair, orthopaedic, wide seat, fabric','Buro','Tidal XL','Black Fabric',720,700,1100,None,1,'ea',680,12,CONT,'Buro.com.au, approx AUD $679, 2025'),
    R(F,'Seating','Task Chair','--','Operator chair, 24hr use, heavy-duty','Buro','20hr+','Black Mesh',670,640,1100,None,1,'ea',850,12,CONT,'Buro.com.au, approx AUD $849, 2025'),

    # Desks & Workstations extras
    R(F,'Desks & Workstations','Straight Desk','2000mm','Executive straight desk, 2000×900mm, veneer','Arteil','Exec 2000','Walnut Veneer',2000,900,730,None,1,'ea',1200,15,CONT,'Epic Office Furniture, approx AUD $1199, 2025'),
    R(F,'Desks & Workstations','Corner Desk','2100mm','L-shaped corner desk, 2100×1200mm, laminate','Rapidline','Corner 2100','White',2100,1200,720,None,1,'ea',900,12,CONT,'Fast Office Furniture, approx AUD $899, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1200mm compact','Compact electric sit-stand desk, 1200×600mm','Ergomotion','MotionDesk 1200','White',1200,600,720,None,1,'ea',850,10,CONT,'Ergomotion.com.au, approx AUD $849, 2025'),
    R(F,'Desks & Workstations','Bench Workstation','6-person','6-person open-plan bench, 3600×1600mm, cable tray','Rapidline','Bench 6P','White',3600,1600,720,None,1,'ea',2800,12,CONT,'Epic Office Furniture, approx AUD $2799, 2025'),
    R(F,'Desks & Workstations','Reception Desk / Counter','Curved','Curved reception counter, laminate, raised panel','Rapidline','Recept C','White',2000,900,1100,None,1,'ea',4000,15,CONT,'Epic Office Furniture, approx AUD $3999, 2025'),
    R(F,'Desks & Workstations','Credenza / Desk Return','800mm pedestal return','Credenza return with pedestal drawer unit','Rapidline','Cred Return 800','White',800,500,720,None,1,'ea',420,12,CONT,'Winc, approx AUD $419, 2025'),

    # Tables extras
    R(F,'Tables','Meeting Table','1200mm 4-person','Round meeting table, 1200mm dia','Rapidline','MTable Rnd 1200','White',1200,1200,720,None,1,'ea',500,15,CONT,'Officeworks, approx AUD $499, 2025'),
    R(F,'Tables','Meeting Table','3000mm 12-person','Boat-shaped conference table, 3000×1200mm','Arteil','Boat 3000','Walnut Veneer',3000,1200,750,None,1,'ea',4000,20,CONT,'Epic Office Furniture, approx AUD $3999, 2025'),
    R(F,'Tables','Boardroom Table','6000mm 24-person','Extra-long boardroom table, 6000×1200mm, 2-piece','Arteil','Board 6000','Walnut Veneer',6000,1200,750,None,1,'ea',12000,20,CONT,'Epic Office Furniture, approx AUD $11999, 2025'),
    R(F,'Tables','Café / Bar Table','Outdoor','Outdoor café table, powder-coated steel, 700mm dia','Extremis','BQ Table','Anthracite',700,700,730,None,1,'ea',450,10,CONT,'Outdoor furniture AU, approx AUD $449, 2025'),
    R(F,'Tables','Coffee Table','Glass round 1000mm','Glass round coffee table, 1000mm dia, chrome legs','Generic','Glass Coffee 1000','Clear Glass/Chrome',1000,1000,420,None,1,'ea',550,10,CONT,'Freedom Furniture, approx AUD $549, 2025'),
    R(F,'Tables','Training Table','Folding 1800mm','Folding training table, 1800×750mm, wheels','Rapidline','Train 1800','White',1800,750,730,None,1,'ea',420,10,CONT,'Winc, approx AUD $419, 2025'),
    R(F,'Tables','Dining Table','8-person','Canteen/breakout dining table, 2000×900mm, 8-person','Generic','Dine 2000','White',2000,900,740,None,1,'ea',800,12,CONT,'Epic Office Furniture, approx AUD $799, 2025'),

    # Storage & Filing extras
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','5-drawer','Lateral filing cabinet, 5-drawer, 900mm W','Steelco','LFC5 900','White',900,470,1680,None,1,'ea',950,20,CONT,'Winc, approx AUD $949, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','2-drawer 1200mm','Lateral filing cabinet, 2-drawer, 1200mm W','Steelco','LFC2 1200','Graphite',1200,470,700,None,1,'ea',700,20,CONT,'Winc, approx AUD $699, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Vertical)','2-drawer','Vertical filing cabinet, 2-drawer, A4, steel','Steelco','VFC2','White',470,620,700,None,1,'ea',300,20,CONT,'Winc, approx AUD $299, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','1800mm W 3-shelf','Wide open bookcase, 1800×300×900mm, 3-shelf','Rapidline','Book 1800L','White',1800,300,900,None,1,'ea',500,15,CONT,'Officeworks, approx AUD $499, 2025'),
    R(F,'Storage & Filing','Storage Cabinet','1200mm W half height','Half-height storage cabinet, 1200mm W, lockable','Steelco','SC1200L','White',1200,470,1000,None,1,'ea',700,20,CONT,'Winc, approx AUD $699, 2025'),
    R(F,'Storage & Filing','Credenza / Buffet','2400mm','Wide credenza / sideboard, 2400mm, glass doors','Arteil','Cred 2400','White',2400,450,730,None,1,'ea',1800,15,CONT,'Epic Office Furniture, approx AUD $1799, 2025'),
    R(F,'Storage & Filing','Locker','6-door half-height','6-door half-height locker, 450×450×900mm per bay','Steelco','Lok6H','Grey',1350,450,900,None,1,'ea',600,20,CONT,'Winc, approx AUD $599, 2025'),
    R(F,'Storage & Filing','Tambour Unit','900mm','Tambour door unit, 900mm W, lockable','Rapidline','Tambour 900','White',900,470,730,None,1,'ea',650,15,CONT,'Winc, approx AUD $649, 2025'),
    R(F,'Storage & Filing','Compactus / Mobile Shelving','4-bay','Mobile shelving compactus, 4-bay, 2100H','Spacerak','Compactus 4B','Grey',2400,900,2100,None,1,'ea',5500,25,CONT,'Storage Systems Australia, approx AUD $5499, 2025'),

    # Screens & Partitions extras
    R(F,'Screens & Partitions','Whiteboard','3600×1200mm','Large magnetic whiteboard 3600×1200mm, MDF backing','Visionchart','WB3612','White',3600,20,1200,None,1,'ea',750,10,CONT,'Winc, approx AUD $749, 2025'),
    R(F,'Screens & Partitions','Acoustic Screen','Panel system wall','Acoustic panel system, wall-fixed, 4m run','Rapidline','Wall Panel Kit','Charcoal Fabric',4000,50,1200,None,1,'ea',1800,12,CONT,'Epic Office Furniture, approx AUD $1799, 2025'),
    R(F,'Screens & Partitions','Pinboard','1200×900mm','Pinboard 1200×900mm, noticeboard, cork','Visionchart','Cork 1209','Cork',1200,20,900,None,1,'ea',150,10,CONT,'Officeworks, approx AUD $149, 2025'),

    # Soft Furnishings extras
    R(F,'Soft Furnishings','Window Blind','Blackout 1800mm','Blockout roller blind, 1800×2100mm, chain operated','Decora','Blockout 1800','White',1800,None,2100,None,1,'ea',280,8,CONT,'Bunnings, approx AUD $279, 2025'),
    R(F,'Soft Furnishings','Window Blind','Sheer 1200mm','Sheer roller blind, 1200×2100mm','Decora','Sheer 1200','White',1200,None,2100,None,1,'ea',150,8,CONT,'Bunnings, approx AUD $149, 2025'),
    R(F,'Soft Furnishings','Rug / Carpet Tile','3×4m','Large area rug, 3000×4000mm, commercial loop pile','Interface','Large Rug 3x4','Grey',3000,4000,None,None,1,'ea',1000,8,CONT,'Interface.com, approx AUD $999, 2025'),
    R(F,'Soft Furnishings','Artwork / Print','Canvas set 3-piece','Set of 3 framed canvas prints, 400×600mm each','Generic','Canvas Set 3','Various',400,50,600,None,3,'ea',200,10,CONT,'Ikea, approx AUD $199/set, 2025'),
    R(F,'Soft Furnishings','Planter / Indoor Plant','Medium table planter','Medium table plant in ceramic pot, 500mm H','Generic','Table Plant M','Various',200,200,500,None,1,'ea',150,5,CONT,'Bunnings, approx AUD $149, 2025'),

    # Additional desk/workstation types for completeness
    R(F,'Desks & Workstations','Straight Desk','1200mm glass','Executive desk, 1200×600mm, toughened glass top','Arteil','Glass Exec 1200','Glass/Chrome',1200,600,730,None,1,'ea',800,12,CONT,'Epic Office Furniture, approx AUD $799, 2025'),
    R(F,'Tables','Meeting Table','2700mm 10-person','Rectangular meeting table, 2700×1200mm, high-gloss laminate','Arteil','MTable 2700','White High Gloss',2700,1200,730,None,1,'ea',2000,15,CONT,'Epic Office Furniture, approx AUD $1999, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Ottoman','Square ottoman, fabric upholstered, 600×600mm','Instyle','Ottoman S','Charcoal Fabric',600,600,420,None,1,'ea',400,10,CONT,'Instyle.com.au, approx AUD $399, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Large ottoman','Large rectangular ottoman bench, 1200×450mm','Instyle','Ottoman L','Charcoal Fabric',1200,450,420,None,1,'ea',700,10,CONT,'Instyle.com.au, approx AUD $699, 2025'),
    R(F,'Seating','Meeting Chair','--','Stackable meeting/conference chair, padded','Buro','Engage','Black Fabric',550,540,870,None,1,'ea',280,10,CONT,'Buro.com.au, approx AUD $279, 2025'),
    R(F,'Seating','Task Chair','--','Mesh task chair, headrest, adjustable lumbar','Buro','Persona','Black Mesh',680,650,1150,None,1,'ea',820,12,CONT,'Buro.com.au, approx AUD $819, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Pedestal)','2-drawer','Mobile pedestal, 2-drawer (1 box + 1 file), lockable','Steelco','Ped2','White',465,500,600,None,1,'ea',320,15,CONT,'Officeworks, approx AUD $319, 2025'),
    R(F,'Tables','Side Table','Nest of 2','Nest of 2 side tables, different heights','Generic','Nest Tables','White/Chrome',550,450,550,None,1,'ea',280,10,CONT,'Freedom Furniture, approx AUD $279, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1600mm','Electric sit-stand desk, 1600×800mm, triple motor','Yaasa','Pro 1600','Matte Black',1600,800,720,None,1,'ea',1600,10,CONT,'Yaasa.com, approx AUD $1599, 2025'),
    R(F,'Screens & Partitions','Room Divider','8-panel','8-panel folding room divider, acoustic fabric','Rapidline','RmDiv8','Grey Fabric',3200,50,1800,None,1,'ea',1200,10,CONT,'Fast Office Furniture, approx AUD $1199, 2025'),
    R(F,'Desks & Workstations','Bench Workstation','8-person','8-person linear bench, 4800×1600mm, power trunking','Rapidline','Bench 8P','White',4800,1600,720,None,1,'ea',3500,12,CONT,'Epic Office Furniture, approx AUD $3499, 2025'),
    R(F,'Tables','Café / Bar Table','Oval','Oval breakout table, 1400×800mm, poseur height 1050','Generic','Oval Poseur','White',1400,800,1050,None,1,'ea',500,10,CONT,'Fast Office Furniture, approx AUD $499, 2025'),
    R(F,'Seating','Stacking Chair','Padded with tablet arm','Stacking chair with fold-out tablet arm','Rapidline','Tab Chair','Black Fabric',550,490,855,None,1,'ea',230,10,CONT,'Winc, approx AUD $229, 2025'),
    R(F,'Seating','Bar Stool','--','Velvet upholstered swivel bar stool, 75cm','Generic','Velvet Stool','Teal Velvet',430,430,760,None,1,'ea',260,8,CONT,'Officeworks, approx AUD $259, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','600mm W tall','Narrow bookcase, 600×300×1800mm, 5-shelf','Rapidline','Book 600H','White',600,300,1800,None,1,'ea',280,15,CONT,'Officeworks, approx AUD $279, 2025'),
]

# =============================================================================
# INDUSTRIAL – additional ~58 records
# =============================================================================
IND = 'Industrial'

industrial_p3 = [
    # More power tools
    R(IND,'Power Tools','Drill (Cordless)','12V compact','Compact cordless drill/driver, 12V, 2×2Ah kit','Makita','DF333DWYE','Blue',None,None,None,None,1,'ea',180,4,PE,'Bunnings, approx AUD $179, 2025'),
    R(IND,'Power Tools','Angle Grinder','125mm battery 18V','Cordless angle grinder, 125mm, 18V brushless, 1×5Ah kit','DeWALT','DCG405P1','Yellow/Black',None,None,None,None,1,'ea',280,5,PE,'Total Tools, approx AUD $279, 2025'),
    R(IND,'Power Tools','Circular Saw','Corded 2200W','Heavy duty circular saw, 235mm, 2200W','Makita','HS8391','Blue/Black',None,None,None,None,1,'ea',250,5,PE,'Total Tools, approx AUD $249, 2025'),
    R(IND,'Power Tools','Rotary Hammer Drill','SDS-Plus cordless','Cordless SDS-Plus hammer drill, 18V, 3 modes','Makita','DHR171RMJ','Blue/Black',None,None,None,None,1,'ea',480,5,PE,'Bunnings, approx AUD $479, 2025'),
    R(IND,'Power Tools','Jigsaw','Orbital action','Corded jigsaw, orbital action, 6-speed, 800W','Bosch','PST 900 PEL','Blue',None,None,None,None,1,'ea',200,5,PE,'Bunnings, approx AUD $199, 2025'),
    R(IND,'Power Tools','Random Orbital Sander','150mm','Random orbital sander, 150mm, 350W, dust bag','Makita','BO6040','Blue/Black',None,None,None,None,1,'ea',200,5,PE,'Bunnings, approx AUD $199, 2025'),
    R(IND,'Power Tools','Bench Grinder','150mm','Bench grinder, 150mm, 250W, eye shields','Ryobi','EBG150','Green',None,None,None,None,1,'ea',150,8,PE,'Bunnings, approx AUD $149, 2025'),
    R(IND,'Power Tools','Impact Wrench','18V 1/2"','Cordless impact wrench, 18V, 1/2" drive, 745Nm','Milwaukee','M18FHIWF12','Red/Black',None,None,None,None,1,'ea',500,5,PE,'Total Tools, approx AUD $499, 2025'),
    R(IND,'Power Tools','Multi-Tool','Cordless oscillating','Cordless oscillating multi-tool, 18V, 5Ah kit','Makita','DTM52RMJ','Blue/Black',None,None,None,None,1,'ea',380,5,PE,'Bunnings, approx AUD $379, 2025'),
    R(IND,'Power Tools','Nail Gun','Brad nailer','Brad nailer, 18ga, 18V cordless','DeWALT','DCN680D1','Yellow/Black',None,None,None,None,1,'ea',350,5,PE,'Bunnings, approx AUD $349, 2025'),

    # More workshop
    R(IND,'Workshop Equipment','Air Compressor','Rotary screw 10HP','Rotary screw compressor, 10HP, 270L receiver','Atlas Copco','GX7 270','Grey/Red',None,None,None,None,1,'ea',8000,15,PE,'Atlas Copco AU, approx AUD $7999, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (MIG)','350A industrial','Heavy-duty MIG welder, 350A, 3-phase, wire feeder','Lincoln Electric','PowerMIG 350MP','Red',None,None,None,None,1,'ea',4500,10,PE,'Lincoln Electric AU, approx AUD $4499, 2025'),
    R(IND,'Workshop Equipment','Tool Cabinet (Mobile)','4-drawer compact','Compact mobile tool cabinet, 4-drawer','Kincrome','K7816','Red',None,None,None,None,1,'ea',600,15,PE,'Kincrome AU, approx AUD $599, 2025'),
    R(IND,'Workshop Equipment','Workbench','Steel peg board 1500mm','Steel workbench with pegboard, 1500mm','Kincrome','K7805','Grey',1500,750,900,None,1,'ea',700,15,PE,'Kincrome AU, approx AUD $699, 2025'),
    R(IND,'Workshop Equipment','Drill Press (Bench)','12-speed','12-speed bench drill press, 550W, laser guide','Jet','JDP-13MF','Grey',None,None,None,None,1,'ea',500,10,PE,'Total Tools, approx AUD $499, 2025'),
    R(IND,'Workshop Equipment','Hydraulic Press','12-tonne','Shop press, 12-tonne, hydraulic','Peerless','12T Press','Black',None,None,None,None,1,'ea',900,15,PE,'Total Tools, approx AUD $899, 2025'),
    R(IND,'Workshop Equipment','Industrial Vacuum','HEPA backpack','HEPA backpack vacuum, asbestos/silica rated, P3','Pullman','CBS30P','Black',None,None,None,None,1,'ea',1200,7,PE,'Pullman AU, approx AUD $1199, 2025'),
    R(IND,'Workshop Equipment','Plasma Cutter','40A','Plasma cutter, 40A, hand-held torch, 12mm cut','CIGWELD','Cutmaster 40','Blue',None,None,None,None,1,'ea',1800,10,PE,'Gasweld, approx AUD $1799, 2025'),
    R(IND,'Workshop Equipment','Plasma Cutter','60A industrial','Plasma cutter, 60A, pilot arc, 20mm cut','Hypertherm','Powermax45 XP','Yellow/Black',None,None,None,None,1,'ea',4500,10,PE,'Hypertherm AU, approx AUD $4499, 2025'),

    # More materials handling
    R(IND,'Materials Handling','Platform Trolley','250kg folding','Folding platform trolley, 250kg, 900×550mm','Sureweld','PF9055','Black',900,550,None,None,1,'ea',200,8,PE,'Bunnings, approx AUD $199, 2025'),
    R(IND,'Materials Handling','Drum Trolley','Forklift drum rotator','Drum rotator attachment for forklift, 200L','Morse','93','Yellow',None,None,None,None,1,'ea',900,10,PE,'Industrial supply AU, approx AUD $899, 2025'),
    R(IND,'Materials Handling','Step Ladder','Industrial 4.5m','Industrial step ladder, 4.5m, 150kg, wide tread','Bailey','FS150-14','Fibreglass',None,None,4500,None,1,'ea',550,10,PE,'Bunnings, approx AUD $549, 2025'),
    R(IND,'Materials Handling','Extension Ladder','12m fibreglass','Fibreglass extension ladder, 12m, 150kg, tri-section','Bailey','FS-36','Fibreglass',None,None,12000,None,1,'ea',900,10,PE,'Bunnings, approx AUD $899, 2025'),
    R(IND,'Materials Handling','Pallet Jack (Manual)','Low-profile 2t','Low-profile pallet jack, 2t, 85mm entry','Noblelift','PTYE2000L','Red',685,1150,1150,None,1,'ea',700,8,PE,'Bunnings, approx AUD $699, 2025'),
    R(IND,'Materials Handling','Stillage / Pallet Cage','Drop-side','Drop-side mesh stillage, 750kg','Loscam','Drop Cage','Grey',1165,840,845,None,1,'ea',850,15,PE,'Loscam AU, approx AUD $849, 2025'),
    R(IND,'Materials Handling','Order Picker','Manual reach','Manual order picker / reach truck, 200kg, 4m lift','Crown','SP 3500','Red',None,None,None,None,1,'ea',4500,8,PE,'Crown Equipment AU, approx AUD $4499, 2025'),

    # More safety
    R(IND,'Safety Equipment','Fire Extinguisher','1kg CO2','1kg CO2 extinguisher (office use)','Chubb','1CO2','Red',None,None,None,None,1,'ea',80,5,PE,'Chubb Fire AU, approx AUD $79, 2025'),
    R(IND,'Safety Equipment','Safety Cabinet (Flammable)','250L','Large flammable liquids cabinet, 250L, forklift sockets','Storemasta','SC250Y','Yellow',1080,590,1670,None,1,'ea',2500,20,PE,'Storemasta AU, approx AUD $2499, 2025'),
    R(IND,'Safety Equipment','Safety Cabinet (Corrosive)','100L','Corrosive storage cabinet, 100L, sump, 2-door','Storemasta','CC100W','White',870,460,850,None,1,'ea',1500,20,PE,'Storemasta AU, approx AUD $1499, 2025'),
    R(IND,'Safety Equipment','Spill Kit','1100L IBC bund','IBC containment bund / spill berm, 1100L','Spill Station','IBC Bund','Yellow',None,None,None,None,1,'ea',500,5,PE,'Spill Station AU, approx AUD $499, 2025'),
    R(IND,'Safety Equipment','First Aid Kit (Industrial)','Vehicle kit','Vehicle first aid kit, soft pouch, AS2675','Trafalgar','Vehicle Kit','Red',None,None,None,None,1,'ea',60,2,PE,'Bunnings, approx AUD $59, 2025'),

    # More measurement & detection
    R(IND,'Measurement & Detection','Gas Detector','CO/flammable fixed','Fixed CO + flammable gas detector, relay, horn/strobe','Honeywell','MIDAS','Black',None,None,None,None,1,'ea',1200,8,PE,'Honeywell AU, approx AUD $1199, 2025'),
    R(IND,'Measurement & Detection','Multimeter','Insulation tester','Insulation resistance tester, 1000V, 200GΩ','Fluke','1587FC','Yellow/Black',None,None,None,None,1,'ea',700,5,PE,'RS Components AU, approx AUD $699, 2025'),
    R(IND,'Measurement & Detection','Laser Level','Multi-line 360°','360° multi-line laser, 3×360° planes, green beam','Bosch','GTL 3-89 G','Blue',None,None,None,None,1,'ea',1200,5,PE,'Sydney Tools, approx AUD $1199, 2025'),
    R(IND,'Measurement & Detection','Tachometer','Digital contact','Contact tachometer, 0.5–20000 RPM, data hold','Extech','461893','Grey',None,None,None,None,1,'ea',250,5,PE,'RS Components AU, approx AUD $249, 2025'),
    R(IND,'Measurement & Detection','Noise Meter','Class 1 precision','Class 1 precision sound level analyser, octave bands','Rion','NL-42','Black',None,None,None,None,1,'ea',2500,5,PE,'ACCO AU, approx AUD $2499, 2025'),
    R(IND,'Measurement & Detection','Thermal Imaging Camera','FLIR mid-range','FLIR thermal camera, 464×348 IR, Wi-Fi, MSX','FLIR','E76','Black',None,None,None,None,1,'ea',7000,5,PE,'RS Components AU, approx AUD $6999, 2025'),
    R(IND,'Measurement & Detection','Vibration Meter','Portable','Portable vibration meter, ISO 10816, accelerometer','Extech','VB450','Grey',None,None,None,None,1,'ea',900,5,PE,'RS Components AU, approx AUD $899, 2025'),
    R(IND,'Measurement & Detection','Anemometer','Vane','Vane anemometer, 0.4–30 m/s, temperature','Testo','405i','Black',None,None,None,None,1,'ea',500,5,PE,'RS Components AU, approx AUD $499, 2025'),
    R(IND,'Measurement & Detection','Pressure Gauge','Digital','Digital pressure gauge, 0–700 bar, 1/4" BSP','Wika','CPG500','Black',None,None,None,None,1,'ea',350,5,PE,'RS Components AU, approx AUD $349, 2025'),
    R(IND,'Measurement & Detection','Oscilloscope','2-channel 70MHz','2-channel digital oscilloscope, 70MHz, 1Gs/s','Rigol','DS1054Z','Black',None,None,None,None,1,'ea',550,5,PE,'RS Components AU, approx AUD $549, 2025'),
]

# =============================================================================
# INFORMATION TECHNOLOGY – additional ~37 records
# =============================================================================
IT = 'Information Technology'

it_p3 = [
    # More computing
    R(IT,'Computing','Laptop / Notebook','MacBook Pro 16"','MacBook Pro 16", M4 Max, 48GB, 1TB SSD','Apple','MacBook Pro 16" M4 Max','Space Black',358,248,17,None,1,'ea',5500,5,CONT,'Apple AU, approx AUD $5499, 2025'),
    R(IT,'Computing','Laptop / Notebook','Business 13"','Business ultrabook, 13.3", Core i5, 16GB, 512GB','Lenovo','ThinkPad E13','Black',308,213,17,None,1,'ea',1500,4,CONT,'Lenovo AU, approx AUD $1499, 2025'),
    R(IT,'Computing','Laptop / Notebook','Gaming/workstation','Mobile workstation, 15.6", Ryzen 9, 32GB, RTX 4070','ASUS','ProArt Studio 16','Black',354,258,19,None,1,'ea',4000,4,CONT,'JB Hi-Fi, approx AUD $3999, 2025'),
    R(IT,'Computing','Tablet','Android 12.4"','Android tablet, 12.4", 2K display, S-Pen','Samsung','Tab S9+','Beige',285,185,6,None,1,'ea',1300,4,CONT,'JB Hi-Fi, approx AUD $1299, 2025'),
    R(IT,'Computing','Tablet','Rugged 10"','Rugged tablet, 10", IP67, drop rated, 4G LTE','Panasonic','Toughbook G2','Black',256,198,21,None,1,'ea',4500,5,CONT,'Panasonic AU, approx AUD $4499, 2025'),
    R(IT,'Computing','Desktop Computer (AIO)','21.5"','All-in-one PC, 21.5", Core i3, 8GB, 512GB SSD','HP','ProOne 400 G9','Silver',None,None,None,21.5,1,'ea',1200,5,CONT,'HP AU, approx AUD $1199, 2025'),
    R(IT,'Computing','Server (Tower)','Rack 1U','1U rack server, dual Xeon, 256GB ECC, 8TB RAID','Dell','PowerEdge R550','Black',482,680,44,None,1,'ea',12000,5,CONT,'Dell AU, approx AUD $11999, 2025'),
    R(IT,'Computing','Mini PC / NUC','i7 performance','Mini PC, Core i7, 32GB, 1TB SSD, dual HDMI','Intel','NUC 14 Pro+','Black',117,112,54,None,1,'ea',1400,5,CONT,'JB Hi-Fi, approx AUD $1399, 2025'),
    R(IT,'Computing','Docking Station','Universal USB-A','Universal USB-A docking station, dual monitor, 60W','Targus','DOCK182','Black',180,85,25,None,1,'ea',250,4,CONT,'Officeworks, approx AUD $249, 2025'),

    # More display & peripherals
    R(IT,'Display & Peripherals','Monitor / Screen','24" touch','24" Full HD touch monitor, 10-point, HDMI','ViewSonic','TD2465','Black',None,None,None,24,1,'ea',700,6,CONT,'Scorptec, approx AUD $699, 2025'),
    R(IT,'Display & Peripherals','Monitor / Screen','49" ultrawide','49" ultrawide curved monitor, 5120×1440','Samsung','S49C950UA','Black',None,None,None,49,1,'ea',2200,6,CONT,'JB Hi-Fi, approx AUD $2199, 2025'),
    R(IT,'Display & Peripherals','Printer (Desktop)','Wide-format A1','Wide-format printer, A1, 24", CAD/GIS prints','HP','DesignJet T250','White',None,None,None,None,1,'ea',1200,5,CONT,'HP AU, approx AUD $1199, 2025'),
    R(IT,'Display & Peripherals','Printer (Multifunction)','A4 Mono high-speed','A4 mono MFP, 55ppm, staple/finisher','Konica Minolta','bizhub 458e','Grey',480,560,740,None,1,'ea',4000,7,CONT,'CopierChoice AU, approx AUD $3999, 2025'),
    R(IT,'Display & Peripherals','Scanner (Flatbed)','A3 flatbed','A3 flatbed scanner, 1200dpi, USB 3.0','Epson','Perfection V850 Pro','White',305,442,110,None,1,'ea',1100,5,CONT,'Officeworks, approx AUD $1099, 2025'),
    R(IT,'Display & Peripherals','UPS (Battery Backup)','2200VA rack','UPS 2200VA/1980W, rack mount, pure sine wave','APC','SRT2200RMXLI','Black',482,680,88,None,1,'ea',1200,5,CONT,'Winc, approx AUD $1199, 2025'),
    R(IT,'Display & Peripherals','Webcam','Conference 4K wide','4K conference webcam, 120° FOV, dual mic','Logitech','MX Brio 705','Black',None,None,None,None,1,'ea',500,4,CONT,'Officeworks, approx AUD $499, 2025'),
    R(IT,'Display & Peripherals','Keyboard','Mechanical wireless','Wireless mechanical keyboard, Cherry MX, backlit','Logitech','MX Keys S','Dark Grey',430,132,24,None,1,'ea',200,4,CONT,'Officeworks, approx AUD $199, 2025'),
    R(IT,'Display & Peripherals','Mouse','Vertical ergonomic','Vertical ergonomic mouse, wireless, 7-button','Logitech','MX Vertical','Graphite',79,74,120,None,1,'ea',130,4,CONT,'Officeworks, approx AUD $129, 2025'),
    R(IT,'Display & Peripherals','Barcode Scanner','Handheld 2D','Handheld 2D barcode scanner, USB, imager','Zebra','DS4608','Black',None,None,None,None,1,'ea',300,5,CONT,'Zebra AU, approx AUD $299, 2025'),
    R(IT,'Display & Peripherals','Barcode Scanner','Wireless 2D','Wireless 2D barcode scanner, Bluetooth, cradle','Zebra','DS8178','Black',None,None,None,None,1,'ea',500,5,CONT,'Zebra AU, approx AUD $499, 2025'),

    # More networking
    R(IT,'Networking & Communications','Network Switch','Core layer 3','L3 managed switch, 24-port SFP+, 10G','Cisco','CBS350-24S-4G','Black',440,242,44,None,1,'ea',3500,7,CONT,'Winc, approx AUD $3499, 2025'),
    R(IT,'Networking & Communications','Wireless Access Point','Outdoor','Outdoor Wi-Fi 6 access point, IP67, 4×4','Cisco','CW9163I','White',None,None,None,None,1,'ea',1800,5,CONT,'Winc, approx AUD $1799, 2025'),
    R(IT,'Networking & Communications','Firewall / Router','SOHO','SOHO router/firewall, 1Gbps, VPN, 5-port','Sophos','XGS87','Black',None,None,None,None,1,'ea',900,5,CONT,'Sophos AU, approx AUD $899, 2025'),
    R(IT,'Networking & Communications','NAS (Network Storage)','2-bay desktop','2-bay NAS, RAID 1, 8TB usable, home/SOHO','Synology','DS223','Black',100,226,165,None,1,'ea',550,5,CONT,'Synology AU, approx AUD $549, 2025'),
    R(IT,'Networking & Communications','PABX / IP PBX','Cloud-hybrid','Cloud-hybrid PBX, 24 extensions, SIP trunk','Yealink','P-Series P5 HS','Black',None,None,None,None,1,'ea',3000,7,CONT,'Yealink AU, approx AUD $2999, 2025'),
    R(IT,'Networking & Communications','VoIP Phone','Conference','IP conference phone, 360° mic, Bluetooth','Yealink','CP965','Black',230,230,60,None,1,'ea',800,5,CONT,'Yealink AU, approx AUD $799, 2025'),
    R(IT,'Networking & Communications','VoIP Phone','DECT cordless','DECT wireless IP phone, 10-hour talk time','Yealink','W73P','Black',None,None,None,None,1,'ea',300,5,CONT,'Yealink AU, approx AUD $299, 2025'),
    R(IT,'Networking & Communications','Patch Panel','48-port','48-port Cat6A patch panel, angled, 2U rack','Netgear','NPP48UPS100','Black',482,95,88,None,1,'ea',200,10,CONT,'Winc, approx AUD $199, 2025'),
    R(IT,'Networking & Communications','Network Rack','42U full-size','42U full-size data cabinet, 800mm wide, glass door','APC','AR3150','Black',600,1070,2020,None,1,'ea',2500,15,CONT,'Winc, approx AUD $2499, 2025'),
]

# =============================================================================
# AUDIO VISUAL – additional ~35 records
# =============================================================================
AV = 'Audio Visual'

av_p3 = [
    # More display systems
    R(AV,'Display Systems','Flat Screen TV','43"','43" 4K Smart TV, HDR10, 3×HDMI','Samsung','QA43Q67D','Black',None,None,None,43,1,'ea',750,8,CONT,'Harvey Norman, approx AUD $749, 2025'),
    R(AV,'Display Systems','Flat Screen TV','50"','50" 4K UHD Smart TV, Google TV','Sony','KD-50X80L','Black',None,None,None,50,1,'ea',1100,8,CONT,'Harvey Norman, approx AUD $1099, 2025'),
    R(AV,'Display Systems','Flat Screen TV','55" commercial','55" commercial display, full HD, 18/7 rated','Samsung','QB55B','Black',None,None,None,55,1,'ea',1800,8,CONT,'Samsung Business AU, approx AUD $1799, 2025'),
    R(AV,'Display Systems','Projector','4000 lumen laser','Laser projector, 4000 lumens, WUXGA, 20K hrs','Epson','EB-L410U','White',None,None,None,None,1,'ea',4500,10,CONT,'Epson AU, approx AUD $4499, 2025'),
    R(AV,'Display Systems','Projector','Mini/portable','Portable mini projector, 900 lumens, 1080p, HDMI/USB','Anker','Nebula Cosmos Max','Black',None,None,None,None,1,'ea',1200,5,CONT,'JB Hi-Fi, approx AUD $1199, 2025'),
    R(AV,'Display Systems','Projection Screen','Portable tripod 2m','Tripod portable screen, 2m W, 16:9','Screenline','Tripod 2m','White',2000,None,None,None,1,'ea',250,8,CONT,'AV distributor AU, approx AUD $249, 2025'),
    R(AV,'Display Systems','Interactive Whiteboard','86"','86" interactive display, 4K, 20-touch, USB-C','Clevertouch','Impact Plus 86','Black',None,None,None,86,1,'ea',8500,7,CONT,'Clevertouch AU, approx AUD $8499, 2025'),
    R(AV,'Display Systems','Digital Signage Screen','32"','32" commercial digital signage, FHD, 24/7','LG','32SM5KE-B','Black',None,None,None,32,1,'ea',1100,7,CONT,'LG Business AU, approx AUD $1099, 2025'),
    R(AV,'Display Systems','LED Video Wall','Direct view 2×3','Direct view LED display system, fine pitch 1.5mm, 2×3m','Absen','Acclaim 1.5','Black',None,None,None,None,1,'ea',25000,10,CONT,'Absen AU distributor, approx AUD $24999, 2025'),

    # More video conferencing
    R(AV,'Video Conferencing','Video Bar (All-in-One)','Huddle room','Compact video bar, 4K, auto-framing, Zoom certified','Jabra','PanaCast 50','Black',None,None,None,None,1,'ea',3200,5,CONT,'Jabra AU, approx AUD $3199, 2025'),
    R(AV,'Video Conferencing','PTZ Camera','IP streaming','IP PTZ camera, 4K, 30×, NDI/HX, streaming','Panasonic','AW-UE70','White',None,None,None,None,1,'ea',5000,5,CONT,'Panasonic AU, approx AUD $4999, 2025'),
    R(AV,'Video Conferencing','Conferencing Speakerphone','USB table','Table USB speakerphone, 8-mic array, 360° pickup','EPOS','EXPAND 40T','Black',None,None,None,None,1,'ea',550,4,CONT,'EPOS AU, approx AUD $549, 2025'),
    R(AV,'Video Conferencing','Video Conferencing Codec','Boardroom','Boardroom kit with 4K camera, touch 10, codec','Cisco','Room Kit Pro','Black',None,None,None,None,1,'ea',18000,5,CONT,'Cisco AU, approx AUD $17999, 2025'),
    R(AV,'Video Conferencing','Collaboration Touch Panel','55" room display','55" room scheduling / booking display, Android','Logitech','Tap Scheduler','White',None,None,None,55,1,'ea',1800,5,CONT,'Logitech AU, approx AUD $1799, 2025'),

    # More audio
    R(AV,'Audio Systems','Ceiling Speaker','70V commercial','70V/100V commercial ceiling speaker, 6W, white','Bosch','LC4-PC30G-4','White',None,None,None,None,1,'ea',250,10,CONT,'Bosch AU, approx AUD $249, 2025'),
    R(AV,'Audio Systems','Amplifier','Class-D 4ch','Class-D 4×250W commercial amplifier, DSP, Dante','Crown','DCi 4|300N','Black',440,240,44,None,1,'ea',2000,10,CONT,'Crown AU, approx AUD $1999, 2025'),
    R(AV,'Audio Systems','Wireless Microphone System','Conference table','Wireless conference table mic system, multi-channel','Shure','MXA910-A','Black',None,None,None,None,1,'ea',2800,8,CONT,'Shure AU, approx AUD $2799, 2025'),
    R(AV,'Audio Systems','Soundbar','Business certified','Teams-certified soundbar for meeting rooms','Yealink','MSpeaker II','Black',None,None,None,None,1,'ea',500,5,CONT,'Yealink AU, approx AUD $499, 2025'),
    R(AV,'Audio Systems','AV Receiver / Amplifier','9.4ch','9.4ch AV receiver, 4K, 11.2 pre-out, Auro-3D','Denon','AVR-X4800H','Black',435,192,361,None,1,'ea',1800,8,CONT,'JB Hi-Fi, approx AUD $1799, 2025'),

    # More AV control
    R(AV,'AV Control & Distribution','AV Control System','Rack controller','AV rack mount control system, 3-series, Ethernet','Crestron','CP4','Black',440,310,44,None,1,'ea',5000,8,CONT,'Crestron AU, approx AUD $4999, 2025'),
    R(AV,'AV Control & Distribution','AV Matrix Switcher','4×4 HDMI 4K','4×4 HDMI matrix switcher, 4K@60Hz, HDR','Atlona','AT-UHD44M','Black',440,183,44,None,1,'ea',1200,8,CONT,'AV distributor AU, approx AUD $1199, 2025'),
    R(AV,'AV Control & Distribution','Streaming / Presentation PC','4K media player','Commercial 4K media player, Android, scheduled playback','BrightSign','LS445','Black',None,None,None,None,1,'ea',500,5,CONT,'BrightSign AU, approx AUD $499, 2025'),
    R(AV,'AV Control & Distribution','HDMI Splitter','8-way','8-way HDMI splitter, 4K@30Hz, HDCP','Generic','HDMI-SP8','Black',220,100,30,None,1,'ea',200,5,CONT,'Scorptec, approx AUD $199, 2025'),
]

# =============================================================================
# VEHICLES – additional ~19 records
# =============================================================================
VH = 'Vehicles & Motorised Plant'

vehicles_p3 = [
    R(VH,'Motor Vehicles','Passenger Car','Budget hatch','Budget small hatch, 4cyl petrol, 5-door, manual','Suzuki','Swift GL','White',3845,1735,1480,None,1,'ea',22000,8,MV,'Suzuki AU, approx AUD $21990, 2025'),
    R(VH,'Motor Vehicles','Passenger Car','Hybrid compact','Compact hybrid sedan, 1.8L, self-charging','Toyota','Corolla Ascent Sport Hybrid','White',4620,1780,1435,None,1,'ea',36000,8,MV,'Toyota AU, approx AUD $35990, 2025'),
    R(VH,'Motor Vehicles','SUV / 4WD','Compact SUV petrol','Compact SUV, 2.5L petrol, AWD, 7-seat','Toyota','RAV4 GXL','White',4600,1855,1685,None,1,'ea',50000,8,MV,'Toyota AU, approx AUD $49990, 2025'),
    R(VH,'Motor Vehicles','SUV / 4WD','Large diesel 7-seat','Large diesel SUV, 2.8L turbo, 4WD, 7-seat','Mitsubishi','Pajero Sport Exceed','White',4785,1815,1835,None,1,'ea',60000,8,MV,'Mitsubishi AU, approx AUD $59990, 2025'),
    R(VH,'Motor Vehicles','Utility Vehicle (Ute)','4WD single cab tray','Single-cab tray ute, diesel, 4WD, service body','Mazda','BT-50 XT','White',5370,1850,1810,None,1,'ea',42000,8,MV,'Mazda AU, approx AUD $41990, 2025'),
    R(VH,'Motor Vehicles','Van / People Mover','SWB cargo van','SWB cargo van, petrol, 5-speed','Hyundai','iLoad SWB','White',4925,1915,1980,None,1,'ea',38000,10,MV,'Hyundai AU, approx AUD $37990, 2025'),
    R(VH,'Motor Vehicles','Electric Vehicle','EV van','Electric cargo van, 150kW, 350km range','LDV','EV DELIVER 9','White',5960,2000,2565,None,1,'ea',75000,10,MV,'LDV AU, approx AUD $74990, 2025'),
    R(VH,'Motorised Plant','Forklift','2t diesel counterbalance','Diesel counterbalance forklift, 2t, 3m mast','Hyster','H2.0XT','Yellow',1150,2400,2100,None,1,'ea',42000,10,PE,'Hyster AU, approx AUD $41990, 2025'),
    R(VH,'Motorised Plant','Pallet Jack (Electric)','High-lift walkie','High-lift electric pallet stacker, 1t, 1.6m lift','Crown','SHR 5700','Blue',760,1400,1800,None,1,'ea',9500,8,PE,'Crown Equipment AU, approx AUD $9499, 2025'),
    R(VH,'Motorised Plant','Scissor Lift','14m rough terrain','Rough terrain scissor lift, 14m, 680kg, diesel','JLG','4394RT','Yellow',2440,3660,2390,None,1,'ea',75000,12,PE,'JLG AU, approx AUD $74990, 2025'),
    R(VH,'Motorised Plant','Generator (Portable)','3.5kVA petrol inverter','Inverter generator, 3.5kVA, silent run, pure sine','Honda','EU35i','Red',640,540,450,None,1,'ea',2500,8,PE,'Honda AU, approx AUD $2499, 2025'),
    R(VH,'Motorised Plant','Generator (Standby)','100kVA diesel','Standby diesel generator, 100kVA, 3-phase, canopy','Cummins','C100D5H','Yellow/Green',3200,1200,2000,None,1,'ea',75000,15,PE,'Cummins AU, approx AUD $74990, 2025'),
    R(VH,'Motorised Plant','Walk-behind Mower','Petrol mulching','Commercial petrol mulching mower, 22" cut','Honda','HRX537HY','Red',570,480,990,None,1,'ea',1800,7,PE,'Bunnings, approx AUD $1799, 2025'),
    R(VH,'Motorised Plant','Ride-on Sweeper','Industrial vacuum sweeper','Industrial vacuum ride-on sweeper, 2t, diesel','Tennant','8400 XP','Orange',1640,2710,2130,None,1,'ea',55000,10,PE,'Tennant AU, approx AUD $54990, 2025'),
    R(VH,'Motorised Plant','Golf Cart / EV Buggy','Hospital porter buggy','Hospital porter / patient transport buggy, electric','Generic','Med Buggy','White',2200,1200,1600,None,1,'ea',15000,8,PE,'Healthcare transport AU, approx AUD $14990, 2025'),
    R(VH,'Motorised Plant','High-Pressure Cleaner','Industrial hot water skid','Industrial hot water pressure washer, skid mount, diesel','Karcher','HDS 14/20-4','Yellow',1800,900,1200,None,1,'ea',15000,8,PE,'Karcher AU, approx AUD $14990, 2025'),
    R(VH,'Motorised Plant','Boom Lift (Cherry Picker)','6m compact','Self-propelled compact boom lift, 6m, electric','Genie','Z-34/22','Yellow',1800,3560,2060,None,1,'ea',38000,10,PE,'Genie AU, approx AUD $37990, 2025'),
    R(VH,'Motorised Plant','Forklift','1t reach truck','Electric reach truck, 1t, 6m lift, narrow aisle','Crown','RR 5700','Red',None,None,None,None,1,'ea',35000,10,PE,'Crown Equipment AU, approx AUD $34990, 2025'),
    R(VH,'Motorised Plant','Generator (Portable)','15kVA diesel trailer','15kVA trailer-mounted diesel generator, 3-phase, automatic','Pramac','E15000','Yellow',None,None,None,None,1,'ea',12000,10,PE,'Generator World AU, approx AUD $11990, 2025'),
]

# =============================================================================
# SAFES – additional ~17 records
# =============================================================================
SS = 'Safes & Storage'

safes_p3 = [
    R(SS,'Safes','Cash / Petty Cash Safe','Countertop mini','Mini cash safe, 8L, digital, anti-tamper','Guardall','GD08','Grey',200,250,170,None,1,'ea',220,15,CONT,'Buy A Safe AU, approx AUD $219, 2025'),
    R(SS,'Safes','Cash / Petty Cash Safe','120L high capacity','High capacity cash safe, 120L, electronic lock, re-locker','Chubb','DPC 120','Grey',430,560,500,None,1,'ea',1500,15,CONT,'Precision Safes AU, approx AUD $1499, 2025'),
    R(SS,'Safes','Deposit Safe','Dual-door','Dual-door deposit safe, 80L, cash+coin capacity','Guardall','GDD80','Grey',340,460,720,None,1,'ea',1200,15,CONT,'Buy A Safe AU, approx AUD $1199, 2025'),
    R(SS,'Safes','Drug / Narcotic Safe','S2 wall mount','Drug safe, S2, wall-mount, dual key','Chubb','Narcotic WM S2','White',200,250,250,None,1,'ea',900,15,CONT,'Precision Safes AU, approx AUD $899, 2025'),
    R(SS,'Safes','Fire Safe','Media/data safe','Data/media safe, 1hr fire, 60°C interior limit','Chubb','Data 30','Grey',300,380,300,None,1,'ea',1500,15,CONT,'Buy A Safe AU, approx AUD $1499, 2025'),
    R(SS,'Safes','Floor Safe','Burglary rated B1','In-floor safe, B1 burglary, combination lock, 20L','Guardall','FS20-B1','Grey',350,350,180,None,1,'ea',1800,15,CONT,'Buy A Safe AU, approx AUD $1799, 2025'),
    R(SS,'Safes','Wall Safe','Digital keypad','Wall safe, digital keypad, 15L, stud mount','Guardall','WS15D','Grey',350,250,250,None,1,'ea',450,15,CONT,'Buy A Safe AU, approx AUD $449, 2025'),
    R(SS,'Safes','Gun / Firearm Safe','Pistol safe biometric','Biometric quick-access pistol safe','Hornady','Rapid Safe 2700','Black',300,220,85,None,1,'ea',500,10,CONT,'Firearms AU, approx AUD $499, 2025'),
    R(SS,'Safes','Laptop / IT Security Safe','6-unit','Laptop/device safe, 6-unit, ventilated, charging outlets','Datamation','DS-LKN-6','Black',450,550,430,None,1,'ea',600,10,CONT,'Winc, approx AUD $599, 2025'),
    R(SS,'Safes','Key Cabinet Safe','200-hook managed','Key management system, 200-hook, RFID access, audit','Traka','Traka210','White',400,110,1000,None,1,'ea',5000,10,CONT,'Traka AU, approx AUD $4999, 2025'),
    R(SS,'Safes','Cash / Petty Cash Safe','Underdesk bolted','Under-desk cash safe, 30L, bolt-down, key lock','Guardall','GD30B','Grey',300,380,300,None,1,'ea',480,15,CONT,'Buy A Safe AU, approx AUD $479, 2025'),
    R(SS,'Safes','Fire Safe','Home/office 30L','Home/office fire safe, 1hr rating, 30L, digital','Chubb','Home 30 Fire','Grey',360,350,330,None,1,'ea',650,15,CONT,'Harvey Norman, approx AUD $649, 2025'),
    R(SS,'Safes','Deposit Safe','Rotary drum','Rotary drum deposit safe, 20L, stainless drum, anti-fish','Chubb','Rotary D20','Grey',300,380,550,None,1,'ea',950,15,CONT,'Buy A Safe AU, approx AUD $949, 2025'),
    R(SS,'Safes','Gun / Firearm Safe','24-gun premium','Premium firearm safe, 24 rifles/handguns, 3-hour fire rating','Rhino','Ironworks 5928F','Black',760,590,1500,None,1,'ea',4500,20,CONT,'Firearms AU, approx AUD $4499, 2025'),
    R(SS,'Safes','Cash / Petty Cash Safe','Pharmacy dispensary','Pharmacy dispensary safe, 60L, restricted access, audit log','Chubb','Pharma Safe','White',350,450,380,None,1,'ea',2000,15,CONT,'Precision Safes AU, approx AUD $1999, 2025'),
    R(SS,'Safes','Key Cabinet Safe','25-hook','Key cabinet, 25-hook, key lock, white','Kaba Mas','Key 25','White',180,80,270,None,1,'ea',150,15,CONT,'Winc, approx AUD $149, 2025'),
    R(SS,'Safes','Fire Safe','Underfloor data','Underfloor data safe, fire/water rated, for server rooms','Kaba','Underfloor Data','Black',600,600,300,None,1,'ea',3500,20,CONT,'Precision Safes AU, approx AUD $3499, 2025'),
]

# =============================================================================
# OFFICE EQUIPMENT – additional ~10 records
# =============================================================================
OE = 'Office Equipment'

office_p3 = [
    R(OE,'Mail & Document','Shredder','Strip-cut high capacity','Strip-cut shredder, high capacity, 30L bin, 18 sheets','Rexel','Auto+ 300X','Black',270,410,570,None,1,'ea',350,5,CONT,'Officeworks, approx AUD $349, 2025'),
    R(OE,'Mail & Document','Laminator','A4 commercial','Commercial A4 laminator, 80/125/250 micron, auto-heat','Fellowes','Venus A4','Black',365,80,55,None,1,'ea',180,5,CONT,'Officeworks, approx AUD $179, 2025'),
    R(OE,'Mail & Document','Franking Machine','High volume','High-volume digital franking machine, weigh platform','Pitney Bowes','SendPro+','Grey',None,None,None,None,1,'ea',5000,5,CONT,'Pitney Bowes AU, approx AUD $4999, 2025'),
    R(OE,'Mail & Document','Label Printer','Barcode thermal transfer','Thermal transfer barcode label printer, 203dpi, 4" wide','Zebra','ZD421','Grey',None,None,None,None,1,'ea',700,5,CONT,'Zebra AU, approx AUD $699, 2025'),
    R(OE,'Presentation','Flip Chart Easel','Mobile whiteboard easel','Mobile double-sided whiteboard easel 900×600mm','Visionchart','Mobile Easel','White',None,None,1800,None,1,'ea',350,8,CONT,'Officeworks, approx AUD $349, 2025'),
    R(OE,'Presentation','Lectern / Podium','Height adjustable','Height-adjustable steel lectern, A4 surface, mic slot','Generic','Adjustable Lectern','Black',500,500,1250,None,1,'ea',400,10,CONT,'AV distributor AU, approx AUD $399, 2025'),
    R(OE,'Presentation','Projection Trolley','Lockable AV trolley','Lockable AV/laptop trolley with power strip, castors','Balt','Balt Locking Cart','Black',700,530,1250,None,1,'ea',500,8,CONT,'AV distributor AU, approx AUD $499, 2025'),
    R(OE,'Security','Cash Register','Self-service kiosk','Self-service payment kiosk, touch screen, EFTPOS','NCR','CX7','Black',None,None,None,None,1,'ea',4000,5,CONT,'NCR AU, approx AUD $3999, 2025'),
    R(OE,'Security','ID Card Printer','Retransfer double-side','Retransfer dual-side ID printer, 300dpi, Ethernet','Fargo','HDPii Plus','Grey',None,None,None,None,1,'ea',3500,5,CONT,'HID Global AU, approx AUD $3499, 2025'),
    R(OE,'Security','EFTPOS / Payment Terminal','Unattended kiosk','Unattended payment terminal, 7" screen, NFC, PIN','Verifone','MX925','Black',None,None,None,None,1,'ea',2000,4,CONT,'Verifone AU, approx AUD $1999, 2025'),
]

# =============================================================================
# MEDICAL – additional records to reach 3×
# =============================================================================
MD = 'Medical & First Aid'

medical_p3 = [
    R(MD,'Medical Equipment','Examination Table','Massage table','Portable massage/treatment table, aluminium, padded','EarthLite','Harmony DX','White',183,71,76,None,1,'ea',600,8,CONT,'Massage table AU, approx AUD $599, 2025'),
    R(MD,'Medical Equipment','Medical Trolley','Medication trolley','Medication dispensing trolley with drawers, locking','Generic','MedTrolley','White',550,450,960,None,1,'ea',1200,10,PE,'Medshop AU, approx AUD $1199, 2025'),
    R(MD,'Medical Equipment','Blood Pressure Monitor','Mercury sphygmomanometer replacement','Aneroid sphygmomanometer, calibrated, desk stand','Riester','Big Ben','Black',None,None,None,None,1,'ea',350,8,CONT,'Medshop AU, approx AUD $349, 2025'),
    R(MD,'Medical Equipment','Nebuliser','Ultrasonic mesh','Portable mesh nebuliser, silent, USB charge','OMRON','MicroAIR U100','White',None,None,None,None,1,'ea',300,5,CONT,'Chemist Warehouse AU, approx AUD $299, 2025'),
    R(MD,'Medical Equipment','Wheelchair','Electric power','Electric power wheelchair, 6km/h, joystick, 120kg','Pride','Jazzy 600 ES','Black',None,None,None,None,1,'ea',4500,7,CONT,'Medshop AU, approx AUD $4499, 2025'),
    R(MD,'Medical Equipment','Height/Weight Scale','BMI scale','BMI/body composition scale, Wi-Fi, 180kg','Seca','mBCA 515','White',None,None,None,None,1,'ea',3500,10,CONT,'Seca AU, approx AUD $3499, 2025'),
    R(MD,'Medical Equipment','Pulse Oximeter','Table-top','Table-top pulse oximeter, large display, alarm','Nellcor','N-595','White',None,None,None,None,1,'ea',900,5,CONT,'Medshop AU, approx AUD $899, 2025'),
    R(MD,'First Aid','AED (Defibrillator)','Outdoor cabinet','Heated outdoor AED cabinet, 24/7, audible alarm','Generic','AED Outdoor Cab','White/Green',None,None,None,None,1,'ea',600,15,CONT,'Defibshop AU, approx AUD $599, 2025'),
    R(MD,'Medical Equipment','Autoclave / Steriliser','Class B 29L','Class B autoclave, 29L, USB data export','Euronda','E10','White',600,440,260,None,1,'ea',8500,10,PE,'Euronda AU, approx AUD $8499, 2025'),
    R(MD,'Medical Equipment','Refrigerator (Medical)','Drug fridge 60L','Drug refrigerator, 60L, alarmed, GMP compliant','Vestfrost','MKF60','White',490,480,650,None,1,'ea',1500,10,PE,'Vestfrost AU, approx AUD $1499, 2025'),
]

# =============================================================================
# FITNESS – additional records to reach 3×
# =============================================================================
FT = 'Fitness & Recreation'

fitness_p3 = [
    R(FT,'Cardio Equipment','Stair Climber','Step mill','Step mill / StairMaster, commercial, 4% grade','Life Fitness','Elevation ST','Black',600,1170,1700,None,1,'ea',8000,10,CONT,'Commercial Fitness Equipment AU, approx AUD $7999, 2025'),
    R(FT,'Strength Equipment','Cable Machine (Functional Trainer)','Wall mount','Wall-mount cable station, 60kg stack × 2','Fitness Ware','WM-FT200','Black',600,300,2100,None,1,'ea',1800,12,CONT,'Compound Fitness AU, approx AUD $1799, 2025'),
    R(FT,'Strength Equipment','Barbell / Rack','EZ curl bar set','EZ curl barbell + plates 30kg + stand','Bodycraft','EZ Set','Black/Chrome',None,None,None,None,1,'set',500,10,CONT,'Rebel Sport, approx AUD $499, 2025'),
    R(FT,'Strength Equipment','Gym Machine Plate Loaded','Chest press','Plate-loaded chest press machine, dual arm','Hammer Strength','MG-CLP','Black',1420,1680,1550,None,1,'ea',3500,15,CONT,'Compound Fitness AU, approx AUD $3499, 2025'),
    R(FT,'Recreation','Air Hockey Table','Compact','Compact air hockey table, 4-foot, home use','Generic','AH-4FT','Blue',1250,660,785,None,1,'ea',450,8,CONT,'iFun AU, approx AUD $449, 2025'),
    R(FT,'Cardio Equipment','Treadmill','Light commercial fold','Light commercial folding treadmill, 18kph, 3HP','Sole','F80','Black',820,2010,1370,None,1,'ea',3200,8,CONT,'Compound Fitness AU, approx AUD $3199, 2025'),
    R(FT,'Cardio Equipment','Exercise Bike (Upright)','Air bike','Air resistance assault bike, unlimited resistance','Assault Fitness','AirBike Classic','Black',610,1020,1150,None,1,'ea',1600,8,CONT,'Compound Fitness AU, approx AUD $1599, 2025'),
]

# =============================================================================
# APPLIANCES – additional records
# =============================================================================
AP = 'Appliances & White Goods'

appliances_p3 = [
    R(AP,'Kitchen Appliances','Coffee Machine (Auto)','Instant hot water urn','Commercial hot water urn, 30L, stainless','Birko','1020103','Stainless Steel',430,290,595,None,1,'ea',600,8,CONT,'Restaurant Supply AU, approx AUD $599, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Display fridge 2-door','Display refrigerator, 2-door, 1000L, supermarket grade','Skope','FMF1300N','Stainless Steel',1322,697,2100,None,1,'ea',5500,12,CONT,'Skope AU, approx AUD $5499, 2025'),
    R(AP,'Kitchen Appliances','Microwave Oven','Heavy duty 34L','Heavy-duty commercial microwave, 34L, 2100W, stainless','Panasonic','NE-2156SR','Stainless Steel',557,490,328,None,1,'ea',1200,8,CONT,'Restaurant Supply AU, approx AUD $1199, 2025'),
    R(AP,'Kitchen Appliances','Oven','Combi oven','Commercial combi steam oven, 6×1/1GN, programmable','Rational','iCombi Pro 6-1/1','Stainless Steel',847,771,754,None,1,'ea',15000,12,CONT,'Rational AU, approx AUD $14999, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Auto)','Plumbed automatic','Plumbed automatic espresso machine, office use, 2L/hr','Franke','A300','Stainless Steel',310,440,380,None,1,'ea',3500,8,CONT,'Franke Coffee AU, approx AUD $3499, 2025'),
    R(AP,'Cleaning','Vacuum Cleaner','Industrial HEPA centralized','Centralized vacuum system, HEPA, 4 inlets, 1400W','Vacumaid','GS50','White',None,None,None,None,1,'ea',1800,10,CONT,'Vacumaid AU, approx AUD $1799, 2025'),
    R(AP,'Cleaning','Floor Polisher','High-speed burnisher','High-speed floor burnisher, 1500RPM, 450mm disc','Pullman','HS450','Black',None,None,None,None,1,'ea',1500,8,CONT,'Pullman AU, approx AUD $1499, 2025'),
]

# =============================================================================
# Combine all Part 3 records + append
# =============================================================================
part3 = (furniture_p3 + industrial_p3 + it_p3 + av_p3 + vehicles_p3 +
         safes_p3 + office_p3 + medical_p3 + fitness_p3 + appliances_p3)

out = Path('Asset_Library_AU.csv')

with open(out, 'r', encoding='utf-8') as f:
    existing = sum(1 for _ in f) - 1

start_uid = 200001 + existing

with open(out, 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    for i, rec in enumerate(part3):
        rec[0] = start_uid + i
        w.writerow(rec)

total = existing + len(part3)
print(f"Part 3 appended: {len(part3)} records")
print(f"  Furniture:             {len(furniture_p3)}")
print(f"  Industrial:            {len(industrial_p3)}")
print(f"  IT:                    {len(it_p3)}")
print(f"  Audio Visual:          {len(av_p3)}")
print(f"  Vehicles:              {len(vehicles_p3)}")
print(f"  Safes:                 {len(safes_p3)}")
print(f"  Office Equipment:      {len(office_p3)}")
print(f"  Medical:               {len(medical_p3)}")
print(f"  Fitness:               {len(fitness_p3)}")
print(f"  Appliances:            {len(appliances_p3)}")
print(f"\nTotal records in file: {total}")
print(f"UID range: 200001 – {200001 + total - 1}")
