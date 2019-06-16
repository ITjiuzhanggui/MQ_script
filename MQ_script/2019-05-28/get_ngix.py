import json

from xmls import XlslSave

path = "C:\\Users\\xinhuizx\\python_Code\\MQ_scr\\data_LOG.json"
with open(path, 'r') as f:
    data = json.load(f)
nginx_data = data.get("default").get("nginx")
clear_nginx_data = data.get("clear").get("nginx")

format_nginx = []


def insert_ngix(data, num):
    for k, v in data.items():
        if k == "Requests per second":
            format_nginx.append([14, num, v])
        if k == "Time per request":
            format_nginx.append([12, num, v])
        if k == "Time per request(all)":
            format_nginx.append([13, num, v])
        if k == "Time taken for tests":
            format_nginx.append([11, num, v])
        if k == "Transfer rate":
            format_nginx.append([15, num, v])


insert_ngix(nginx_data, 1)
insert_ngix(clear_nginx_data, 2)
print(format_nginx)
XlslSave().append_excel(format_nginx)

# pip install  xlrd==0.6.1
