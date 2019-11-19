mydata=1,2,3,4,5,6
print(type(mydata))
#mydata=()#元组为空
print(type(mydata))
#mydata[1]=10#不可以修改
print(mydata[1])
for i in range(len(mydata)):
    print(mydata[i],id(mydata[i]))