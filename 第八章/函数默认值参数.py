
def introtude(name,gender,age=6):
    print(f"大家好，我的名字是：{name}，是一个{gender}，今年{age}岁了")

#调用函数时，默认参数可以不写

#如果不设置age，那么就是6岁
introtude("小明",gender = "男生")
introtude(name ="小红",gender = "男生",)
introtude(name ="小红",gender = "男生",age=8)