print("-".join("abcdefg"))#字符串每个元素之间插入一个字符串间隔
print("-".join("abcd efg"))#空格算一个字符

for i in range(1,50):
    print("8888".rjust(i,'*'))#i长度，左边填充*
    #print("8888".ljust(i,'*'))