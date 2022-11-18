# 字典dict是一种表达”键值对“的数据结构，可以根据”键key“设置和获取对应的”值value“
# 语法  dict = {key1：value, key2:value}
# 注意大括号  举例 user = {"id": 123, "name": "xiaoming", age: 20}

# 创建一个空字典
data = {}

# 创建一个人的信息字典
user = {"id": 123, "name": "小明", "age": 20}

# 创建多个人的信息字典
users = {
    "小明": "男",
    "小花": "女",
    "小白": "女",
    "小刚": "男",
}

print(data, type(data))
print(user, type(user))
print(users, type(users))
