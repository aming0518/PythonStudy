#for i in range(1,100):
    #print(i)

#for i in range(100):#运行100次 从0到99
   # print(i)
#for i in range(0,100,2):#每次间隔为2 但是不包含100
   # print(i)

import time
starttime=time.time()
lastnum=0
num=0
while num<10000000:
    num+=1
    lastnum+=num
print(lastnum)
endtime=time.time()
print(endtime-starttime)
