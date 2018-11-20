import  pymysql


def    addEmp(name,pwd,birthday,address,salary,sex,phone):
       conn = pymysql.connect(host="127.0.0.1", port=3306, database="thzmdb2",
                       user="root", password="123456", charset="utf8")

       dbcursor = conn.cursor()

       sql = "INSERT  INTO  t_emp(ename,epwd,ebirthday,eaddress,esalary,esex,ephone)" \
             " values(%s,%s,%s,%s,%s,%s,%s)"

       dbcursor.execute(sql, (name,pwd,birthday,address,salary,sex,phone))

       #insert
       conn.commit()

       print('插入数据成功')

#方法调用
addEmp('刘燕凤','2222','2008-07-01','泰州',1000,'女','13913321091')

