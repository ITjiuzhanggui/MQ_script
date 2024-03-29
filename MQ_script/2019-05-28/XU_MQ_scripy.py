#!/usr/bin/env python

import os
import re
import json
import xlrd
from xlutils import copy
from pprint import pprint

# for i in range(5):
#     os.system("make tests > logs/%s.logs 2>&1 "%str(i))


# class PsrsingLong(object):
#     def __init__(self):
#         self.filename = '1.logs'
#
#     def  match(self):
#         with open(self.filename, 'r') as f:
#             lines = f.readlines()
#
#             for line in lines:
#                 nginx = re.search(r'nginx/nginx.sh', line)
#
#                 if nginx:
#                     nginx_info_up = re.search(r'Test docker hub official image first', line)
#
#                     if nginx_info_up:
#                         nginx_hub = re.search(r'Time taken for tests:')
#
#
# def main():
#     for i in range(1):
#         os.system("make tests > logs/%s.logs 2>&1 "%str(i))
#
# if __name__ == '__main__':
#     main()

# http_str = """"""
#
# def get_from_http(file_name):
#     with open(file_name,'r') as f:
#         lines = f.readline()
#         while lines :
#             yield lines
#             lines = f.readline()
#
# for lines in get_from_http("1.logs"):
#     if lines.startswith("httpd/httpd.sh"):
#         print(lines)


data = {
    "default": {
        "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {},
    },

    "clear": {
        "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {},
    }
}


