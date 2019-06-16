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


def get_golang_status():
    status_file_name = "clr_status.logs"
    case_list = ["golang", "clearlinux/golang", "default", "clearlinux"]

    with open(status_file_name, 'r') as f:
        lines = f.readlines()
    part_lines = []
    for line in lines:

        part_lines.append(line)
        if line.startswith("\n"):
            break
    # print(part_lines)

    for line in part_lines:
        # print(line)
        for case in case_list:
            # print(case)
            if line.startswith(case):
                line_split = line.split()
                # print(line_split)
                if line_split[1] == "latest":
                    if line_split[0] == "golang":
                        data.get("status_def")["golang"].update({
                            "golang": line_split[-1][0:3]
                        })
                    if line_split[0] == "clearlinux/golang":
                        data.get("ststus_Clr")["golang"].update({
                            "clearlinux/golang": line_split[-1][0:3]
                        })

                if line_split[-3] == "Size:":
                    if line_split[0] == "default":
                        data.get("status_def")["golang"].update({
                            "default base layer Size": line_split[-2]
                        })
                        data.get("status_def")["golang"].update({
                            "default microservice layer Size": line_split[-2]
                        })
                    if line_split[0] == "clearlinux":
                        data.get("ststus_Clr")["golang"].update({
                            "clearlinux base layer Size": line_split[-2]
                        })
                        data.get("ststus_Clr")["golang"].update({
                            "clearlinux microservice layer Size": line_split[-2]
                        })


if __name__ == '__main__':
    get_golang_status()
    pprint(data)
