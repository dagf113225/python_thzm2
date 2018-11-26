from  aip  import  AipImageClassify


app_id="11082928"
api_key="cS8Tohau7MxlauYY79kv69V9"
secret_key="sGsfH4CxWSNV1O9Xcd3ZGvRsrbey9Xvt"

def   getfilepath(filepath):
    with open(filepath,"rb") as fp:
        return fp.read()

image=getfilepath("a11.jpg")

client=AipImageClassify(app_id,api_key,secret_key)
name=client.carDetect(image, options={"top_num":1})["result"][0]["name"]
print(name)