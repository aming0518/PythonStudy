

num=lambda a,b:a+b
          #参数a,b 返回值a+b

print(num(1,2))

num3=lambda a,b,c:a*b*c
print(num3(1,2,3))


print((lambda a,b:a+b)(100,200))#匿名函数


#python下最强的hello
(lambda mystr:print(mystr))("hello")