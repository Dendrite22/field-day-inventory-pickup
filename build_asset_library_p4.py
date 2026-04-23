"""Part 4 – top-up to reach 3× for remaining under-target categories."""
import csv
from pathlib import Path

COND_LABELS = {0:'Not Present',1:'As New',2:'Good',3:'Fair',4:'Poor',5:'Very Poor'}
RUL_MAP     = {0:None,1:1.00,2:0.75,3:0.50,4:0.25,5:0.00}

def row(l1,l2,l3,l4,desc,make,model,colour,w,d,h,scr,qty,uom,rate,eff,ins,src,cond=2):
    rul=RUL_MAP[cond]; erc=round(rate*qty,2)
    iv=round(erc*rul,2) if rul is not None else 0.00
    return ['','','','','','',l1,l2,l3,l4,desc,cond,COND_LABELS[cond],'','',
            qty,uom,w or '',d or '',h or '',scr or '',make,model,'','',colour,
            f'Source: {src}',rate,erc,rul if rul is not None else '',iv,ins,eff]

R=row; CONT='Contents'; PE='Plant & Equipment'

F='Furniture'
furniture_p4=[
    R(F,'Seating','Task Chair','--','Leather executive chair, high-back, chrome star base','Buro','Exec HC','Black Leather',700,680,1280,None,1,'ea',1100,12,CONT,'Buro.com.au, approx AUD $1099, 2025'),
    R(F,'Seating','Visitor Chair','--','Guest chair, timber legs, upholstered seat & back','Generic','Timber Guest','Charcoal/Timber',560,540,820,None,1,'ea',320,10,CONT,'Fast Office Furniture, approx AUD $319, 2025'),
    R(F,'Seating','Lounge Chair / Sofa','4-seater','4-seat modular lounge, fabric, metal legs','Instyle','Modular 4S Square','Light Grey Fabric',2400,900,760,None,1,'ea',5500,12,CONT,'Instyle.com.au, approx AUD $5499, 2025'),
    R(F,'Seating','Meeting Chair','--','Ergonomic conference chair, mesh, lumbar adjust','Humanscale','Diffrient Smart','Black Mesh',580,560,890,None,1,'ea',900,12,CONT,'Humanscale AU, approx AUD $899, 2025'),
    R(F,'Seating','Stacking Chair','--','Outdoor polypropylene stacking chair, UV resistant','Kartell','Masters','Transparent',490,520,850,None,1,'ea',180,10,CONT,'Stylecraft AU, approx AUD $179, 2025'),
    R(F,'Desks & Workstations','Straight Desk','1000mm','Compact straight desk, 1000×600mm, laminate, for small spaces','Rapidline','Swift 1000','White',1000,600,720,None,1,'ea',280,12,CONT,'Officeworks, approx AUD $279, 2025'),
    R(F,'Desks & Workstations','Corner Desk','2400mm','Large L-shape desk, 2400×2000mm, executive veneer','Arteil','L-Exec XL','Walnut Veneer',2400,2000,730,None,1,'ea',1600,15,CONT,'Epic Office Furniture, approx AUD $1599, 2025'),
    R(F,'Desks & Workstations','Height-Adjustable Desk','2000mm wide','Wide electric sit-stand desk, 2000×800mm','Ergomotion','MotionDesk 2000','White',2000,800,720,None,1,'ea',1450,10,CONT,'Ergomotion.com.au, approx AUD $1449, 2025'),
    R(F,'Tables','Meeting Table','2400mm round','Round meeting table, 2400mm dia, veneer, pedestal base','Arteil','Round Board 2400','Walnut Veneer',2400,2400,750,None,1,'ea',5000,20,CONT,'Epic Office Furniture, approx AUD $4999, 2025'),
    R(F,'Tables','Café / Bar Table','Round 800mm','Breakout café table, round 800mm dia, white laminate','Generic','Cafe Rnd 800','White',800,800,730,None,1,'ea',300,10,CONT,'Fast Office Furniture, approx AUD $299, 2025'),
    R(F,'Tables','Coffee Table','Timber 1400mm','Timber coffee table, 1400×700mm, solid oak legs','Generic','Timber Coffee L','Natural Timber',1400,700,450,None,1,'ea',700,12,CONT,'Freedom Furniture, approx AUD $699, 2025'),
    R(F,'Storage & Filing','Filing Cabinet (Lateral)','3-drawer 1200mm','Lateral filing cabinet, 3-drawer, 1200mm W, graphite','Steelco','LFC3 1200','Graphite',1200,470,1050,None,1,'ea',900,20,CONT,'Winc, approx AUD $899, 2025'),
    R(F,'Storage & Filing','Bookcase / Shelf Unit','1800mm W glass doors','Wide bookcase with glass sliding doors, 1800mm W','Arteil','WideBook 1800G','White',1800,400,1800,None,1,'ea',1100,15,CONT,'Epic Office Furniture, approx AUD $1099, 2025'),
    R(F,'Storage & Filing','Storage Cabinet','600mm W full height','Narrow full-height storage cabinet, 600mm W','Steelco','SC600H','White',600,470,1830,None,1,'ea',500,20,CONT,'Winc, approx AUD $499, 2025'),
    R(F,'Storage & Filing','Locker','12-door','12-door locker bank, 300×450mm per bay','Steelco','Lok12','Grey',3600,450,1830,None,1,'ea',900,20,CONT,'Winc, approx AUD $899, 2025'),
    R(F,'Screens & Partitions','Acoustic Screen','Glass panel','Glass partition panel, 1200×1500mm, aluminium frame','Generic','Glass Panel','Clear/Aluminium',1200,12,1500,None,1,'ea',800,15,CONT,'Epic Office Furniture, approx AUD $799, 2025'),
    R(F,'Screens & Partitions','Whiteboard','1500×900mm','Magnetic whiteboard 1500×900mm','Visionchart','WB1509','White',1500,20,900,None,1,'ea',260,10,CONT,'Officeworks, approx AUD $259, 2025'),
    R(F,'Soft Furnishings','Window Blind','Plantation shutter 900mm','Plantation shutter panel, 900mm W, timber composite','Blinds Online','Plantation 900','White',900,70,2100,None,1,'ea',450,12,CONT,'Blinds Online AU, approx AUD $449, 2025'),
    R(F,'Soft Furnishings','Rug / Carpet Tile','500×500 tiles 10-pack','Interface carpet tiles, 500×500mm, 10-pack (2.5m²)','Interface','Tile Pack 10','Charcoal',500,500,None,None,10,'ea',80,8,CONT,'Interface.com, approx AUD $79/tile, 2025'),
    R(F,'Desks & Workstations','Bench Workstation','3-person','3-person bench workstation, 3600×800mm, white','Rapidline','Bench 3P','White',3600,800,720,None,1,'ea',1400,12,CONT,'Epic Office Furniture, approx AUD $1399, 2025'),
    R(F,'Tables','Boardroom Table','2400mm 10-person','Boardroom table, 2400×1000mm, veneer, cable port','Arteil','Board 2400','Walnut Veneer',2400,1000,750,None,1,'ea',2800,20,CONT,'Epic Office Furniture, approx AUD $2799, 2025'),
    R(F,'Seating','Task Chair','--','Anti-static ESD task chair, cleanroom use','Generic','ESD Chair','Black Conductive',650,620,1050,None,1,'ea',650,10,CONT,'Industrial supply AU, approx AUD $649, 2025'),
    R(F,'Seating','Task Chair','--','Saddle stool, height adjustable, clinical use','HÅG','Capisco','Black Fabric',None,None,None,None,1,'ea',950,12,CONT,'Flokk AU, approx AUD $949, 2025'),
    R(F,'Tables','Training Table','Folding 1200mm nesting','Nesting training table, 1200×600mm, rollable','Rapidline','Nest 1200','White',1200,600,730,None,1,'ea',310,10,CONT,'Winc, approx AUD $309, 2025'),
    R(F,'Storage & Filing','Plan Chest','A1 7-drawer','Plan chest, A1 format, 7-drawer, metal','Esselte','PlanChest A1 XL','Grey',1280,940,1380,None,1,'ea',2200,20,CONT,'Winc, approx AUD $2199, 2025'),
    R(F,'Screens & Partitions','Pinboard','600×900mm','Pinboard 600×900mm, fabric face, wall-mount','Visionchart','PB6090','Blue Fabric',600,20,900,None,1,'ea',90,10,CONT,'Officeworks, approx AUD $89, 2025'),
    R(F,'Desks & Workstations','Reception Desk / Counter','U-shape','U-shape reception counter with knee space','Rapidline','Recept U','White',2800,1800,1100,None,1,'ea',5500,15,CONT,'Fast Office Furniture, approx AUD $5499, 2025'),
    R(F,'Seating','Bench Seat','Outdoor park bench','Outdoor park bench, timber slat, cast iron frame','Generic','Park Bench','Natural/Black',1800,450,900,None,1,'ea',600,15,CONT,'Outdoor furniture AU, approx AUD $599, 2025'),
    R(F,'Seating','Visitor Chair','--','Visitor sled-base chair, plastic shell','Vitra','HAL','Natural',530,570,790,None,1,'ea',450,10,CONT,'Stylecraft AU, approx AUD $449, 2025'),
    R(F,'Tables','Height-Adjustable Table','Standing meeting 1200mm','Standing meeting table, electric, 1200×700mm','Ergomotion','SitStand Sm','White',1200,700,750,None,1,'ea',1200,10,CONT,'Ergomotion.com.au, approx AUD $1199, 2025'),
    R(F,'Storage & Filing','Compactus / Mobile Shelving','8-bay','Large compactus, 8-bay, 3600H, archive quality','Spacerak','Compactus 8B','Grey',4800,900,3600,None,1,'ea',12000,25,CONT,'Storage Systems Australia, approx AUD $11999, 2025'),
    R(F,'Soft Furnishings','Artwork / Print','Canvas triptych','Large canvas triptych, 3×panels 600×900mm','Generic','Triptych L','Abstract',600,50,900,None,3,'ea',350,10,CONT,'Art supply AU, approx AUD $349/set, 2025'),
    R(F,'Soft Furnishings','Planter / Indoor Plant','Tall corner planter','Tall corner indoor tree in pot, 1800mm H','Generic','Tall Plant','Various',500,500,1800,None,1,'ea',500,5,CONT,'Bunnings, approx AUD $499, 2025'),
    R(F,'Tables','Dining Table','4-person','Breakout dining table, 1200×700mm, 4-person','Generic','Dine 1200','Natural Timber',1200,700,740,None,1,'ea',400,12,CONT,'Officeworks, approx AUD $399, 2025'),
    R(F,'Seating','Drafting Chair','--','Draughtsman chair, mesh back, adjustable footring','Buro','Draft Mesh','Black Mesh',530,520,950,None,1,'ea',580,10,CONT,'Buro.com.au, approx AUD $579, 2025'),
]

