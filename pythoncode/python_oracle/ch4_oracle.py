import  cx_Oracle

def  checkUserLogin(name,pwd):
     conn=cx_Oracle.connect("student/student@127.0.0.1/XE")
     dbcursor=conn.cursor()
     sql='select  count(*)   from  t_employee  where tname=:name ' \
         ' and  trim(tpwd)=:pwd'
     params={"name":name,"pwd":pwd}
     dbcursor.execute(sql,params)
     data=dbcursor.fetchone()
     print("%s"%(data))

def   countTsalary(name):
    conn = cx_Oracle.connect("student/student@127.0.0.1/XE")
    dbcursor = conn.cursor()
    sql = "select round(tsalary/(select  sum(tsalary)  from t_employee ),3) " \
          " from  t_employee  where tname=:name"
    params = {"name": name}
    dbcursor.execute(sql, params)
    data = dbcursor.fetchone()
    print("%s" % (data))

def   countTsalaryOne(name):
    conn = cx_Oracle.connect("student/student@127.0.0.1/XE")
    dbcursor = conn.cursor()
    sql = "select  tsalary+nvl(tmoney,0) from  t_employee  where tname=:name"
    params = {"name": name}
    dbcursor.execute(sql, params)
    data = dbcursor.fetchone()
    print("%s" % (data))

def  queryPagedata(pageNum):
    conn = cx_Oracle.connect("student/student@127.0.0.1/XE")
    dbcursor = conn.cursor()
    sql = "select  *  from (select  rownum  rm,  e.* from   t_employee   e where rownum<=:endNum) temp  where  temp.rm>:startNum"
    params = {"endNum": pageNum*3,"startNum":(pageNum-1)*3}
    dbcursor.execute(sql, params)
    data = dbcursor.fetchall()

    for onedata in data:
         print("{0}" .format (onedata))


#checkUserLogin('李涛','1234')
#countTsalaryOne("丁凯")
queryPagedata(1)