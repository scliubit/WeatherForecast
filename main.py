import json
import time
import os
import socket
import re
from Alert import Alert as Alt
import urllib
import httplib2
from urllib import request
AlertObj = Alt()
# For IP address
ip_url = "http://www.ipip.net"
with request.urlopen(ip_url) as urlf:
    urlstring = urlf.read()
    ip = re.findall(b'\d+\.\d+\.\d+\.\d+', urlstring)[1]
    ipstring = ip.decode()
    if ipstring == '':
        AlertObj.Warn("Fail to get your IPv4 - Address")
# For Local IP(Might not be used actually...)
hostname = socket.gethostname()
localIP = socket.gethostbyname(hostname)
AlertObj.Info("Hello %s user." % hostname)
AlertObj.Info("Your Local IP:        {}".format(localIP))
AlertObj.Info("Your IPv4 Address:    {}".format(ipstring))
now = time.time()
AlertObj.Info('System time:          ' + str(now))
with open("city.json", 'r') as f:
    city = json.load(f)
AlertObj.Info('Load cities in        {} s'.format(float(time.time() - now)))
now = time.time()
AlertObj.Info("System time:          {}".format(now))
# =====Finish reading in=====
params = urllib.parse.urlencode({
    'ip': ipstring,
    'datatype': 'jsonp',
    'callback': 'find'
})
url = 'http://api.ip138.com/query/?' + params
# This token was bought by the writer.
# Do not use is token frequently for there's a limit (about 1000 times).
headers = {"token": "b00aec67a7e5e29de57e4d0c530ee044"}
http = httplib2.Http()
response, content = http.request(url, 'GET', headers=headers)
content = eval(str(content, 'utf-8')[5:-1])
AlertObj.Info("Your Location         {} {} {}".format(content['data'][
    0], content['data'][1], content['data'][2]))
AlertObj.Info("ISP                   {} {}".format(content['data'][0], content[
    'data'][3]))

os.system('pause')