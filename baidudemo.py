#coding:utf-8（测试）
import requests
r=requests.get('https://www.baidu.com/')
print(r.url)
print(r.encoding)
print(r.content)
print(r.headers)
print(r.cookies)
