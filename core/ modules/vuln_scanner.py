# modules/vuln_scanner.py
import requests

class VulnerabilityScanner:
    def scan_sql_injection(self, url):
        # محاكاة فحص SQL Injection
        try:
            payload = "' OR 1=1--"
            response = requests.get(f"{url}?id={payload}")
            if "error" in response.text.lower():
                print(f"[!] SQL Injection vulnerability detected in {url}")
        except:
            print("[-] Connection error")
