#标识符的命名规范
#python中的单行注释是用 #来表示

#标识符
'''所谓的标识符就是给程序的变量，构造函数，
方法起名字的一个原则,原则是不能够被违背的'''
#原则就是不能够去违背的

'''

1.python变量的命名
首字母不能够以数字，特殊字符开头,
首字母可以是_，字母
第二个字母可以是数字，字母，_，特殊字符不可以
任意长度

关键字不能够做为标识符

2.方法  ()  同上
'''

#内置函数，python已经创建好的函数
print("----------")

a1=input("请输入一个值:")
print(a1)

#自己定义一个函数，也叫做方法
#定义方法的关键字叫做def 方法名(方法的参数):
def  wr1():
      print("这是函数wr1的输出")
      print("***********")



      print()

print("_____________________")

#方法的调用执行
wr1()

a5=input("请输出一个数:")
if  int(a5)>10:
    print("a5大于10")

else:
    print("a5小于10")



