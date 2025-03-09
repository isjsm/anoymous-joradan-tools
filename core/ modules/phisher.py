# modules/phisher.py
from flask import Flask, request

class PhishingSimulator:
    def __init__(self):
        self.app = Flask(__name__)

    def create_fake_login(self):
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                # تخزين بيانات الاعتماد بشكل آمن (للتدريب)
                print(f"[!] Credentials captured: {request.form}")
                return "Login successful (Fake)"
            return """
                <form method="POST">
                    Username: <input type="text" name="username"><br>
                    Password: <input type="password" name="password"><br>
                    <input type="submit" value="Login">
                </form>
            """
