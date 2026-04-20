marks_data = []

def add_marks(student_id, subject, marks):
    marks_data.append({
        "student_id": student_id,
        "subject": subject,
        "marks": marks
    })
    return {"message": "Marks added successfully"}

def get_marks(student_id):
    result = [m for m in marks_data if m["student_id"] == student_id]
    if not result:
        raise Exception("Marks not found")
    return result