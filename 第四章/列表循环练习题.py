grades = [77, 88, 73, 99, 82, 89, 95, 86, 93]
grades.sort(reverse=True)
print(grades)
print("最高分：", max(grades))
print("最低分：", min(grades))
print("平均分：", sum(grades)/len(grades))
print(":3",grades[:3])
grades.sort()
print(grades)
print("7:",grades[7:])

#for的玩意tm地会进行横向排序
print("前三名：")
for grade in grades[:3]:
    print(grade)