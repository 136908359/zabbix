#!/usr/bin/env python
import re
import json

r = r"[s|v]d[a-z]$"
rstr = re.compile(r)

disk_list = []
disk_dict = {}

with open("/proc/partitions") as f:
    for line in f:
        if rstr.search(line):
                disk_list.append({"{#DISKNAME}":line.split()[-1:][0]})
disk_dict["data"] = disk_list
print json.dumps(disk_dict)

