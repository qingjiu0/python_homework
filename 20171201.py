var1 = 'Hello World!'
var2 = "Python Runoob"
print(var1)
print(var2)
# 索引
print(var1[-1])
print(var1[-2])
print("************")
print( "var1[4]: ", var1[4],"var1[:4]: ", var1[:4],"var1[4:]: ", var1[4:],"var1+var2:",var1+var2)

# 分片中  【4:】第4位（01234）及以后，包括4  【：4】第4位以前，不包括4
print("var2[1:7]:",var2[1:7])
b="0123456789"
print(b[4::2])  #从第4位开始往后，包含第四位，每2个间距往后输
print(b[4::-2])  #从第4位开始往前，包含第四位，每2个间距往前输
print("@@@@@@@@@@@@@@@@")

#序列相加
print("更新字符串：-",var1[:6]+' python')
print("更新字符串：-",var1[:6]+var2)
print("更新字符串：-",var1[:6]+var2[:2])
print("更新字符串：-",var1[:6]+var2[2:])
print("var1[4]")

#乘法
print("var1*2:",var1*2)
print("（var1+var2)*2:",(var1+var2)*2)
print("var1+var2*2:",var1+var2*2)
print("var1+2*var2:",var1+2*var2)
print("var1*-2:",var1*-2)
print("var1*0:",var1*0)