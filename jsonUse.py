import json

#reading json files
with open("JSON.json", "r") as f:
    data = json.load(f)
#If you get jsonstring instead of json file, you need to use json.loads(fstr)
print(data)#return python dictionary of json file

#writing json files
my_data = {"name": "John", "age": 12}
#transform python dictionary into json string
jsonstr = json.dumps(my_data, indent = 2)

with open("JSON.json", "w") as f:
    f.write(jsonstr)
    #or
    json.dump(my_data, f)
    


