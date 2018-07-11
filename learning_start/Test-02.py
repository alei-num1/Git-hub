import requests

url1 = "https://item.jd.com/3042415.html"
try:
    r = requests.get(url1)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("Fail")
# print(r.status_code)
# print(r.encoding)