def read_logs(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        return f.readlines()


from six import add_metaclass
from abc import ABCMeta, abstractmethod, abstractproperty
from functools import lru_cache

@add_metaclass(ABCMeta)
class A(ABCMeta):
    def __init__(self):
        self.lines = self.read_logs('1.logs')

    @lru_cache(None, typed=False)
    def useCache(cls, data):
        def cache(data):
            return data

        return cache(data)

    def read_logs(self, file_name):
        with open(file_name, 'r', encoding="utf-8") as f:
            return self.useCache(f.readlines())

    @abstractmethod
    def get(cls):
        ''''''
        pass


class Clear_Http(A):

    def get(self):
        lines =self.lines
        for i in lines[lines.index("httpd/httpd.sh\n"):lines.index("httpd-server\n")]:
            if i.startswith("Time taken for tests"):
                num = re.findall("\d+\.?\d*", i)
                data.get("default").get("httpd").update(
                    {"Time taken for tests": num[0]}
                )

class Nginx(A):
    def get(self):
        lines = self.lines
        for i in lines[lines.index("httpd/httpd.sh\n"):lines.index("httpd-server\n")]:
            if i.startswith("Time taken for tests"):
                num = re.findall("\d+\.?\d*", i)
                data.get("default").get("httpd").update(
                    {"Time taken for tests": num[0]}
                )


def get_from_httpd(lines):
    for i in lines[lines.index("httpd/httpd.sh\n"):lines.index("httpd-server\n")]:
        if i.startswith("Time taken for tests"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("httpd").update(
                {"Time taken for tests": num[0]}
            )

        if i.endswith("[ms] (mean)\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("httpd").update(
                {"Time per request": num[0]}
            )

        if i.endswith("(mean, across all concurrent requests)\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("httpd").update(
                {"Time per request(all)": num[0]}
            )

        if i.startswith("Requests per second"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("httpd").update(
                {"Requests per second": num[0]}
            )

        if i.startswith("Transfer rate"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("httpd").update(
                {"Transfer rate": num[0]}
            )


def get_from_nginx(lines):
    """nginx unit tests analysis"""
    for i in lines[lines.index("nginx/nginx.sh\n"):lines.index("nginx-server\n")]:
        if i.startswith("Time taken for tests"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("nginx").update(
                {"Time taken for tests": num[0]})
        if i.endswith("[ms] (mean)\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("nginx").update(
                {"Time per request": num[0]}
            )
        if i.endswith("(mean, across all concurrent requests)\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("nginx").update(
                {"Time per request(all)": num[0]}
            )
        if i.startswith("Requests per second"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("nginx").update(
                {"Requests per second": num[0]}
            )
        if i.startswith("Transfer rate"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("nginx").update(
                {"Transfer rate": num[0]}
            )


def get_from_memcached(lines):
    '''memcached unit tests analysis'''
    for i in lines[lines.index("memcached/memcached.sh\n"):lines.index("memcached-server\n")]:
        if i.startswith("Sets"):
            num = re.findall("---|\d+\.?\d*", i)
            num[-1] += " KB/sec"
            data.get("default").get("memcached").update(
                {"Sets": num[-2:]})

        if i.startswith("Gets"):
            num = re.findall("---|\d+\.?\d*", i)
            num[-1] += " KB/sec"
            data.get("default").get("memcached").update(
                {"Gets": num[-2:]})

        # if i.startswith("Waits"):
        #     # print(i)
        #     num = re.findall("---|\d+\.?\d*", i)
        #     num[-1] += " KB/sec"
        #     data.get("default").get("memcached").update(
        #         {"Waits": num[-2:]})

        if i.startswith("Totals"):
            num = re.findall("---|\d+\.?\d*", i)
            num[-1] += " KB/sec"
            data.get("default").get("memcached").update(
                {"Totals": num[-2:]})


def get_from_redis(lines):
    """redis unit tests analysis"""
    influs_defaut = []
    for i in lines[lines.index("redis/redis.sh\n"):lines.index("some-redis\n")]:
        influs_defaut.append(i)

    for i in influs_defaut[
             influs_defaut.index("====== PING_INLINE ======\n"):influs_defaut.index("====== PING_BULK ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"PING_INLINE": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== PING_BULK ======\n"):influs_defaut.index("====== SET ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"PING_BULK": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== SET ======\n"):influs_defaut.index("====== GET ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"SET": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== GET ======\n"):influs_defaut.index("====== INCR ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"GET": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== INCR ======\n"):influs_defaut.index("====== LPUSH ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"INCR": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== LPUSH ======\n"):influs_defaut.index("====== RPUSH ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LPUSH": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== RPUSH ======\n"):influs_defaut.index("====== LPOP ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"RPUSH": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== LPOP ======\n"):influs_defaut.index("====== RPOP ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LPOP": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== RPOP ======\n"):influs_defaut.index("====== SADD ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"RPOP": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== SADD ======\n"):influs_defaut.index("====== HSET ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"SADD": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== HSET ======\n"):influs_defaut.index("====== SPOP ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"HSET": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== SPOP ======\n"):influs_defaut.index(
            "====== LPUSH (needed to benchmark LRANGE) ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"SPOP": num[0]}
            )

    for i in influs_defaut[
             influs_defaut.index("====== LPUSH (needed to benchmark LRANGE) ======\n"):influs_defaut.index(
                 "====== LRANGE_100 (first 100 elements) ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LPUSH (needed to benchmark LRANGE)": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== LRANGE_100 (first 100 elements) ======\n"):influs_defaut.index(
            "====== LRANGE_300 (first 300 elements) ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LRANGE_100 (first 100 elements)": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== LRANGE_300 (first 300 elements) ======\n"):influs_defaut.index(
            "====== LRANGE_500 (first 450 elements) ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LRANGE_300 (first 300 elements)": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== LRANGE_500 (first 450 elements) ======\n"):influs_defaut.index(
            "====== LRANGE_600 (first 600 elements) ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LRANGE_500 (first 450 elements)": num[0]}
            )

    for i in influs_defaut[influs_defaut.index("====== LRANGE_600 (first 600 elements) ======\n"):influs_defaut.index(
            "====== MSET (10 keys) ======\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"LRANGE_600 (first 600 elements)": num[0]}
            )

    influs_defaut.append("some-redis\n")
    for i in influs_defaut[influs_defaut.index("====== MSET (10 keys) ======\n"):influs_defaut.index("some-redis\n")]:
        if i.endswith("requests per second\n"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("redis").update(
                {"MSET (10 keys)": num[0]}
            )


def get_from_php(lines):
    """php unit tests analysis"""

    for i in lines[lines.index("php/php.sh\n"):lines.index("[php] [INFO] Test clear docker image:\n")]:

        if i.startswith("Score"):
            num = re.findall("\d+\.?\d*", i)
            data.get("default").get("php").update(
                {"phpbench": num[0]}
            )


def get_from_python(lines):
    """python unit tests analysis"""

    for i in lines[lines.index("python/python.sh\n"):lines.index("[python] [INFO] Test clear docker image:\n")]:

        if i.startswith("Totals"):
            num = re.findall("\d+\.?\d*", i)
            num[0] = {"minimum": num[0]}
            num[1] = {"average": num[1]}
            data.get("default").get("python").update(
                {"Totals": num[-2:]}
            )


def get_from_golang(lines):
    """golang unit tests analysis"""
    for i in lines[lines.index("golang/golang.sh\n"):lines.index("[golang] [INFO] Test clear docker image:\n")]:
        if i.startswith("BenchmarkBuild"):
            num = re.findall("\d+\.?\d* ns/op", i)
            data.get("default").get("golang").update(
                {"BenchmarkBuild": num[0][:-6]}
            )

        if i.startswith("BenchmarkGarbage"):
            num = re.findall("\d+\.?\d* ns/op", i)
            data.get("default").get("golang").update(
                {"BenchmarkGarbage": num[0][:-6]}
            )

        if i.startswith("BenchmarkHTTP"):
            num = re.findall("\d+\.?\d* ns/op", i)
            data.get("default").get("golang").update(
                {"BenchmarkHTTP": num[0][:-6]}
            )

        if i.startswith("BenchmarkJSON"):
            num = re.findall("\d+\.?\d* ns/op", i)
            data.get("default").get("golang").update(
                {"BenchmarkJSON": num[0][:-6]}
            )


def get_from_postgres():
    """postgres unit tests analysis"""
    pass


def get_from_nodejs():
    pass


if __name__ == '__main__':
    file_name = '0.logs'
    lines = read_logs(file_name)
    get_from_httpd(lines)
    get_from_nginx(lines)
    get_from_memcached(lines)
    get_from_redis(lines)
    get_from_php(lines)
    get_from_python(lines)
    get_from_golang(lines)
    pprint(data)
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)





# 找到一个唯一的位置，就可以匹配（第二方案）
    # start = 0
    # end = 0
    # for item in lines:
    #     if item.startswith("[php] [INFO] Test clear docker"):
    #         start = lines.index(item)
    #     if item.startswith("PHPBench   :"):
    #         end = lines.index(item)
    # for i in lines[start:end+8]:
    #     if i.startswith("Score"):
    #         num = re.findall("\d+\.?\d*", i)
    #         print(num)
    #         data.get("clear").get("php").update(
    #             {"Score": num[0]}
    #         )

# 万能大法（php）
#     start = 0
#     end_list = []
#     for item in lines:
#         if item.startswith("[php] [INFO] Test clear docker"):
#             start = lines.index(item)
#     for item in lines:
#         if re.findall(".*\/*\.sh", item) and lines.index(item) > start:
#             end_list.append(lines.index(item))
#     for i in lines[start:end_list[0]]:
#         if i.startswith("Score"):
#             num = re.findall("\d+\.?\d*", i)
#             data.get("clear").get("php").update(
#                 {"Score": num[0]}
#             )


# python 的万能打法
# def clr_from_python(lines):
#     start = 0
#     end_list = []
#     for item in lines:
#         if item.startswith("[python] [INFO] Test clear docker image"):
#             start = lines.index(item)
#     for item in lines:
#         if re.findall(".*\/*\.sh", item) and lines.index(item) > start:
#             end_list.append(lines.index(item))
#     for i in lines[start:end_list[0]]:
#         if i.startswith("Totals"):
#             num = re.findall("\d+\.?\d*", i)
#             num[0] = {"minimum": num[0]}
#             num[1] = {"average": num[1]}
#             data.get("clear").get("python").update(
#                 {"Totals": num}
#             )
