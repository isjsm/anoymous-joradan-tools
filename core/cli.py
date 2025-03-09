import os
import sys
import argparse
from pyfiglet import Figlet
from .security import EthicalCheck
from ..modules import network, phishing, vuln_scan, wireless
from ..utils.logger import Logger

class CLI:
    def __init__(self):
        self.check_ethics()
        self.setup_logger()
        self.parser = argparse.ArgumentParser(
            description="AnoymousJordan Security Toolkit | FOR EDUCATIONAL PURPOSES ONLY"
        )
        self.setup_arguments()
        self.show_banner()

    def check_ethics(self):
        """التأكد من الموافقة على الاستخدام التعليمي"""
        agreement = input("هل توافق على استخدام هذه الأداة للأغراض التعليمية فقط؟ [نعم/لا]: ")
        if agreement.lower() != 'نعم':
            sys.exit("الخروج...")

    def show_banner(self):
        """عرض الـ Banner باستخدام Figlet"""
        f = Figlet(font='slant')
        print("\033[91m" + f.renderText('Anoymous Jordan') + "\033[0m")
        print("\033[93mToolkit Version 2.0 | STRICTLY EDUCATIONAL\033[0m\n")

    def setup_arguments(self):
        """تعريف أوامر سطر الأوامر"""
        subparsers = self.parser.add_subparsers(dest='command')

        # فحص الشبكات
        network_parser = subparsers.add_parser('scan', help='فحص الشبكات')
        network_parser.add_argument('-t', '--target', required=True, help='الهدف (مثال: 192.168.1.0/24)')

        # كشف الثغرات
        vuln_parser = subparsers.add_parser('vuln', help='كشف الثغرات')
        vuln_parser.add_argument('-u', '--url', required=True, help='رابط الموقع')

        # الهندسة الاجتماعية
        phish_parser = subparsers.add_parser('phish', help='محاكاة هجوم تصيد')
        phish_parser.add_argument('--template', choices=['facebook', 'gmail'], required=True)

        # أمن لاسلكي
        wireless_parser = subparsers.add_parser('wifi', help='تحليل الشبكات اللاسلكية')
        wireless_parser.add_argument('-i', '--interface', default='wlan0', help='واجهة الشبكة')

    def run(self):
        args = self.parser.parse_args()
        if args.command == 'scan':
            network.NetworkScanner.scan(args.target)
        elif args.command == 'vuln':
            vuln_scan.VulnerabilityScanner.scan(args.url)
        # ... إكمال باقي الأوامر
