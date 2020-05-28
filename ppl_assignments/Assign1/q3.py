# Run this script as root 

import time 
from datetime import datetime as dt 

# change hosts path according to your OS 
hosts_path = "/etc/hosts"
# localhost's IP 
redirect = "127.0.0.1"

option = int(input("1.Block\n2.Unblock\n"))
def block():
    website = input("Enter website to be blocked:")
    with open(hosts_path, 'r+') as file: 
        content = file.read() 
        if website in content:
            pass
        else:
            file.write(redirect + " " + website + "\n") 
    print("Website blocked")

def unblock(): 
    website = input("Enter website to be unblocked:")
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website):
                file.write(line)
        file.truncate()
    print("Website unblocked")

if option == 1:
    block()
if option == 2:
    unblock()

