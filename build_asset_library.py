"""
Asset Library AU – generator script
Produces Asset_Library_AU.csv starting at ID 200001.
Run in two passes: this file builds Part 1 (Furniture, IT, AV, Appliances).
Part 2 (Fitness, Vehicles, Industrial, Medical, Safes, Office) is appended by
build_asset_library_p2.py.
"""
import csv
from pathlib import Path

HEADERS = [
    'Unique ID','Asset ID (Client)','Parent Asset','Address','Level','Sub Location',
    'Asset Category (L1)','Asset Category (L2)','Asset Category (L3)','Asset Category (L4)',
    'Item Description','Condition Rating (0-5)','Condition Rating Label','Photo 1','Photo 2',
    'Quantity','Unit of Measurement','Width (mm)','Depth (mm)','Height (mm)','Screen Size (inches)',
    'Make / Brand','Model','Serial Number','Asset Tag / Label','Colour / Finish',
    'Comments / Recommendations','Unit Rate - RCN ($)','Estimated Replacement Cost ($)',
    'Remaining Useful Life (%)','Indemnity Value ($)','Insurance Schedule Category',
    'Effective Life (years)'
]

COND_LABELS = {0:'Not Present',1:'As New',2:'Good',3:'Fair',4:'Poor',5:'Very Poor'}
RUL_MAP     = {0:None,1:1.00,2:0.75,3:0.50,4:0.25,5:0.00}

