

import os
import time
import re
A = '\x1b[1;97m'
A1 = '\x1b[38;5;196m'
A2 = '\x1b[1;33m'
A3 = '\x1b[1;96m'
A4 = '\x1b[38;5;8m'
A5 = '\x1b[38;5;48m'
A6 = '\x1b[38;5;47m'
A7 = '\x1b[38;5;49m'
A8 = '\x1b[38;5;50m'
A9 = '\x1b[1;34m'
A10 = '\x1b[38;5;14m'
A11 = '\x1b[38;5;123m'
A12 = '\x1b[38;5;122m'
A13 = '\x1b[38;5;86m'
A14 = '\x1b[38;5;121m'
A15 = '\x1b[38;5;205m'
A16 = '\x1b[1;92m\x1b[38;5;208m'
A17 = '\x1b[1;92m\x1b[38;5;209m'
A18 = '\x1b[1;92m\x1b[38;5;210m'
A19 = '\x1b[1;92m\x1b[38;5;211m'
A20 = '\x1b[1;92m\x1b[38;5;212m'
A21 = '\x1b[1;92m\x1b[38;5;46m'
A22 = '\x1b[1;92m\x1b[38;5;47m'
A23 = '\x1b[1;92m\x1b[38;5;48m'
A24 = '\x1b[1;92m\x1b[38;5;49m'
A25 = '\x1b[1;92m\x1b[38;5;50m'

def banner():
    os.system('clear')
    print('\n\x1b[38;5;46m\n\x1b[1;92m\x1b[38;5;59m██   ██ █████ABIR KHAN█ ████████  █████  ██\n\x1b[1;92m\x1b[38;5;47m██   ██ ██     ABIR KHAN   ██ ██\n\x1b[1;92m\x1b[38;5;210m███████ █████  ABIR KHAN██    ██    ███████ ██\n\x1b[1;92m\x1b[38;5;50m██   ██ ██      ██ ABIR KHAN█    ██    ██   ██ ██\n\x1b[1;92m\x1b[38;5;208m██   ██ ███ABIR KHAN█   ████    ██    ██   ██ ██ \n\n\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━')


def menu():
    os.system('clear')
    banner()
    print('\x1b[38;5;46m 【A】TERMUX BESIC SETUP ')
    print('\x1b[1;92m\x1b[38;5;208m 【00/X】EXIT  ')
    select = input('\x1b[1;92m\x1b[38;5;59m 【❯❯】CHOOSE ➤\x1b[1;92m\x1b[38;5;59m ')
    if select == 'A':
        BESIC()
        return None
    if None == '00':
        TESTING()
        return None


def BESIC():
    os.system('clear')
    banner()
    print('    [\x1b[1;91m■\x1b[0m□□□□□□□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;92m■■\x1b[0m□□□□□□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;93m■■■\x1b[0m□□□□□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;94m■■■■\x1b[0m□□□□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;95m■■■■■\x1b[0m□□□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;96m■■■■■■\x1b[0m□□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;92m\x1b[38;5;210m■■■■■■■\x1b[0m□□□]')
    time.sleep(0.5)
    print('    [\x1b[1;92m\x1b[38;5;208m■■■■■■■■\x1b[0m□□]')
    time.sleep(0.5)
    print('    [\x1b[1;92m\x1b[38;5;209m■■■■■■■■■\x1b[0m□]')
    time.sleep(0.5)
    print('    [\x1b[1;97m■■■■■■■■■■\x1b[0m]')
    SETUP()


def SETUP():
    os.system('clear')
    banner()
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m ⪀')
    time.sleep(0.5)
    print('    【\x1b[1;92m\x1b[38;5;59m PKG\x1b[1;92m\x1b[38;5;59m UPDATE】')
    os.system('pkg update')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59m PKG\x1b[1;92m\x1b[38;5;59m UPGRADE ⪀')
    os.system('pkg upgrade')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m PYTHON ⪀')
    os.system('pkg install python -y')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m PYTHON2 ⪀')
    os.system('pkg install python2')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m PYTHON3 ⪀')
    os.system('pkg install python3')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m TMUX ⪀')
    os.system('apt install tmux')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m REQUESTS ⪀')
    os.system('pip install requests')
    os.system('pip2 install requests')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m PYCURL ⪀')
    os.system('pip install pycurl')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m MECHANIZE ⪀')
    os.system('pip install mechanize')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m BS4 ⪀')
    os.system('pip install bs4')
    os.system('pip2 install bs4')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m RICH ⪀')
    os.system('pip install rich')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m LOLCAT ⪀')
    os.system('gem install lolcat')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m PHP ⪀')
    os.system('pip install php')
    os.system('pip install lolcat')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m FETURES ⪀')
    os.system('pip install futures')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m espeak ⪀')
    os.system('pkg install espeak')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m HTTPX ⪀')
    os.system('pkg install httpx')
    os.system('pip install httpx')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m requests ⪀')
    os.system('pip install requests')
    print('    ⪀ \x1b[1;92m\x1b[38;5;59mINSTALLING\x1b[1;92m\x1b[38;5;59m fix-broken ⪀')
    os.system('apt --fix-broken install')
    print('⪀ \x1b[1;92m\x1b[38;5;47m━━━━━━━━━━━【=】 PKG UPDATE DONE 🤝🇧🇩💖【=】━━━━━━━━━━━━━━ ')

menu()
