for i in range(10):
    for j in range(10):
        print(j, end=" ")
        if j == 5:
            break  # 跳出J这个循环
    if i == 5:
        break  # 跳出I这个循环
        print("")

for i in range(10):
    for j in range(10):
        if j == 5:
            continue # 筛选5
        print(j, end=" ")

        print("")