IND='Industrial'
industrial_p4=[
    R(IND,'Power Tools','Impact Wrench','Cordless 3/4"','Cordless impact wrench, 18V, 3/4" drive, 1500Nm','Milwaukee','M18FHIWF34','Red/Black',None,None,None,None,1,'ea',750,5,PE,'Total Tools, approx AUD $749, 2025'),
    R(IND,'Power Tools','Rotary Hammer Drill','SDS-Max 36V cordless','Cordless SDS-Max demolition hammer, 36V, 10J','Makita','DHR400','Blue/Black',None,None,None,None,1,'ea',1200,5,PE,'Total Tools, approx AUD $1199, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (MIG)','Gasless portable','Gasless MIG welder, 90A, portable, 240V','Unimig','Viper 90','Blue',None,None,None,None,1,'ea',300,8,PE,'Total Tools, approx AUD $299, 2025'),
    R(IND,'Workshop Equipment','Air Compressor','Twin-tank 24L','Twin-tank portable compressor, 24L, 2HP, oil-free','Stanley Fatmax','SXCMS1524XE','Yellow',None,None,None,None,1,'ea',350,6,PE,'Bunnings, approx AUD $349, 2025'),
    R(IND,'Workshop Equipment','Tool Cabinet (Mobile)','Stainless top 15-drawer','Premium mobile tool cabinet, 15-drawer, stainless steel work top','Kincrome','K7960S','Black/Red',None,None,None,None,1,'ea',3000,15,PE,'Kincrome AU, approx AUD $2999, 2025'),
    R(IND,'Workshop Equipment','Workbench','Folding','Wall-mounted folding workbench, 1200mm, 200kg','Generic','FoldBench 1200','Black',1200,600,900,None,1,'ea',450,12,PE,'Total Tools, approx AUD $449, 2025'),
    R(IND,'Materials Handling','Sack Trolley','Telescoping handle','Telescoping handle sack trolley, 150kg, solid rubber','Wesco','SuperhandV2','Black',None,None,None,None,1,'ea',200,8,PE,'Bunnings, approx AUD $199, 2025'),
    R(IND,'Materials Handling','Extension Ladder','Combination 2.5–4.2m','Combination ladder, 2.5m straight / 1.5m step, 120kg','Gorilla','GCL-11','Silver',None,None,4200,None,1,'ea',300,10,PE,'Bunnings, approx AUD $299, 2025'),
    R(IND,'Safety Equipment','Safety Cabinet (Flammable)','50L','Flammable liquids safety cabinet, 50L, manual close','Storemasta','SC50Y','Yellow',620,430,580,None,1,'ea',650,20,PE,'Storemasta AU, approx AUD $649, 2025'),
    R(IND,'Safety Equipment','Spill Kit','Marine spill kit','Marine oil spill kit, 50L absorbent, bag + pads','Spill Station','Marine SK50','Yellow',None,None,None,None,1,'ea',200,3,PE,'Spill Station AU, approx AUD $199, 2025'),
    R(IND,'Measurement & Detection','Multimeter','Bench top bench meter','Bench-top digital multimeter, 6½ digit','Keysight','34461A','Grey',None,None,None,None,1,'ea',2000,8,PE,'RS Components AU, approx AUD $1999, 2025'),
    R(IND,'Measurement & Detection','Gas Detector','Toxic gas personal','Personal toxic gas monitor, H2S + CO, clip-on','Industrial Scientific','Ventis MX4','Yellow',None,None,None,None,1,'ea',600,3,PE,'Industrial Scientific AU, approx AUD $599, 2025'),
    R(IND,'Power Tools','Drill (Cordless)','Right angle 18V','Right-angle cordless drill, 18V, compact head','Milwaukee','M18BRAIW','Red/Black',None,None,None,None,1,'ea',320,5,PE,'Total Tools, approx AUD $319, 2025'),
    R(IND,'Workshop Equipment','Band Saw','Portable horizontal','Portable horizontal/vertical band saw, 1250W','Makita','LB1200F','Blue/Black',None,None,None,None,1,'ea',1800,10,PE,'Total Tools, approx AUD $1799, 2025'),
    R(IND,'Workshop Equipment','Industrial Vacuum','Hazardous dust','Hazardous dust class H vacuum, 1200W, HEPA H14','Nilfisk','GM 82 H','Yellow',None,None,None,None,1,'ea',1800,7,PE,'Nilfisk AU, approx AUD $1799, 2025'),
    R(IND,'Materials Handling','Order Picker','Electric stand-on','Electric stand-on order picker, 200kg, 4m','Crown','GPC3000','Red',None,None,None,None,1,'ea',12000,8,PE,'Crown Equipment AU, approx AUD $11999, 2025'),
    R(IND,'Measurement & Detection','Thermal Imaging Camera','Building inspection','Thermal imaging camera for building inspection, 160×120','Fluke','TiS10','Black',None,None,None,None,1,'ea',800,5,PE,'RS Components AU, approx AUD $799, 2025'),
]

