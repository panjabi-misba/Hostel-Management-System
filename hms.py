# Hostel Management System - Version 2.0
# Features: allot/vacate rooms, fine calculation, online room search

rooms = ["Room 101", "Room 102", "Room 103"]

def allot_room(room_id, student_id):
    print("Room", room_id, "allotted to student", student_id)

def vacate_room(room_id):
    print("Room", room_id, "vacated")

def calculate_fine(days_late, rate=50):
    fine = days_late * rate
    print("Fine = Rs.", fine)
    return fine

def search_room(room_id):
    if room_id in rooms:
        print(room_id, "is available")
    else:
        print(room_id, "not found")
