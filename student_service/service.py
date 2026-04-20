students = []

def add_student(student_id, name):
    students.append({
        "student_id": student_id,
        "name": name
    })
    return {"message": "Student added successfully"}