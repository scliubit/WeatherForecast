import json
import time
import os
import socket
import re
from Alert import Alert as Alt
import urllib
from urllib import request
from urllib.parse import quote
import httplib2
from weather import WeatherInfo
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
# Please buy a token(free for 1000 times).
token = ""
if token == "":
    AlertObj.Warn("No available token!")
    exit()
headers = {"token": token}
http = httplib2.Http()
response, content = http.request(url, 'GET', headers=headers)
content = eval(str(content, 'utf-8')[5:-1])
AlertObj.Info("Your Location         {} {} {}".format(content['data'][
    0], content['data'][1], content['data'][2]))
AlertObj.Info("ISP                   {} {}".format(content['data'][0], content[
    'data'][3]))
# get an accurate location
url = "https://www.ipip.net/ip.html"
string = request.urlopen(url).read()
xre = b'(<div style="text-align: center;color:red;font-size: 20px;font-weight: 600;">)(.+)(</div>)'
z = re.search(xre, string).group(2).decode()
print(z)
location = z.split(" ")
city = location[-1]
# finish
key = ""
if key == "":
    AlertObj.Warn("No available KEY!")
    exit()
url = "https://free-api.heweather.com/v5/weather?city=" + quote(
    city) + "&key=" + key

content = request.urlopen(url).read()
data = json.loads(content.decode())

wobj = WeatherInfo(data)
print(wobj.basic)

os.system('pause')