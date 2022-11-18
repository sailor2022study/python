#创建一个人的信息
uesr = {"d":123, "name": "xiaoming", "age": 20}

#遍历键值对
for key, value in uesr.items():
    print(key, value)

print(uesr.items())
print(list(uesr.items()))