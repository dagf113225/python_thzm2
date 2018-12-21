from  flask  import   Flask
import   suds
from  flask  import   render_template
from  suds  import   client

#pip   install suds-jurko

webapp=Flask(__name__)


@webapp.route("/index")
def   defaultView():
      print("-------加载首页视图------------")

      #python自己不要去访问数据库
      url="http://127.0.0.1:8100/userdataservice/user?wsdl"

      #python访问webservice客户端对象
      client=suds.client.Client(url)

      result=client.service.queryRoleData()

      print(result)

      return  render_template("index.html")



if __name__=="__main__":
    webapp.run(debug=True,port=8200)