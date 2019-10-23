import os
cmd=input("cmd")
while(cmd!="退出"):
    if cmd=="记事本":
        os.system("notepad")
    elif  cmd=="计算器":
        os.system("calc")
    cmd=input("cmd")