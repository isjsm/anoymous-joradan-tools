#!/usr/bin/env python3
import os
import sys
import subprocess
from getpass import getpass
from pyfiglet import Figlet

class Installer:
    def __init__(self):
        self.packages = [
            'python3', 'python3-pip', 'git',
            'nmap', 'aircrack-ng', 'sqlmap',
            'wireshark', 'flask', 'scapy',
            'python3-cryptography', 'openssl'
        ]
        self.requirements = ['requirements.txt']
        self.config_dir = '/etc/anoymousjordan'
        self.log_dir = '/var/log/anoymousjordan'

    def show_banner(self):
        f = Figlet(font='slant')
        print("\033[91m" + f.renderText('Anoymous Jordan') + "\033[0m")
        print("\033[93mInstaller Version 2.0 | EDUCATIONAL USE ONLY\033[0m\n")

    def check_root(self):
        if os.geteuid() != 0:
            sys.exit("الرجاء تشغيل التثبيت بصلاحية root: sudo python3 install.py")

    def install_packages(self):
        print("[*] Updating system...")
        subprocess.run(['apt', 'update'], check=True)
        print("[*] Installing dependencies...")
        subprocess.run(['apt', 'install', '-y'] + self.packages, check=True)

    def setup_python(self):
        print("[*] Installing Python dependencies...")
        subprocess.run(['pip3', 'install', '-r', 'requirements.txt'], check=True)

    def create_directories(self):
        print("[*] Creating configuration directories...")
        os.makedirs(self.config_dir, exist_ok=True)
        os.makedirs(self.log_dir, exist_ok=True)
        subprocess.run(['cp', 'config/config.ini', self.config_dir], check=True)

    def setup_autocomplete(self):
        print("[*] Enabling command autocompletion...")
        with open('/etc/bash_completion.d/anoymousjordan', 'w') as f:
            f.write('_anoymousjordan()\n{\n  local cur\n  COMPREPLY=()\n  cur="${COMP_WORDS[COMP_CWORD]}"\n  commands="scan vuln phish wifi help"\n  COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )\n}\ncomplete -F _anoymousjordan anoymousjordan')

    def finish(self):
        print("\n[*] التثبيت اكتمل بنجاح!")
        print("[-] الأوامر المتاحة:")
        print("    anoymousjordan scan -t 192.168.1.0/24")
        print("    anoymousjordan phish --template facebook")
        print("    anoymousjordan vuln -u http://example.com")

    def run(self):
        self.show_banner()
        self.check_root()
        self.install_packages()
        self.setup_python()
        self.create_directories()
        self.setup_autocomplete()
        self.finish()

if __name__ == '__main__':
    try:
        Installer().run()
    except subprocess.CalledProcessError as e:
        sys.exit(f"[-] خطأ في التثبيت: {e}")
    except KeyboardInterrupt:
        sys.exit("\n[i] التثبيت ملغى")
