import nmap
from scapy.all import ARP, Ether, srp
from ..utils.logger import Logger

class NetworkScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.logger = Logger(__name__)

    @staticmethod
    def scan(target):
        """فحص شامل للشبكة باستخدام nmap و scapy"""
        try:
            # فحص ARP مع Scapy
            arp = ARP(pdst=target)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether/arp
            result = srp(packet, timeout=2, verbose=0)[0]

            # عرض النتائج
            print("الأجهزة النشطة:")
            for sent, received in result:
                print(f"IP: {received.psrc} | MAC: {received.hwsrc}")

            # فحص منافذ مع Nmap
            print("\nفحص المنافذ:")
            nm = nmap.PortScanner()
            nm.scan(hosts=target, arguments='-p 1-1000 -sV')
            for host in nm.all_hosts():
                print(f"Host : {host}")
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in ports:
                        print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

        except Exception as e:
            Logger.error(f"خطأ في فحص الشبكة: {str(e)}")
