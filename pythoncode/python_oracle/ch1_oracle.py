import  cx_Oracle  as  cxo


conn=cxo.connect("student/student@127.0.0.1/XE")
print(conn)

sql="select  tname  from   t_stus"

cursor=conn.cursor()
cursor.execute(sql)

datas=cursor.fetchall()
print(datas)