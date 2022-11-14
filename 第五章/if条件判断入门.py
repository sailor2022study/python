#学生成绩
grades = [66, 55, 75, 80 ,54]

for grade in grades:
    print("**,你的成绩是：", grade)
    if grade >= 60:
        print("恭喜你，通过了考试")
        print("请继续保持")
    else:
        print("很遗憾，你的成绩不及格")
        print("请继续努力")



grade = 70
print(grade in  grades)
print(grade >= 60)
"""
if开头，后面是一个“条件测试"，后面是冒号，类似for语句
下面可以通过缩进放多行代码，被if控制
else是"否则"的意思，如果if不通过，执行else的代码

if条件：执行A else：执行B
如果测试通过则执行A，否则执行B

grade in grade 和grade>=60
这个语句叫条件测试表达式
返回ture或false，表达真假

"""