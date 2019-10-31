mylist =[1,2,3,4,5,6,7]#列表，容纳多个数据
print(len(mylist))
mylist.append(8)#增加数据
print(len(mylist))
for data in mylist:#循环遍历列表
    print("------",data)
print(mylist)
print(mylist[1:3])#不包含第三个元素
print(mylist+mylist[4:6])#字符串的加法