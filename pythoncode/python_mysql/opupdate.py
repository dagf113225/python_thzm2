import   pymysql

conn=pymysql.connect(host="127.0.0.1",port=3306,database="thzmdb2",
                 user="root",password="123456",charset="utf8")

dbcursor=conn.cursor()

sql='UPDATE t_emp  SET  epwd=%s  WHERE eid=%s'

dbcursor.execute(sql,('123456',6))

conn.commit()