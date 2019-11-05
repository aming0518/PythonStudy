mystr="张三 李四 王五"
print(mystr.find("张三"))#find返回第一个，从头部开始
print(mystr.rfind("张三"))#rfind返回第一个，从尾部开始


#找到了返回元素位置，未找到返回-1

print(mystr.find("张三",3,6))#第一个参数是要查找的字符串，第二个起始，第三个结束



print(mystr.index("张三"))#判断字符串是否存在，存在则返回下标，否则返回-1
print(mystr.rindex("张三"))#rindex查找，返回最后一个下标