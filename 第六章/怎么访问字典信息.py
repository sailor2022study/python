#创建一个的信息字典
user = {"id": 123, "name": "小明", "age": 18}

print(user["id"])
print(user["age"])
print(user["name"])

#如下如果写user["grade"] 会报错keyerror：”grade“

#写get就不会报错，也可以指定默认值
print(user.get("grade"))
print(user.get("grade", 80))