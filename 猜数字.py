import random
startnum=random.randint(1,10)
num=eval(input("请输入一个数字"))
while  num!=startnum:
    if num>startnum:
        print("big")
    else:
        print("small")
        num=eval(input("再次输入"))
else:
    print("right")
