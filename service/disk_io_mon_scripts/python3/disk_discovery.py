#/usr/bin/python
#This script is used to discovery disk on the server
import subprocess
import json
import sys
#V_DISK = sys.argv[1]
#v_sta = sys.argv[2]
sta = ['rrqm','wrqm','rps','wps','rKBps','wKBps','avgrq-sz','avgqu-sz','await','r_await','w_await','svctm','util']
args="cat /proc/diskstats |grep -E '\ssd[a-z]\s|\sxvd[a-z]\s|\svd[a-z]\s'|awk '{print $3}'|sort|uniq 2>/dev/null"
t = subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0]
 
disks=[]
 
for disk in t.split('\n'):
    if len(disk) != 0:
       disks.append({'{#DISK_NAME}':disk})
print json.dumps({'data':disks},indent=4,separators=(',',':'))
#print(disks)
#for Disks in disks:
#	for key,value in Disks.items():
#		print(value)
#		if V_DISK in value:
#			if v_sta in sta:
#				print(sta.index(v_sta))
#				a = sta.index(v_sta) + 2
#				arg = "iostat -dxkt |grep '%s' |tail -1|awk '{print $%s}'" %(value,a)
#				s = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE).communicate()[0]
#				print(s.split("\n")[0])
#for Sta in sta:
#	print(Sta)
