import os
import subprocess

# use subprocess to check the process id based on the process name
getPID = subprocess.Popen("ps aux | pgrep gst-launch-1.0", shell=True, stdout=subprocess.PIPE).stdout
pid = getPID.read()
print("My process id is", pid.decode())

if pid.decode() is "":
    print("No Process running")
else:
    # use system command to kill the process
    os.system('kill -9 %s' % pid.decode())

