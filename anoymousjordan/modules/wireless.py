import os
from scapy.all import *
from ..utils.logger import Logger

class WirelessScanner:
    def __init__(self, interface='wlan0'):
        self.interface = interface
        self.logger = Logger(__name__)

    def scan_networks(self):
        print("[*] جاري فحص الشبكات اللاسلكية...")
        networks = []
        def packet_handler(pkt):
            if pkt.haslayer(Dot11Beacon):
                ssid = pkt[Dot11Elt].info.decode()
                bssid = pkt[Dot11].addr2
                signal = -(256 - ord(pkt.notdecoded[-4:-3]))
                networks.append({
                    'SSID': ssid,
                    'BSSID': bssid,
                    'Signal': f"{signal} dBm"
                })
        sniff(iface=self.interface, prn=packet_handler, timeout=10)
        return networks

    def capture_handshake(self, target_bssid):
        print(f"[*] Capturing handshake for {target_bssid}")
        # كود متطور لالتقاط الـ handshake
        # يتطلب وضع الواجهة في وضع المراقبة
        os.system(f"airmon-ng start {self.interface}")
        os.system(f"airodump-ng -d {target_bssid} {self.interface}mon")
