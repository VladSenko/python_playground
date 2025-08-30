students = [
    {"name": "John", "grade": 1},
    {"name": "Tedd", "grade": 2},
    {"name": "Samantha", "grade": 3},
    {"name": "Alice", "grade": 4}
]


def get_av_grade():
    total_grade = 0

    for student in students:
        if "grade" in student:
            total_grade += student["grade"]

    return total_grade/len(students)


print(get_av_grade())
