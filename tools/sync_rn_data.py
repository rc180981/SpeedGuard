with open('d:/FAJAR Apps/speed-violation-app/initial_data_126.js', 'r', encoding='utf-8') as f:
    js_initial = f.read()

# Replace "const INITIAL =" with "export const INITIAL_DATA ="
rn_data = js_initial.replace("const INITIAL =", "export const INITIAL_DATA =")

full_file = f"""// ===================================================================
// DATA.js  –  Initial seed data + type definitions (126 records)
// ===================================================================

export const SPEED_LIMIT = 20; // KM/JAM

/** @typedef {{{{ id:number, date:string, name:string, area:string, speed:number,
 *              dept:string, nik:string, plat:string, vehicle:string,
 *              status:'Baru'|'Proses'|'Selesai', remark:string }}}} Violation */

{rn_data}

export const AREA_OPTIONS = [
  'Area sisi selatan wh3',
  'Area sisi selatan wh4',
  'Area sisi utara wh3',
  'Area sisi utara wh4',
  'Area pintu masuk',
  'Area parkir',
  'Lainnya',
];

export const VEHICLE_OPTIONS = ['MOTOR', 'MOBIL', 'TRUCK', 'FORKLIFT', 'SEPEDA', 'Lainnya'];
export const STATUS_OPTIONS  = ['Baru', 'Proses', 'Selesai'];
"""

with open('d:/FAJAR Apps/SpeedGuardApp/src/data/data.js', 'w', encoding='utf-8') as f:
    f.write(full_file)

print('Updated SpeedGuardApp/src/data/data.js with 126 records!')
