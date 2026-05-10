import socket
import os
import sys
from datetime import datetime
import pyfiglet

banner = pyfiglet.figlet_format("PORT_SCANNER")
print(banner)
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid ammount of Argument")

print("_"*50)
print("Scanning target: "+target)
print("Scanning started at: "+str(datetime.now()))
print("_"*50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        results = s.connect_ex((target,port))
        if results == 0 :
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Exiting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be solved")
    sys.exit()
except socket.error:
    print("Server not responding")
    sys.exit()
