import requests
import os

url3 = "http://img01.zhangtu.com/topic/zuimei/guangxi/10.jpg"
root = "C://学习笔记//"
path = root + url3.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir()
    if not os.path.exists(path):
        r = requests.get(url3)
        with open(path, 'wb') as p:
            p.write(r.content)
            p.close()
            print("Success")
    else:
        print("文件已经存在")
except:
    print("爬取失败")