IT='Information Technology'
it_p4=[
    R(IT,'Computing','Laptop / Notebook','Chromebook','Chromebook, 14", Intel Celeron, 8GB, 128GB eMMC','Lenovo','IdeaPad Flex 3i CB','Grey',325,225,18,None,1,'ea',600,4,CONT,'JB Hi-Fi, approx AUD $599, 2025'),
    R(IT,'Display & Peripherals','Printer (Desktop)','Receipt printer','Thermal receipt printer, USB/Ethernet, 80mm','Epson','TM-T88VI','Black',148,206,148,None,1,'ea',350,5,CONT,'Winc, approx AUD $349, 2025'),
    R(IT,'Display & Peripherals','Monitor / Screen','21.5" FHD','21.5" Full HD monitor, IPS, VGA/HDMI','HP','V22i','Black',None,None,None,21.5,1,'ea',280,6,CONT,'JB Hi-Fi, approx AUD $279, 2025'),
    R(IT,'Networking & Communications','Wireless Access Point','Mesh node','Wi-Fi 6E mesh node, tri-band, 6GHz','Netgear','Orbi RBK863S','White',None,None,None,None,1,'ea',500,5,CONT,'JB Hi-Fi, approx AUD $499, 2025'),
    R(IT,'Networking & Communications','NAS (Network Storage)','12-bay rackmount','12-bay rack NAS, 180TB usable, enterprise RAID','QNAP','TVS-h1288X','Black',482,519,88,None,1,'ea',8000,5,CONT,'QNAP AU, approx AUD $7999, 2025'),
    R(IT,'Computing','Desktop Computer (Tower)','Workstation i9','High-performance tower workstation, Core i9, 128GB, 4TB SSD, RTX 4090','HP','Z4 G5','Silver',175,445,400,None,1,'ea',8500,5,CONT,'HP AU, approx AUD $8499, 2025'),
    R(IT,'Display & Peripherals','UPS (Battery Backup)','700VA','UPS 700VA/420W, tower, LCD, AVR','CyberPower','CP700EPFCLCD','Black',None,None,None,None,1,'ea',220,5,CONT,'JB Hi-Fi, approx AUD $219, 2025'),
    R(IT,'Display & Peripherals','Webcam','Streaming 4K','Streaming webcam, 4K/60fps, AI background removal','Elgato','Facecam Pro','Black',None,None,None,None,1,'ea',350,4,CONT,'JB Hi-Fi, approx AUD $349, 2025'),
]

