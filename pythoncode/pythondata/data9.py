items={"name":"李欣","age":30,
       "address":"南京"}

items["sex"]="男"

print(items)

#遍历数据
#key
for key  in  items.keys():
     print("key-->",key,items[key])

print("------------------")
#value
for  value  in  items.values():
    print("value-->", value)
print("------------------")
#key,value
for   key,value  in  items.items():
    print(key,value)

print("------------------")


vass={"a1":[{"k1":"10"},{"k2":"20"}]}

lists=vass["a1"]
print(lists)
print("----------------------------")
for  item in  lists:
     for  key,value  in item.items():
         print(key,"---->",value)

