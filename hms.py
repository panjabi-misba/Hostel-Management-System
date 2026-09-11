# Hostel Management System - Version 1.1
# Features: allot and vacate rooms, fine calculation

def allot_room(room_id, student_id):
    print("Room", room_id, "allotted to student", student_id)

def vacate_room(room_id):
    print("Room", room_id, "vacated")

def calculate_fine(days_late, rate=50):
    fine = days_late * rate
    print("Fine = Rs.", fine)
    return fine