AV='Audio Visual'
av_p4=[
    R(AV,'Display Systems','Flat Screen TV','32"','32" Full HD Smart TV, HDR10','Samsung','UA32T5300','Black',None,None,None,32,1,'ea',450,8,CONT,'Harvey Norman, approx AUD $449, 2025'),
    R(AV,'Display Systems','Flat Screen TV','40"','40" 4K Smart TV, HDR, Wi-Fi, 3×HDMI','Hisense','40A5','Black',None,None,None,40,1,'ea',650,8,CONT,'Harvey Norman, approx AUD $649, 2025'),
    R(AV,'Display Systems','Projector','Laser 3LCD 6000lm','3LCD laser projector, 6000lm, WUXGA, sealed optics','Epson','EB-PU1006W','White',None,None,None,None,1,'ea',6000,10,CONT,'Epson AU, approx AUD $5999, 2025'),
    R(AV,'Video Conferencing','Video Bar (All-in-One)','MTR Windows','Video bar with built-in Windows PC, Teams Room','Neat','Neat Board 50','White',None,None,None,None,1,'ea',5500,5,CONT,'Neat AU, approx AUD $5499, 2025'),
    R(AV,'Audio Systems','Ceiling Speaker','Pendant commercial','Pendant commercial speaker, 200mm, 8Ω, black','Bosch','LC1-PC60G-8','Black',None,None,None,None,1,'ea',300,10,CONT,'Bosch AU, approx AUD $299, 2025'),
    R(AV,'Audio Systems','Wireless Microphone System','In-ear monitor','Wireless in-ear monitor system, 2-channel UHF','Sennheiser','EW-D IEM K','Black',None,None,None,None,1,'ea',1800,8,CONT,'Sennheiser AU, approx AUD $1799, 2025'),
    R(AV,'AV Control & Distribution','AV Matrix Switcher','HDBaseT 8×8','8×8 HDBaseT extender/matrix, 4K, 100m reach','Atlona','Velocity AT-VGW-HW-3','Black',440,200,44,None,1,'ea',4500,8,CONT,'AV distributor AU, approx AUD $4499, 2025'),
    R(AV,'Video Conferencing','Conferencing Speakerphone','AI noise cancelling','AI noise-cancelling room speakerphone, USB-C','EPOS','Expand 40T Pro','Black',None,None,None,None,1,'ea',900,4,CONT,'EPOS AU, approx AUD $899, 2025'),
    R(AV,'Display Systems','Interactive Whiteboard','55" classroom','55" interactive display, student-height, classroom','Clevertouch','UX Pro 55','Black',None,None,None,55,1,'ea',3200,7,CONT,'Clevertouch AU, approx AUD $3199, 2025'),
    R(AV,'AV Control & Distribution','Streaming / Presentation PC','4K NUC rack','4K NUC rack mount media server, i7, 16GB, SSD','Intel','NUC Rack','Black',None,None,None,None,1,'ea',1400,5,CONT,'Intel AU, approx AUD $1399, 2025'),
    R(AV,'Display Systems','Digital Signage Screen','65" outdoor','65" outdoor digital signage, IP56, 2500nit brightness','LG','65XE4F','Black',None,None,None,65,1,'ea',6500,8,CONT,'LG Business AU, approx AUD $6499, 2025'),
    R(AV,'Video Conferencing','PTZ Camera','USB 30x','USB PTZ camera, 30× optical zoom, 1080p','Avipas','AV-1081U','Black',None,None,None,None,1,'ea',1200,5,CONT,'AV distributor AU, approx AUD $1199, 2025'),
]

