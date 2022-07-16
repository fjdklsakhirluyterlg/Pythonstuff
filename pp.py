import subprocess
import platform
import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("py terminal [Version 1.0 BETA]")
while True:
    code = input(">>>")
    if code == "ping":
        host = input("Enter website to ping:")
        num = input("how many times to ping:")
        
        
        def ping(host):
            param = '-c'
            command = ['ping', param, num, host]
            return subprocess.call(command)
        print(ping(host))