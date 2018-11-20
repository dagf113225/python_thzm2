#pip  install  pymysql
#pymysql  python操作mysql数据库的模块




#1.连接数据库python-->mysql
#导入模块
import   pymysql
#声明一个连接对象
#connect(host="127.0.0.1",port=3306, database="thzmdb2"
#user="root",password="123456",dataset="utf8")
connectionObj=pymysql.connect(host="127.0.0.1",port=3306,
                              database="thzmdb2",user="root",
                              password="123456",charset="utf8")
print(connectionObj)

#2.获取操作数据库的游标对象
dboperator=connectionObj.cursor()
#3.构建sql语句
#sql="select  *  from  t_students"
sql="select  sname,sphone,sface from  t_students "
#4.执行sql语句
dboperator.execute(sql)
#5.select查询  fetchall-->查询所有
#alldatas=dboperator.fetchall()
#print(alldatas)
#onedata=dboperator.fetchone()
#print(onedata)
datas=dboperator.fetchmany(3)
print(datas)









