import   pymysql


def   checkLogin(*args):
      conn = pymysql.connect(host="127.0.0.1", port=3306, database="thzmdb2",
                       user="root", password="123456", charset="utf8")

      dbcursor=conn.cursor()

      sql='SELECT  COUNT(*)   FROM  t_emp  WHERE ename=%s  AND epwd=%s'

      dbcursor.execute(sql,args)

      datas=dbcursor.fetchone()
      print(datas[0])