def row(l1,l2,l3,l4,desc,make,model,colour,w,d,h,scr,qty,uom,rate,eff,ins,src,cond=2):
    rul = RUL_MAP[cond]
    erc = round(rate * qty, 2)
    iv  = round(erc * rul, 2) if rul is not None else 0.00
    return [
        '',       # UID assigned later
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

R = row   # shorthand

# =============================================================================
# FURNITURE
# =============================================================================
F = 'Furniture'
CONT = 'Contents'

furniture = [
    # ── Seating ───────────────────────────────────────────────────────────────
    R(F,'Seating','Task Chair','--','Ergonomic mesh task chair, adjustable lumbar & armrests','Buro','Metro II','Black Mesh',670,640,1100,None,1,'ea',650,12,CONT,'Winc, approx AUD $649, 2025'),
    R(F,'Seating','Task Chair','--','Mid-back mesh task chair, fixed arms','Rapidline','EG100','Black Mesh',650,620,1050,None,1,'ea',450,12,CONT,'Officeworks, approx AUD $449, 2025'),
    R(F,'Seating','Task Chair','--','High-back leather executive chair, chrome base','Buro','Roma','Black Leather',700,700,1250,None,1,'ea',900,12,CONT,'Winc, approx AUD $899, 2025'),
    R(F,'Seating','Task Chair','--','Budget fabric task chair, fixed height arms','Rapidline','Vesta','Grey Fabric',600,580,960,None,1,'ea',280,10,CONT,'Officeworks, approx AUD $279, 2025'),
    R(F,'Seating','Task Chair','--','Premium ergonomic task chair, fully adjustable','Herman Miller','Aeron (Size B)','Black Mesh',680,650,1070,None,1,'ea',2500,15,CONT,'Herman Miller AU, approx AUD $2499, 2025'),
    R(F,'Seating','Task Chair','--','Ergonomic task chair, 4D arms, mesh back','Humanscale','Freedom','Black Mesh',660,640,1100,None,1,'ea',1800,15,CONT,'Humanscale AU, approx AUD $1799, 2025'),
    R(F,'Seating','Task Chair','--','Mesh task chair, contoured back, nylon base','Rapidline','EG400','Black Mesh',660,640,1100,None,1,'ea',550,12,CONT,'Rapidline.com.au, approx AUD $549, 2025'),
    R(F,'Seating','Task Chair','--','Task chair, upholstered seat, mesh back, castors','Steelcase','Leap V2','Charcoal Fabric',680,660,1100,None,1,'ea',2200,15,CONT,'Steelcase AU, approx AUD $2199, 2025'),
    R(F,'Seating','Task Chair','--','Heavy-duty operator chair, 150kg rated','Buro','Tidal HD','Black Fabric',700,680,1150,None,1,'ea',750,12,CONT,'Buro.com.au, approx AUD $749, 2025'),
    R(F,'Seating','Visitor Chair','--','4-leg visitor chair, upholstered seat & back','Buro','Elan','Charcoal Fabric',545,545,800,None,1,'ea',280,10,CONT,'Officeworks, approx AUD $279, 2025'),
    R(F,'Seating','Visitor Chair','--','Chrome cantilever visitor chair, padded seat','Rapidline','CL100C','Black Fabric',560,530,830,None,1,'ea',220,10,CONT,'Officeworks, approx AUD $219, 2025'),
    R(F,'Seating','Visitor Chair','--','Visitor chair, upholstered, wood legs','Buro','Jina','Charcoal Fabric',530,530,810,None,1,'ea',350,10,CONT,'Winc, approx AUD $349, 2025'),
    R(F,'Seating','Visitor Chair','--','Stackable visitor chair with link arms','Rapidline','Eternity','Black Fabric',540,540,810,None,1,'ea',180,10,CONT,'Epic Office Furniture, approx AUD $179, 2025'),
    R(F,'Seating','Meeting Chair','--','Mesh back meeting chair, 4-star base','Buro','Mentor','Black Mesh',560,530,880,None,1,'ea',380,12,CONT,'Buro.com.au, approx AUD $379, 2025'),
    R(F,'Seating','Meeting Chair','--','Upholstered meeting chair, chrome legs','Rapidline','Endeavour','Charcoal Fabric',550,540,840,None,1,'ea',320,10,CONT,'Winc, approx AUD $319, 2025'),
    R(F,'Seating','Meeting Chair','--','Premium meeting chair, leather, castors','Buro','York','Black Leather',610,580,1000,None,1,'ea',650,12,CONT,'Buro.com.au, approx AUD $649, 2025'),
    R(F,'Seating','Meeting Chair','--','Meeting chair, mesh back, 5-star base on castors','Humanscale','Diffrient World','Black Mesh',590,560,900,None,1,'ea',1200,12,CONT,'Humanscale AU, approx AUD $1199, 2025'),
    R(F,'Seating','Stacking Chair','--','Polypropylene 4-leg stacking chair','Rapidline','Air','White',490,490,810,None,1,'ea',120,10,CONT,'Officeworks, approx AUD $119, 2025'),
    R(F,'Seating','Stacking Chair','--','Padded stacking chair, linking arms','Rapidline','Activ','Charcoal Fabric',520,490,830,None,1,'ea',160,10,CONT,'Epic Office Furniture, approx AUD $159, 2025'),
    R(F,'Seating','Stacking Chair','--','Steel frame stacking chair, upholstered','Rapidline','Nexus','Grey Fabric',520,495,840,None,1,'ea',190,10,CONT,'Fast Office Furniture, approx AUD $189, 2025'),
    R(F,'Seating','Stacking Chair','--','Heavy-duty polypropylene stacking chair','Rapidline','Pro 500','Black',490,490,800,None,1,'ea',145,10,CONT,'Winc, approx AUD $145, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Single','Single lounge chair, fabric upholstery, timber legs','Instyle','Lyndon','Charcoal Fabric',800,800,760,None,1,'ea',900,12,CONT,'Instyle.com.au, approx AUD $899, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Single','Reception tub chair, vinyl upholstery','Rapidline','Luna','Black Vinyl',710,720,730,None,1,'ea',550,12,CONT,'Fast Office Furniture, approx AUD $549, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','Single','Executive lounge chair, genuine leather','Buro','Luxe','Black Leather',830,830,870,None,1,'ea',1400,15,CONT,'Buro.com.au, approx AUD $1399, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','2-seater','2-seat sofa, fabric upholstery, timber base','Instyle','Lounge 2S','Charcoal Fabric',1400,800,760,None,1,'ea',1800,12,CONT,'Instyle.com.au, approx AUD $1799, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','2-seater','2-seat reception sofa, vinyl upholstery','Rapidline','Luna 2S','Black Vinyl',1350,720,730,None,1,'ea',1100,12,CONT,'Fast Office Furniture, approx AUD $1099, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','3-seater','3-seat sofa, fabric upholstery, metal legs','Instyle','Lounge 3S','Light Grey Fabric',2000,800,760,None,1,'ea',2400,12,CONT,'Instyle.com.au, approx AUD $2399, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','3-seater','3-seat reception sofa, vinyl','Rapidline','Luna 3S','Black Vinyl',1950,720,730,None,1,'ea',1500,12,CONT,'Epic Office Furniture, approx AUD $1499, 2025'),
    R(F,'Seating','Bar Stool','--','Adjustable height bar stool, chrome footrest','Rapidline','Alto','Black Vinyl',430,430,630,None,1,'ea',250,10,CONT,'Officeworks, approx AUD $249, 2025'),
    R(F,'Seating','Bar Stool','--','Wooden bar stool, fixed height 750mm','Generic','Timber Stool','Natural Timber',380,380,750,None,1,'ea',180,10,CONT,'Officeworks, approx AUD $179, 2025'),
    R(F,'Seating','Bar Stool','--','Padded swivel bar stool, gas lift','Buro','Alto Swivel','Black Fabric',430,430,650,None,1,'ea',320,10,CONT,'Buro.com.au, approx AUD $319, 2025'),
    R(F,'Seating','Bench Seat','--','2-seater upholstered bench seat, reception area','Rapidline','Axiom 2S','Charcoal Fabric',1200,500,450,None,1,'ea',700,12,CONT,'Epic Office Furniture, approx AUD $699, 2025'),
    R(F,'Seating','Bench Seat','--','Backless bench seat, timber frame','Generic','Timber Bench','Natural Timber',1800,400,460,None,1,'ea',500,12,CONT,'Fast Office Furniture, approx AUD $499, 2025'),
    R(F,'Seating','Drafting Chair','--','Draughtsman chair, height adjustable, footring','Buro','Vogue Draft','Black Fabric',530,520,950,None,1,'ea',480,10,CONT,'Buro.com.au, approx AUD $479, 2025'),
    R(F,'Seating','Kneeling Chair','--','Ergonomic kneeling chair, adjustable','Generic','Kneeler','Black Fabric',500,500,630,None,1,'ea',220,8,CONT,'Officeworks, approx AUD $219, 2025'),
    R(F,'Seating','Training Chair','--','Tablet-arm training chair, upholstered','Rapidline','Train','Black Fabric',590,540,870,None,1,'ea',290,10,CONT,'Winc, approx AUD $289, 2025'),

    # ── Desks & Workstations ─────────────────────────────────────────────────
    R(F,'Desks & Workstations','Straight Desk','1200mm','Straight desk, 1200×750mm, laminate top','Rapidline','Swift 1200','White',1200,750,720,None,1,'ea',350,12,CONT,'Officeworks, approx AUD $349, 2025'),
    R(F,'Desks & Workstations','Straight Desk','1500mm','Straight desk, 1500×750mm, laminate top','Rapidline','Swift 1500','White',1500,750,720,None,1,'ea',420,12,CONT,'Officeworks, approx AUD $419, 2025'),
    R(F,'Desks & Workstations','Straight Desk','1800mm','Straight desk, 1800×800mm, laminate top','Rapidline','Swift 1800','White',1800,800,720,None,1,'ea',520,12,CONT,'Winc, approx AUD $519, 2025'),
    R(F,'Desks & Workstations','Straight Desk','1500mm','Executive straight desk, 1500×750mm, timber veneer','Arteil','Exec 1500','Walnut Veneer',1500,750,730,None,1,'ea',750,15,CONT,'Epic Office Furniture, approx AUD $749, 2025'),
    R(F,'Desks & Workstations','Straight Desk','1800mm','Executive straight desk, 1800×900mm, timber veneer','Arteil','Exec 1800','Walnut Veneer',1800,900,730,None,1,'ea',950,15,CONT,'Epic Office Furniture, approx AUD $949, 2025'),
    R(F,'Desks & Workstations','Corner Desk','1500mm','Corner workstation, 1500×1500mm, laminate','Rapidline','Corner 1500','White',1500,1500,720,None,1,'ea',550,12,CONT,'Officeworks, approx AUD $549, 2025'),
    R(F,'Desks & Workstations','Corner Desk','1800mm','Corner workstation, 1800×1800mm, laminate','Rapidline','Corner 1800','White',1800,1800,720,None,1,'ea',750,12,CONT,'Fast Office Furniture, approx AUD $749, 2025'),
    R(F,'Desks & Workstations','Corner Desk','1800mm','L-shaped executive desk, 1800×1800mm, veneer','Arteil','L-Exec','Walnut Veneer',1800,1800,730,None,1,'ea',1200,15,CONT,'Epic Office Furniture, approx AUD $1199, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1400mm','Electric sit-stand desk, 1400×700mm','Ergomotion','MotionDesk 1400','White',1400,700,720,None,1,'ea',950,10,CONT,'Ergomotion.com.au, approx AUD $949, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1500mm','Electric sit-stand desk, 1500×750mm','Ergomotion','MotionDesk 1500','White',1500,750,720,None,1,'ea',1050,10,CONT,'Ergomotion.com.au, approx AUD $1049, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1800mm','Electric sit-stand desk, 1800×800mm, dual motor','Ergomotion','MotionDesk 1800','White',1800,800,720,None,1,'ea',1250,10,CONT,'Ergomotion.com.au, approx AUD $1249, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1500mm','Sit-stand desk 1500×750mm, manual crank','Officeworks','Artiss','White',1500,750,720,None,1,'ea',450,8,CONT,'Officeworks, approx AUD $449, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','1800mm','Electric sit-stand, 1800×800mm, memory presets','Yaasa','One','Matte Black',1800,800,720,None,1,'ea',1400,10,CONT,'Yaasa.com, approx AUD $1399, 2025'),
    R(F,'Desks & Workstations','Reception Desk / Counter','Single','Reception counter, single-sided, laminate','Rapidline','Recept S','White',1800,800,1100,None,1,'ea',2200,15,CONT,'Epic Office Furniture, approx AUD $2199, 2025'),
    R(F,'Desks & Workstations','Reception Desk / Counter','L-shape','Reception counter, L-shape, laminate','Rapidline','Recept L','White',2400,1200,1100,None,1,'ea',3500,15,CONT,'Fast Office Furniture, approx AUD $3499, 2025'),
    R(F,'Desks & Workstations','Credenza / Desk Return','1200mm','Desk return / credenza, 1200×500mm, laminate','Rapidline','Return 1200','White',1200,500,720,None,1,'ea',280,12,CONT,'Officeworks, approx AUD $279, 2025'),
    R(F,'Desks & Workstations','Credenza / Desk Return','1600mm','Desk return / credenza, 1600×500mm, laminate','Rapidline','Return 1600','White',1600,500,720,None,1,'ea',350,12,CONT,'Winc, approx AUD $349, 2025'),
    R(F,'Desks & Workstations','Bench Workstation','2-person','2-person bench workstation, 2400×800mm','Rapidline','Bench 2P','White',2400,800,720,None,1,'ea',900,12,CONT,'Fast Office Furniture, approx AUD $899, 2025'),
    R(F,'Desks & Workstations','Bench Workstation','4-person','4-person bench workstation, 4800×1600mm','Rapidline','Bench 4P','White',4800,1600,720,None,1,'ea',1800,12,CONT,'Epic Office Furniture, approx AUD $1799, 2025'),

    # ── Tables ───────────────────────────────────────────────────────────────
    R(F,'Tables','Meeting Table','1800mm 6-person','Rectangular meeting table, 1800×900mm','Rapidline','MTable 1800','White',1800,900,720,None,1,'ea',700,15,CONT,'Officeworks, approx AUD $699, 2025'),
    R(F,'Tables','Meeting Table','2100mm 8-person','Rectangular meeting table, 2100×1000mm','Rapidline','MTable 2100','White',2100,1000,720,None,1,'ea',900,15,CONT,'Fast Office Furniture, approx AUD $899, 2025'),
    R(F,'Tables','Meeting Table','2400mm 10-person','Rectangular meeting table, 2400×1000mm','Rapidline','MTable 2400','White',2400,1000,730,None,1,'ea',1100,15,CONT,'Epic Office Furniture, approx AUD $1099, 2025'),
    R(F,'Tables','Meeting Table','1800mm round','Round meeting table, 1800mm dia, laminate','Rapidline','MTable Rd 1800','White',1800,1800,720,None,1,'ea',900,15,CONT,'Epic Office Furniture, approx AUD $899, 2025'),
    R(F,'Tables','Boardroom Table','3000mm 12-person','Boardroom table, 3000×1200mm, veneer, cable tray','Arteil','Board 3000','Walnut Veneer',3000,1200,750,None,1,'ea',3500,20,CONT,'Epic Office Furniture, approx AUD $3499, 2025'),
    R(F,'Tables','Boardroom Table','4200mm 16-person','Boardroom table, 4200×1200mm, veneer, cable management','Arteil','Board 4200','Walnut Veneer',4200,1200,750,None,1,'ea',6000,20,CONT,'Epic Office Furniture, approx AUD $5999, 2025'),
    R(F,'Tables','Boardroom Table','3600mm 14-person','Boardroom table, 3600×1200mm, laminate, power module','Rapidline','Board 3600','Black',3600,1200,750,None,1,'ea',4500,20,CONT,'Fast Office Furniture, approx AUD $4499, 2025'),
    R(F,'Tables','Training Table','1200mm','Folding training table, 1200×600mm, laminate','Rapidline','Train 1200','White',1200,600,730,None,1,'ea',280,10,CONT,'Officeworks, approx AUD $279, 2025'),
    R(F,'Tables','Training Table','1500mm','Folding training table, 1500×750mm, laminate','Rapidline','Train 1500','White',1500,750,730,None,1,'ea',350,10,CONT,'Winc, approx AUD $349, 2025'),
    R(F,'Tables','Café / Bar Table','Round 700mm','Café table, round 700mm dia, chrome leg','Generic','Cafe Rnd 700','White',700,700,730,None,1,'ea',280,10,CONT,'Officeworks, approx AUD $279, 2025'),
    R(F,'Tables','Café / Bar Table','Square 700mm','Café table, square 700×700mm, timber top','Generic','Cafe Sq 700','Natural Timber',700,700,730,None,1,'ea',320,10,CONT,'Officeworks, approx AUD $319, 2025'),
    R(F,'Tables','Café / Bar Table','Round 600mm poseur','Poseur/bar table, round 600mm, chrome','Generic','Poseur 600','White',600,600,1050,None,1,'ea',350,10,CONT,'Fast Office Furniture, approx AUD $349, 2025'),
    R(F,'Tables','Coffee Table','Rectangular','Rectangular coffee table, 1200×600mm, veneer','Arteil','Coffee Rect','Walnut Veneer',1200,600,450,None,1,'ea',500,12,CONT,'Epic Office Furniture, approx AUD $499, 2025'),
    R(F,'Tables','Coffee Table','Round','Round coffee table, 800mm dia, glass top','Generic','Coffee Rnd 800','Black Frame / Glass',800,800,450,None,1,'ea',400,10,CONT,'Freedom Furniture, approx AUD $399, 2025'),
    R(F,'Tables','Side Table','--','Side table, 500×500mm, laminate','Generic','Side 500','White',500,500,550,None,1,'ea',180,10,CONT,'Officeworks, approx AUD $179, 2025'),
    R(F,'Tables','Height-Adjustable Table','--','Height-adjustable meeting table, 1600×800mm, electric','Ergomotion','SitStand Meeting','White',1600,800,750,None,1,'ea',1600,10,CONT,'Ergomotion.com.au, approx AUD $1599, 2025'),
    R(F,'Tables','Dining Table','6-person','Dining table, 1600×900mm, canteen/breakout','Generic','Dine 1600','Natural Timber',1600,900,740,None,1,'ea',600,12,CONT,'Officeworks, approx AUD $599, 2025'),

    # ── Storage & Filing ─────────────────────────────────────────────────────
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','2-drawer','Lateral filing cabinet, 2-drawer, 900mm W','Steelco','LFC2 900','White',900,470,700,None,1,'ea',550,20,CONT,'Winc, approx AUD $549, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','3-drawer','Lateral filing cabinet, 3-drawer, 900mm W','Steelco','LFC3 900','White',900,470,1050,None,1,'ea',700,20,CONT,'Winc, approx AUD $699, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','4-drawer','Lateral filing cabinet, 4-drawer, 900mm W','Steelco','LFC4 900','White',900,470,1375,None,1,'ea',850,20,CONT,'Winc, approx AUD $849, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','2-drawer','Lateral filing cabinet, 2-drawer, 1200mm W','Steelco','LFC2 1200','White',1200,470,700,None,1,'ea',700,20,CONT,'Winc, approx AUD $699, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Pedestal)','3-drawer','Mobile pedestal, 3-drawer (2 box + 1 file)','Steelco','Ped3','White',465,500,710,None,1,'ea',380,15,CONT,'Officeworks, approx AUD $379, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Pedestal)','3-drawer','Fixed pedestal, 3-drawer, lockable','Steelco','FPed3','White',465,500,710,None,1,'ea',350,15,CONT,'Winc, approx AUD $349, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Vertical)','4-drawer','Vertical filing cabinet, 4-drawer, A4','Steelco','VFC4','White',470,620,1320,None,1,'ea',480,20,CONT,'Winc, approx AUD $479, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','900mm W 3-shelf','Open bookcase, 900×300×900mm, 3-shelf','Rapidline','Book 900','White',900,300,900,None,1,'ea',220,15,CONT,'Officeworks, approx AUD $219, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','900mm W 5-shelf','Open bookcase, 900×300×1800mm, 5-shelf','Rapidline','Book 900H','White',900,300,1800,None,1,'ea',350,15,CONT,'Officeworks, approx AUD $349, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','1200mm W 5-shelf','Open bookcase, 1200×300×1800mm, 5-shelf','Rapidline','Book 1200H','White',1200,300,1800,None,1,'ea',420,15,CONT,'Winc, approx AUD $419, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','900mm W 3-shelf glass doors','Bookcase with glass doors, 900×400×1800mm','Arteil','GlassBook 900','White',900,400,1800,None,1,'ea',650,15,CONT,'Epic Office Furniture, approx AUD $649, 2025'),
    R(F,'Storage & Filing','Storage Cabinet','900mm W full height','Full-height storage cabinet with lock, 900mm W','Steelco','SC900H','White',900,470,1830,None,1,'ea',750,20,CONT,'Winc, approx AUD $749, 2025'),
    R(F,'Storage & Filing','Storage Cabinet','1200mm W full height','Full-height storage cabinet with lock, 1200mm W','Steelco','SC1200H','White',1200,470,1830,None,1,'ea',900,20,CONT,'Winc, approx AUD $899, 2025'),
    R(F,'Storage & Filing','Storage Cabinet','900mm W half height','Half-height storage cabinet with lock, 900mm W','Steelco','SC900L','White',900,470,1000,None,1,'ea',550,20,CONT,'Winc, approx AUD $549, 2025'),
    R(F,'Storage & Filing','Credenza / Buffet','1600mm','Credenza 1600×450mm, laminate, lockable','Arteil','Cred 1600','White',1600,450,730,None,1,'ea',900,15,CONT,'Epic Office Furniture, approx AUD $899, 2025'),
    R(F,'Storage & Filing','Credenza / Buffet','1800mm','Credenza 1800×450mm, veneer, lockable','Arteil','Cred 1800','Walnut Veneer',1800,450,730,None,1,'ea',1200,15,CONT,'Epic Office Furniture, approx AUD $1199, 2025'),
    R(F,'Storage & Filing','Locker','Single-door','Single-door locker, 300×450×1830mm, key lock','Steelco','Lok1','Grey',300,450,1830,None,1,'ea',220,20,CONT,'Winc, approx AUD $219, 2025'),
    R(F,'Storage & Filing','Locker','Double-door','Double-door locker, 300×450×1830mm, key lock','Steelco','Lok2','Grey',300,450,1830,None,1,'ea',280,20,CONT,'Winc, approx AUD $279, 2025'),
    R(F,'Storage & Filing','Locker','4-door','4-door locker, 300×450×1830mm','Steelco','Lok4','Grey',300,450,1830,None,1,'ea',380,20,CONT,'Winc, approx AUD $379, 2025'),
    R(F,'Storage & Filing','Tambour Unit','1600mm','Tambour unit/tambour door credenza, 1600mm','Rapidline','Tambour 1600','White',1600,470,730,None,1,'ea',950,15,CONT,'Winc, approx AUD $949, 2025'),
    R(F,'Storage & Filing','Compactus / Mobile Shelving','6-bay','Mobile shelving compactus, 6-bay, 2400H','Spacerak','Compactus 6B','Grey',3600,900,2400,None,1,'ea',8000,25,CONT,'Storage Systems Australia, approx AUD $7999, 2025'),
    R(F,'Storage & Filing','Plan Chest','A0 5-drawer','Plan chest, A0 format, 5-drawer, metal','Esselte','PlanChest A0','Grey',1280,940,940,None,1,'ea',1500,20,CONT,'Winc, approx AUD $1499, 2025'),

    # ── Screens & Partitions ─────────────────────────────────────────────────
    R(F,'Screens & Partitions','Acoustic Screen','1200×1200mm','Freestanding acoustic screen, 1200×1200mm, fabric','Rapidline','AcScreen 1200','Charcoal Fabric',1200,50,1200,None,1,'ea',380,10,CONT,'Winc, approx AUD $379, 2025'),
    R(F,'Screens & Partitions','Acoustic Screen','1200×1500mm','Freestanding acoustic screen, 1200×1500mm','Rapidline','AcScreen 1500','Charcoal Fabric',1200,50,1500,None,1,'ea',450,10,CONT,'Winc, approx AUD $449, 2025'),
    R(F,'Screens & Partitions','Acoustic Screen','1500×1800mm','Freestanding acoustic screen, 1500×1800mm','Rapidline','AcScreen 1800','Charcoal Fabric',1500,50,1800,None,1,'ea',550,10,CONT,'Epic Office Furniture, approx AUD $549, 2025'),
    R(F,'Screens & Partitions','Acoustic Screen','Desk divider','Desk-mount acoustic divider, 1200×400mm','Rapidline','DeskDiv','Charcoal Fabric',1200,30,400,None,1,'ea',180,8,CONT,'Officeworks, approx AUD $179, 2025'),
    R(F,'Screens & Partitions','Whiteboard','1200×900mm','Magnetic whiteboard 1200×900mm, aluminium frame','Visionchart','WB1209','White',1200,20,900,None,1,'ea',200,10,CONT,'Officeworks, approx AUD $199, 2025'),
    R(F,'Screens & Partitions','Whiteboard','1800×900mm','Magnetic whiteboard 1800×900mm, aluminium frame','Visionchart','WB1809','White',1800,20,900,None,1,'ea',320,10,CONT,'Officeworks, approx AUD $319, 2025'),
    R(F,'Screens & Partitions','Whiteboard','2400×1200mm','Magnetic whiteboard 2400×1200mm, aluminium frame','Visionchart','WB2412','White',2400,20,1200,None,1,'ea',500,10,CONT,'Winc, approx AUD $499, 2025'),
    R(F,'Screens & Partitions','Pinboard','900×600mm','Pinboard 900×600mm, fabric, aluminium frame','Visionchart','PB9060','Grey Fabric',900,20,600,None,1,'ea',120,10,CONT,'Officeworks, approx AUD $119, 2025'),
    R(F,'Screens & Partitions','Pinboard','1800×900mm','Pinboard 1800×900mm, fabric, aluminium frame','Visionchart','PB1809','Grey Fabric',1800,20,900,None,1,'ea',220,10,CONT,'Officeworks, approx AUD $219, 2025'),
    R(F,'Screens & Partitions','Room Divider','4-panel','4-panel folding room divider, fabric covered','Rapidline','RmDiv4','Charcoal Fabric',1600,50,1800,None,1,'ea',650,10,CONT,'Fast Office Furniture, approx AUD $649, 2025'),
    R(F,'Screens & Partitions','Room Divider','6-panel','6-panel folding room divider, fabric covered','Rapidline','RmDiv6','Charcoal Fabric',2400,50,1800,None,1,'ea',900,10,CONT,'Fast Office Furniture, approx AUD $899, 2025'),

    # ── Soft Furnishings ─────────────────────────────────────────────────────
    R(F,'Soft Furnishings','Window Blind','Vertical 1800mm','Vertical blind, 1800×1800mm, fabric','Luxaflex','Vertiflex','Grey',1800,None,1800,None,1,'ea',350,8,CONT,'Harvey Norman, approx AUD $349, 2025'),
    R(F,'Soft Furnishings','Window Blind','Roller 1500mm','Roller blind, 1500×1800mm, blockout','Decora','Blackout Roller','Charcoal',1500,None,1800,None,1,'ea',220,8,CONT,'Bunnings, approx AUD $219, 2025'),
    R(F,'Soft Furnishings','Window Blind','Venetian 1200mm','Aluminium venetian blind, 1200×1800mm','Decora','Venetian 50mm','Silver',1200,None,1800,None,1,'ea',180,10,CONT,'Bunnings, approx AUD $179, 2025'),
    R(F,'Soft Furnishings','Rug / Carpet Tile','2×3m','Area rug, 2000×3000mm, commercial grade','Interface','Carpet Tile 2x3','Charcoal',2000,3000,None,None,1,'ea',600,8,CONT,'Interface.com, approx AUD $599, 2025'),
    R(F,'Soft Furnishings','Rug / Carpet Tile','1.6×2.3m','Area rug, 1600×2300mm, loop pile','Interface','Carpet Tile 1.6x2.3','Grey',1600,2300,None,None,1,'ea',380,8,CONT,'Interface.com, approx AUD $379, 2025'),
    R(F,'Soft Furnishings','Artwork / Print','Large framed','Large framed artwork / print, 1200×800mm','Generic','Artwork L','Various',1200,50,800,None,1,'ea',400,10,CONT,'Ikea/Officeworks, approx AUD $399, 2025'),
    R(F,'Soft Furnishings','Artwork / Print','Medium framed','Medium framed artwork / print, 600×800mm','Generic','Artwork M','Various',600,50,800,None,1,'ea',200,10,CONT,'Ikea, approx AUD $199, 2025'),
    R(F,'Soft Furnishings','Planter / Indoor Plant','Large floor planter','Large indoor plant in pot, floor standing, 1200mm H','Generic','Floor Plant L','Various',400,400,1200,None,1,'ea',350,5,CONT,'Bunnings, approx AUD $349, 2025'),
    R(F,'Soft Furnishings','Planter / Indoor Plant','Small desktop planter','Desktop planter/succulent, 200mm','Generic','Desktop Plant','Various',200,200,200,None,1,'ea',60,5,CONT,'Bunnings, approx AUD $59, 2025'),
]

