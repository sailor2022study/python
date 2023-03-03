import random

target = random.randint(1,100)
#print("target",target)

count = 1
success = False
while count <= 10:
    print("#" * 20)
    number = input("请输入一个数字:")
    number = int(number)

    if number ==target:
        print("恭喜你猜对了，数字是",target)
        success = True
        break
    elif number < target:
        print("你猜的小了")
    else:
        print("你猜的大了")

    count += 1

if not success:
    print("很遗憾，你没有猜对，正确的数字是：",target)
