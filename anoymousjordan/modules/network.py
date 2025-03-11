import nmap
from scapy.all import ARP, Ether, srp
from ..utils.logger import Logger

class NetworkScanner:
    @staticmethod
    def scan(target):
        try:
            print(colored(f"[*] Scanning network: {target}", "cyan"))
            arp = ARP(pdst=target)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp
            result = srp(packet, timeout=2, verbose=0)[0]

            print(colored("\n[+] Live hosts:", "green"))
            for sent, received in result:
                print(f"IP: {received.psrc} | MAC: {received.hwsrc}")

            nm = nmap.PortScanner()
            nm.scan(hosts=target, arguments='-p 1-1000 -sV')
            print(colored("\n[+] Open ports:", "green"))
            for host in nm.all_hosts():
                print(f"Host: {host}")
                for proto in nm[host].all_protocols():
                    ports = nm[host][proto].keys()
                    for port in ports:
                        print(f"Port: {port}\tState: {nm[host][proto][port]['state']}")

        except Exception as e:
            Logger.error(f"Error during network scan: {str(e)}")
