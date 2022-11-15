#最简单的判断
grade = 70
if grade >= 60:
    print("你的成绩及格了")

#if 配合else 表达如果、否则的含义
grade = 70
if grade>= 60:
    print("恭喜，你的成绩及格了")
else:
    print("很遗憾，你没通过考试")

#if配合多个elif和else，表达很多个条件
grade = 70
if grade < 60:
    print("不及格")
elif grade < 80:
    print("良好")
elif grade < 90:
    print("中等")
else:
    print("优秀")
#注意，如果if...elif...else的写法，只有一个条件会被执行
#模拟已注册列表
users = ["xiaoming", "xiaobai", "xiaogan"]

#正确相当于多个测试，独立测试
new_user = "xiaog"
if len(new_user) < 6:
    print("长度不足6位，不通过")
if new_user in users:
    print("名字已经被注册，不通过")

#错误：如果第一个条件满足，后面测试则不会执行
new_user = "xiaobai"
if len(new_user) < 6:
    print("长度不足6位，不通过")
elif new_user in users:
    print("名字已经被注册，不通过")