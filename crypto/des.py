from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64


def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


def encrypt_des(text):
    key = get_random_bytes(8)
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(text).encode())

    return {
        "cipher": base64.b64encode(ciphertext).decode(),
        "key": base64.b64encode(key).decode(),
        "iv": base64.b64encode(iv).decode()
    }


def decrypt_des(data):
    key = base64.b64decode(data['key'])
    iv = base64.b64decode(data['iv'])
    ciphertext = base64.b64decode(data['cipher'])

    cipher = DES.new(key, DES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext).decode().strip()