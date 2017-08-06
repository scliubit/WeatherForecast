#!/usr/bin/python
# -*- coding: utf-8 -*-
#python3
import urllib
from urllib import request
import httplib2
import re

url = "http://www.ipip.net"
#获取外网IP
with request.urlopen(url) as urlf:
    urlstring = urlf.read()
    print(re.findall(b'\d+\.\d+\.\d+\.\d+', urlstring)[1])

exit()
params = urllib.parse.urlencode({
    'ip': '219.143.205.143',
    'datatype': 'jsonp',
    'callback': 'find'
})
url = 'http://api.ip138.com/query/?' + params
headers = {"token": "b00aec67a7e5e29de57e4d0c530ee044"}  #token为示例
http = httplib2.Http()
response, content = http.request(url, 'GET', headers=headers)
content = eval(str(content, 'utf-8')[5:-1])
print("您的位置为{} {} {}".format(content['data'][0], content['data'][1], content[
    'data'][2]))
print("服务供应商为 {} {}".format(content['data'][0], content['data'][3]))
