#pass  #空语句  什么都不执行

import os
cmd=input("输入指令")
if  cmd=="关机":
    os.system("shutdown -s -t  200")
else:
    pass #占坑作用
print("game over")