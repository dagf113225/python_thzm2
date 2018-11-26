import  cx_Oracle  as  cxo


conn=cxo.connect("student/student@127.0.0.1/XE")
print(conn)

sql="select     tname  from   t_employee  where  tdnum  in " \
    "(select dnum  from   t_depts  where  dname=:name)"

#oracle传入参数是键值对  字典类型
params={"name":"技术部"}

cursor=conn.cursor()
cursor.execute(sql,params)

datas=cursor.fetchall()
print(datas)