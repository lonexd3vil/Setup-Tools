#!/bin/bash 

echo "Volla you finally found it. You really wanna continue?"

read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Enter Your Choice: \e[0m\en' CHOICE

if [ "$CHOICE" = "yes" ];

then 
sleep 1 && clear

    echo "Initiating Downloads"
    sleep 1 && clear
    apt update
    apt upgrade -y
    apt full-upgrade -y

    sleep 1

    echo "[!] Downloading HumenError"
    curl -L -o humen-error.zip https://github.com/samadbloch/HumenError/archive/master.zip
    unzip humen-error
    rm humen-error.zip
    echo "[!] Done Downliading HumenError"

    echo "[!] Downloading SocialFish"
    curl -L -o SocialFish.zip https://github.com/UndeadSec/SocialFish/archive/master.zip
    unzip SocialFish
    rm SocialFish.zip
    echo "[!] Done Downlaoding SocialFish"
    sleep 1
    echo "[*] Downlaoding WiFite"
    curl -L -o WiFite.zip https://github.com/derv82/wifite/archive/master.zip
    unzip WiFite
    rm WiFite.zip
    echo "[!] Done Downloading WiFite"
    sleep 1
    echo "[*] Downloading WI-FI Phisher"
    curl -L -o WiFi-Phisher.zip https://github.com/wifiphisher/wifiphisher/archive/master.zip
    unzip WiFi-Phisher
    rm WiFi-Phisher.zip
    echo "[!] Done Downloading WiFi-Phisher"
    sleep 1
    echo "[!] Downloading Penetration-Testing Framework"
    curl -L -o penetration-testing-framework.zip https://github.com/veerupandey/Penetration-Testing-Toolkit/archive/master.zip
    unzip penetration-testing-framework
    rm penetration-testing-framework.zip
    echo "[!] Done Downloading Penetration Testing Frmawork"
    sleep 1
    echo "[!] Downloading Morpheus"
    curl -L -o morpheus.zip https://github.com/r00t-3xp10it/morpheus/archive/master.zip
    unzip morpheus
    rm morpheus.zip
    echo "[!] Done Downloading Morpheus"
    sleep 1
    echo "[!] Downloading Netool-Toolkit"
    curl -L -o netool-toolkit https://github.com/r00t-3xp10it/netool-toolkit/archive/master.zip
    unzip netool-toolkit 
    rm netool-toolkit.zip
    echo "[!] Done Downloading Netool-Toolkit"
    sleep 1
    echo "[!] Downloading Hakku Framework"
    curl -L -o hakku.zip https://github.com/4shadoww/hakkuframework/archive/master.zip
    unzip hakku
    rm hakku.zip
    echo "[!] Done Downloading Hakku-Framework"
    sleep 1
    echo "[!] Downloading Dracnmap"
    curl -L -o dracnmap.zip https://github.com/Screetsec/Dracnmap/archive/master.zip
    unzip dracnmap
    rm dracnmap.zip
    echo "[!] Done Downloading Dracnmap"
    sleep 1
    echo "[!] Downloading The-Eye"
    curl -L -o the-eye.zip https://github.com/EgeBalci/The-Eye/archive/master.zip
    unzip the-eye 
    rm the-eye.zip 
    echo "[!] Done Downloading The-Eye"
    sleep 1
    echo "[!] Downlaoding Xerxes"
    curl -L -o xerxes.zip https://github.com/XCHADXFAQ77X/XERXES/archive/master.zip
    unzip xerxes
    rm xerxes.zip
    echo "[!] Done Downloading Xerxes"
    sleep 1
    echo "[!] Downloading Airgeddon"
    curl -L -o airgeddon.zip https://github.com/v1s1t0r1sh3r3/airgeddon/archive/master.zip
    unzip airgeddon
    rm airgeddon.zip
    echo "[!] Done Downloading Airgeddon"
    sleep 1
    echo "[!] Downloading Routersploit"
    curl -L -o routersploit.zip https://github.com/threat9/routersploit/archive/master.zip
    unzip routersploit
    rm routersploit.zip
    echo "[!] Done Downloading Routersploit"
    echo "[!] Setting up RouterSploit Dependencies"
    sleep 1
    pip install future
    pip install requests 
    pip install paramiko 
    pip install pysnmp 
    pip install pycryptodome 
    pip install pytest 
    pip install pytest-forked
    pip install pytest-xdist
    pip install flake8 
    echo "[!] Done Downloading Dependencies For RouterSploit"
    sleep 1
    echo "[*] Adding Bluetooth Low Energy Support"
    apt-get install libglib2.0-dev
    python3 -m pip install bluepy
    echo "[!] Done Adding bluetooth low energy support"
    sleep 1
    echo "[!] Downloading Eternal-Scanner"
    curl -L -o eternal-scanner.zip https://github.com/peterpt/eternal_scanner/archive/master.zip
    unzip eternal-scanner
    rm eternal-scanner.zip
    sleep 1
    echo "[*] Setting up Eternal-Scanner"
    apt-get install masscan metasploit-framework wget python-pip python-crypto python-impacket python-pyasn1-modules netcat
    pip install crypto && pip install impacket && pip install pyasn1-modules
    echo "[!] Done Downloading eternal-scanner"
    sleep 1
    echo "[!] Downloading Eaphammer"
    curl -L -o eaphammer.zip https://github.com/s0lst1c3/eaphammer/archive/master.zip
    unzip eaphammer
    rm eaphammer.zip
    echo "[!] Done Downloading Eaphommer"
    sleep 1
    echo "[!] Downloading VMR"
    curl -L -o vmr.zip https://github.com/chunkingz/VMR-MDK-K2-2017R-012x4/archive/master.zip
    unzip vmr 
    rm vmr.zip 
    echo "[!] Done Downloading VMR"
    sleep 1
    echo "[!] Downloading Wi-Fi Pumpkin"
    curl -L -o wifi-pumpkin.zip https://github.com/P0cL4bs/WiFi-Pumpkin/archive/master.zip
    unzip wifi-pumpkin
    rm wifi-pumpkin.zip
    echo "[!] Done Downloading Wi-Fi Pumpkin"
    sleep 1
    echo "[!] Downloading Gloom-Framework"
    curl -L -o gloom.zip https://github.com/StreetSec/Gloom-Framework/archive/master.zip
    unzip gloom
    rm gloom.zip
    echo "[!] Done Downloading Gloom-Framework"
    sleep 1
    echo "[!] Downloading SecHub"
    curl -L -o sechub.zip https://github.com/cys3c/secHub/archive/master.zip
    unzip sechub 
    rm sechub.zip
    echo "[!] Done Downloading SecHub"
    sleep 1
    echo "[!] Downloading BeeLoger"
    curl -L -o beeloger.zip https://github.com/4w4k3/BeeLogger/archive/master.zip
    unzip beeloger 
    rm beeloger.zip
    echo "[!] Done Downloading BeeLoger"
    sleep 1
    echo "[!] Downloading Pupy"
    curl -L -o pupy.zip https://github.com/n1nj4sec/pupy/archive/unstable.zip
    unzip pupy 
    rm pupy.zip
    echo "[!] Done Downloading Pupy"
    sleep 1
    echo "[!] Downloading TheFatRat"
    curl -L -o fatrat.zip https://github.com/Screetsec/TheFatRat/archive/master.zip
    unzip fatrat
    rm fatrat.zip
    echo "[!] Done Downloading TheFatRat"
    sleep 1
    echo "[!] Downloading Empire"
    curl -L -o empire.zip https://github.com/EmpireProject/Empire/archive/master.zip
    unzip empire 
    rm empire.zip
    echo "[!] Done Downloading Empire"
    sleep 1
    echo "[!] Downloading Dr0p1t-Framework"
    curl -L -o dr0p1t-framework.zip https://github.com/D4Vinci/Dr0p1t-Framework/archive/master.zip
    unzip dr0p1t-framework
    rm dr0p1t-framework.zip
    pip install flask
    echo "[!] Done Downloading Dr0p1t-Framework"
    sleep 1
    echo "[!] Downloading Veil-Framework"
    apt update 
    apt upgrade
    apt install veil -y 
    echo "[!] Done Downloading Veil Framework"
    sleep 1
    echo "[!] Downloading Evil-Droid"
    curl -L -o evil-droid.zip https://github.com/M4sc3r4n0/Evil-Droid/archive/master.zip
    unzip evil-droid
    rm evil-droid.zip
    echo "[!] Done Downloading Evil-Droid"
    sleep 1
    echo "[!] Downloading AutoSploit"
    curl -L -o autosploit.zip https://github.com/NullArray/AutoSploit/archive/master.zip
    unzip autosploit
    rm autosploit.zip
    pip install psutil 
    pip install beautifulsoup4 
    echo "[!] Done Downloading AutoSploit"
    sleep 1
    echo "[!] Downloading Sn1per"
    curl -L -o sniper.zip https://github.com/1N3/Sn1per/archive/master.zip
    unzip sniper 
    rm sniper.zip 
    echo "[!] Done Downloading Sn1per"
    sleep 1
    echo "[!] Downloading Recon-Dog"
    curl -L -o recon-dog.zip https://github.com/s0md3v/ReconDog/archive/master.zip
    unzip recon-dog
    rm recon-dog.zip
    pip install tld 
    echo "[!] Done Downloading Recon-Dog"
    sleep 1
    echo "[!] Downloading Infoga"
    curl -L -o infoga.zip https://github.com/m4ll0k/Infoga/archive/master.zip
    unzip infoga 
    rm infoga.zip 
    echo "[!] Done Downloading Infoga"
    sleep 1
    echo "[!] Downloading KnockMail"
    curl -L -o knockmail.zip https://github.com/4w4k3/KnockMail/archive/master.zip
    unzip knockmail
    rm knockmail.zip
    pip install validate_email 
    pip install pyDNS
    echo "[!] Done Downloading KnockMail"
    sleep 1
    echo "[!] Downloading Operative-Framework"
    curl -L -o or.zip https://github.com/graniet/operative-framework/archive/master.zip
    unzip or 
    rm or.zip 
    echo "[!] Done Downloading Operative-Framework"
    sleep 1
    echo "[!] Downloading Striker"
    curl -L -o striker.zip https://github.com/s0md3v/Striker/archive/master.zip
    unzip striker 
    rm striker.zip
    echo "[!] Done Downloading Striker"
    sleep 2
    echo "[*] Done Downloading All Tools."

else 
    echo ""
    echo $'\n\e[1;92m\e[0m\e[1;77m\e[0m\e[1;92m See ya later then \e[0m\en'
fi