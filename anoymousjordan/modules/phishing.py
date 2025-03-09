from flask import Flask, request, render_template
from ..utils.encryption import AESEncryptor
from ..utils.logger import Logger
import os

class PhishingSimulator:
    def __init__(self):
        self.app = Flask(__name__)
        self.encryptor = AESEncryptor(os.getenv('SECRET_KEY', 'default_key'))
        self.logger = Logger(__name__)

    def setup_routes(self):
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                # تشفير بيانات الاعتماد فورًا
                credentials = {
                    'username': request.form['username'],
                    'password': self.encryptor.encrypt(request.form['password'])
                }
                self.logger.warning(f"Credentials captured: {credentials}")
                return render_template('success.html')
            return render_template('login.html')

    def run_server(self, port=5000):
        """تشغيل خادم الويب مع تقييد الوصول"""
        try:
            self.setup_routes()
            self.app.run(host='127.0.0.1', port=port, ssl_context='adhoc')
        except Exception as e:
            self.logger.error(f"فشل في تشغيل الخادم: {str(e)}")
