import  pymysql  as  pm


#1.连接数据库
conn=pm.connect(host="127.0.0.1",port=3306,database="thzmdb2",user="root",password="123456",charset="utf8")
print(conn)

#2.获取操作数据库对象，游标
dbcursor=conn.cursor()

#3.定义sql语句  select :查询，一定有返回
sql='SELECT  *  FROM  t_emp'

#4.使用游标对象执行sql
dbcursor.execute(sql)

#5.获取数据  1.fetchall所有

#默认都到一个元祖类型
datas=dbcursor.fetchall()

print(datas)