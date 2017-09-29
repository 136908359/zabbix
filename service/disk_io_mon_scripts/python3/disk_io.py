#!/usr/bin/env python
import sys
import psutil
import re

if len(sys.argv) < 3:
    sys.exit()

disk_name,disk_oper = sys.argv[1],sys.argv[2]
# sys.argv[1] = sda|sdb|...
# sys.argv[2] = read|write

def get_Diskinfo(diskName):
    r = r'%s'% diskName
    dstr = re.compile(r)

    disk = psutil.disk_io_counters(perdisk=True)
    io_dict = {}
    read_dict = {}
    write_dict = {}
#   io_dict = {"read":{}}

    for k,v in disk.items():
        if dstr.match(k):
                read_dict[diskName] = read_dict.get(diskName,0) + disk[k][0]
                write_dict[diskName] = write_dict.get(diskName,0) + disk[k][1]
                io_dict["read"] = read_dict
                io_dict["write"] = write_dict
                return io_dict # return {'read': {'sda': 417110}, 'write': {'sda': 173839}}

print(get_Diskinfo(disk_name)[disk_oper][disk_name])

