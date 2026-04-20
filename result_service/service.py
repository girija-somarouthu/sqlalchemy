from marks_service.service import get_marks

def get_result(student_id):
    marks = get_marks(student_id)

    total = sum(m["marks"] for m in marks)
    avg = total / len(marks)

    if avg >= 50:
        return {"average": avg, "result": "Pass"}
    else:
        return {"average": avg, "result": "Fail"}