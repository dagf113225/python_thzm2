import  cx_Oracle


conn=cx_Oracle.connect("student/student@127.0.0.1/XE")
dbcursor=conn.cursor()
sql='select  count(*)  from  t_employee'
dbcursor.execute(sql)
data=dbcursor.fetchone()
print(data)
print("{0}".format(data))
print("%s"%(data))

