mydict={"abcdefg":1,"10010":2}
print(type(mydict))#dict是set的强化版，左边是key，不允许重复，右边value可以重复
print(mydict)
for key in mydict:
    print(key,mydict[key])#循环字典