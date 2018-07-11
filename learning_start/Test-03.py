import requests

url2 = "https://www.amazon.cn/dp/B07D591SYY/ref=cngwdyfloorv2_recs_0/458-1971680-3825635?" \
       "pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_" \
       "r=67GS240BB2VC190K3C52&pf_rd_r=67GS240BB2VC190K3C52&pf_rd_t=36701&pf_rd_" \
       "p=538883d8-3c6e-4f6f-89c9-fedbbcdc164f&pf_rd_p=538883d8-3c6e-4f6f-89c9-fedbbcdc164f&pf_rd_i=desktop"
# r = requests.get(url2)
# print(r.status_code)
# print(r.encoding)
# print(r.apparent_encoding)
# r.encoding = r.apparent_encoding
# print(r.text)
# print(r.request.headers)
kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url2, headers=kv)
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.request.headers)
print(r.text[:1000])
