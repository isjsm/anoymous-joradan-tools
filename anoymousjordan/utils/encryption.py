from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class AESEncryptor:
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.cipher = AES.new(self.key, AES.MODE_CBC)

    def encrypt(self, plaintext):
        """تشفير AES-256-CBC"""
        ct_bytes = self.cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        iv = base64.b64encode(self.cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return f"{iv}:{ct}"

    def decrypt(self, ciphertext):
        """فك التشفير"""
        iv, ct = ciphertext.split(':')
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
