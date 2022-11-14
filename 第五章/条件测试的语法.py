"""
字符串和数字比较运算符
== 等于  != 不等于
>  大于  <  小于
>= 大于等于 <= 小于等于
"""
"""
成员运算符
date = [2, 3, 4, 6]
3 in data
3 not in data 
"""

"""
逻辑运算符
and 并且
or 或
not 非

也可以加括号区分
（a==b） and （c==d）
"""
"""
字符串的等于、不等于判断
value = "apple"
print(value = "pear")
print(value = "apple")

输出结果
False
True
"""

"""
一个元素、一个列表、可以判断元素在列表中、不在列表中的判断
numbers = [3, 4, 6, 8]
print("3 in numbers :", 3 in numbers)
print("5 in numbers :", 5 in numbers)

输出结果
TRUE
FALSE
"""

"""
and 和 or 可以混合使用，and的优先级更高（先执行and再执行or）；如果需要改变优先级
需要加括号。
a==3 and “pear” not in fruits or value = ”ok“先执行and再执行or
a==3 and (”pear“ not in fruits or value = "ok)先执行or再执行and
"

"""