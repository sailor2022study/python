numbers = list(range(10))
print(numbers)
print("2:5",numbers[2:5])
#从2的位置开始，到位置5结束，不包含位置5
print(":6", numbers[:6])
#从0开始，到5结束，不包括6
print("3:", numbers[3:])
#从3开始，到结束,不包括第三个元素
print(":",numbers[:])
#包含所以元素
print("3:9:2",numbers[3:9:2])