import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Ali Al-kelabi",
            "major": "Mechatronics",
            "starting_year": 2018,
            "total_attendance": 14,
            "standing": "N",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Abdullah",
            "major": "Mechatronics",
            "starting_year": 2017,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Omar",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 13,
            "standing": "VG",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)