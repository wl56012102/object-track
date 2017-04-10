import subprocess
import time

#p=subprocess.Popen(["ping","-c4","127.0.0.1"],stdout=subprocess.PIPE)
p=subprocess.Popen(["opentld","-d","CAM"],stdout=subprocess.PIPE)
returncode = p.poll()
while returncode ==None:
    line = p.stdout.readline()
    returncode=p.poll()
    line=line.strip()
    print line

print 'return code:',returncode