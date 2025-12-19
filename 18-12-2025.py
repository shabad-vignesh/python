#API request example
#mport requests
#rl = "https://api.github.com/data"
#ata = { 'email': 'shabadvignesh2004@gmail.com', 'username':'shabadvignesh' }
#equests.post(url, json=data)

import json #built in 
#json.loads() ->json string -> python
#json.dumps() ->python -> json:- Api
#json.dump() ->python file -> json file
#json.load() -> json sting file -> python file

data = {
    "email": "shabadvignesh2004@gmail.com",
    "username": "shabadvignesh"
}
print(type(data)) #dict
json_data = json.dumps(data)
print(type(json_data)) #str
print(json_data) 

#example on the loads first convert json string to python data
json_string = '{"email": "shabadvignesh2004@gmail.com", "username": "shabadvignesh"}'
python_data = json.loads(json_string)   
print(type(python_data)) #dict
print(python_data)