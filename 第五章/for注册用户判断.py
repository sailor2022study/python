curr_users = ["小明", "小李", "小白", "小黑"]
new_users = ["小陈", "小李", "小白", "小亮"]
for new_user in new_users:
    if new_user in curr_users:
        print("这个用户名已经被注册过了：", new_user)
    else:
        print("这个用户名没有被注册过：", new_user)