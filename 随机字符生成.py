import time

timesdata=time.time()
print(timesdata)
timesdata=int(timesdata)
timesdata=timesdata%26  #数字限定在0-26之间
print(timesdata)


print(chr(ord('A')+timesdata)) #基数+变数生成随机字符
print(ord('Z'))