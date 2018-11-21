import cx_Oracle as  co

#连接oracle  11.2
conn=co.connect("student/student@127.0.0.1/XE")
print(conn)

oracledb=conn.cursor()
sql='select  *  from  t_stus'
oracledb.execute(sql)

datas=oracledb.fetchall()
print(datas)

#print(datas[-1])


