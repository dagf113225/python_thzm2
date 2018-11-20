s1="1234"

#输出值
print("s1的值为",s1)
print("s1的类型为",type(s1))
print("s1的地址为",id(s1))

print("-------------------")
s2='1234'

#输出值
print("s2的值为",s2)
print("s2的类型为",type(s2))
print("s3的地址为",id(s2))

print("-------------------")
#字符串不能够和整数类型执行+运算

#print(s1+10)

print(s1+"10")
print(s1+'10')

a5="123456"

a6="123456"

print(a5==a6)
print(a5  is  a6)

a7="12345"
a7=a7+"6"
#天汇智码-李欣     南科技-李欣
#==比较的是值
print(a5==a7)

#is 比较的是地址
print(a5  is  a7)
