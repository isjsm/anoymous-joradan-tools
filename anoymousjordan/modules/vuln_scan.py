import requests
from bs4 import BeautifulSoup
from sqlmapapi import SQLMapAPI
from ..utils.logger import Logger

class VulnerabilityScanner:
    def __init__(self):
        self.sqlmap_api = SQLMapAPI('http://127.0.0.1:8775')
        self.logger = Logger(__name__)

    def check_sqli(self, url):
        try:
            # فحص أولي باستخدام طلب معدل
            payload = "' OR 1=1--"
            response = requests.get(f"{url}{payload}")
            if "error" in response.text.lower():
                self.logger.warning(f"SQLi Vulnerability detected in {url}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"SQLi Check Error: {e}")
            return False

    def full_scan(self, url):
        task_id = self.sqlmap_api.create_task()
        self.sqlmap_api.set_option(task_id, {'url': url})
        self.sqlmap_api.start_task(task_id)
        
        # تتبع حالة الفحص
        while True:
            status = self.sqlmap_api.get_status(task_id)
            if status['status'] == 'terminated':
                results = self.sqlmap_api.get_results(task_id)
                self.sqlmap_api.delete_task(task_id)
                return results
