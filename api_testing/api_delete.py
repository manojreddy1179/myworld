import requests

# API url
url="https://reqres.in/api/users?page=2"
#delete url
response=requests.delete(url)
#fetch response code
print(response.status_code)

#response
assert response.status_code==204