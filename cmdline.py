#ecoding:utf-8
import os
import re

def run(cmd):
    cmds=[]
    flag=False
    tmp=os.popen("busybox").read().splitlines()
    for i in range(len(tmp)):
        if tmp[i].strip().startswith("["):
            flag=True
        if flag:
            cmds+=tmp[i].split(",")
    for i in (range(len(cmds))):
        print()
        if cmds[i].startswith("\t"):
            cmds[i]=cmds[i][2:]
    if cmd:
        if cmd.split()[0] in cmds:
            return os.popen("busybox "+cmd).read()
        else:
            return os.popen(cmd).read()
    else:
        return ""

while True:
    cmd=input("cmdline>>>")
    if cmd =="exit":
        break
    result=run(cmd)
    print(result)