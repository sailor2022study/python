def itrotude(name,gender):
    print(f"大家好，我的名字是：{name}，是一个小{gender}")

#可以用形参名= 值的方式提供实参
itrotude(name = "小明",gender = "男生")
#也可以位置参数与关键参数进行搭配
itrotude("小红",gender = "女生")