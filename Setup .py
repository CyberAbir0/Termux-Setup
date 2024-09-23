from os import system as ALLMasTerx1001
import os
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred

bblack = "\033[1;30m"  # Black
M = "\033[1;31m"       # Red
H = "\033[1;32m"       # Green
Y = "\033[1;33m"       # Yellow
bblue = "\033[1;34m"   # Blue
P = "\033[1;35m"       # Purple
C = "\033[1;36m"       # Cyan
B = "\033[1;37m"       # White

my_color = [B, C, P, H]
warna = random.choice(my_color)

logo = ("""
              
  _________       __                
 /   _____/ _____/  |_ __ ________  
 \_____  \_/ __ \   __\  |  \____ \ 
 /        \  ___/|  | |  |  /  |_> >
/_______  /\___  >__| |____/|   __/ 
        \/     \/           |__|    
     
\033[1;33mo|-------------------------------------------------------------\033[1;33m|o
\033[1;33mo| \033[1;32mCODED BY : \033[1;33mAbir Khan                                \033[1;33m|o
\033[1;33mo| \033[1;32mGITHUB   : \033[1;33mCyberAbir01                                    \033[1;33m|o
\033[1;33mo| \033[1;32mFACEBOOK : \033[1;33mAbir Khan                                 \033[1;33m|o
\033[1;33mo| \033[1;32mTELEGRAM : \033[1;33mDHCFABIR                          \033[1;33m|o
\033[1;33mo|-------------------------------------------------------------\033[1;33m|o
""")

def linex():
    print('\033[1;33mo|-------------------------------------------------------------\033[1;33m|o')

def clear():
    os.system('clear')
    print(logo)

def install_package(package):
    print(f"Installing: {package}")
    ALLMasTerx1001(package)

def ARAFAT():
    clear()
    ALLMasTerx1001('xdg-openhttps://www.facebook.com/CyberAbir121')
    print(f'{B} [{warna}01{B}] \33[0;41mFULL SETUP\033[0;92m ')
    print(f'{B} [{warna}02{B}] \33[0;41mBASIC SETUP\033[0;92m ')
    print(f'{B} [{warna}03{B}] Facebook  ')
    print(f'{B} [{warna}00{B}] EXIT PROGRAM')
    linex()
    option = input(f' {B}[{warna}??{B}] CHOOSE OPTION>> ')
    
    if option in ['01', '1']:
        FULLSETUP()
    elif option in ['02', '2']:
        FULLSETUP()
    elif option in ['03', '3']:
        ALLMasTerx1001('xdg-open https://www.facebook.com/CyberAbir121')
    else:
        exit('WELCOME🙃!')

def FULLSETUP():
    clear()
    packages = [
        "pkg update -y", "pkg upgrade -y", "pkg install python -y", 
        "pkg install python2 -y", "pkg install python3 -y", "pkg install python-pip",
        "pkg install wget", "pkg install fish", "pkg install ruby", "pkg install help",
        "pkg install git", "pkg install dnsutils", "pkg install php", "pkg install perl",
        "pkg install lua", "pkg install parallel", "pkg install nmap", "pkg install bash",
        "pkg install clang", "pkg install nano", "pkg install w3m", "pkg install hydra",
        "pkg install figlet", "pkg install cowsay", "pkg install curl", "pkg install tar",
        "pkg install zip", "pkg install unzip", "pkg install net-tools", "pkg install tor -y",
        "pkg install sudo -y", "pkg install wireshark", "pkg install wgetrc", "pkg install wcalc",
        "pkg install openssl", "pkg install openssl-tool", "pkg install bmon", "pkg install vpn",
        "pkg install unrar", "pkg install toilet", "pkg install proot", "pkg install vim",
        "pkg install vim-python", "pkg install goaccess", "pkg install golang", "pkg install tmux",
        "pkg install mtools", "pkg install screen", "pkg install neofetch", "pkg install mariadb",
        "pkg install dropbear", "pkg install openssh", "pip2 install wget", "pip install bs4",
        "pip2 install bs4", "pip install requests", "pip2 install requests", "pip install mechanize",
        "pip2 install mechanize"
    ]

    with tred(max_workers=4) as executor:
        executor.map(install_package, packages)

ARAFAT ()