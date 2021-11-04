#conding:utf-8
import requests
import json
payload = {"yoyo":"hello world",
          "pythonQQ群":"226296743"}
# r=requests.post('http://httpbin.org/post',data=payload)
# print(r.text)
#转化成json格式
data_json=json.dumps(payload)
r=requests.post('http://httpbin.org/post',json=data_json)
print(r.text)