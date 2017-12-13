'''
while循环
'''
#求1～100递加   1+2+3+···+99+100

n=100
sum=0
counter=1
while counter<=n:
    sum=sum+counter
    counter+=1
print("1到%d之和为%d"%(n,sum))


n=100
sum=1
counter=1
while counter<=n:
    sum=sum*counter
    counter+=1
print("1到%d之积为%d"%(n,sum))


#1-1/2+1/3-1/4+·····+1/99-1/100
n=100
result=0
counter=1
while counter<=n:
    result=result+((-1)**(counter+1))*(1/counter)
    counter+=1
print("1-1/2+1/3-1/4+...+%d之和为%a"%(n,result))

'''
无限循环
'''

var1=1
while var1==1:
    num=int(input("输入一个数字："))
    print("你输入的数字是：",num)
print("goodbye")
#按control+c终止循环
var1=3
var1==1
if var1==1:
    print(1)
else:
    print(2)


'''
while .... else语句
'''

count=0
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"等于5")

#for循环  可以遍历任何序列的项目，如列表或字符串
language=["c","c++","python","java","vb"]
for X in language:
    if X == "java":
        break
    if X == "java":
        continue
    print(X)

language=["c","c++","python","java","vb"]
for X in language:
    if X == "python":
        continue
    if X == "python":
        break
    print(X)

#遍历  最后一次为开  取不到边界
for X in range(-1,9,10):   #往右，单个步长后超过右范围 仅输出开始值
    print("x",X)
for X0 in range(-1,9,-1):     #往左，开始值为左边界，往左没数  问题：为什么不输出开始值x0 -1
    print("x0",X0)
for X1 in range(-1,-11,-2):  #往左，开始值为右边界，往左有数 ，左边界为开区间，左开右闭
    print("x1",X1)
for X2 in range(-11,-1,2):  #往右，开始值为左边界，往右有数，右边界为开区间，左闭右开
    print("x2",X2)
for X3 in range(-1,-11,2):  #往右，开始值为右边界，往右没数了  问题：为什么不输出x3 -1
    print("x3",X3)
for y in range(10):   #默认往右，单个步长为1，从0开始
    print("x",y)

#作业   检查输入说数是不是阿姆斯特朗数

num=int(input("输入一个正整数"))
if type(num)==int:
    if num>0:
        if num>1 :
            c = len(str(num))
            if c==3:
                x=num//10*(c-1)
                y=num//10-x*10
                z=num//1-x*100-y*10
                if num==x**c+y**c+z**c:
                    print("%d是阿姆斯特朗数"%num)
                else:
                    print("%d不是阿姆斯特朗数"%num)
            elif c==2:
                x=num//10*(c-1)
                y=num//1-x*10
                if num==x**c+y**c:
                    print("%d是阿姆斯特朗数"%num)
                else:
                    print("%d不是阿姆斯特朗数"%num)
            else:
                if num==num**c:
                    print("%d是阿姆斯特朗数"%num)
                else:
                    print("%d不是阿姆斯特朗数"%num)
            
    else:
        print("请输入正整数")
else:
    print("请输入正整数")


    
