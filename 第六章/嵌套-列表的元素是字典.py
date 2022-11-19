students = [
    {"id": 101, "name": "xiaoming", "grade": 88},
    {"id": 102, "name": "xiaochen", "grade": 78},
    {"id": 103, "name": "xiaohong", "grade": 68},
    {"id": 104, "name": "xiaobai", "grade": 89},
]

for student in students:
    id, name, grade = student["id"], student["name"], student["grade"]
    print(f"学号为{id}的姓名为{name}，成绩是{grade}分")
    