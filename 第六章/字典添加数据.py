# 创建多个人信息的字典
grades = {"小明": 88, "小花": 99, "小白": 78, "小李": 77}
print(grades)


#如下两个，因为key不存在，会新镇键值对
grades["小红"] = 90
grades["小张"] = 92
#如下一个，因为小白之前存在键，所以值会被修改
grades["小白"] = 77

print(grades)