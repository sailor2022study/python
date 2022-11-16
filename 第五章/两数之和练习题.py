numbers = [2, 3, 5, 8, 7, 4, 1, 6]
for a in numbers:
    for b in numbers:
        if a + b == 8:
            print(a, b)



result = []
numbers = [2, 3, 5, 8, 7, 4, 1, 6]
target = 8
for a in numbers:
    for b in numbers:
        if a + b == target and (a, b) not in result:
            print(f"我们已经找了一对：{a} + {b} == {target}")
            result.append((a,b))
            result.append((b,a))