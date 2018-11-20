import   pymysql  as  pdb

#*args,可变参数 方法的参数是个元祖()
def   addEmp(*args):
    conn = pdb.connect(host="127.0.0.1", port=3306, database="thzmdb2",
                           user="root", password="123456", charset="utf8")

    dbcursor = conn.cursor()

    sql = "INSERT  INTO  t_emp(ename,epwd,ebirthday,eaddress,esalary,esex,ephone)" \
          " values(%s,%s,%s,%s,%s,%s,%s)"

    dbcursor.execute(sql, args)

    # insert
    conn.commit()

    print('插入数据成功')

addEmp('王英','3333','2008-07-01','泰州',1000,'女','13913321091')