# =============================================================================
# INFORMATION TECHNOLOGY
# =============================================================================
IT = 'Information Technology'
CONT = 'Contents'

information_technology = [
    # ── Computing ────────────────────────────────────────────────────────────
    R(IT,'Computing','Desktop Computer (Tower)','i5','Desktop PC, Intel Core i5, 16GB RAM, 512GB SSD, Win 11 Pro','Dell','OptiPlex 7020 SFF','Black',175,292,358,None,1,'ea',1300,5,CONT,'Dell AU, approx AUD $1299, 2025'),
    R(IT,'Computing','Desktop Computer (Tower)','i7','Desktop PC, Intel Core i7, 32GB RAM, 1TB SSD, Win 11 Pro','Dell','OptiPlex 7020 Tower','Black',165,445,358,None,1,'ea',1750,5,CONT,'Dell AU, approx AUD $1749, 2025'),
    R(IT,'Computing','Desktop Computer (Tower)','High-perf','High-performance workstation, Core i9, 64GB RAM, 2TB SSD','Dell','Precision 5860','Black',165,445,400,None,1,'ea',4500,5,CONT,'Dell AU, approx AUD $4499, 2025'),
    R(IT,'Computing','Desktop Computer (Tower)','Budget i3','Budget desktop, Intel Core i3, 8GB RAM, 256GB SSD','HP','ProDesk 405 G9','Black',160,350,340,None,1,'ea',850,5,CONT,'HP AU, approx AUD $849, 2025'),
    R(IT,'Computing','Desktop Computer (AIO)','24-inch','All-in-one PC, 24", Core i5, 16GB, 512GB SSD','Dell','OptiPlex AIO 7410','Black',None,None,None,24,1,'ea',1900,5,CONT,'Dell AU, approx AUD $1899, 2025'),
    R(IT,'Computing','Desktop Computer (AIO)','27-inch','All-in-one PC, 27", Core i7, 32GB, 1TB SSD, touchscreen','HP','EliteOne 870 G9','Silver',None,None,None,27,1,'ea',2800,5,CONT,'HP AU, approx AUD $2799, 2025'),
    R(IT,'Computing','Laptop / Notebook','Business 14"','Business laptop, 14", Core i5, 16GB, 512GB SSD','Dell','Latitude 5440','Grey',323,222,20,None,1,'ea',1650,4,CONT,'Dell AU, approx AUD $1649, 2025'),
    R(IT,'Computing','Laptop / Notebook','Business 15"','Business laptop, 15.6", Core i7, 32GB, 1TB SSD','Dell','Latitude 5540','Grey',356,234,20,None,1,'ea',2200,4,CONT,'Dell AU, approx AUD $2199, 2025'),
    R(IT,'Computing','Laptop / Notebook','Premium 14"','Premium ultrabook, 14", Core i7, 32GB, 1TB SSD','Lenovo','ThinkPad X1 Carbon Gen 12','Black',315,222,15,None,1,'ea',2900,4,CONT,'Lenovo AU, approx AUD $2899, 2025'),
    R(IT,'Computing','Laptop / Notebook','MacBook Pro 14"','MacBook Pro 14", M4 Pro chip, 24GB, 512GB SSD','Apple','MacBook Pro 14" M4 Pro','Space Black',312,221,16,None,1,'ea',3200,5,CONT,'Apple AU, approx AUD $3199, 2025'),
    R(IT,'Computing','Laptop / Notebook','MacBook Air 13"','MacBook Air 13", M3 chip, 16GB, 256GB SSD','Apple','MacBook Air 13" M3','Midnight',304,215,11,None,1,'ea',1999,5,CONT,'Apple AU, approx AUD $1999, 2025'),
    R(IT,'Computing','Laptop / Notebook','Budget 14"','Entry-level laptop, 14", Core i5, 8GB, 256GB SSD','HP','ProBook 440 G11','Silver',324,226,19,None,1,'ea',1200,4,CONT,'JB Hi-Fi, approx AUD $1199, 2025'),
    R(IT,'Computing','Tablet','iPad 10th gen','iPad 10th Gen, 10.9", 64GB Wi-Fi','Apple','iPad 10th Gen','Silver',249,179,7,None,1,'ea',750,4,CONT,'Apple AU, approx AUD $749, 2025'),
    R(IT,'Computing','Tablet','iPad Pro 11"','iPad Pro 11", M4, 256GB Wi-Fi','Apple','iPad Pro 11" M4','Space Grey',249,177,6,None,1,'ea',1700,4,CONT,'Apple AU, approx AUD $1699, 2025'),
    R(IT,'Computing','Tablet','Surface Pro 11"','Surface Pro 11", Snapdragon X Plus, 16GB, 256GB','Microsoft','Surface Pro 11','Platinum',287,209,9,None,1,'ea',2000,4,CONT,'Microsoft AU, approx AUD $1999, 2025'),
    R(IT,'Computing','Server (Tower)','Entry-level','Entry-level tower server, Xeon E-2400, 32GB ECC, 2TB RAID','Dell','PowerEdge T150','Black',175,444,360,None,1,'ea',3500,5,CONT,'Dell AU, approx AUD $3499, 2025'),
    R(IT,'Computing','Server (Tower)','Mid-range','Mid-range tower server, Xeon Silver, 64GB ECC, 4TB RAID','Dell','PowerEdge T350','Black',175,538,423,None,1,'ea',6500,5,CONT,'Dell AU, approx AUD $6499, 2025'),
    R(IT,'Computing','Mini PC / NUC','i5','Mini PC, Intel Core i5, 16GB, 512GB SSD','Intel','NUC 13 Pro','Black',117,112,54,None,1,'ea',900,5,CONT,'JB Hi-Fi, approx AUD $899, 2025'),
    R(IT,'Computing','Docking Station','USB-C','USB-C docking station, dual monitor, 100W PD','Dell','WD22TB4','Black',220,87,20,None,1,'ea',450,4,CONT,'Dell AU, approx AUD $449, 2025'),
    R(IT,'Computing','Docking Station','Thunderbolt 4','Thunderbolt 4 docking station, 96W PD','Belkin','INC004','Black',235,97,22,None,1,'ea',550,4,CONT,'JB Hi-Fi, approx AUD $549, 2025'),

    # ── Display & Peripherals ─────────────────────────────────────────────────
    R(IT,'Display & Peripherals','Monitor / Screen','24" FHD','24" Full HD monitor, IPS, HDMI/DP','Dell','P2422H','Black',None,None,None,24,1,'ea',380,6,CONT,'Dell AU, approx AUD $379, 2025'),
    R(IT,'Display & Peripherals','Monitor / Screen','27" QHD','27" QHD monitor, IPS, USB-C, HDMI/DP','Dell','P2723DE','Black',None,None,None,27,1,'ea',650,6,CONT,'Dell AU, approx AUD $649, 2025'),
    R(IT,'Display & Peripherals','Monitor / Screen','27" 4K','27" 4K UHD monitor, USB-C 90W','LG','27UK850','Black',None,None,None,27,1,'ea',750,6,CONT,'JB Hi-Fi, approx AUD $749, 2025'),
    R(IT,'Display & Peripherals','Monitor / Screen','32" 4K','32" 4K monitor, USB-C, thunderbolt','Samsung','S32B800','Black',None,None,None,32,1,'ea',1100,6,CONT,'JB Hi-Fi, approx AUD $1099, 2025'),
    R(IT,'Display & Peripherals','Monitor / Screen','34" Ultrawide','34" ultrawide curved monitor, WQHD','LG','34WP65C','Black',None,None,None,34,1,'ea',900,6,CONT,'JB Hi-Fi, approx AUD $899, 2025'),
    R(IT,'Display & Peripherals','Printer (Desktop)','A4 Laser Mono','Laser printer, A4 mono, 38ppm, duplex','Brother','HL-L5210DW','Black',359,382,236,None,1,'ea',400,5,CONT,'Officeworks, approx AUD $399, 2025'),
    R(IT,'Display & Peripherals','Printer (Desktop)','A4 Inkjet Colour','Inkjet MFP, A4 colour, print/scan/copy','Epson','EcoTank ET-4850','Black',375,347,230,None,1,'ea',500,5,CONT,'Officeworks, approx AUD $499, 2025'),
    R(IT,'Display & Peripherals','Printer (Multifunction)','A4 Laser Colour','MFP, A4 colour laser, print/scan/copy/fax','Brother','MFC-L8690CDW','Black',469,499,333,None,1,'ea',750,5,CONT,'Officeworks, approx AUD $749, 2025'),
    R(IT,'Display & Peripherals','Printer (Multifunction)','A3 Colour Laser','A3 colour laser MFP, print/scan/copy, 30ppm','Konica Minolta','bizhub C257i','Grey',587,616,699,None,1,'ea',4500,7,CONT,'CopierChoice AU, approx AUD $4499, 2025'),
    R(IT,'Display & Peripherals','Printer (Multifunction)','A3 High-speed','A3 high-speed mono MFP, 50ppm, production grade','Konica Minolta','bizhub 558e','Grey',587,650,850,None,1,'ea',6500,7,CONT,'CopierChoice AU, approx AUD $6499, 2025'),
    R(IT,'Display & Peripherals','Scanner (Flatbed)','A4','A4 flatbed scanner, 1200dpi, USB','Canon','CanoScan LiDE 400','White',253,163,36,None,1,'ea',180,5,CONT,'Officeworks, approx AUD $179, 2025'),
    R(IT,'Display & Peripherals','Scanner (Sheet-fed)','A4 30ppm','Sheet-fed document scanner, A4, 30ppm duplex','Fujitsu','fi-7160','Black',168,158,156,None,1,'ea',1200,5,CONT,'Winc, approx AUD $1199, 2025'),
    R(IT,'Display & Peripherals','UPS (Battery Backup)','600VA','UPS 600VA/360W, USB, 4 outlet','APC','BX600CI-AS','Black',320,100,142,None,1,'ea',180,5,CONT,'Officeworks, approx AUD $179, 2025'),
    R(IT,'Display & Peripherals','UPS (Battery Backup)','1500VA','UPS 1500VA/900W, LCD, USB, rack/tower','APC','SMC1500IC','Black',432,150,202,None,1,'ea',550,5,CONT,'Winc, approx AUD $549, 2025'),
    R(IT,'Display & Peripherals','UPS (Battery Backup)','3000VA','UPS 3000VA rack mount, network management card','APC','SRT3000RMXLI','Black',482,680,88,None,1,'ea',1800,5,CONT,'Winc, approx AUD $1799, 2025'),
    R(IT,'Display & Peripherals','Webcam','HD 1080p','1080p full HD webcam, built-in mic','Logitech','C920s Pro','Black',88,31,55,None,1,'ea',180,4,CONT,'Officeworks, approx AUD $179, 2025'),
    R(IT,'Display & Peripherals','Webcam','4K','4K webcam with auto-framing','Logitech','BRIO 4K','Black',102,27,33,None,1,'ea',320,4,CONT,'JB Hi-Fi, approx AUD $319, 2025'),
    R(IT,'Display & Peripherals','Keyboard','Wireless','Wireless keyboard, full-size, slim','Logitech','MK470','Black',433,132,20,None,1,'ea',120,4,CONT,'Officeworks, approx AUD $119, 2025'),
    R(IT,'Display & Peripherals','Mouse','Wireless','Wireless ergonomic mouse','Logitech','MX Master 3S','Black',126,84,48,None,1,'ea',130,4,CONT,'Officeworks, approx AUD $129, 2025'),

    # ── Networking & Communications ───────────────────────────────────────────
    R(IT,'Networking & Communications','Network Switch','8-port unmanaged','8-port Gigabit Ethernet switch, unmanaged','Netgear','GS308','Black',158,74,27,None,1,'ea',80,5,CONT,'JB Hi-Fi, approx AUD $79, 2025'),
    R(IT,'Networking & Communications','Network Switch','24-port managed','24-port managed Gigabit switch, PoE+, 1U rack','Cisco','CBS250-24P','Black',440,202,44,None,1,'ea',900,7,CONT,'Winc, approx AUD $899, 2025'),
    R(IT,'Networking & Communications','Network Switch','48-port managed','48-port managed Gigabit switch, 1U rack','Cisco','CBS350-48P','Black',440,202,44,None,1,'ea',1800,7,CONT,'Winc, approx AUD $1799, 2025'),
    R(IT,'Networking & Communications','Network Switch','24-port PoE+','24-port PoE+ switch, 370W budget, managed','Ubiquiti','UniFi USW-24-PoE','Black',440,105,44,None,1,'ea',750,7,CONT,'Wireless1, approx AUD $749, 2025'),
    R(IT,'Networking & Communications','Wireless Access Point','Ceiling mount','Wi-Fi 6 ceiling-mount access point, 4×4 MIMO','Cisco','Catalyst 9130AX','White',None,None,None,None,1,'ea',1200,5,CONT,'Winc, approx AUD $1199, 2025'),
    R(IT,'Networking & Communications','Wireless Access Point','Wall mount','Wi-Fi 6 wall-mount access point','Ubiquiti','UniFi U6 Lite','White',None,None,None,None,1,'ea',280,5,CONT,'Wireless1, approx AUD $279, 2025'),
    R(IT,'Networking & Communications','Firewall / Router','SMB','SMB next-gen firewall, 1Gbps throughput','Fortinet','FortiGate 80F','Black',214,160,38,None,1,'ea',1800,5,CONT,'Fortinet AU, approx AUD $1799, 2025'),
    R(IT,'Networking & Communications','Firewall / Router','Enterprise','Enterprise firewall appliance, multi-port SFP+','Fortinet','FortiGate 200F','Black',440,280,44,None,1,'ea',6000,5,CONT,'Fortinet AU, approx AUD $5999, 2025'),
    R(IT,'Networking & Communications','NAS (Network Storage)','4-bay','4-bay NAS, 40TB usable, RAID 5','Synology','DS923+','Black',166,199,108,None,1,'ea',1500,5,CONT,'Synology AU, approx AUD $1499, 2025'),
    R(IT,'Networking & Communications','NAS (Network Storage)','8-bay','8-bay enterprise NAS, 80TB usable','Synology','DS1823xs+','Black',157,228,233,None,1,'ea',3500,5,CONT,'Synology AU, approx AUD $3499, 2025'),
    R(IT,'Networking & Communications','Network Rack','12U wall mount','12U wall-mount network rack, 550mm deep','Generic','WR12U','Black',600,550,650,None,1,'ea',550,15,CONT,'Winc, approx AUD $549, 2025'),
    R(IT,'Networking & Communications','Network Rack','22U floor stand','22U floor-standing network rack','Generic','FR22U','Black',600,800,1100,None,1,'ea',900,15,CONT,'Winc, approx AUD $899, 2025'),
    R(IT,'Networking & Communications','PABX / IP PBX','16-ext','IP PBX system, 16-extension capacity, SIP','Yealink','P-Series P5','Black',None,None,None,None,1,'ea',2200,7,CONT,'Yealink AU, approx AUD $2199, 2025'),
    R(IT,'Networking & Communications','PABX / IP PBX','48-ext','IP PBX, 48-extension, unified communications','Cisco','BE6000S','Black',440,310,44,None,1,'ea',5500,7,CONT,'Cisco AU, approx AUD $5499, 2025'),
    R(IT,'Networking & Communications','VoIP Phone','Standard','IP desk phone, colour display, PoE','Yealink','T54W','Black',212,184,132,None,1,'ea',250,5,CONT,'Yealink AU, approx AUD $249, 2025'),
    R(IT,'Networking & Communications','VoIP Phone','Executive','Executive IP phone, 7" touchscreen, video','Yealink','T58W','Black',220,195,170,None,1,'ea',450,5,CONT,'Yealink AU, approx AUD $449, 2025'),
    R(IT,'Networking & Communications','Patch Panel','24-port','24-port Cat6 patch panel, 1U rack','Netgear','NPP24UPS100','Black',482,95,44,None,1,'ea',120,10,CONT,'Winc, approx AUD $119, 2025'),
]

