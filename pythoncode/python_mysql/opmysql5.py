import  pymysql  as  pm

def  queryPage(pageNum):
     conn=pm.connect(host="127.0.0.1",port=3306,database="thzmdb2",user="root",password="123456",charset="utf8")
     sql="select  * from  t_stus  limit  %s,%s"
     dbcursor=conn.cursor()
     dbcursor.execute(sql,((pageNum-1)*3,3))
     datas=dbcursor.fetchall()
     #print(datas)
     for  data in  datas:
         print(data)

queryPage(2)