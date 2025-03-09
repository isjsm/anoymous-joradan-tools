import requests
from bs4 import BeautifulSoup
from ..utils.logger import Logger
from sqlmapapi import SQLMapAPI

class VulnerabilityScanner:
    def __init__(self):
        self.sqlmap_api = SQLMapAPI()
        self.logger = Logger(__name__)

    def scan_sql_injection(self, url):
        """فحص متقدم لثغرات SQL Injection"""
        try:
            # فحص أولي مع requests
            response = requests.get(url + "'")
            if "SQL syntax" in response.text:
                self.logger.warning(f"SQLi Vulnerability detected in {url}")

            # فحص متقدم مع SQLMap API
            task_id = self.sqlmap_api.start_scan(url)
            if self.sqlmap_api.get_status(task_id)['vulnerable']:
                self.logger.critical(f"Confirmed SQLi via SQLMap: {url}")

        except Exception as e:
            self.logger.error(f"SQLi Scan Error: {str(e)}")