# =============================================================================
# AUDIO VISUAL
# =============================================================================
AV = 'Audio Visual'

audio_visual = [
    # ── Display Systems ───────────────────────────────────────────────────────
    R(AV,'Display Systems','Flat Screen TV','55"','55" 4K UHD Smart TV, wall-mount bracket','Samsung','QA55Q70D','Black',None,None,None,55,1,'ea',1200,8,CONT,'Harvey Norman, approx AUD $1199, 2025'),
    R(AV,'Display Systems','Flat Screen TV','65"','65" 4K QLED Smart TV','Samsung','QA65Q70D','Black',None,None,None,65,1,'ea',1800,8,CONT,'Harvey Norman, approx AUD $1799, 2025'),
    R(AV,'Display Systems','Flat Screen TV','65" commercial','65" 4K commercial display, landscape/portrait','Samsung','QM65B','Black',None,None,None,65,1,'ea',2800,8,CONT,'Samsung Business AU, approx AUD $2799, 2025'),
    R(AV,'Display Systems','Flat Screen TV','75"','75" 4K Smart TV, HDR, Wi-Fi','Hisense','75U8HAU','Black',None,None,None,75,1,'ea',2200,8,CONT,'Harvey Norman, approx AUD $2199, 2025'),
    R(AV,'Display Systems','Flat Screen TV','75" commercial','75" 4K commercial display, 24/7 rated','LG','75UH5J','Black',None,None,None,75,1,'ea',3800,8,CONT,'LG Business AU, approx AUD $3799, 2025'),
    R(AV,'Display Systems','Flat Screen TV','85"','85" 4K Smart TV, QLED, local dimming','Samsung','QA85Q80D','Black',None,None,None,85,1,'ea',3500,8,CONT,'Harvey Norman, approx AUD $3499, 2025'),
    R(AV,'Display Systems','Flat Screen TV','98"','98" 4K commercial display, ultra large format','LG','98UR640S','Black',None,None,None,98,1,'ea',9500,8,CONT,'LG Business AU, approx AUD $9499, 2025'),
    R(AV,'Display Systems','Projector','3000 lumen','DLP projector, 3000 lumens, 1080p, HDMI','Epson','EH-TW5825','White',302,232,99,None,1,'ea',1100,8,CONT,'JB Hi-Fi, approx AUD $1099, 2025'),
    R(AV,'Display Systems','Projector','5000 lumen','Installation projector, 5000 lumens, WUXGA','Epson','EB-L520U','White',400,296,115,None,1,'ea',3500,8,CONT,'Epson AU, approx AUD $3499, 2025'),
    R(AV,'Display Systems','Projector','8000 lumen','Large venue projector, 8000 lumens, 4K','Sony','VPL-FHZ85','White',464,530,175,None,1,'ea',8000,10,CONT,'Sony AU, approx AUD $7999, 2025'),
    R(AV,'Display Systems','Projection Screen','Manual 2400mm','Manual pull-down screen, 2.4m W, 16:9, matte white','Screenline','Manual 2400','White',2400,None,None,None,1,'ea',450,10,CONT,'AV distributor AU, approx AUD $449, 2025'),
    R(AV,'Display Systems','Projection Screen','Electric 3000mm','Electric drop-down screen, 3m W, 16:9, motorised','Screenline','Electric 3000','White',3000,None,None,None,1,'ea',1200,10,CONT,'AV distributor AU, approx AUD $1199, 2025'),
    R(AV,'Display Systems','Interactive Whiteboard','65"','65" interactive flat panel display, 4K, multi-touch','SMART','Board 65 6000S','Black',None,None,None,65,1,'ea',4500,7,CONT,'SMART Technologies AU, approx AUD $4499, 2025'),
    R(AV,'Display Systems','Interactive Whiteboard','75"','75" interactive display, 4K touchscreen, Android','Clevertouch','Impact Max 75','Black',None,None,None,75,1,'ea',5800,7,CONT,'Clevertouch AU, approx AUD $5799, 2025'),
    R(AV,'Display Systems','Digital Signage Screen','43"','43" commercial digital signage display, portrait/landscape','Samsung','QM43B','Black',None,None,None,43,1,'ea',1500,7,CONT,'Samsung Business AU, approx AUD $1499, 2025'),
    R(AV,'Display Systems','Digital Signage Screen','55"','55" commercial digital signage, 24/7 rated','LG','55UH5J','Black',None,None,None,55,1,'ea',2200,7,CONT,'LG Business AU, approx AUD $2199, 2025'),
    R(AV,'Display Systems','LED Video Wall','2×2 panel','2×2 LED video wall, 1.8mm pixel pitch, per panel','Absen','A1800-M','Black',None,None,None,None,1,'ea',4500,10,CONT,'Absen AU distributor, approx AUD $4499/panel, 2025'),

    # ── Video Conferencing ────────────────────────────────────────────────────
    R(AV,'Video Conferencing','Video Bar (All-in-One)','Small room','Video bar, 4K camera, array mic, Teams/Zoom certified','Logitech','Rally Bar Mini','Black',None,None,None,None,1,'ea',2800,5,CONT,'Logitech AU, approx AUD $2799, 2025'),
    R(AV,'Video Conferencing','Video Bar (All-in-One)','Medium room','Video bar, 4K camera, AI tracking, speakerphone','Logitech','Rally Bar','Black',None,None,None,None,1,'ea',4500,5,CONT,'Logitech AU, approx AUD $4499, 2025'),
    R(AV,'Video Conferencing','Video Bar (All-in-One)','Large room','Conference bar system with 120° FOV, 15m pickup','Poly','Studio E70','Black',None,None,None,None,1,'ea',6500,5,CONT,'Poly AU, approx AUD $6499, 2025'),
    R(AV,'Video Conferencing','PTZ Camera','1080p','PTZ camera, 1080p, 12× optical zoom, USB/HDMI','HuddleCamHD','HC-30X-USB','Grey',None,None,None,None,1,'ea',1800,5,CONT,'AV distributor AU, approx AUD $1799, 2025'),
    R(AV,'Video Conferencing','PTZ Camera','4K','4K PTZ camera, 30× optical zoom, IP streaming','Panasonic','AW-UE50','Black',None,None,None,None,1,'ea',4000,5,CONT,'Panasonic AU, approx AUD $3999, 2025'),
    R(AV,'Video Conferencing','Conferencing Speakerphone','Portable','Portable Bluetooth conference speakerphone','Jabra','Speak2 75','Black',None,None,None,None,1,'ea',450,4,CONT,'Officeworks, approx AUD $449, 2025'),
    R(AV,'Video Conferencing','Conferencing Speakerphone','Room','Room-grade conference speakerphone, USB/Bluetooth','Jabra','Speak2 85','Black',None,None,None,None,1,'ea',700,4,CONT,'Officeworks, approx AUD $699, 2025'),
    R(AV,'Video Conferencing','Video Conferencing Codec','Room','Room kit with camera/codec/touch controller','Cisco','Room Kit Plus','Black',None,None,None,None,1,'ea',9500,5,CONT,'Cisco AU, approx AUD $9499, 2025'),
    R(AV,'Video Conferencing','Collaboration Touch Panel','10"','10" touch panel for room booking / VC control','Yealink','RoomPanel 10','Black',None,None,None,None,1,'ea',1200,5,CONT,'Yealink AU, approx AUD $1199, 2025'),
    R(AV,'Video Conferencing','Collaboration Touch Panel','7"','7" touch panel controller for AV/VC systems','Crestron','TSW-770','Black',None,None,None,None,1,'ea',2200,5,CONT,'Crestron AU, approx AUD $2199, 2025'),

    # ── Audio Systems ─────────────────────────────────────────────────────────
    R(AV,'Audio Systems','Soundbar','Small','Soundbar, 2.0ch, HDMI ARC, Bluetooth, 80W','Sonos','Beam Gen2','Black',None,None,None,None,1,'ea',700,7,CONT,'JB Hi-Fi, approx AUD $699, 2025'),
    R(AV,'Audio Systems','Soundbar','Large','Soundbar, 3.1ch, 360W, Dolby Atmos, Wi-Fi','Samsung','HW-Q900A','Black',None,None,None,None,1,'ea',1200,7,CONT,'JB Hi-Fi, approx AUD $1199, 2025'),
    R(AV,'Audio Systems','Ceiling Speaker','6.5"','In-ceiling speaker, 6.5", 2-way, 60W, white','Yamaha','NS-IW280CWH','White',None,None,None,None,1,'ea',250,10,CONT,'Yamaha AU, approx AUD $249, 2025'),
    R(AV,'Audio Systems','Ceiling Speaker','8" commercial','Commercial ceiling speaker, 8", 100V line, pendant','Bosch','LBC3956/00','White',None,None,None,None,1,'ea',350,10,CONT,'Bosch AU, approx AUD $349, 2025'),
    R(AV,'Audio Systems','Amplifier','Stereo 2ch','Stereo amplifier, 2×100W, XLR/RCA inputs','Crown','XLS 1002','Black',None,None,None,None,1,'ea',550,10,CONT,'Audio distributor AU, approx AUD $549, 2025'),
    R(AV,'Audio Systems','Amplifier','Multi-zone 4ch','Multi-zone amplifier, 4×100W, background music','Crown','XLi 1500','Black',None,None,None,None,1,'ea',900,10,CONT,'Audio distributor AU, approx AUD $899, 2025'),
    R(AV,'Audio Systems','AV Receiver / Amplifier','7.2ch','7.2ch AV receiver, Dolby Atmos, 4K, Wi-Fi','Yamaha','RX-V6A','Black',435,168,327,None,1,'ea',900,8,CONT,'JB Hi-Fi, approx AUD $899, 2025'),
    R(AV,'Audio Systems','Wireless Microphone System','Handheld','Wireless handheld mic system, dual channel UHF','Shure','SLX-D Dual','Black',None,None,None,None,1,'ea',1600,8,CONT,'Shure AU, approx AUD $1599, 2025'),
    R(AV,'Audio Systems','Wireless Microphone System','Lapel/bodypack','Wireless bodypack mic system, dual channel','Sennheiser','EW-DX2','Black',None,None,None,None,1,'ea',2200,8,CONT,'Sennheiser AU, approx AUD $2199, 2025'),

    # ── AV Control & Distribution ─────────────────────────────────────────────
    R(AV,'AV Control & Distribution','AV Control System','Touch panel','AV control system with 7" touch panel','Crestron','DM-NVX-360','Black',None,None,None,None,1,'ea',3500,8,CONT,'Crestron AU, approx AUD $3499, 2025'),
    R(AV,'AV Control & Distribution','AV Matrix Switcher','8×8 HDMI','8×8 HDMI matrix switcher 4K, RS232 control','Atlona','AT-UHD-CAT-8ED','Black',440,240,44,None,1,'ea',2800,8,CONT,'AV distributor AU, approx AUD $2799, 2025'),
    R(AV,'AV Control & Distribution','HDMI Splitter','4-way','4-way HDMI splitter, 4K@60Hz, HDCP','Generic','HDMI-SP4K','Black',150,90,25,None,1,'ea',120,5,CONT,'Scorptec, approx AUD $119, 2025'),
    R(AV,'AV Control & Distribution','Streaming / Presentation PC','Mini PC','Presentation/streaming mini PC, Core i5, 16GB','Dell','OptiPlex Micro','Black',183,178,36,None,1,'ea',950,5,CONT,'Dell AU, approx AUD $949, 2025'),
]

