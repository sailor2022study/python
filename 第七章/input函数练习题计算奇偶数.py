"""
求余数函数练习题：
1.使用input，提示让用户输入一个数字；
2.将输入变成数字类型；
3.计算是奇数还是偶数，给用户展示结果；

"""
number = input("请输入一个数字：")
number = int(number)
if number % 2 == 0:
    print(f"你输入的是{number},它是一个偶数")
else:
    print(f"你输入的是{number},它是一个奇数")
