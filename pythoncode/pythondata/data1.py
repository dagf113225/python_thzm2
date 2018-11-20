#python数据类型和变量紧密联系
#变量对应着数据类型，对应着运算

#python变量 1.变量的输出
# 2.变量的类型  3.变量的内存地址(身份)

#整型变量
a=100
#python字符串不能够使用+，连接整型
print("a的值为:",a)

#这个变量类型。python变量类型在定义时不需要声明
#但是实际是有 的
#type(),输出类型
print("a的类型为:",type(a))

#内存地址  id()方法
print("a的地址为:",id(a))

print("----------------")

a1=100
print("a1的地址为:",id(a1))

a2=101
print("a2的地址为:",id(a2))

#运算符   == 返回的是bool  True
print(a==a1)  #True   Python ==比较的是值
print(a1==a2) #False
print(id(a1)  is  id(a2))  #is比较的是地址

print(a1  is  a2)