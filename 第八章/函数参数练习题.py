def computer(x,y,method = "add"):
    if method == "add":
        print(x+y)
    #下面的if可以换成elif
    if method == "sub":
        print(x-y)
    if method == "mul":
        print(x*y)
    if method == "div":
        print(x/y)

computer(4,4,method="div")
computer(4,4,"div")
computer(4,y=4,method = "sub")
computer(y=4,x=4)
computer(method="mul",x=5,y=6)