mystr="hello python2 python3"
print(mystr.capitalize())#第一个字符大写
print(mystr)

#打印金字塔1
mystr1="8888"
for i in range(6,40,2):
    for j in range((40-i)//2,0,-1):
        print(" ",end="")

    print(mystr1.center(i,'*'))


'''
center(width,fillchar)
返回一个指定的宽度 width居中的字符串，fillchar为填充的字符 默认为空格
'''



mystr2="hello python2 hello python3"
print(mystr2.count('python'))#判断字符串出现的次数
print(mystr2.count('python',10))#从第十个字符开始判断
print(mystr2.count('python',10,15))#从第十个到第十五个