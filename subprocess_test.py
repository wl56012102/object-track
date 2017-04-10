import subprocess
import time

f = subprocess.Popen(["opentld","-d","CAM"],stdout=subprocess.PIPE)
while True:
    line = f.stdout.readlines()
    if not line: break
    for a in line:
        print(a)
#rc = superprocess.Popen(["opentld","-d","CAM"],bufsize=0)

#while True:
 #   line = rc.stdout.readline()
  #  time.sleep(1)
   # if not line: break

#    print line
