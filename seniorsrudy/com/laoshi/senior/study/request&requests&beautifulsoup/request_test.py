from urllib import request
from urllib import parse

url = 'http://www.baidu.com/'
response = request.urlopen(url, timeout=1)  # 最好设置超时时间
print(response.read().decode('utf-8'))  # decode('utf8')  解析中文 utf-8  一个汉字三个字节  gbk  一个汉字 两个字节

data = bytes(parse.urlencode({'name': 'zhangsan'}), encoding='utf8')
response2 = request.urlopen('http://httpbin.org/post', data=data, timeout=1)
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "name": "zhangsan"
#   },
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Content-Length": "13",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.7",
#     "X-Amzn-Trace-Id": "Root=1-61ee0e7f-7e49540b353d71ee0678f284"
#   },
#   "json": null,
#   "origin": "114.247.16.106",
#   "url": "http://httpbin.org/post"
# }
print(response2.read().decode('utf8'))

response3 = request.urlopen('http://httpbin.org/get', timeout=1)
# {
#   "args": {},
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.7",
#     "X-Amzn-Trace-Id": "Root=1-61ee0f30-04372c557d4685ff6ad0d67e"
#   },
#   "origin": "114.247.16.106",
#   "url": "http://httpbin.org/get"
# }

print(response3.read().decode('utf8'))


headers = {
    "Accept-Encoding": "identity",
    "Content-Length": "13",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-61ee0e7f-7e49540b353d71ee0678f284"
}

data4 = bytes(parse.urlencode({'name': 'zhangsan'}), encoding='utf8')
req = request.Request(url='http://httpbin.org/post', data=data4, method='POST', headers=headers)
response4 = request.urlopen(req)
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "name": "zhangsan"
#   },
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Content-Length": "13",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
#     "X-Amzn-Trace-Id": "Self=1-61ee10ba-6281e6e71728266f2ba0dc7c;Root=1-61ee0e7f-7e49540b353d71ee0678f284"
#   },
#   "json": null,
#   "origin": "114.247.16.106",
#   "url": "http://httpbin.org/post"
# }
print(response4.read().decode('utf8'))
