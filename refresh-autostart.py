#!/bin/env python3
from os import listdir, popen
directory=popen("echo $HOME").read().strip()+"/.config/"
files=listdir(directory+"autostart/")
result=""
for filename in files:
    with open(directory+"autostart/"+filename,"r",encoding="UTF-8") as file:
        for line in file.readlines():
            if line[:5]=="Exec=": 
                result+="exec "+line[5:]
                break
with open(directory+"i3/startup-apps","w") as file: file.write(result)
