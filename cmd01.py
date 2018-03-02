import sys
import subprocess  

while True:
    p1 = subprocess.Popen("sh",stdin=subprocess.PIPE,stdout=sys.stdout,stderr=sys.stderr)
    cmd=input("$>")
    if cmd == "exit":break
    out,error=p1.communicate(cmd.encode())   
    print(out)