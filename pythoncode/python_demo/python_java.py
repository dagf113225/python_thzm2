import suds

#https://www.cnblogs.com/dhf327/p/4741943.html

#pip install suds-jurko
from suds.client import Client

url="http://localhost:8025/DaoServiceImpl/dao?wsdl"

client = suds.client.Client(url)


result2=client.service.queryAll();
print(result2)


'''result1=client.service.sum(10,20)
print(result1)'''