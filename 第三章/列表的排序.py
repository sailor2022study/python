grades=[77,99,84,67,85]
print(grades)

grades.sort()
print(grades)

grades.sort(reverse=True)
print(grades)
#注意，这里直接修改了列表本身。

#sorted(list)是一个新函数，它不会改变列表本身，会返回一个新的排序后的列表。
grades=[77,99,84,67,85]
print(grades)

new_graces=sorted(grades)
print(grades,new_graces)

new_graces=sorted(grades,reverse=True)
print(grades,new_graces)

a=grades
print(a)