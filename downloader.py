#!/usr/bin/env python

import urllib.request
import os
import time 

print("This will be a lengthy process")
print("It may take around over 1 gb of data so be aware")
time.sleep(3)

print("SCRIPT STARTING IN 5 SECS")
time.sleep(1)
print("SCRIPT STARTING IN 4 SECS")
time.sleep(1)
print("SCRIPT STARTING IN 3 SECS")
time.sleep(1)
print("SCRIPT STARTING IN 2 SECS")
time.sleep(1)
print("SCRIPT STARTING IN 1 SECS")
time.sleep(1)
print("CHECKING FOR ANY UPDATES")
os.system('apt full-upgrade -y')

print("Sytem is updated")
print("[*] Downloading SocialFish")

url = 'https://github.com/UndeadSec/SocialFish/archive/master.zip'
urllib.request.urlretrieve(url, 'SocialFish.zip')
file = 'SocialFish.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done downlaoding SocialFish")

print("[*] Downlaoding WiFite")
url = 'https://github.com/derv82/wifite/archive/master.zip'
urllib.request.urlretrieve(url, 'WiFite.zip')
file = 'WiFite.zip'

os.system('unzip ' + file)
os.system('rm '+ file)
print("[!] Done Downloading WiFite")

print("[*] Downloading WI-FI Phisher")
url = 'https://github.com/wifiphisher/wifiphisher/archive/master.zip'
urllib.request.urlretrieve(url, 'wifiphiser.zip')
file = 'wifiphiser.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading WiFiPhisher")

print("[*] Downloading Penertation-Testing-Framework")
url = 'https://github.com/veerupandey/Penetration-Testing-Toolkit/archive/master.zip'
urllib.request.urlretrieve(url, 'Penetration-Testing-Toolkit.zip')
file = 'Penetration-Testing-Toolkit.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downlaoding Penetration-Testing-Toolkit")

print("[*] Downloading Morpheus")
url = 'https://github.com/r00t-3xp10it/morpheus/archive/master.zip'
urllib.request.urlretrieve(url, 'morpheus.zip')
file = 'morpheus.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downlaoding Morpheus")

print("[*] Downlaoding Netool-toolkit")
url = 'https://github.com/r00t-3xp10it/netool-toolkit/archive/master.zip'
urllib.request.urlretrieve(url, 'netool-toolkit.zip')
file = 'netool-toolkit.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Netool-Toolkit")

print("[*] Downloading Hakku FrameWork")
url = 'https://github.com/4shadoww/hakkuframework/archive/master.zip'
urllib.request.urlretrieve(url, 'hakku-framework.zip')
file = 'hakku-framework.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Hakku Framework")

print("[*] Downloading Dracnmap")
url = 'https://github.com/Screetsec/Dracnmap/archive/master.zip'
urllib.request.urlretrieve(url, 'dracnmap.zip')
file = 'dracnmap.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Dracnmap")

print("[*] Downloading The Eye")
url = 'https://github.com/EgeBalci/The-Eye/archive/master.zip'
urllib.request.urlretrieve(url, 'The-Eye.zip')
file = 'The-Eye.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[*] Done Downloading The-Eye")

print("[*] Downloading Xerxes")
url = 'https://github.com/XCHADXFAQ77X/XERXES/archive/master.zip'
urllib.request.urlretrieve(url, 'xerxes.zip')
file = 'xerxes.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading xerxes")
print("[!] Done Setting up xerxes")

print("[*] Downloading Airgeddon")
url = 'https://github.com/v1s1t0r1sh3r3/airgeddon/archive/master.zip'
urllib.request.urlretrieve(url, 'airgeddon.zip')
file = 'airgeddon.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Airgeddon")

print("[*] Downloading Routersploit")
url = 'https://github.com/threat9/routersploit/archive/master.zip'
urllib.request.urlretrieve(url, 'routersploit.zip')
file = 'routersploit.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
os.system('apt-get install python3-pip ')
os.system('pip3 install future ')
os.system('pip3 install requests ')
os.system('pip3 install paramiko ')
os.system('pip3 install pysnmp ')
os.system('pip3 install pycryptodome ')
os.system('pip3 install future ')
os.system('pip3 install pycryptodome ')
os.system('pip3 install pytest ')
os.system('pip3 install pytest-forked ')
os.system('pip3 install pytest-xdist ')
os.system('pip3 install flake8 ')

print("[!] Done Downloading Routersploit")
print("[*] Adding Bluetooth Low Energy Support")

os.system('apt-get install libglib2.0-dev ')
os.system('python3 -m pip install bluepy ')

print("[!] Done Adding bluetooth low energy support")

print("[*] Downloading Eternal-Scanner")
url = 'https://github.com/peterpt/eternal_scanner/archive/master.zip'
urllib.request.urlretrieve(url, 'eternal-scanner.zip')
file = 'eternal-scanner.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
os.system('apt-get install masscan metasploit-framework wget python-pip python-crypto python-impacket python-pyasn1-modules netcat ')
os.system('pip install crypto && pip install impacket && pip install pyasn1-modules ')

print("[*] Done Downloading eternal-scanner")
print("[*] Done Setting up dependencies for eternal-scanner")

print("[*] Downloading Eaphammer")
url = 'https://github.com/s0lst1c3/eaphammer/archive/master.zip'
urllib.request.urlretrieve(url, 'eaphammer.zip')
file = 'eaphammer.zip'

os.system('unzip ' + file)
os.system('rm ' + file)

