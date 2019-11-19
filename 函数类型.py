import random

def go():#没有参数 没有 返回值
    print("hello world")

go()#()调用函数


def goprint(num):#有参数，无返回值
    print("hello",num)
goprint(6)

def getdata():#没有参数  有返回值
    return random.randint(0,100)#返回一个随机数

print(getdata())

def add(num1,num2):#有输入有输出
    return num1+num2
num=add(2,2)
print(num)  