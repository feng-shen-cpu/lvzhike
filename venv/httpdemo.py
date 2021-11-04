#coding:utf-8
import requests
#找找看搜索功能
par={"Keywords":"yoyoketang"}
#请求博客首页
r=requests.get('http://zzk.cnblogs.com/s/blogrpost',params=par)
print (r.status_code)
print (r.text)