print("[*] Downloading VMR")
url = 'https://github.com/chunkingz/VMR-MDK-K2-2017R-012x4/archive/master.zip'
urllib.request.urlretrieve(url, 'VMR-MDK-K2.zip')
file = 'VMR-MDK-K2.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading VMR-MDK-K2")

print("[*] Downloading Wi-Fi Pumpkin")
url = 'https://github.com/P0cL4bs/WiFi-Pumpkin/archive/master.zip'
urllib.request.urlretrieve(url, 'wifi-pumpkin.zip')
file = 'wifi-pumpkin.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
os.system('cd wifi-pumpkin ')
os.system('./installer.sh --install ')
os.system('cd .. ')
print("[!] Done Downloading wifi-pumpkin")

print("[*] Downloading Gloom Framework")
url = 'https://github.com/StreetSec/Gloom-Framework/archive/master.zip'
urllib.request.urlretrieve(url, 'Gloom-Framework.zip')
file = 'Gloom-Framework.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print('[!] Done Downloading Gloom-Framework')

print("[*] Downloading secHub")
url = 'https://github.com/cys3c/secHub/archive/master.zip'
urllib.request.urlretrieve(url, 'secHub.zip')
file = 'secHub.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading secHub")

print("GOING FOR THE REMOTE ACCESS TOOLS")
time.sleep(2)
print("[*] Downloading BeeLogger")
url = 'https://github.com/4w4k3/BeeLogger/archive/master.zip'
urllib.request.urlretrieve(url, 'BeeLogger.zip')
file = 'BeeLogger.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading BeeLogger")

print("[*] Downloading Pupy")
url = 'https://github.com/n1nj4sec/pupy/archive/unstable.zip'
urllib.request.urlretrieve(url, 'pupy.zip')
file = 'pupy.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Pupy")

print("[*] Downloading TheFatRat")
url = 'https://github.com/Screetsec/TheFatRat/archive/master.zip'
urllib.request.urlretrieve(url, 'TheFatRat.zip')
file = 'TheFatRat.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downlaoding TheFatRat")

print("[*] Downloading Empire")
url = 'https://github.com/EmpireProject/Empire/archive/master.zip'
urllib.request.urlretrieve(url, 'Empire.zip')
file = 'Empire.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Empire")

print("[*] Downlaoding Dr0p1t-Framework")
url = 'https://github.com/D4Vinci/Dr0p1t-Framework/archive/master.zip'
urllib.request.urlretrieve(url, 'Dr0p1t-Framework.zip')
file = 'Dr0p1t-Framework.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("INSTALLING SERVER REQUIRMENTS")
time.sleep(1)
os.system('pip3 install flask ')
time.sleep(1)
print("[!] Done Downloading Dr0p1t-Framework")

print("[*] Downloading Veil-Framework")
os.system('apt install veil -y ')
os.system('apt full upgrade -y ')
time.sleep(2)
print("[!] Done Downloading Veil-Framework")

print("[*] Downloading Evil-Droid")
url = 'https://github.com/M4sc3r4n0/Evil-Droid/archive/master.zip'
urllib.request.urlretrieve(url, 'Evil-Droid')
file = 'Evil-Droid'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Evil-Droid")

print("[*] Downloading AutoSploit")
url = 'https://github.com/NullArray/AutoSploit/archive/master.zip'
urllib.request.urlretrieve(url, 'AutoSploit.zip')
file = 'AutoSploit.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
os.system('pip3 install requests ')
os.system('pip3 install psutil ')
os.system('pip3 install beautifulsoup4 ')
print("[!] Done Downloading AutoSploit")

print("STARTING INFORMATION GATHERING TOOLS")
time.sleep(2)
print("[*] Downloading Sn1per")
url = 'https://github.com/1N3/Sn1per/archive/master.zip'
urllib.request.urlretrieve(url, 'Sn1per.zip')
file = 'Sn1per.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Sn1per")

print("[*] Downloading ReconDog")
url = 'https://github.com/s0md3v/ReconDog/archive/master.zip'
urllib.request.urlretrieve(url, 'ReconDog.zip')
file = 'ReconDog.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
os.system('pip3 install tld ')
os.system('pip3 install requests ')
print("[!] Done Downloading ReconDog")

print("[*] Downloading Infoga")
url = 'https://github.com/m4ll0k/Infoga/archive/master.zip'
urllib.request.urlretrieve(url, 'Infoga.zip')
file = 'Infoga.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Infoga")

print("[*] Downloading KonckMail")
url = 'https://github.com/4w4k3/KnockMail/archive/master.zip'
urllib.request.urlretrieve(url, 'KnockMail.zip')
file = 'KnockMail.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
os.system('pip3 install validate_email ')
os.system('pip install pyDNS ')
print("[!] Done Downloading KnockMail")

print("[*] Downloading Operative-Framework")
url = 'https://github.com/graniet/operative-framework/archive/master.zip'
urllib.request.urlretrieve(url, 'operative-framework.zip')
file = 'operative-framework.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downlaoding Operative-Framework")

print("[*] Downloading Striker")
url = 'https://github.com/s0md3v/Striker/archive/master.zip'
urllib.request.urlretrieve(url, 'Striker.zip')
file = 'Striker.zip'

os.system('unzip ' + file)
os.system('rm ' + file)
print("[!] Done Downloading Striker")

time.sleep(3)
print("[*] Download Finished" , "All tools are now downloaded")
