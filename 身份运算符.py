num1=3
num2=3
print(id(num1),id(num2))
if num1   is  num2:
    print("同一个地址 ")

num1=4
if  num1 is  num2:
        print("同地址")
else:
        print("不同地址")


#is is not   判断地址是否相同