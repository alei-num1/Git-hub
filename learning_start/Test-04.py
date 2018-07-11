import requests

kv = {'wd': 'Python'}
r = requests.get("https://www.baidu.com/s", params=kv)
print(r.status_code)
print(r.request.url)
