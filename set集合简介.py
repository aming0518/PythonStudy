mylist=[1,1,1]
myset={1,1,1}#元素不可重合
print(mylist)
print(myset)

set1={1,2,3,4}
set2={1,2,7,8}
print(set1-set2)#set1有set2没有的  差集
print(set1|set2)#set1和set2的并集
print(set1&set2)#set1和set2的交集
print(set1^set2)#set1和set2的并集减去交集