AP='Appliances & White Goods'
appliances_p4=[
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Chest freezer 300L','Commercial chest freezer, 300L, solid lid','Westinghouse','WCF302','White',1090,640,850,None,1,'ea',800,10,CONT,'Harvey Norman, approx AUD $799, 2025'),
    R(AP,'Kitchen Appliances','Coffee Machine (Pod)','Caffitaly capsule','Office capsule coffee machine, 1.2L, 19-bar','Caffitaly','S35','Silver',270,395,330,None,1,'ea',280,5,CONT,'Harvey Norman, approx AUD $279, 2025'),
    R(AP,'Kitchen Appliances','Toaster','Commercial pop-up 6-slice','Commercial 6-slice toaster, 3000W, stainless steel','Waring','WCT800','Stainless Steel',420,190,225,None,1,'ea',350,8,CONT,'Restaurant Supply AU, approx AUD $349, 2025'),
    R(AP,'Kitchen Appliances','Water Cooler / Dispenser','Mains cold-only','Mains-connected cold water cooler, stainless, under-counter','Zip','Chiller','Stainless Steel',300,375,900,None,1,'ea',500,8,CONT,'Zip Water AU, approx AUD $499, 2025'),
    R(AP,'Laundry Appliances','Washing Machine','Industrial 18kg','Industrial washing machine, 18kg, coin-op, stainless drum','Speed Queen','TC18','White',750,750,1150,None,1,'ea',4500,15,CONT,'Speed Queen AU, approx AUD $4499, 2025'),
    R(AP,'Kitchen Appliances','Refrigerator / Fridge','Wine fridge 40-bottle','Wine refrigerator, 40-bottle, dual zone','Vintec','V40SG2E','Stainless',440,580,850,None,1,'ea',700,8,CONT,'Harvey Norman, approx AUD $699, 2025'),
    R(AP,'Cleaning','Vacuum Cleaner','Cordless upright','Cordless upright vacuum, 25V, HEPA, self-emptying','Dyson','V15 Detect Absolute','Yellow/Purple',None,None,None,None,1,'ea',1200,5,CONT,'JB Hi-Fi, approx AUD $1199, 2025'),
]

part4 = furniture_p4+industrial_p4+it_p4+av_p4+appliances_p4

out=Path('Asset_Library_AU.csv')
with open(out,'r',encoding='utf-8') as f:
    existing=sum(1 for _ in f)-1
start_uid=200001+existing

with open(out,'a',newline='',encoding='utf-8') as f:
    w=csv.writer(f)
    for i,rec in enumerate(part4):
        rec[0]=start_uid+i
        w.writerow(rec)

total=existing+len(part4)
print(f"Part 4 appended: {len(part4)} records")
print(f"Total in file: {total}  |  UID range: 200001–{200001+total-1}")
