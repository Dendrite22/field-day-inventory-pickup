"""
Asset Library AU – Part 2
Appends Fitness, Vehicles, Industrial, Medical, Safes, Office Equipment
to Asset_Library_AU.csv (created by build_asset_library.py).
Run AFTER Part 1.
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
# FITNESS & RECREATION
# =============================================================================
FT = 'Fitness & Recreation'

fitness = [
    R(FT,'Cardio Equipment','Treadmill','Commercial light','Commercial treadmill, 15kph, 3.0HP, touchscreen console','Life Fitness','T3','Black',850,1930,1350,None,1,'ea',5500,10,CONT,'Commercial Fitness Equipment AU, approx AUD $5499, 2025'),
    R(FT,'Cardio Equipment','Treadmill','Commercial heavy duty','Commercial treadmill, 22kph, 4.0HP, 10" screen, 200kg rated','Life Fitness','Integrity+','Black',900,2100,1400,None,1,'ea',9500,10,CONT,'Commercial Fitness Equipment AU, approx AUD $9499, 2025'),
    R(FT,'Cardio Equipment','Treadmill','Home/light commercial','Folding treadmill, 18kph, 2.5HP, Bluetooth','NordicTrack','T6.5S','Black',800,1700,1350,None,1,'ea',2500,8,CONT,'JB Hi-Fi, approx AUD $2499, 2025'),
    R(FT,'Cardio Equipment','Elliptical / Cross Trainer','Commercial','Commercial elliptical cross trainer, 25-level resistance','Life Fitness','E1','Black',610,1530,1680,None,1,'ea',6500,10,CONT,'Compound Fitness AU, approx AUD $6499, 2025'),
    R(FT,'Cardio Equipment','Elliptical / Cross Trainer','Mid-range','Elliptical, 20-level resistance, 7" display','Sole','E25','Black',610,1530,1680,None,1,'ea',2800,8,CONT,'Compound Fitness AU, approx AUD $2799, 2025'),
    R(FT,'Cardio Equipment','Rowing Machine','Air rower commercial','Air rower, commercial grade, PM5 monitor','Concept2','RowErg','Black',244,581,1395,None,1,'ea',1900,10,CONT,'Concept2 AU, approx AUD $1899, 2025'),
    R(FT,'Cardio Equipment','Rowing Machine','Water rower','Water resistance rowing machine, beech wood','WaterRower','Natural','Natural Wood',560,580,1750,None,1,'ea',2200,10,CONT,'WaterRower AU, approx AUD $2199, 2025'),
    R(FT,'Cardio Equipment','Rowing Machine','Magnetic commercial','Magnetic rowing machine, 16-level resistance, LCD','Life Fitness','Row HX','Black',530,1960,860,None,1,'ea',3000,10,CONT,'Compound Fitness AU, approx AUD $2999, 2025'),
    R(FT,'Cardio Equipment','Exercise Bike (Upright)','Commercial upright','Commercial upright bike, 25-level resistance, console','Life Fitness','C1','Black',560,1020,1380,None,1,'ea',2200,10,CONT,'Commercial Fitness Equipment AU, approx AUD $2199, 2025'),
    R(FT,'Cardio Equipment','Exercise Bike (Upright)','Spin/indoor cycle','Commercial spin bike, weighted flywheel, toe clips','Schwinn','IC8','Black',500,1080,1080,None,1,'ea',1800,8,CONT,'Compound Fitness AU, approx AUD $1799, 2025'),
    R(FT,'Cardio Equipment','Exercise Bike (Recumbent)','Commercial','Commercial recumbent bike, 25-level, heart rate grip','Life Fitness','R1','Black',640,1490,1320,None,1,'ea',3200,10,CONT,'Commercial Fitness Equipment AU, approx AUD $3199, 2025'),
    R(FT,'Cardio Equipment','Exercise Bike (Recumbent)','Mid-range','Recumbent bike, 16-level, mesh seat','Sole','R92','Black',610,1520,1330,None,1,'ea',2000,8,CONT,'Compound Fitness AU, approx AUD $1999, 2025'),
    R(FT,'Cardio Equipment','Stair Climber','Commercial','Commercial stair climber / stepper, 25-level','Life Fitness','SC Base','Black',750,1320,1650,None,1,'ea',6000,10,CONT,'Commercial Fitness Equipment AU, approx AUD $5999, 2025'),

    R(FT,'Strength Equipment','Weight Bench','Flat','Flat weight bench, commercial, 300kg rated','Hammer Strength','FID Bench','Black',1440,640,430,None,1,'ea',600,12,CONT,'Compound Fitness AU, approx AUD $599, 2025'),
    R(FT,'Strength Equipment','Weight Bench','FID adjustable','FID adjustable weight bench, commercial grade','Hammer Strength','FID Adjustable','Black',1400,640,590,None,1,'ea',950,12,CONT,'Compound Fitness AU, approx AUD $949, 2025'),
    R(FT,'Strength Equipment','Squat Rack','Half rack','Half rack with pull-up bar, weight storage','Force USA','G3','Black',1050,1050,2200,None,1,'ea',1800,15,CONT,'Force USA AU, approx AUD $1799, 2025'),
    R(FT,'Strength Equipment','Squat Rack','Full power rack','Full power rack, safeties, weight storage, pull-up','Force USA','G12','Black',1220,1220,2440,None,1,'ea',3500,15,CONT,'Force USA AU, approx AUD $3499, 2025'),
    R(FT,'Strength Equipment','Cable Machine (Functional Trainer)','Dual stack','Dual stack functional trainer, 2×100kg','Force USA','FT100','Black',1200,900,2200,None,1,'ea',4500,15,CONT,'Force USA AU, approx AUD $4499, 2025'),
    R(FT,'Strength Equipment','Cable Machine (Functional Trainer)','Single stack','Single-stack cable machine, 200kg','Hammer Strength','MG-CSL','Black',900,900,2100,None,1,'ea',2800,15,CONT,'Compound Fitness AU, approx AUD $2799, 2025'),
    R(FT,'Strength Equipment','Dumbbell Rack','20-pair','20-pair dumbbell rack, A-frame, 3-tier','Hammer Strength','HDUMBRACK','Black',1800,600,1100,None,1,'ea',700,15,CONT,'Compound Fitness AU, approx AUD $699, 2025'),
    R(FT,'Strength Equipment','Dumbbell Rack','5-50lb set + rack','Hex dumbbell set 2.5–25kg (10 pairs) + rack','Hammer Strength','HEXSET','Black',None,None,None,None,1,'set',2200,15,CONT,'Compound Fitness AU, approx AUD $2199, 2025'),
    R(FT,'Strength Equipment','Barbell / Rack','Olympic barbell set','Olympic barbell 20kg + 100kg weight plate set + rack','Bodycraft','BB-Set','Black / Chrome',None,None,None,None,1,'set',1500,15,CONT,'Compound Fitness AU, approx AUD $1499, 2025'),
    R(FT,'Strength Equipment','Lat Pulldown Machine','Plate loaded','Lat pulldown / seated row, plate loaded','Hammer Strength','ISO Low Row','Black',1570,1840,1510,None,1,'ea',3500,15,CONT,'Compound Fitness AU, approx AUD $3499, 2025'),
    R(FT,'Strength Equipment','Leg Press Machine','Plate loaded','45° leg press, plate-loaded, commercial','Hammer Strength','ISO Leg Press','Black',1930,1680,1450,None,1,'ea',4000,15,CONT,'Compound Fitness AU, approx AUD $3999, 2025'),
    R(FT,'Strength Equipment','Smith Machine','Commercial','Commercial Smith machine, linear bearings','Force USA','G20 Smith','Black',1490,1500,2250,None,1,'ea',3200,15,CONT,'Force USA AU, approx AUD $3199, 2025'),

    R(FT,'Recreation','Pool Table','7-foot','7-foot billiards/pool table, slate bed, accessories','Billiard Factory','Emerald 7ft','Green Baize',2140,1200,780,None,1,'ea',3500,15,CONT,'Billiard Factory AU, approx AUD $3499, 2025'),
    R(FT,'Recreation','Pool Table','8-foot','8-foot slate pool table, full accessories kit','Billiard Factory','Emerald 8ft','Green Baize',2440,1330,780,None,1,'ea',5000,15,CONT,'Billiard Factory AU, approx AUD $4999, 2025'),
    R(FT,'Recreation','Table Tennis Table','Foldable indoor','Foldable indoor table tennis table, tournament size','Butterfly','Centrefold 25','Blue',1525,2740,760,None,1,'ea',900,10,CONT,'Butterfly AU, approx AUD $899, 2025'),
    R(FT,'Recreation','Table Tennis Table','Outdoor','All-weather outdoor table tennis table','Cornilleau','500 Outdoor','Grey/Blue',1525,2740,760,None,1,'ea',1500,10,CONT,'Cornilleau AU, approx AUD $1499, 2025'),
    R(FT,'Recreation','Foosball Table','Standard','Standard foosball/table football, solid steel rods','Garlando','G-500','Black',760,1370,880,None,1,'ea',700,10,CONT,'Online retailers AU, approx AUD $699, 2025'),
    R(FT,'Recreation','Foosball Table','Commercial','Commercial coin-op foosball table, heavy duty','Garlando','G-2000','Black',760,1370,880,None,1,'ea',1500,10,CONT,'Online retailers AU, approx AUD $1499, 2025'),
    R(FT,'Recreation','Air Hockey Table','Full size','7-foot air hockey table, electronic scoring','Generic','AH-7FT','Black',1960,1050,780,None,1,'ea',900,10,CONT,'iFun AU, approx AUD $899, 2025'),
    R(FT,'Recreation','Punching Bag','Heavy bag','Heavy punching bag, 45kg, chain mount','Everlast','Omnistrike','Black',None,None,None,None,1,'ea',400,8,CONT,'Rebel Sport, approx AUD $399, 2025'),
]

# =============================================================================
# VEHICLES & MOTORISED PLANT
# =============================================================================
VH = 'Vehicles & Motorised Plant'

vehicles = [
    # ── Motor Vehicles ────────────────────────────────────────────────────────
    R(VH,'Motor Vehicles','Passenger Car','Small sedan','Small sedan, 4cyl petrol, 5-door hatch, auto','Toyota','Corolla GX','White',4620,1780,1455,None,1,'ea',32000,8,MV,'Toyota AU, approx AUD $31990, 2025'),
    R(VH,'Motor Vehicles','Passenger Car','Medium sedan','Medium sedan, 2.5L hybrid, auto','Toyota','Camry Ascent','White',4905,1840,1445,None,1,'ea',38000,8,MV,'Toyota AU, approx AUD $37990, 2025'),
    R(VH,'Motor Vehicles','Passenger Car','Large executive','Large executive sedan, 2.0T, premium','Hyundai','Sonata N Line','White',4900,1860,1445,None,1,'ea',45000,8,MV,'Hyundai AU, approx AUD $44990, 2025'),
    R(VH,'Motor Vehicles','SUV / 4WD','Small SUV','Small SUV, 2.0L petrol, FWD, 5-seat','Mazda','CX-3 Maxx','White',4275,1765,1535,None,1,'ea',30000,8,MV,'Mazda AU, approx AUD $29990, 2025'),
    R(VH,'Motor Vehicles','SUV / 4WD','Medium SUV','Medium SUV, hybrid, AWD, 5-seat','Toyota','RAV4 GX Hybrid','White',4600,1855,1685,None,1,'ea',46000,8,MV,'Toyota AU, approx AUD $45990, 2025'),
    R(VH,'Motor Vehicles','SUV / 4WD','Large 4WD','Large 4WD wagon, diesel, 7-seat','Toyota','LandCruiser 300 GX','White',4950,1980,1870,None,1,'ea',90000,10,MV,'Toyota AU, approx AUD $89990, 2025'),
    R(VH,'Motor Vehicles','SUV / 4WD','Mid-size 4WD','Mid-size 4WD, diesel, 5-seat, tow-rated 3.5t','Toyota','HiLux Rugged X','White',5330,1855,1815,None,1,'ea',68000,8,MV,'Toyota AU, approx AUD $67990, 2025'),
    R(VH,'Motor Vehicles','Utility Vehicle (Ute)','4WD single cab','Single-cab ute, diesel, manual, payload 1t','Ford','Ranger XL','White',5346,1860,1815,None,1,'ea',40000,8,MV,'Ford AU, approx AUD $39990, 2025'),
    R(VH,'Motor Vehicles','Utility Vehicle (Ute)','4WD dual cab','Dual-cab ute, diesel, auto, tub liner','Toyota','HiLux SR5','White',5330,1855,1815,None,1,'ea',58000,8,MV,'Toyota AU, approx AUD $57990, 2025'),
    R(VH,'Motor Vehicles','Utility Vehicle (Ute)','4WD dual cab premium','Dual-cab ute, diesel, premium spec, leather','Ford','Ranger Wildtrak','White',5346,1860,1815,None,1,'ea',68000,8,MV,'Ford AU, approx AUD $67990, 2025'),
    R(VH,'Motor Vehicles','Van / People Mover','LWB van cargo','LWB cargo van, diesel, 1.5m load floor','Hyundai','iLoad LWB','White',5150,1915,1980,None,1,'ea',42000,10,MV,'Hyundai AU, approx AUD $41990, 2025'),
    R(VH,'Motor Vehicles','Van / People Mover','People mover 8-seat','8-seat people mover, petrol/hybrid, auto','Kia','Carnival S Hybrid','White',5115,1995,1765,None,1,'ea',56000,10,MV,'Kia AU, approx AUD $55990, 2025'),
    R(VH,'Motor Vehicles','Van / People Mover','High-roof van','High-roof cargo van, diesel, swivel rack','Mercedes-Benz','Sprinter 314CDI','White',5910,1993,2650,None,1,'ea',72000,10,MV,'Mercedes-Benz AU, approx AUD $71990, 2025'),
    R(VH,'Motor Vehicles','Minibus','12-seat','12-seat minibus, diesel, auto, A/C','Toyota','HiAce Commuter','White',5380,1950,2285,None,1,'ea',65000,10,MV,'Toyota AU, approx AUD $64990, 2025'),
    R(VH,'Motor Vehicles','Minibus','21-seat','21-seat minibus, MAN diesel, A/C','Bus & Coach','MAN 21-seat','White',7500,2200,2800,None,1,'ea',150000,15,MV,'Bus industry AU, approx AUD $149990, 2025'),
    R(VH,'Motor Vehicles','Electric Vehicle','Small EV hatch','Small EV, 66kWh battery, 490km range','BYD','Atto 3 Extended','White',4455,1875,1615,None,1,'ea',45000,8,MV,'BYD AU, approx AUD $44990, 2025'),
    R(VH,'Motor Vehicles','Electric Vehicle','Medium EV sedan','Medium EV, 82kWh battery, 568km range','Tesla','Model 3 RWD','White',4694,1849,1443,None,1,'ea',60000,8,MV,'Tesla AU, approx AUD $59990, 2025'),
    R(VH,'Motor Vehicles','Electric Vehicle','Large EV SUV','Large EV SUV, 100kWh, AWD, 7-seat','Tesla','Model X','White',5037,1999,1684,None,1,'ea',120000,8,MV,'Tesla AU, approx AUD $119990, 2025'),
    R(VH,'Motor Vehicles','Electric Vehicle','EV ute','Electric ute, range-extender, dual motor AWD','LDV','MIFA 9 EV Ute','White',5260,1960,1860,None,1,'ea',70000,8,MV,'LDV AU, approx AUD $69990, 2025'),

    # ── Motorised Plant ───────────────────────────────────────────────────────
    R(VH,'Motorised Plant','Forklift','2.5t LPG','LPG counterbalance forklift, 2.5t capacity, 3m lift','Toyota','8FGF25','Yellow',1200,2550,2100,None,1,'ea',45000,10,PE,'Toyota Material Handling AU, approx AUD $44990, 2025'),
    R(VH,'Motorised Plant','Forklift','3t electric','Electric counterbalance forklift, 3t, 4.5m mast','Toyota','8FBMT30','Yellow',1200,2750,2200,None,1,'ea',55000,10,PE,'Toyota Material Handling AU, approx AUD $54990, 2025'),
    R(VH,'Motorised Plant','Forklift','1.5t sit-down electric','Sit-down electric forklift, 1.5t, 3m lift','Crown','SC5700','Red',1100,2400,1900,None,1,'ea',38000,10,PE,'Crown Equipment AU, approx AUD $37990, 2025'),
    R(VH,'Motorised Plant','Pallet Jack (Electric)','1.5t ride-on','Ride-on electric pallet jack, 1.5t, 1.2m forks','Crown','PE 4500','Blue',840,2390,1300,None,1,'ea',11000,8,PE,'Crown Equipment AU, approx AUD $10990, 2025'),
    R(VH,'Motorised Plant','Pallet Jack (Electric)','2t walkie','Walkie electric pallet jack, 2t, 1.2m forks','Toyota','LPE200','Blue',760,2370,1200,None,1,'ea',7500,8,PE,'Toyota Material Handling AU, approx AUD $7490, 2025'),
    R(VH,'Motorised Plant','Scissor Lift','6m electric','Electric scissor lift, 6m working height, 230kg','Haulotte','Optimum 8','Yellow',820,1500,1800,None,1,'ea',18000,10,PE,'Kennards Hire cost ref; new approx AUD $17990, 2025'),
    R(VH,'Motorised Plant','Scissor Lift','10m electric','Electric scissor lift, 10m working height, 230kg','Haulotte','COMPACT 12','Yellow',820,2230,1870,None,1,'ea',28000,10,PE,'Haulotte AU, approx AUD $27990, 2025'),
    R(VH,'Motorised Plant','Boom Lift (Cherry Picker)','12m articulating','12m articulating boom lift, diesel, 230kg','JLG','450AJ','Yellow',1800,5160,2310,None,1,'ea',55000,12,PE,'JLG AU, approx AUD $54990, 2025'),
    R(VH,'Motorised Plant','Boom Lift (Cherry Picker)','20m telescopic','20m telescopic boom lift, diesel, 230kg','JLG','660SJ','Yellow',2490,8490,2490,None,1,'ea',120000,12,PE,'JLG AU, approx AUD $119990, 2025'),
    R(VH,'Motorised Plant','Generator (Portable)','5kVA petrol','Portable petrol generator, 5kVA, single phase, AVR','Pramac','ES5000','Yellow',680,490,505,None,1,'ea',2800,10,PE,'Generator World AU, approx AUD $2799, 2025'),
    R(VH,'Motorised Plant','Generator (Portable)','10kVA diesel','Portable diesel generator, 10kVA, single phase','Pramac','E10000','Yellow',890,600,700,None,1,'ea',5500,10,PE,'Generator World AU, approx AUD $5499, 2025'),
    R(VH,'Motorised Plant','Generator (Standby)','20kVA diesel','Standby diesel generator, 20kVA, 3-phase, AMF','Cummins','C20D6H','Yellow/Green',2100,800,1300,None,1,'ea',18000,15,PE,'Cummins AU, approx AUD $17990, 2025'),
    R(VH,'Motorised Plant','Generator (Standby)','60kVA diesel','Standby diesel generator, 60kVA, 3-phase, weatherproof canopy','Cummins','C60D5H','Yellow/Green',2800,1100,1600,None,1,'ea',40000,15,PE,'Cummins AU, approx AUD $39990, 2025'),
    R(VH,'Motorised Plant','Golf Cart / EV Buggy','2-seat','Electric golf cart, 2-seat, 48V lithium, folding windscreen','Club Car','Tempo 2','White',2420,1200,1820,None,1,'ea',12000,8,PE,'Club Car AU, approx AUD $11990, 2025'),
    R(VH,'Motorised Plant','Golf Cart / EV Buggy','4-seat','Electric golf cart, 4-seat, 48V, canopy','Club Car','Onward 4','White',3140,1200,1820,None,1,'ea',18000,8,PE,'Club Car AU, approx AUD $17990, 2025'),
    R(VH,'Motorised Plant','Golf Cart / EV Buggy','Utility buggy','Utility electric buggy, flatbed, 600kg payload','Club Car','Carryall 1500','Yellow',3700,1485,1950,None,1,'ea',22000,8,PE,'Club Car AU, approx AUD $21990, 2025'),
    R(VH,'Motorised Plant','Ride-on Mower','Commercial zero-turn','Commercial zero-turn mower, 52" cut, 25HP Kawasaki','Husqvarna','MZ54S','Orange/Black',1620,1540,1090,None,1,'ea',9500,8,PE,'Husqvarna AU, approx AUD $9490, 2025'),
    R(VH,'Motorised Plant','Ride-on Mower','Diesel tractor','Diesel ride-on mower tractor, 42" cut, 22HP','Kubota','GX21HD','Orange',1850,1750,1420,None,1,'ea',13000,10,PE,'Kubota AU, approx AUD $12990, 2025'),
    R(VH,'Motorised Plant','Walk-behind Mower','Commercial self-propelled','Commercial self-propelled mower, 21" cut, Honda engine','Honda','HRX217','Red',565,480,935,None,1,'ea',1400,7,PE,'Bunnings, approx AUD $1399, 2025'),
    R(VH,'Motorised Plant','High-Pressure Cleaner','Cold water 200 bar','Cold water pressure washer, 200 bar, 15L/min','Karcher','HD 7/18 CX','Yellow',850,545,1030,None,1,'ea',3200,8,PE,'Karcher AU, approx AUD $3199, 2025'),
    R(VH,'Motorised Plant','High-Pressure Cleaner','Hot water','Hot water pressure washer, 180 bar, diesel','Karcher','HDS 8/18 CX','Yellow',1130,640,1220,None,1,'ea',8000,8,PE,'Karcher AU, approx AUD $7999, 2025'),
    R(VH,'Motorised Plant','Ride-on Sweeper','Small petrol','Walk-behind sweeper, 76cm, petrol, commercial','Tennant','S6','Orange',760,810,1160,None,1,'ea',5500,8,PE,'Tennant AU, approx AUD $5499, 2025'),
]

# =============================================================================
# INDUSTRIAL
# =============================================================================
IND = 'Industrial'

industrial = [
    # ── Power Tools ───────────────────────────────────────────────────────────
    R(IND,'Power Tools','Angle Grinder','115mm corded','Angle grinder, 115mm, 840W, corded','Makita','GA4530R','Blue/Black',None,None,None,None,1,'ea',120,5,PE,'Bunnings, approx AUD $119, 2025'),
    R(IND,'Power Tools','Angle Grinder','125mm corded','Angle grinder, 125mm, 1000W, corded','Makita','GA5034R','Blue/Black',None,None,None,None,1,'ea',150,5,PE,'Bunnings, approx AUD $149, 2025'),
    R(IND,'Power Tools','Angle Grinder','230mm corded','Angle grinder, 230mm, 2000W, corded','Makita','GA9020SF','Blue/Black',None,None,None,None,1,'ea',280,5,PE,'Bunnings, approx AUD $279, 2025'),
    R(IND,'Power Tools','Angle Grinder','125mm cordless 18V','Cordless angle grinder, 125mm, 18V brushless','Makita','DGA504Z','Blue/Black',None,None,None,None,1,'ea',250,5,PE,'Bunnings, approx AUD $249, 2025'),
    R(IND,'Power Tools','Circular Saw','165mm corded','Circular saw, 165mm, 1200W, corded','Makita','HS6601','Blue/Black',None,None,None,None,1,'ea',180,5,PE,'Bunnings, approx AUD $179, 2025'),
    R(IND,'Power Tools','Circular Saw','185mm cordless 18V','Cordless circular saw, 185mm, 18V brushless','DeWALT','DCS570N','Yellow/Black',None,None,None,None,1,'ea',300,5,PE,'Bunnings, approx AUD $299, 2025'),
    R(IND,'Power Tools','Jigsaw','Corded','Jigsaw, 750W, pendulum action, corded','Bosch','GST 160 BCE','Blue',None,None,None,None,1,'ea',250,5,PE,'Bunnings, approx AUD $249, 2025'),
    R(IND,'Power Tools','Jigsaw','Cordless 18V','Cordless jigsaw, 18V, brushless','DeWALT','DCS334N','Yellow/Black',None,None,None,None,1,'ea',230,5,PE,'Bunnings, approx AUD $229, 2025'),
    R(IND,'Power Tools','Drill (Cordless)','18V 2-speed','Cordless drill/driver, 18V, 2-speed, 2×5Ah kit','Makita','DDF459RME','Blue/Black',None,None,None,None,1,'ea',300,5,PE,'Bunnings, approx AUD $299, 2025'),
    R(IND,'Power Tools','Drill (Cordless)','18V brushless kit','Cordless drill/driver, 18V brushless, 2×5Ah battery kit','DeWALT','DCD791D2T','Yellow/Black',None,None,None,None,1,'ea',380,5,PE,'Bunnings, approx AUD $379, 2025'),
    R(IND,'Power Tools','Drill (Cordless)','Heavy duty 18V hammer','Cordless combi hammer drill, 18V, 2-speed','Makita','DHP484RMJ','Blue/Black',None,None,None,None,1,'ea',350,5,PE,'Bunnings, approx AUD $349, 2025'),
    R(IND,'Power Tools','Impact Driver (Cordless)','18V brushless','Cordless impact driver, 18V brushless, 185Nm','DeWALT','DCF887D2','Yellow/Black',None,None,None,None,1,'ea',320,5,PE,'Bunnings, approx AUD $319, 2025'),
    R(IND,'Power Tools','Impact Driver (Cordless)','18V Makita','Cordless impact driver, 18V, quick-change chuck','Makita','DTD153RME','Blue/Black',None,None,None,None,1,'ea',290,5,PE,'Bunnings, approx AUD $289, 2025'),
    R(IND,'Power Tools','Rotary Hammer Drill','SDS-Plus 800W','SDS-Plus rotary hammer drill, 800W, 3-mode','Bosch','GBH 2-26','Blue',None,None,None,None,1,'ea',320,5,PE,'Bunnings, approx AUD $319, 2025'),
    R(IND,'Power Tools','Rotary Hammer Drill','SDS-Max heavy duty','SDS-Max heavy-duty demolition hammer, 1500W','Makita','HR4013C','Blue/Black',None,None,None,None,1,'ea',900,5,PE,'Total Tools, approx AUD $899, 2025'),
    R(IND,'Power Tools','Random Orbital Sander','125mm','Random orbital sander, 125mm, 300W, corded','Makita','BO5041K','Blue/Black',None,None,None,None,1,'ea',160,5,PE,'Bunnings, approx AUD $159, 2025'),
    R(IND,'Power Tools','Random Orbital Sander','125mm cordless','Cordless random orbital sander, 125mm, 18V','DeWALT','DCW210B','Yellow/Black',None,None,None,None,1,'ea',200,5,PE,'Bunnings, approx AUD $199, 2025'),
    R(IND,'Power Tools','Reciprocating Saw','Corded','Reciprocating saw, 1100W, variable speed, corded','Bosch','GSA 1300 PCE','Blue',None,None,None,None,1,'ea',280,5,PE,'Bunnings, approx AUD $279, 2025'),
    R(IND,'Power Tools','Reciprocating Saw','Cordless 18V','Cordless reciprocating saw, 18V brushless','DeWALT','DCS367N','Yellow/Black',None,None,None,None,1,'ea',260,5,PE,'Bunnings, approx AUD $259, 2025'),
    R(IND,'Power Tools','Router','Fixed base 2300W','Fixed-base router, 2300W, plunge action','Makita','RP2301FC','Blue/Black',None,None,None,None,1,'ea',350,5,PE,'Total Tools, approx AUD $349, 2025'),
    R(IND,'Power Tools','Heat Gun','2000W','Heat gun, 2000W, 2-speed, LCD temperature','Bosch','GHG 18-60','Blue',None,None,None,None,1,'ea',150,5,PE,'Bunnings, approx AUD $149, 2025'),
    R(IND,'Power Tools','Bench Grinder','200mm','Bench grinder, 200mm, 370W, eye shields','Jet','JBG-8A','Grey',None,None,None,None,1,'ea',280,8,PE,'Total Tools, approx AUD $279, 2025'),

    # ── Workshop Equipment ────────────────────────────────────────────────────
    R(IND,'Workshop Equipment','Air Compressor','50L belt-drive','Belt-drive air compressor, 50L tank, 2.5HP','Pilot Air','K25-50','Black/Red',None,None,None,None,1,'ea',600,8,PE,'Gasweld, approx AUD $599, 2025'),
    R(IND,'Workshop Equipment','Air Compressor','100L belt-drive','Belt-drive air compressor, 100L, 3HP, oil-cooled','Pilot Air','K25-100','Black/Red',None,None,None,None,1,'ea',950,8,PE,'Gasweld, approx AUD $949, 2025'),
    R(IND,'Workshop Equipment','Air Compressor','200L industrial','Industrial piston compressor, 200L, 5.5HP','Pilot Air','K50-200','Black/Red',None,None,None,None,1,'ea',2000,10,PE,'Gasweld, approx AUD $1999, 2025'),
    R(IND,'Workshop Equipment','Air Compressor','Portable 8L','Portable pancake air compressor, 8L, 1HP, oil-free','Ryobi','PCM500','Black/Yellow',None,None,None,None,1,'ea',220,6,PE,'Bunnings, approx AUD $219, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (MIG)','130A gasless','MIG welder, 130A gasless, portable','CIGWELD','Weldskill 130','Blue',None,None,None,None,1,'ea',550,8,PE,'Gasweld, approx AUD $549, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (MIG)','180A gas/gasless','MIG welder, 180A, gas or gasless, synergic','CIGWELD','Weldskill 180','Blue',None,None,None,None,1,'ea',900,8,PE,'Gasweld, approx AUD $899, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (MIG)','250A industrial','Industrial MIG welder, 250A, wire feed','Lincoln Electric','PowerMIG 256','Red',None,None,None,None,1,'ea',2200,10,PE,'Lincoln Electric AU, approx AUD $2199, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (TIG)','200A TIG/MMA','TIG/MMA welder, 200A, AC/DC, foot pedal','Everlast','PowerTIG 200DV','Yellow',None,None,None,None,1,'ea',1800,10,PE,'Gasweld, approx AUD $1799, 2025'),
    R(IND,'Workshop Equipment','Welding Machine (TIG)','315A industrial','Industrial AC/DC TIG welder, 315A, water cooled','Miller','Dynasty 315','Blue',None,None,None,None,1,'ea',6500,10,PE,'Miller Welding AU, approx AUD $6499, 2025'),
    R(IND,'Workshop Equipment','Band Saw','14" bench','14" bench bandsaw, 750W, rip fence','Jet','JWBS-14OS','Grey',None,None,None,None,1,'ea',1200,10,PE,'Total Tools, approx AUD $1199, 2025'),
    R(IND,'Workshop Equipment','Band Saw','Industrial floor','Industrial floor bandsaw, 2HP, cast iron table','Jet','JWBS-18','Grey',None,None,None,None,1,'ea',3500,10,PE,'Total Tools, approx AUD $3499, 2025'),
    R(IND,'Workshop Equipment','Drill Press (Bench)','16-speed','16-speed bench drill press, 370W, MT2','Jet','JDP-17DX','Grey',None,None,None,None,1,'ea',700,10,PE,'Total Tools, approx AUD $699, 2025'),
    R(IND,'Workshop Equipment','Hydraulic Press','20-tonne','Shop press, 20-tonne, hydraulic, floor stand','Peerless','20T Press','Black',None,None,None,None,1,'ea',1500,15,PE,'Total Tools, approx AUD $1499, 2025'),
    R(IND,'Workshop Equipment','Parts Washer','Bench top','Bench-top parts washer, 40L, electric pump','Generic','PW40','Black',None,None,None,None,1,'ea',500,8,PE,'Total Tools, approx AUD $499, 2025'),
    R(IND,'Workshop Equipment','Parts Washer','Industrial','Industrial parts washer, 100L, heated','Allied Products','IPW100','Grey',None,None,None,None,1,'ea',1800,10,PE,'Industrial supply AU, approx AUD $1799, 2025'),
    R(IND,'Workshop Equipment','Tool Cabinet (Mobile)','7-drawer','Mobile tool cabinet, 7-drawer, lockable, ball bearing slides','Kincrome','K7820B','Black',None,None,None,None,1,'ea',900,15,PE,'Kincrome AU, approx AUD $899, 2025'),
    R(IND,'Workshop Equipment','Tool Cabinet (Mobile)','11-drawer','Mobile tool cabinet, 11-drawer, stainless top, locking','Kincrome','K7950S','Red/Black',None,None,None,None,1,'ea',1800,15,PE,'Kincrome AU, approx AUD $1799, 2025'),
    R(IND,'Workshop Equipment','Workbench','1800mm steel','Steel workbench, 1800×750mm, shelf, drawer','Kincrome','K7800','Grey',1800,750,900,None,1,'ea',800,15,PE,'Kincrome AU, approx AUD $799, 2025'),
    R(IND,'Workshop Equipment','Workbench','2400mm heavy duty','Heavy-duty steel workbench, 2400mm, 1000kg rated','Kincrome','K7812','Grey',2400,750,900,None,1,'ea',1400,15,PE,'Kincrome AU, approx AUD $1399, 2025'),
    R(IND,'Workshop Equipment','Industrial Vacuum','30L wet/dry','30L wet/dry industrial vacuum, HEPA, 1400W','Nilfisk','Attix 33','Yellow',None,None,None,None,1,'ea',800,7,PE,'Nilfisk AU, approx AUD $799, 2025'),
    R(IND,'Workshop Equipment','Industrial Vacuum','Three-phase','3-phase industrial vacuum, 60L, HEPA H13','Nilfisk','VHW321','Yellow',None,None,None,None,1,'ea',2500,8,PE,'Nilfisk AU, approx AUD $2499, 2025'),
    R(IND,'Workshop Equipment','Tyre Changer','Leverless','Leverless tyre changer, semi-automatic, 24"','John Bean','TC325P','Black',None,None,None,None,1,'ea',4000,10,PE,'Snap-on Equipment AU, approx AUD $3999, 2025'),
    R(IND,'Workshop Equipment','Wheel Balancer','Static/dynamic','Static/dynamic wheel balancer, 65kg rated','John Bean','V3400','Black',None,None,None,None,1,'ea',5000,10,PE,'Snap-on Equipment AU, approx AUD $4999, 2025'),

    # ── Materials Handling ────────────────────────────────────────────────────
    R(IND,'Materials Handling','Pallet Jack (Manual)','2.5t','Manual hydraulic pallet jack, 2.5t, 1150mm forks','Noblelift','PTE2500','Red',550,1150,1200,None,1,'ea',550,8,PE,'Bunnings, approx AUD $549, 2025'),
    R(IND,'Materials Handling','Pallet Jack (Manual)','3t long fork','Manual pallet jack, 3t, 1800mm long forks','Noblelift','PTE3000L','Red',550,1800,1200,None,1,'ea',700,8,PE,'Total Tools, approx AUD $699, 2025'),
    R(IND,'Materials Handling','Sack Trolley','200kg','Steel sack trolley, 200kg, rubber wheels','Generic','ST200','Black',None,None,None,None,1,'ea',120,8,PE,'Bunnings, approx AUD $119, 2025'),
    R(IND,'Materials Handling','Sack Trolley','300kg heavy duty','Heavy-duty sack trolley, 300kg, pneumatic tyres','Wesco','LT300','Black',None,None,None,None,1,'ea',250,8,PE,'Bunnings, approx AUD $249, 2025'),
    R(IND,'Materials Handling','Sack Trolley','Stair climber','Motorised stair climbing sack trolley, 100kg','Zonzini','Domino','Black',None,None,None,None,1,'ea',2800,8,PE,'Sydney Tools, approx AUD $2799, 2025'),
    R(IND,'Materials Handling','Platform Trolley','500kg','Platform trolley, 500kg, 1000×600mm','Sureweld','PT1060','Black',1000,600,None,None,1,'ea',280,8,PE,'Bunnings, approx AUD $279, 2025'),
    R(IND,'Materials Handling','Platform Trolley','1000kg','Heavy-duty platform trolley, 1000kg, 1200×800mm','Sureweld','PT1280H','Black',1200,800,None,None,1,'ea',450,8,PE,'Total Tools, approx AUD $449, 2025'),
    R(IND,'Materials Handling','Drum Trolley','200L','Drum trolley, 200L drum capacity, screw clamp','Spill Station','DTR200','Yellow',None,None,None,None,1,'ea',450,8,PE,'Spill Station AU, approx AUD $449, 2025'),
    R(IND,'Materials Handling','Step Ladder','1.8m fibreglass','Fibreglass step ladder, 1.8m, 150kg rated','Bailey','FS14','Fibreglass',None,None,1800,None,1,'ea',280,10,PE,'Bunnings, approx AUD $279, 2025'),
    R(IND,'Materials Handling','Step Ladder','2.4m aluminium','Aluminium step ladder, 2.4m, 120kg rated','Gorilla','GLW-0905','Silver',None,None,2400,None,1,'ea',220,10,PE,'Bunnings, approx AUD $219, 2025'),
    R(IND,'Materials Handling','Step Ladder','3m multi-purpose','Multi-purpose ladder, 3m, aluminium, 150kg','Gorilla','GMPB-22','Silver',None,None,3000,None,1,'ea',350,10,PE,'Bunnings, approx AUD $349, 2025'),
    R(IND,'Materials Handling','Extension Ladder','3.6m','Aluminium extension ladder, 3.6m, 120kg','Bailey','ESA-12','Silver',None,None,3600,None,1,'ea',280,10,PE,'Bunnings, approx AUD $279, 2025'),
    R(IND,'Materials Handling','Extension Ladder','6m','Aluminium extension ladder, 6m, 120kg, rope & pulley','Bailey','ESA-20','Silver',None,None,6000,None,1,'ea',400,10,PE,'Bunnings, approx AUD $399, 2025'),
    R(IND,'Materials Handling','Extension Ladder','9m fibreglass','Fibreglass extension ladder, 9m, 150kg, insulated','Bailey','FS-30','Fibreglass',None,None,9000,None,1,'ea',700,10,PE,'Bunnings, approx AUD $699, 2025'),
    R(IND,'Materials Handling','Stillage / Pallet Cage','1t mesh','Mesh stillage cage, 1t, 1165×840×845mm','Loscam','Mesh Cage','Grey',1165,840,845,None,1,'ea',700,15,PE,'Loscam AU, approx AUD $699, 2025'),

    # ── Safety Equipment ──────────────────────────────────────────────────────
    R(IND,'Safety Equipment','Fire Extinguisher','2.5kg ABE','2.5kg ABE dry chemical extinguisher, wall bracket','Chubb','2.5ABE','Red',None,None,None,None,1,'ea',80,5,PE,'Chubb Fire AU, approx AUD $79, 2025'),
    R(IND,'Safety Equipment','Fire Extinguisher','4.5kg ABE','4.5kg ABE dry chemical extinguisher','Chubb','4.5ABE','Red',None,None,None,None,1,'ea',120,5,PE,'Chubb Fire AU, approx AUD $119, 2025'),
    R(IND,'Safety Equipment','Fire Extinguisher','9L wet chemical','9L wet chemical extinguisher (commercial kitchen)','Chubb','9LWC','Red',None,None,None,None,1,'ea',250,5,PE,'Chubb Fire AU, approx AUD $249, 2025'),
    R(IND,'Safety Equipment','Fire Extinguisher','5kg CO2','5kg CO2 extinguisher (electrical/IT)','Chubb','5CO2','Red',None,None,None,None,1,'ea',220,5,PE,'Chubb Fire AU, approx AUD $219, 2025'),
    R(IND,'Safety Equipment','Fire Hose Reel','30m','Fire hose reel, 30m, wall-mount, brass nozzle','Wormald','WHR30','Red',None,None,None,None,1,'ea',350,10,PE,'Wormald AU, approx AUD $349, 2025'),
    R(IND,'Safety Equipment','Safety Cabinet (Flammable)','30L','Flammable liquids safety cabinet, 30L, yellow, AS1940','Storemasta','SC30Y','Yellow',460,350,430,None,1,'ea',450,20,PE,'Storemasta AU, approx AUD $449, 2025'),
    R(IND,'Safety Equipment','Safety Cabinet (Flammable)','100L','Flammable liquids safety cabinet, 100L, AS1940','Storemasta','SC100Y','Yellow',870,460,850,None,1,'ea',900,20,PE,'Storemasta AU, approx AUD $899, 2025'),
    R(IND,'Safety Equipment','Safety Cabinet (Corrosive)','30L','Corrosive storage cabinet, 30L, polyethylene, white','Storemasta','CC30W','White',460,350,430,None,1,'ea',550,20,PE,'Storemasta AU, approx AUD $549, 2025'),
    R(IND,'Safety Equipment','Spill Kit','20L absorbent','Spill kit, 20L absorbent, poly bag + socks + pads','Spill Station','SK20G','Yellow',None,None,None,None,1,'ea',120,3,PE,'Spill Station AU, approx AUD $119, 2025'),
    R(IND,'Safety Equipment','Spill Kit','240L drum kit','240L drum spill kit, chemical resistant, IBC pads','Spill Station','SK240D','Yellow',None,None,None,None,1,'ea',350,3,PE,'Spill Station AU, approx AUD $349, 2025'),
    R(IND,'Safety Equipment','Safety Shower / Eyewash (Combined)','Plumbed','Plumbed safety shower + eyewash station, ANSI','Hughes Safety','W-2000','Yellow/Green',None,None,2140,None,1,'ea',1500,15,PE,'Hughes Safety AU, approx AUD $1499, 2025'),
    R(IND,'Safety Equipment','First Aid Kit (Industrial)','Type C workplace','Type C workplace first aid kit, 25-person','Trafalgar','Type C','Green',None,None,None,None,1,'ea',150,3,PE,'Bunnings, approx AUD $149, 2025'),
    R(IND,'Safety Equipment','First Aid Kit (Industrial)','Large 50-person','Large workplace first aid kit, 50-person','Trafalgar','Type D','Green',None,None,None,None,1,'ea',280,3,PE,'Winc, approx AUD $279, 2025'),

    # ── Measurement & Detection ───────────────────────────────────────────────
    R(IND,'Measurement & Detection','Gas Detector','4-gas portable','4-gas detector, LEL/O2/CO/H2S, LCD, clip-on','Honeywell','BW MicroClip','Yellow',None,None,None,None,1,'ea',900,3,PE,'Honeywell AU, approx AUD $899, 2025'),
    R(IND,'Measurement & Detection','Gas Detector','Fixed detector panel','Fixed gas detection panel, 4-zone, relay outputs','Oldham','OLCT 100','Black',None,None,None,None,1,'ea',2500,8,PE,'Oldham AU, approx AUD $2499, 2025'),
    R(IND,'Measurement & Detection','Multimeter','True RMS digital','True RMS digital multimeter, CATIII 600V','Fluke','117','Yellow/Black',None,None,None,None,1,'ea',350,5,PE,'RS Components AU, approx AUD $349, 2025'),
    R(IND,'Measurement & Detection','Multimeter','Clamp meter','AC/DC clamp meter, 600A, CATIII','Fluke','323','Yellow/Black',None,None,None,None,1,'ea',280,5,PE,'RS Components AU, approx AUD $279, 2025'),
    R(IND,'Measurement & Detection','Laser Level','Cross-line','Cross-line laser level, ±0.3mm/m, self-levelling','Bosch','GLL 3-80','Blue',None,None,None,None,1,'ea',380,5,PE,'Bunnings, approx AUD $379, 2025'),
    R(IND,'Measurement & Detection','Laser Level','Rotary','Rotary laser level, 600m range, self-levelling','Bosch','GRL 300 HV','Blue',None,None,None,None,1,'ea',900,8,PE,'Sydney Tools, approx AUD $899, 2025'),
    R(IND,'Measurement & Detection','Thermal Imaging Camera','Entry-level','Thermal imaging camera, 160×120 IR, -20 to 550°C','FLIR','TG267','Grey',None,None,None,None,1,'ea',1200,5,PE,'RS Components AU, approx AUD $1199, 2025'),
    R(IND,'Measurement & Detection','Thermal Imaging Camera','Professional','Professional thermal camera, 320×240 IR, Wi-Fi','FLIR','E54','Grey',None,None,None,None,1,'ea',4500,5,PE,'RS Components AU, approx AUD $4499, 2025'),
    R(IND,'Measurement & Detection','Noise Meter','Class 2','Class 2 sound level meter, 30-130dB, data logger','Extech','HD600','White',None,None,None,None,1,'ea',650,5,PE,'RS Components AU, approx AUD $649, 2025'),
    R(IND,'Measurement & Detection','Tachometer','Non-contact laser','Non-contact laser tachometer, 10–99999 RPM','Extech','461920','Grey',None,None,None,None,1,'ea',200,5,PE,'RS Components AU, approx AUD $199, 2025'),
]

# =============================================================================
# MEDICAL & FIRST AID
# =============================================================================
MD = 'Medical & First Aid'

medical = [
    # ── First Aid ─────────────────────────────────────────────────────────────
    R(MD,'First Aid','AED (Defibrillator)','Semi-auto','AED, semi-automatic, adult/child pads, wall cabinet','Zoll','AED 3','White/Red',None,None,None,None,1,'ea',2800,8,CONT,'Defibshop AU, approx AUD $2799, 2025'),
    R(MD,'First Aid','AED (Defibrillator)','Fully automatic','AED, fully automatic, real CPR feedback, Wi-Fi','Physio-Control','LIFEPAK CR2','White/Red',None,None,None,None,1,'ea',3200,8,CONT,'Defibshop AU, approx AUD $3199, 2025'),
    R(MD,'First Aid','AED (Defibrillator)','Budget semi-auto','Budget AED, semi-automatic, voice guidance','Heartsine','PAD 350P','White/Blue',None,None,None,None,1,'ea',1600,8,CONT,'Defibshop AU, approx AUD $1599, 2025'),
    R(MD,'First Aid','AED (Defibrillator)','Wall cabinet','AED wall cabinet with alarm, lockable','Generic','AED-CAB','White/Red',None,None,None,None,1,'ea',250,15,CONT,'Defibshop AU, approx AUD $249, 2025'),
    R(MD,'First Aid','First Aid Kit','Type C 25-person','Type C workplace first aid kit, 25-person, blue bag','Trafalgar','Type C 25P','Green',None,None,None,None,1,'ea',120,2,CONT,'Bunnings, approx AUD $119, 2025'),
    R(MD,'First Aid','First Aid Kit','Type D 50-person','Type D workplace first aid kit, 50-person, hard case','Trafalgar','Type D 50P','Green',None,None,None,None,1,'ea',280,2,CONT,'Winc, approx AUD $279, 2025'),
    R(MD,'First Aid','First Aid Kit','Remote/trauma kit','Remote area first aid kit, trauma supplies, 100-person','St John','RAFA 100','Green',None,None,None,None,1,'ea',600,2,CONT,'St John AU, approx AUD $599, 2025'),
    R(MD,'First Aid','Stretcher','Folding','Folding aluminium stretcher, 150kg rated','Ferno','Model 35A','Black',None,None,None,None,1,'ea',950,10,PE,'Ferno AU, approx AUD $949, 2025'),
    R(MD,'First Aid','Stretcher','Stair chair','Stair chair evacuator, foldable, 250kg rated','Ferno','Model 40','Black',None,None,None,None,1,'ea',1800,10,PE,'Ferno AU, approx AUD $1799, 2025'),
    R(MD,'First Aid','Eyewash Station','Wall-mount bottle','Eyewash station, 2×500mL saline, wall-mount','Plum Safety','Emergency Eye Wash','Green/White',None,None,None,None,1,'ea',80,2,CONT,'Blackwoods, approx AUD $79, 2025'),
    R(MD,'First Aid','Eyewash Station','Plumbed station','Plumbed eyewash station, ANSI Z358.1, stainless','Guardian','GW series','Chrome',None,None,None,None,1,'ea',600,15,CONT,'Guardian Equipment AU, approx AUD $599, 2025'),

    # ── Medical Equipment ─────────────────────────────────────────────────────
    R(MD,'Medical Equipment','Examination Table','Standard electric','Electric examination table, height-adjustable, paper roll','Promotal','Equipmed','White',1900,700,850,None,1,'ea',3500,15,PE,'Medshop AU, approx AUD $3499, 2025'),
    R(MD,'Medical Equipment','Examination Table','Manual hydraulic','Manual hydraulic examination table, 3-section','Remfit','Remploy 3S','White',1850,650,830,None,1,'ea',2000,15,PE,'Medshop AU, approx AUD $1999, 2025'),
    R(MD,'Medical Equipment','Examination Table','Chiropractic table','Chiropractic/physio treatment table, drop pieces','Lloyd Table','Zenith 220','Cream',2050,750,600,None,1,'ea',4500,15,PE,'Chiropractic supply AU, approx AUD $4499, 2025'),
    R(MD,'Medical Equipment','Examination Table','Gynaecology table','Gynaecological examination table, electric, stirrups','Promotal','GYN Electric','White',1900,700,850,None,1,'ea',6000,15,PE,'Medshop AU, approx AUD $5999, 2025'),
    R(MD,'Medical Equipment','Blood Pressure Monitor','Digital automatic','Digital automatic BP monitor, validated, adult cuff','Welch Allyn','ProBP 3400','White',None,None,None,None,1,'ea',450,8,CONT,'Medshop AU, approx AUD $449, 2025'),
    R(MD,'Medical Equipment','Blood Pressure Monitor','Ambulatory 24hr','24-hour ambulatory blood pressure monitor, software','Welch Allyn','ABPM 7100','White',None,None,None,None,1,'ea',1800,8,CONT,'Medshop AU, approx AUD $1799, 2025'),
    R(MD,'Medical Equipment','Blood Pressure Monitor','Wrist digital','Wrist digital BP monitor','Omron','HEM-6321T','White',None,None,None,None,1,'ea',120,5,CONT,'Chemist Warehouse AU, approx AUD $119, 2025'),
    R(MD,'Medical Equipment','Medical Trolley','Crash trolley','Medical emergency trolley with drawers, resus supplies','Capsa Healthcare','S20','Grey',None,None,None,None,1,'ea',1800,10,PE,'Medshop AU, approx AUD $1799, 2025'),
    R(MD,'Medical Equipment','Medical Trolley','Procedure trolley','Stainless procedure trolley, 2-shelf, push-handle','Generic','SST-2','Chrome',600,400,900,None,1,'ea',600,10,PE,'Medshop AU, approx AUD $599, 2025'),
    R(MD,'Medical Equipment','Medical Trolley','Dressing trolley','Dressing trolley, stainless steel, 3-tier','Generic','DT3S','Chrome',600,400,950,None,1,'ea',550,10,PE,'Medshop AU, approx AUD $549, 2025'),
    R(MD,'Medical Equipment','Autoclave / Steriliser','17L benchtop','Benchtop autoclave, 17L, class B, dental/medical','W&H','Lisa 17L','White',500,430,250,None,1,'ea',5500,10,PE,'W&H AU, approx AUD $5499, 2025'),
    R(MD,'Medical Equipment','Autoclave / Steriliser','22L','Autoclave steriliser, 22L, class N, stainless chamber','W&H','Lisa 22L','White',600,430,250,None,1,'ea',7000,10,PE,'W&H AU, approx AUD $6999, 2025'),
    R(MD,'Medical Equipment','Dental Chair','Standard electric','Dental treatment chair, electric, programmable positions','A-DEC','500','White',None,None,None,None,1,'ea',18000,15,PE,'A-DEC AU, approx AUD $17990, 2025'),
    R(MD,'Medical Equipment','Height/Weight Scale','Digital LCD','Digital height/weight scale, LCD, 200kg, 200cm','Seca','763','White',None,None,None,None,1,'ea',900,10,CONT,'Seca AU, approx AUD $899, 2025'),
    R(MD,'Medical Equipment','Pulse Oximeter','Fingertip clinical','Fingertip pulse oximeter, SpO2/PR, clinical grade','Nellcor','PM10N','White',None,None,None,None,1,'ea',200,5,CONT,'Medshop AU, approx AUD $199, 2025'),
    R(MD,'Medical Equipment','Refrigerator (Medical)','Vaccine 150L','Vaccine refrigerator, 150L, +2 to +8°C, data logger','Vestfrost','MK 144','White',540,535,875,None,1,'ea',2800,10,PE,'Vestfrost AU, approx AUD $2799, 2025'),
    R(MD,'Medical Equipment','Refrigerator (Medical)','Blood bank 380L','Blood bank refrigerator, 380L, ±0.5°C, alarm','Helmer','iB380','White',580,650,1950,None,1,'ea',8000,10,PE,'Helmer Scientific AU, approx AUD $7999, 2025'),
    R(MD,'Medical Equipment','Nebuliser','Compressor','Compressor nebuliser, for aerosol drug delivery','PARI','Compact','White',None,None,None,None,1,'ea',180,5,CONT,'Chemist Warehouse AU, approx AUD $179, 2025'),
    R(MD,'Medical Equipment','Wheelchair','Standard manual','Standard manual wheelchair, 46cm seat, folding','Drive Medical','Cruiser III','Silver',None,None,None,None,1,'ea',350,7,CONT,'Medshop AU, approx AUD $349, 2025'),
    R(MD,'Medical Equipment','Wheelchair','Bariatric','Bariatric manual wheelchair, 60cm seat, 250kg','Invacare','XLT','Black',None,None,None,None,1,'ea',1200,7,CONT,'Medshop AU, approx AUD $1199, 2025'),
    R(MD,'Medical Equipment','IV Stand','Adjustable','IV pole / drip stand, 5-leg base, adjustable height','Generic','IVS-5','Chrome',None,None,None,None,1,'ea',150,7,CONT,'Medshop AU, approx AUD $149, 2025'),
]

# =============================================================================
# SAFES & STORAGE
# =============================================================================
SS = 'Safes & Storage'

safes = [
    R(SS,'Safes','Cash / Petty Cash Safe','20L digital','Cash safe, 20L, digital keypad, 4mm steel body','Guardall','GD20','Grey',250,300,230,None,1,'ea',350,15,CONT,'Buy A Safe AU, approx AUD $349, 2025'),
    R(SS,'Safes','Cash / Petty Cash Safe','45L digital','Cash safe, 45L, dual lock (key+digital)','Guardall','GD45','Grey',300,400,320,None,1,'ea',550,15,CONT,'Buy A Safe AU, approx AUD $549, 2025'),
    R(SS,'Safes','Cash / Petty Cash Safe','Under-counter','Under-counter cash safe, 15L, anchor bolts','Chubb','Elements C15','Grey',280,350,200,None,1,'ea',400,15,CONT,'Buy A Safe AU, approx AUD $399, 2025'),
    R(SS,'Safes','Cash / Petty Cash Safe','Heavy duty 60L','Heavy-duty cash safe, 60L, digital, re-locker','Chubb','DPC 60','Grey',380,500,400,None,1,'ea',900,15,CONT,'Buy A Safe AU, approx AUD $899, 2025'),
    R(SS,'Safes','Deposit Safe','Front-load drop','Front-loading deposit safe, 40L, anti-fish baffle','Guardall','GDD40','Grey',280,380,620,None,1,'ea',700,15,CONT,'Buy A Safe AU, approx AUD $699, 2025'),
    R(SS,'Safes','Deposit Safe','Large deposit','Large deposit safe, 100L, dual custody digital','Chubb','Elements D100','Grey',380,500,800,None,1,'ea',1500,15,CONT,'Buy A Safe AU, approx AUD $1499, 2025'),
    R(SS,'Safes','Fire Safe','B-rated document','Document fire safe, B-rated, 30min/260°C, 50L','Chubb','Elements Fire 50L','Grey',360,450,360,None,1,'ea',750,15,CONT,'Buy A Safe AU, approx AUD $749, 2025'),
    R(SS,'Safes','Fire Safe','1hr 90L','1-hour fire safe, 90L, data media protection','Chubb','Elements Fire 90L','Grey',460,550,440,None,1,'ea',1200,15,CONT,'Buy A Safe AU, approx AUD $1199, 2025'),
    R(SS,'Safes','Fire Safe','2hr large','2-hour fire/burglary safe, 200L, high security','Gardall','2HR-2020','Grey',600,640,720,None,1,'ea',3000,20,CONT,'Buy A Safe AU, approx AUD $2999, 2025'),
    R(SS,'Safes','Drug / Narcotic Safe','S2 rating','Drug / narcotic safe, S2 rating, dual key','Chubb','Narcotic Safe S2','White',250,300,300,None,1,'ea',1200,15,CONT,'Precision Safes AU, approx AUD $1199, 2025'),
    R(SS,'Safes','Drug / Narcotic Safe','S4 high security','High-security narcotics safe, S4 graded, dual control','Gunnebo','Lotus S4','Grey',300,380,350,None,1,'ea',2500,15,CONT,'Precision Safes AU, approx AUD $2499, 2025'),
    R(SS,'Safes','Floor Safe','Concealed in-floor','In-floor concealed safe, 12L, anti-drill plate','Chubb','Floor Safe FS12','Grey',280,280,120,None,1,'ea',1000,15,CONT,'Buy A Safe AU, approx AUD $999, 2025'),
    R(SS,'Safes','Wall Safe','Concealed','Concealed wall safe, 10L, key lock, fitted to stud wall','Guardall','WS10','Grey',300,200,200,None,1,'ea',350,15,CONT,'Buy A Safe AU, approx AUD $349, 2025'),
    R(SS,'Safes','Gun / Firearm Safe','6-gun long arm','Long arm safe, 6-gun, key lock, foam lined','Guardall','GLS6','Black',200,250,1400,None,1,'ea',650,20,CONT,'Buy A Safe AU, approx AUD $649, 2025'),
    R(SS,'Safes','Gun / Firearm Safe','12-gun heavy duty','Heavy-duty firearm safe, 12 rifles, 3mm steel, digital','Hornady','Rapid Safe 12G','Black',300,450,1500,None,1,'ea',1800,20,CONT,'Buy A Safe AU, approx AUD $1799, 2025'),
    R(SS,'Safes','Laptop / IT Security Safe','Laptop charging','Laptop safe, 10-unit charging, 3mm steel, digital lock','Datamation','DS-LKN-10','Black',500,600,500,None,1,'ea',800,10,CONT,'Winc, approx AUD $799, 2025'),
    R(SS,'Safes','Key Cabinet Safe','20-hook','Key cabinet, 20-hook, key lock, wall-mount','Kaba Mas','Key 20','Grey',150,80,250,None,1,'ea',200,15,CONT,'Winc, approx AUD $199, 2025'),
    R(SS,'Safes','Key Cabinet Safe','50-hook digital','Key cabinet, 50-hook, digital lock, audit log','Kaba Mas','Key 50D','Grey',250,80,350,None,1,'ea',600,15,CONT,'Winc, approx AUD $599, 2025'),
    R(SS,'Safes','Key Cabinet Safe','100-hook managed','Key management cabinet, 100-hook, electronic, biometric','Traka','Traka21','White',300,100,540,None,1,'ea',2500,10,CONT,'Traka AU, approx AUD $2499, 2025'),
]

# =============================================================================
# OFFICE EQUIPMENT
# =============================================================================
OE = 'Office Equipment'

office_equipment = [
    # ── Mail & Document ───────────────────────────────────────────────────────
    R(OE,'Mail & Document','Shredder','Cross-cut P-4','Cross-cut paper shredder, P-4 security, 10 sheets, 23L bin','Fellowes','Powershred 79Ci','Black',225,380,430,None,1,'ea',280,5,CONT,'Officeworks, approx AUD $279, 2025'),
    R(OE,'Mail & Document','Shredder','Micro-cut P-5','Micro-cut shredder, P-5 security, 8 sheets, 23L','Fellowes','Powershred 99Ci','Black',225,380,430,None,1,'ea',420,5,CONT,'Officeworks, approx AUD $419, 2025'),
    R(OE,'Mail & Document','Shredder','Micro-cut P-6','High-security micro-cut shredder, P-6, 6 sheets','Dahle','410','Black',230,390,450,None,1,'ea',600,5,CONT,'Winc, approx AUD $599, 2025'),
    R(OE,'Mail & Document','Shredder','Industrial large bin','Industrial shredder, P-4, 40L bin, 20 sheets','Dahle','504','Black',360,490,700,None,1,'ea',900,5,CONT,'Winc, approx AUD $899, 2025'),
    R(OE,'Mail & Document','Laminator','A4','A4 laminator, hot/cold, 80–250 micron','Fellowes','Saturn3i A4','Black',385,80,58,None,1,'ea',120,5,CONT,'Officeworks, approx AUD $119, 2025'),
    R(OE,'Mail & Document','Laminator','A3','A3 laminator, hot/cold, up to 250 micron','Fellowes','Saturn3i A3','Black',520,100,70,None,1,'ea',200,5,CONT,'Officeworks, approx AUD $199, 2025'),
    R(OE,'Mail & Document','Laminator','Professional A3','Professional A3 laminator, 125 micron, carrier sheets','Fellowes','Helix A3','Black',550,120,80,None,1,'ea',380,5,CONT,'Winc, approx AUD $379, 2025'),
    R(OE,'Mail & Document','Franking Machine','Low volume','Franking machine, low volume, 2-year contract','Pitney Bowes','SendPro C','Grey',None,None,None,None,1,'ea',1800,5,CONT,'Pitney Bowes AU, approx AUD $1799, 2025'),
    R(OE,'Mail & Document','Franking Machine','Mid volume','Franking machine, mid volume, colour touchscreen','FP Mailing','Optimail 30','Grey',None,None,None,None,1,'ea',3000,5,CONT,'FP Mailing AU, approx AUD $2999, 2025'),
    R(OE,'Mail & Document','Folding Machine','Desktop','Desktop paper folding machine, C/Z/V fold, 2000 sheets/hr','Formax','FD 314','Grey',None,None,None,None,1,'ea',900,8,CONT,'Winc, approx AUD $899, 2025'),
    R(OE,'Mail & Document','Label Printer','Desktop thermal','Desktop thermal label printer, 203dpi, USB/Bluetooth','Brother','QL-820NWB','Black',175,130,80,None,1,'ea',220,4,CONT,'Officeworks, approx AUD $219, 2025'),
    R(OE,'Mail & Document','Label Printer','Industrial thermal','Industrial thermal label printer, 300dpi, network','Zebra','ZT411','Grey',None,None,None,None,1,'ea',1500,5,CONT,'Zebra AU, approx AUD $1499, 2025'),

    # ── Presentation ──────────────────────────────────────────────────────────
    R(OE,'Presentation','Flip Chart Easel','A1 adjustable','A1 flip chart easel, aluminium, adjustable height','Visionchart','JD7 Adjustable','Silver',None,None,1800,None,1,'ea',250,8,CONT,'Officeworks, approx AUD $249, 2025'),
    R(OE,'Presentation','Flip Chart Easel','A1 magnetic','A1 magnetic flipchart easel with castors','Visionchart','JD12','Silver',None,None,1800,None,1,'ea',450,8,CONT,'Officeworks, approx AUD $449, 2025'),
    R(OE,'Presentation','Lectern / Podium','Timber veneer','Timber veneer lectern with mic shelf and cable management','Generic','Podium T','Walnut Veneer',600,500,1150,None,1,'ea',800,15,CONT,'Epic Office Furniture, approx AUD $799, 2025'),
    R(OE,'Presentation','Lectern / Podium','Acrylic clear','Clear acrylic podium / lectern, modern design','Generic','Acrylic Podium','Clear',450,400,1100,None,1,'ea',600,15,CONT,'AV distributor AU, approx AUD $599, 2025'),
    R(OE,'Presentation','Projection Trolley','AV cart','AV projection cart, height adjustable, 2-shelf','Balt','Balt AV Cart','Black',600,500,1200,None,1,'ea',350,8,CONT,'AV distributor AU, approx AUD $349, 2025'),

    # ── Security / Payments ───────────────────────────────────────────────────
    R(OE,'Security','EFTPOS / Payment Terminal','Countertop','Countertop EFTPOS terminal, contactless, PIN','Ingenico','Desk/5000','Black',None,None,None,None,1,'ea',450,4,CONT,'Tyro / ANZ lease equiv, approx AUD $449, 2025'),
    R(OE,'Security','EFTPOS / Payment Terminal','Mobile','Mobile EFTPOS terminal, 4G, rechargeable','Ingenico','Move/5000','White',None,None,None,None,1,'ea',650,4,CONT,'Tyro, approx AUD $649, 2025'),
    R(OE,'Security','EFTPOS / Payment Terminal','Integrated POS','Integrated POS terminal, touch display, barcode scanner','Verifone','T650p','Black',None,None,None,None,1,'ea',1200,4,CONT,'Verifone AU, approx AUD $1199, 2025'),
    R(OE,'Security','ID Card Printer','Entry-level','Direct-to-card ID printer, single-side, USB','HID Fargo','DTC1250e','White',None,None,None,None,1,'ea',800,5,CONT,'HID Global AU, approx AUD $799, 2025'),
    R(OE,'Security','ID Card Printer','Dual-side','Dual-sided ID card printer with lamination','HID Fargo','HDP5000','Grey',None,None,None,None,1,'ea',2500,5,CONT,'HID Global AU, approx AUD $2499, 2025'),
    R(OE,'Security','Cash Register','POS touchscreen','POS touch-screen cash register, receipt printer, cash drawer','Casio','V-R7100','Black',None,None,None,None,1,'ea',1500,5,CONT,'Winc, approx AUD $1499, 2025'),
]

# =============================================================================
# Combine Part 2 + append to CSV
# =============================================================================
part2 = fitness + vehicles + industrial + medical + safes + office_equipment

out = Path('Asset_Library_AU.csv')

# Count rows already in file to get starting UID
with open(out, 'r', encoding='utf-8') as f:
    existing = sum(1 for _ in f) - 1   # subtract header row

start_uid = 200001 + existing

with open(out, 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    for i, rec in enumerate(part2):
        rec[0] = start_uid + i
        w.writerow(rec)

total = existing + len(part2)
print(f"Part 2 appended: {len(part2)} records")
print(f"  Fitness & Recreation:       {len(fitness)}")
print(f"  Vehicles & Motorised Plant: {len(vehicles)}")
print(f"  Industrial:                 {len(industrial)}")
print(f"  Medical & First Aid:        {len(medical)}")
print(f"  Safes & Storage:            {len(safes)}")
print(f"  Office Equipment:           {len(office_equipment)}")
print(f"\nTotal records in file: {total}")
print(f"UID range: 200001 – {200001 + total - 1}")
