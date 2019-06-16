import sys
from pprint import pprint

data = {
    "default": {
        "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {}, "node": {}
    },

    "clear": {
        "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {}, "node": {}
    },

    "status_def": {
        "golang": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "node": {}
    },

    "ststus_Clr": {
        "golang": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "node": {}
    }
}


def get_golang_size(key):
    status_file_name = "clr_status.logs"
    case_list = [key, "clearlinux/%s" % key, "default", "clearlinux"]

    # f = open(status_file_name, 'r')
    # lines = f.readlines()
    part_lines = []

    with open(status_file_name, encoding='utf-8', ) as txtfile:
        lines = txtfile.readlines()
        for lineno, line in enumerate(lines):
            # print(str(lineno) + "--->" + line)
            if key in line and line.split()[0] == key:
                key_lineno = lineno
                for index in range(key_lineno, key_lineno + 20):
                    print(lines[index])
                    part_lines.append(lines[index])
                    if lines[index].startswith("\n"):
                        break

    for line in part_lines:
        # print(line)
        for case in case_list:
            # print(case)
            if line.startswith(case):
                line_split = line.split()
                # print(line_split)
                if line_split[1] == "latest":
                    if line_split[0] == key:
                        data.get("status_def")[key].update({
                            key: line_split[-1][0:3]
                        })
                    if line_split[0] == "clearlinux/%s" % key:
                        data.get("ststus_Clr")[key].update({
                            "clearlinux/%s" % key: line_split[-1][0:3]
                        })

                if line_split[-3] == "Size:":
                    if line_split[0] == "default":
                        data.get("status_def")[key].update({
                            "default base layer Size": line_split[-2]
                        })
                        data.get("status_def")[key].update({
                            "default microservice layer Size": line_split[-2]
                        })
                    if line_split[0] == "clearlinux":
                        data.get("ststus_Clr")[key].update({
                            "clearlinux base layer Size": line_split[-2]
                        })
                        data.get("ststus_Clr")[key].update({
                            "clearlinux microservice layer Size": line_split[-2]
                        })


if __name__ == '__main__':
    case_list = ["golang", "nginx", "memcached", "redis", "php", "python", "node"]
    for case in case_list:
        get_golang_size(case)
    pprint(data)
