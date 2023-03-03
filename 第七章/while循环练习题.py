"""
简单的快递运费计算程序
小于1kg 7元
大于1kg 小于3kg
7＋2x
大于3kg
7＋3x
"""
while True:
    weight = input("请输入物品的重量，输入quit则退出：")
    weight = float(weight)

    if weight == "quit":
        break
    else:
        if weight <= 0:
            print("输入错误，请重新输入")
            continue
        if weight <= 1:
            print("金额是：7元")
        elif weight > 1 and weight < 3:
            print("金额是：",(7+2*weight))
        elif weight >= 3:
            print("金额是：",(7+3*weight))




