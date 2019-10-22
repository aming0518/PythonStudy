def Test():
    def TestX():
        print("hello world")
    TestX()

Test()



def text():
    num=10
    def  txetin():
        nonlocal num#引用外层变量
        num=100     #没有nonlocal，内层覆盖外层，新建一个变量
        print(num)
    txetin()
    print(num)
text()