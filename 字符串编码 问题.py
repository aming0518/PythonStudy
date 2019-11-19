

#utf-8一个汉字两个字节
a=bytes("你好abc","utf-8")
print(a)
a=bytes("你好中国abc","gbk")
print(a)
#不同编码大小不一样 内容不一样


print(b'\xe4\xbd\xa0\xe5\xa5\xbdabc'.decode("utf-8"))#解码，不同类型不可转换

#encode  和   decode
print(type("hello".encode("utf-8")))#字符串转换为二进制编码
print(type(b'\xe4\xbd\xa0\xe5\xa5\xbdabc'.decode("utf-8")))#二进制编码转化为字符串



mystr="hello python"
mystr1="hello 中国"
print(mystr.encode("utf-8"))
print(mystr1.encode("utf-8"))
print(b'hello python'.decode("utf-8"))
print(b'hello \xe4\xbd\xa0\xe5\xa5\xbd'.decode("utf-8"))
print(b'hello python'.decode("gbk"))


#英文的东西，任何编码无所谓，GBK，UTF-8对于英文编码
#汉字注意编码的格式，不同的编码结果不一样，同样的二进制，换一种编码一般解析出错



print(b'hello \xe4\xbd\xa0\xe5\xa5\xbd'.decode("gbk","ignore"))
#ignore 强行解码  会导致乱码