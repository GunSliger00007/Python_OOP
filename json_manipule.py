import json
with open("file.json","r") as file:
    content=json.load(file)
    
print(content)

data={
    "name":"Gehendra",
    "age":20,
}
with open("Data.json","w") as file:
    json.dump(data,file,indent=4)