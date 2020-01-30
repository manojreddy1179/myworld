import requests
import json

url="https://reqres.in/api/users"

file=open('D:\\Manoj_python\\res.json','r')
json_input=file.read()
request_json=json.loads(json_input)

print(request_json)
response=requests.post(url,request_json)
print(response.content)
#validating response code
assert response.status_code ==201