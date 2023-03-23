def introduce(name,gender):
    """
    幼儿园的自我介绍
    :param name:
    :param gender:
    :return:
    """
    print(f"大家好，我的名字是：{name},是个小{gender}")

#位置实参需要按顺序提供
introduce("小明","男生")
introduce("小明","女生")