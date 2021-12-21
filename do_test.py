import subprocess
command=['python3', 'main.py', ]
try:
    res = subprocess.check_call(command)
except:
    print("localhost shutdown.")