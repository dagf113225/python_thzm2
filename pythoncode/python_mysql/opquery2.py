import  pymysql  as  pm


#1.连接数据库
conn=pm.connect(host="127.0.0.1",port=3306,database="thzmdb2",user="root",password="123456",charset="utf8")
print(conn)

#2.获取操作数据库对象，游标  Dict
#得到字典类型
dbcursor=conn.cursor(pm.cursors.DictCursor)

#3.定义sql语句  select :查询，一定有返回
sql='SELECT  *  FROM  t_emp'

#4.使用游标对象执行sql
dbcursor.execute(sql)

#5.获取数据  1.fetchall所有

#默认都到一个元祖类型
datas=dbcursor.fetchall()

print(datas)

'''
[
{'eid': 1, 'ename': '李欣', 'epwd': '000000', 'ebirthday': datetime.datetime(1976, 12, 30, 0, 0), 'eaddress': '南京', 'esalary': 8900.0, 'esex': '男', 'ephone': '13913321086'}, 
{'eid': 3, 'ename': '贾春雷', 'epwd': '111111', 'ebirthday': datetime.datetime(1997, 7, 1, 0, 0), 'eaddress': '泰州', 'esalary': 1000.0, 'esex': '男', 'ephone': '13913321099'}, 
{'eid': 4, 'ename': '刘燕凤', 'epwd': '2222', 'ebirthday': datetime.datetime(2008, 7, 1, 0, 0), 'eaddress': '泰州', 'esalary': 1000.0, 'esex': '女', 'ephone': '13913321091'}, 
{'eid': 6, 'ename': '王英', 'epwd': '3333', 'ebirthday': datetime.datetime(2008, 7, 1, 0, 0), 'eaddress': '泰州', 'esalary': 1000.0, 'esex': '女', 'ephone': '13913321091'}
]

'''