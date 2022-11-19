students = {
"xiaoming":{"id":1, "grade": 88},
    "xiaobai":{"id":2, "grade": 86},
    "xiaoli":{"id":3, "grade": 99},
    "xiaoyan":{"id":4, "grade": 100},
}

for name, info in students.items():
    id, grade = info["id"],info["grade"]
    print(f"姓名为{id},学号为{id}，成绩为{grade}")