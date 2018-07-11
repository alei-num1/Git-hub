import requests

r = requests.get("https://www.baidu.com")
print(r.status_code)
print(r.headers)
print(r.text)

# print(r.apparent_encoding)
# print(r.encoding)
# print(r.content)
r.encoding = 'utf-8'
print(r.text)

