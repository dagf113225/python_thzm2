import   pymysql

conn=pymysql.connect(host="127.0.0.1",port=3306,database="thzmdb2",
                 user="root",password="123456",charset="utf8")

dbcursor=conn.cursor()

sql='DELETE  FROM  t_emp  WHERE ename=%s'

dbcursor.execute(sql,('王英'))

#insert|update|delete
conn.commit()

#pip  install   pymysql ,
#pip  install    flask