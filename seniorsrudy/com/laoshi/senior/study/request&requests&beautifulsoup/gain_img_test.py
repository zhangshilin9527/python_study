import requests
import re

url = 'http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F'

response = requests.get(url).text
# <div class="grid-item work-thumbnail">
#     <a href="http://www.cnu.cc/works/564632" class="thumbnail" target="_blank">
# 	<div class="title">
# 		击
# 		</div>
# 	<div class="author">
# 		林明小川
# 	</div>
# 		<img src="http://imgoss.cnu.cc/2201/18/18e1c18313c53541a13014fcb1aedcdb.jpg?width=2000&amp;height=3000&x-oss-process=style/flow280" alt="击">
#      </a>
# </div>

#  . 匹配任意的单个字符
#  * 匹配前面的字符出现0次-n次
#  ? 匹配前面的字符出现0次-1次
# .*?  不适用贪婪模式 只匹配第一个
# pattern = re.compile('<a href="(.*?)".*?title">(.*?)</div>', re.S)
pattern = re.compile('<a href="(.*?)".*?title">(.*?)</div>.*?author">(.*?)</div>', re.S)
results = re.findall(pattern, response)
# print(results)
data = []

for result in results:
    url, name, author = result
    data.append([url, re.sub('\s', '', name), re.sub('\s', '', author)])
    # print(url, re.sub('\s', '', name), re.sub('\s', '', author))
print(len(data))
for dd in data:
    url, name, author = dd
    print('url:%s, name:%s, author:%s' % (url, name, author))
