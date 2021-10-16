import subprocess
command=['python', '-m', 'http.server', '8000']
try:
    res = subprocess.check_call(command)
except:
    print("localhost shutdown.")