# =============================================================================
# APPLIANCES & WHITE GOODS
# =============================================================================
AP = 'Appliances & White Goods'

appliances = [
    # ── Kitchen Appliances ────────────────────────────────────────────────────
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','French door','French door refrigerator, 600L, water dispenser','Samsung','RF60A91R1B4','Stainless Steel',835,735,1830,None,1,'ea',3200,12,CONT,'Harvey Norman, approx AUD $3199, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Top mount','Top-mount fridge, 420L, energy star rated','Fisher & Paykel','RF442BLPX6','Stainless Steel',680,700,1740,None,1,'ea',1400,12,CONT,'Harvey Norman, approx AUD $1399, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Upright commercial','Upright commercial refrigerator, 440L, glass door','Skope','SKF440','Stainless Steel',620,675,1950,None,1,'ea',2800,10,CONT,'Skope AU, approx AUD $2799, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Under-bench 160L','Under-bench refrigerator, 160L, stainless','Westinghouse','WRB3200WA','Stainless Steel',600,600,850,None,1,'ea',900,10,CONT,'Harvey Norman, approx AUD $899, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Bar fridge 90L','Bar fridge, 90L, glass door, reversible hinge','Hisense','HR6BF90','Black Glass',440,500,850,None,1,'ea',500,8,CONT,'Harvey Norman, approx AUD $499, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Medical/pharmacy','Medical refrigerator, 150L, temp monitoring','Vestfrost','HF-140','White',600,640,860,None,1,'ea',2200,10,CONT,'Medshop AU, approx AUD $2199, 2025'),
    R(AP,'Kitchen Appliances','Dishwasher','Underbench 60cm','Built-in dishwasher, 60cm, 14 place, 5-star','Bosch','SMS6ZCI10A','Stainless Steel',600,600,845,None,1,'ea',1600,12,CONT,'Harvey Norman, approx AUD $1599, 2025'),
    R(AP,'Kitchen Appliances','Dishwasher','Underbench 45cm','Built-in dishwasher, 45cm, 9 place','Bosch','SPV4IMX20A','White',450,600,820,None,1,'ea',1100,12,CONT,'Harvey Norman, approx AUD $1099, 2025'),
    R(AP,'Kitchen Appliances','Dishwasher','Commercial pass-through','Commercial pass-through dishwasher, 500 plates/hr','Winterhalter','PT-L','Stainless Steel',600,715,1450,None,1,'ea',8500,12,CONT,'Winterhalter AU, approx AUD $8499, 2025'),
    R(AP,'Kitchen Appliances','Microwave Oven','Standard 30L','Countertop microwave, 30L, 1100W, inverter','Panasonic','NN-SD271S','Silver',517,388,298,None,1,'ea',280,8,CONT,'Harvey Norman, approx AUD $279, 2025'),
    R(AP,'Kitchen Appliances','Microwave Oven','Commercial','Commercial microwave, 25L, 1800W, heavy duty','Panasonic','NE-1887','Stainless Steel',517,480,308,None,1,'ea',900,8,CONT,'Restaurant Supply AU, approx AUD $899, 2025'),
    R(AP,'Kitchen Appliances','Microwave Oven','Convection','Convection microwave oven, 44L, 1000W','Westinghouse','WMF4502SC','Stainless Steel',595,430,393,None,1,'ea',450,8,CONT,'Harvey Norman, approx AUD $449, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Auto)','Bean to cup 1-grp','Bean-to-cup automatic coffee machine, 1-group','Jura','E8','Chrome',280,440,340,None,1,'ea',2000,8,CONT,'Harvey Norman, approx AUD $1999, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Auto)','Commercial 2-grp','Commercial espresso machine, 2-group, dual boiler','Sanremo','Cafe Racer 2GR','Stainless Steel',700,490,560,None,1,'ea',6500,10,CONT,'Coffee machine distributor AU, approx AUD $6499, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Auto)','Office bean-to-cup','Office bean-to-cup, 1.8L tank, auto cleaning','DeLonghi','Dinamica ECAM350.55','Silver',240,430,350,None,1,'ea',1200,8,CONT,'Harvey Norman, approx AUD $1199, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Pod)','Nespresso','Nespresso pod machine, 19-bar pump','Breville','Vertuo Next VNX100','Black',135,380,310,None,1,'ea',200,5,CONT,'Harvey Norman, approx AUD $199, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Pod)','Nespresso Pro commercial','Nespresso Professional pod machine','Nespresso','Zenius PRO','Black',215,455,380,None,1,'ea',500,5,CONT,'Nespresso AU, approx AUD $499, 2025'),
    R(AP,'Kitchen Appliances','Kettle','Commercial 1.7L','Stainless steel kettle, 1.7L, 2400W','Breville','BKE830','Stainless Steel',260,165,230,None,1,'ea',100,5,CONT,'Harvey Norman, approx AUD $99, 2025'),
    R(AP,'Kitchen Appliances','Kettle','Commercial 3L','Commercial urn/kettle, 3L, variable temp','DeLonghi','KBX3116','Stainless Steel',285,190,285,None,1,'ea',150,5,CONT,'Harvey Norman, approx AUD $149, 2025'),
    R(AP,'Kitchen Appliances','Toaster','4-slice','4-slice toaster, 1800W, stainless','Breville','the Smart Toast 4S','Brushed Stainless',375,175,195,None,1,'ea',130,5,CONT,'Harvey Norman, approx AUD $129, 2025'),
    R(AP,'Kitchen Appliances','Toaster','Commercial conveyor','Commercial conveyor toaster, 450 slices/hr','Hatco','TF-1750','Stainless Steel',460,305,295,None,1,'ea',2000,8,CONT,'Restaurant Supply AU, approx AUD $1999, 2025'),
    R(AP,'Kitchen Appliances','Water Cooler / Dispenser','Freestanding','Freestanding water cooler, hot & cold, bottle-less','Zip','HydroTap G5','Chrome',310,375,1120,None,1,'ea',700,8,CONT,'Zip Water AU, approx AUD $699, 2025'),
    R(AP,'Kitchen Appliances','Water Cooler / Dispenser','Zip under-bench','Under-bench HydroTap, boiling/chilled/sparkling','Zip','HydroTap BC','Chrome',340,440,450,None,1,'ea',1800,10,CONT,'Zip Water AU, approx AUD $1799, 2025'),
    R(AP,'Kitchen Appliances','Water Cooler / Dispenser','Point-of-use benchtop','Benchtop water purifier, hot/cold, tankless','Brita','Vivreau Top','White',150,310,410,None,1,'ea',500,8,CONT,'Brita AU, approx AUD $499, 2025'),

    # ── Laundry Appliances ────────────────────────────────────────────────────
    R(AP,'Laundry Appliances','Washing Machine','Front loader 9kg','Front loader washing machine, 9kg, 4-star water','Samsung','WW90T534DAW','White',600,600,850,None,1,'ea',1200,12,CONT,'Harvey Norman, approx AUD $1199, 2025'),
    R(AP,'Laundry Appliances','Washing Machine','Commercial top loader 14kg','Commercial washing machine, 14kg, coin-op optional','Speed Queen','TC5','White',700,700,1100,None,1,'ea',3000,15,CONT,'Speed Queen AU, approx AUD $2999, 2025'),
    R(AP,'Laundry Appliances','Dryer','Condenser 9kg','Condenser dryer, 9kg, heat pump, 5-star','Samsung','DV90BB9445GE','White',600,600,850,None,1,'ea',1400,12,CONT,'Harvey Norman, approx AUD $1399, 2025'),
    R(AP,'Laundry Appliances','Dryer','Commercial 14kg','Commercial dryer, 14kg, gas/electric, stainless drum','Speed Queen','DC5','White',700,700,1100,None,1,'ea',2800,15,CONT,'Speed Queen AU, approx AUD $2799, 2025'),
    R(AP,'Laundry Appliances','Ironing Board','Commercial','Heavy-duty ironing board, adjustable height, steel','Brabantia','Pro','Chrome/Grey',1350,450,None,None,1,'ea',180,8,CONT,'Harvey Norman, approx AUD $179, 2025'),

    # ── Cleaning ─────────────────────────────────────────────────────────────
    R(AP,'Cleaning','Vacuum Cleaner','Upright commercial','Commercial upright vacuum, HEPA, 12.5L bag','Nilfisk','UPRIGHT','Red',None,None,None,None,1,'ea',600,7,CONT,'Nilfisk AU, approx AUD $599, 2025'),
    R(AP,'Cleaning','Vacuum Cleaner','Backpack','Backpack vacuum cleaner, 5.7L, HEPA','Pullman','BACKPACK','Yellow',None,None,None,None,1,'ea',500,7,CONT,'Pullman AU, approx AUD $499, 2025'),
    R(AP,'Cleaning','Vacuum Cleaner','Wet/dry industrial','Wet/dry vacuum, 30L, stainless steel','Karcher','WD 5 Premium','Yellow/Black',380,395,540,None,1,'ea',350,7,CONT,'Bunnings, approx AUD $349, 2025'),
    R(AP,'Cleaning','Vacuum Cleaner','Barrel/canister','Barrel vacuum, 15L, HEPA, for hard floors','Nilfisk','GS80','Blue',None,None,None,None,1,'ea',400,7,CONT,'Nilfisk AU, approx AUD $399, 2025'),
    R(AP,'Cleaning','Vacuum Cleaner','Robot','Robot vacuum, mapping, auto-empty base','iRobot','Roomba j9+','Black',None,None,None,None,1,'ea',1200,4,CONT,'JB Hi-Fi, approx AUD $1199, 2025'),
    R(AP,'Cleaning','Steam Cleaner','Commercial','Commercial steam cleaner, 4L boiler, trolley','Karcher','DE 4002','Yellow',None,None,None,None,1,'ea',800,7,CONT,'Karcher AU, approx AUD $799, 2025'),
    R(AP,'Cleaning','Floor Polisher','Rotary','Rotary floor polisher, 430mm dia, commercial','Pullman','Cyclone 17','Black',None,None,None,None,1,'ea',900,8,CONT,'Pullman AU, approx AUD $899, 2025'),
    R(AP,'Cleaning','Floor Polisher','Auto-scrubber','Ride-on floor scrubber, 50cm path, battery','Nilfisk','SC250','White/Blue',None,None,None,None,1,'ea',5000,8,CONT,'Nilfisk AU, approx AUD $4999, 2025'),
]

