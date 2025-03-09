# في utils/logger.py
def secure_log(data):
    encrypted = AESEncryptor().encrypt(str(data))
    with open('/var/log/anoymousjordan/secure.log', 'a') as f:
        f.write(f"{encrypted}\n")
