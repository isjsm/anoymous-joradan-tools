#!/usr/bin/env python3
import os
import sys
from pyfiglet import Figlet
from termcolor import colored
from .security import EthicalCheck
from ..modules import network, phishing, vuln_scan, wireless
from ..utils.logger import Logger

class CLI:
    def __init__(self):
        self.tools = {
            "01": {"name": "Network Scanner", "func": network.NetworkScanner.scan},
            "02": {"name": "Vulnerability Scanner", "func": vuln_scan.VulnerabilityScanner.scan},
            "03": {"name": "Phishing Simulator", "func": phishing.PhishingSimulator.run},
            "04": {"name": "Wireless Network Analyzer", "func": wireless.WirelessScanner.scan_networks},
            "99": {"name": "Exit", "func": self.exit_tool}
        }
        self.logger = Logger(__name__)
        self.check_ethics()

    def check_ethics(self):
        """التأكد من الموافقة على الاستخدام التعليمي"""
        print(colored("\n[!] WARNING: This tool is for educational purposes only.", "red", attrs=["bold"]))
        agreement = input("Do you agree to use this tool responsibly? [y/N]: ")
        if agreement.lower() != 'y':
            sys.exit("Exiting...")

    def show_banner(self):
        """عرض الـ Banner باستخدام Figlet و Echo"""
        os.system("clear")
        f = Figlet(font='slant')
        banner = f.renderText('Anoymous Jordan')
        print(colored(banner, "green"))
        print(colored("Version 2.0 | STRICTLY FOR EDUCATIONAL PURPOSES\n", "yellow"))

    def show_menu(self):
        """عرض القائمة الرئيسية"""
        print(colored("[*] Main Menu:", "cyan"))
        for key, tool in self.tools.items():
            print(f"[{key}] {tool['name']}")
        print()

    def run(self):
        """تشغيل الواجهة التفاعلية"""
        while True:
            self.show_banner()
            self.show_menu()
            choice = input(colored("[?] Select an option: ", "blue"))
            if choice in self.tools:
                self.execute_tool(choice)
            else:
                print(colored("[-] Invalid option. Please try again.", "red"))

    def execute_tool(self, choice):
        """تنفيذ الأداة المختارة"""
        tool = self.tools[choice]
        if choice == "99":
            tool["func"]()
        elif choice == "01":
            target = input(colored("[?] Enter target (e.g., 192.168.1.0/24): ", "blue"))
            tool["func"](target)
        elif choice == "02":
            url = input(colored("[?] Enter target URL: ", "blue"))
            tool["func"](url)
        elif choice == "03":
            template = input(colored("[?] Choose template (facebook/gmail): ", "blue"))
            port = input(colored("[?] Enter port (default: 443): ", "blue")) or 443
            tool["func"](template, int(port))
        elif choice == "04":
            interface = input(colored("[?] Enter wireless interface (default: wlan0): ", "blue")) or "wlan0"
            tool["func"](interface)

    def exit_tool(self):
        """إنهاء البرنامج"""
        print(colored("[*] Exiting AnoymousJordan Toolkit...", "green"))
        sys.exit(0)
