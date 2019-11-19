mylist=dir("")#dir返回的是一个列表
print(type(""))
print(mylist)#包含所有的函数 属性
for i in mylist:#遍历打印
    print(i)
    print(help("str."+i))#打印函数说明
