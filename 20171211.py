'''
python if 条件控制语句
'''
var1=100
if var1:
    print("var1 is true")

#Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
var2=0
if var2:
    print("0 is true")
else:
    print("0 is false")

var3=100
if var3:
    print("100 is true")
else:
    print("100 is false")


season = int(input("月份"))
if season>=1 and season <=3:
    print("春季")
elif season>3 and season<=6:
    print("夏季")
elif season>6 and season<=9:
    print("秋季")
elif season>9 and season<=12:
    print("冬季")    
else:
    print("无效值")
#退出提示
input("点击enter键退出")

'''
==操作符
'''
#数字
print(5==6)
#变量
x=5
y=6
z=5
f=4.3
print(x==y)
print(z==x)
print(z==f)
print(z>=f)


'''
猜字谜游戏
'''
number=7
guess=0
while guess != number:
    guess=int(input("你猜的数字"))
    if guess==number:
        print("猜对了")
    elif guess > number:
        print("猜大了")
    elif guess < number:
        print("猜小了")
#退出提示
input("点击enter键退出")

'''
if 嵌套
'''
num=int(input("输入一个数字"))
if num%2==0:
    if num%3==0:
        print("该数字可以整除2和3")
    else:
        print("该数字可以整除2，但不能整除3")
else:
    if num%3==0:
        print("该数字可以整除3，但不能整除2")
    else:
        print("该数字既可以整除3，也不能整除2")