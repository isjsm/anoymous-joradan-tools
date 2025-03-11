#!/usr/bin/env python3
import os
import subprocess
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

    def show_banner(self):
        f = Figlet(font='slant')
        print("\033[91m" + f.renderText('Anoymous Jordan') + "\033[0m")
        print("\033[93mInstaller Version 2.0 | EDUCATIONAL USE ONLY\033[0m\n")

    def install_packages(self):
        print("[*] Installing dependencies...")
        subprocess.run(['apt', 'update'], check=True)
        subprocess.run(['apt', 'install', '-y'] + self.packages, check=True)

    def setup_python(self):
        print("[*] Installing Python dependencies...")
        subprocess.run(['pip3', 'install', '-r', 'requirements.txt'], check=True)

    def create_directories(self):
        print("[*] Creating configuration directories...")
        os.makedirs(self.config_dir, exist_ok=True)
        subprocess.run(['cp', 'config/config.ini', self.config_dir], check=True)

    def finish(self):
        print("\n[*] Installation completed successfully!")
        print("[-] Run the tool using: sudo anoymousjordan")

    def run(self):
        self.show_banner()
        self.install_packages()
        self.setup_python()
        self.create_directories()
        self.finish()

if __name__ == '__main__':
    Installer().run()