# =============================================================================
# Combine Part 1 records
# =============================================================================
all_records = furniture + information_technology + audio_visual + appliances

HEADERS = [
    'Unique ID','Asset ID (Client)','Parent Asset','Address','Level','Sub Location',
    'Asset Category (L1)','Asset Category (L2)','Asset Category (L3)','Asset Category (L4)',
    'Item Description','Condition Rating (0-5)','Condition Rating Label','Photo 1','Photo 2',
    'Quantity','Unit of Measurement','Width (mm)','Depth (mm)','Height (mm)','Screen Size (inches)',
    'Make / Brand','Model','Serial Number','Asset Tag / Label','Colour / Finish',
    'Comments / Recommendations','Unit Rate - RCN ($)','Estimated Replacement Cost ($)',
    'Remaining Useful Life (%)','Indemnity Value ($)','Insurance Schedule Category',
    'Effective Life (years)'
]

out = Path('Asset_Library_AU.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(HEADERS)
    for i, rec in enumerate(all_records):
        rec[0] = 200001 + i
        w.writerow(rec)

print(f"Part 1 written: {len(all_records)} records to {out}")
print(f"  Furniture:             {len(furniture)}")
print(f"  Information Technology:{len(information_technology)}")
print(f"  Audio Visual:          {len(audio_visual)}")
print(f"  Appliances:            {len(appliances)}")
print(f"Last ID used: {200001 + len(all_records) - 1}")
