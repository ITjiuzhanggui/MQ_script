
import re

a = ["redis/redis.sh"]

for i in a:
    if re.findall(".*\/*\.sh",i):
        print(1)
