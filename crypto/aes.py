from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def encrypt_aes(text):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())

    return {
        "cipher": base64.b64encode(ciphertext).decode(),
        "key": base64.b64encode(key).decode(),
        "nonce": base64.b64encode(cipher.nonce).decode(),
        "tag": base64.b64encode(tag).decode()
    }


def decrypt_aes(data):
    key = base64.b64decode(data['key'])
    nonce = base64.b64decode(data['nonce'])
    tag = base64.b64decode(data['tag'])
    ciphertext = base64.b64decode(data['cipher'])

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()