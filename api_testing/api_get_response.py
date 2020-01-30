import requests
import jsonpath
import json
#url
url="https://reqres.in/api/users?page=2"

response=requests.get(url)

json_response=json.loads(response.text)

pages=jsonpath.jsonpath(json_response,'total_pages')
print(pages[0])
assert pages[0]==2