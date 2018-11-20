#python 元祖类型 数组

#()  方法名()
arrays=(1,2,3)
print(arrays)
print(type(arrays))
print(id(arrays))

print("---------------")
arrays1=(1,2,3)
print(arrays1)
print(type(arrays1))
print(id(arrays1))
print("---------------")

print(arrays==arrays1)
print(arrays is  arrays1)

#定长定值数据类型
print(arrays[0])
print(len(arrays))

#元祖类型是不能够改变值和长度
#arrays[0]=20
#print(arrays)

#元祖类型的遍历
for value  in  arrays:
    print("其中的每一个值为:",value)

#求和
a2=(1,"2",3,"8")