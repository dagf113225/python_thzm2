import   pymysql as  pdb


conn=pdb.connect(host="127.0.0.1",port=3306,database="thzmdb2",
                 user="root",password="123456",charset="utf8")

print(conn)


dbcursor=conn.cursor()

sql="INSERT  INTO  t_emp(ename,epwd,ebirthday,eaddress,esalary,esex,ephone)" \
    " values(%s,%s,%s,%s,%s,%s,%s)"

dbcursor.execute(sql,('贾春雷','111111','1997-07-01','泰州',1000,'男','13913321099'))

#提交插入的数据到数据库  python操作数据 是手动  ，就需要你commit()
#insert   into|  update |delete
conn.commit()