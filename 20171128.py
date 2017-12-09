
'''
算数的运算符
'''
a=21
b=10
c=0
#输出c=a+b 31
c=a+b
print("line1-value of c is",c)
#输出c=a-b 11
c=a-b
print("line2-value of c is",c)
#输出c=a*b 210
c=a*b
print("line3-value of c is",c)
#输出c=a/b 2.1   返回结果为浮点型
c=a/b
print("line4-value of c is",c)
#输出c=a%b 取模-返回除法的余数 1
c=a%b
print("line5-value of c is",c)
#输出c=a**b 幂-a的b次方 8
a=2
b=3
c=a**b
print("line6-value of c is",c)
#输出=a//b a/b商的整数部分 2
a=10
b=5
c=a//b
print("line7-value of c is",c)


#判断a与b是否相等     结果：is not equal
if (a==b):
    print("line1-a is equal to b")
else:
    print("line1-a is not equal to b")
#判断a与b是否不相等1  !=     结果：is not equal
if (a!=b):
    print("line2-a is not equal to b")
else:
    print("line2-a is equal to b")
    '''
    这段仅适用于python2,python3中没有<>语法
#判断a与b是否不相等1  <>
if ( a '<>' b ):
   print "3 - a 不等于 b"
else:
   print "3 - a 等于 b"
   '''

#判断a是否<b
if (a<b):
    print("line4-a is less than b")
else:
    print("line4-a is not less than b")
if (a>b):
    print("line5-a is greater than b")
else:
    print("line5-a is not greater than b")

a=5
b=20
if (a<=b):
    print("line6-a is either less than b")
else:
    print("line6-a is neither less than b")
if (a>=b):
    print("line7-a is either greater than b")
else:
    print("line5-a is neither greater than b")

'''
python赋值运算符
'''
a=21
b=10
c=0
#21+10=31
c=a+b
print("line-1 value of c is",c)
#31+21=52
c+=a
print("line-2 value of c is",c)
#52-21=31
c-=a
print("line-3 value of c is",c)
#31*21=651
c*=a
print("line-4 value of c is",c)
#651/21=31.0  /整除 其结果为浮点型
c/=a
print("line-5 value of c is",c)

c=2
#2/21=0 余2
c%=a
print("line-6 value of c is",c)
#2**21=2097152
c**=a
print("line-7 value of c is",c)
#2097152//21=99864
c//=a
print("line-8 value of c is",c)

'''
python位运算符 
'''
a=60  #0011 1100
b=13  #0000 1101
c=0
#位运算&:参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0  仅1+1输出1，其余输出0
c=a&b  #0000 1100  
print("line1-value of c is",c)
#按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
c=a|b  #0011 1101
print("line2-value of c is",c)
#按位异或运算符：当两对应的二进位相异时，结果为1
c=a^b  #0011 0001
print("line2-value of c is",c)
#按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
c=~a  #1100 0011
print("line2-value of c is",c)
#左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
c=a<<2  # 1111 0000
print("line2-value of c is",c)
#右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数
c=a>>2  # 1111
print("line2-value of c is",c)




'''
python逻辑运算符
'''
a = 10
b = 20
c=0
#布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
if ( a and b ):
   print ("line1-a and b are ture")
else:
   print ("line1-either a is not ture or b is not ture")
 
if ( a or b ):
   print ("line2-either a is ture or b is true or both are ture")
else:
   print ("line2-neither a is ture or b is true ")
 

a = 0
if ( a and b ):
   print ("line3-a and b is true")
else:
   print ("line3-a and b is not true")
 
if ( a or b ):
   print ("line4-either a is ture or b is true or both are ture")
else:
   print ("ine4-neither a is ture or b is true")
 
if not( a and b ):
   print ("line5-a and b are ture")
else:
   print ("line5-either a is not ture or b is not true")

'''
python成员运算符
'''
a=0
b=10
list=[1,2,3,4,5]
#判断a是否在list里面   不在
if (a in list):
    print("line1-a is available in the given list")
else:
    print("line1-a is not available in the given list")
#判断a是否不在list里面   不在
if (b not in list):
    print("line2-b is not available in the given list")
else:
    print("line2-b is available in the given list")

'''
python身份运算符
'''
a=20
b=20
#判断a与b是否引用自同一个对象
if (a is b):
    print("line1-a and b have same identity")
else:
    print("line1-a and b do not have same identity")

if (id(a)==id(b)):
    print("line2.1-a and b have same identity")
else:
    print("line2.1-a and b do not have same identity")

if (id(a) is id(b)):
    print("line2.2-a and b have same identity")
else:
    print("line2.2-a and b do not have same identity")


b=30
if (a is b):
    print("line3-a and b have same identity")
else:
    print("line3-a and b do not have same identity")

if (a is not b):
    print("line4-a and b do not have same identity")
else:
    print("line4-a and b have same identity")

'''
python运算符优先级
'''
a=20
b=10
c=15
d=5
e=0
e=(a+b)*c/d   #(30*15)/5 =90.0
print("value of (a+b)*c/d is",e)

e=((a+b)*c)/d
print("value of ((a+b)*c)/d is",e)

e=(a+b)*(c/d)  #30*3.0=90.0 
print("value of (a+b)*(c/d) is",e)

e=a+(b*c)/d   #20+150/5=50.0
print("value of a+(b*c)/d is",e)
