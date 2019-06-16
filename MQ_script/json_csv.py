import json
import csv


def read_logs():
    with open(path, "a+") as f:
        csv_write = csv.writer(f)
        csv.writer.writerow(file_name)


if __name__ == '__main__':
    path = "C:\\Users\\xinhuizx\\python_Code\\MQ_scr"
    file_name = "C:\\Users\\xinhuizx\\python_Code\\MQ_scr\\2019-06-10\\json\\status\\1560175612.json"
