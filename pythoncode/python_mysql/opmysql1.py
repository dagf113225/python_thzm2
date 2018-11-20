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
datas=dbcursor.fetchall()

#print(datas)
'''

((1, '李欣', '000000', datetime.datetime(1976, 12, 30, 0, 0), '南京', 8900.0, '男', '13913321086'), (3, '贾春雷', '111111', datetime.datetime(1997, 7, 1, 0, 0), '泰州', 1000.0, '男', '13913321099'), (4, '刘燕凤', '2222', datetime.datetime(2008, 7, 1, 0, 0), '泰州', 1000.0, '女', '13913321091'))


'''

for  onedata in  datas:
    print(onedata)
    for  value  in  onedata:
        print(value)