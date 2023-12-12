import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://accuface-logix-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "72112032":
        {
            "name": "Gunti Jagadeesh",
            "major": "Btech CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-14 00:54:34"
        },
    "72112237":
        {
            "name": "Siva Sankar",
            "major": "Btech CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-10-14 00:54:34"
        },
    "72112266":
        {
            "name": "Ramu",
            "major": "Btech CSE",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-14 00:54:34"
        },
    "72211875":
        {
            "name": "Lakshmi Reddy",
            "major": "Btech CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-14 00:54:34"
        },
   "72211953":
        {
            "name": "Vamsi",
            "major": "Btech CSE",
            "starting_year": 2022,
            "total_attendance":0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-14 00:54:34"
        },
   "72314756":
        {
            "name": "Bharath",
            "major": "Btech CSE",
            "starting_year": 2023,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-14 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)