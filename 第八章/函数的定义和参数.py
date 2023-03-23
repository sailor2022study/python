def print_hello():
    """
    这是一个函数的定义
    用于打印一段文字
    :return:
    """
    print("hello world")
    print("hello 廖玉婷")

#这里调用一个函数，注意不要忘了括号
print_hello()
print_hello()

#函数的参数
def introduce(name):
    """
    幼儿园的自我介绍    :param name:
    :return:
    """
    print(f"大家好，我的名字是：{name}")

#调用函数的时候，可以传递不同的参数，多次调用
introduce("小明")
introduce("小红")