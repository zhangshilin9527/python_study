import requests

# url1 = 'http://httpbin.org/get'
# data1 = {'name': 'zhangsan', 'sex': 1}
# reponse1 = requests.get(url1, data1 =data1)
# print(reponse1.json())

url2 = 'http://httpbin.org/post'
data2 = {'name': 'lisi', 'sex': 2}
reponse1 = requests.post(url2, data2)
print(reponse1.json())


