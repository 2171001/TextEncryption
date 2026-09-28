from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def generate_keys():
    key = RSA.generate(2048)
    return key.publickey(), key


def save_keys(pub, priv):
    with open("public.pem", "wb") as f:
        f.write(pub.export_key())
    with open("private.pem", "wb") as f:
        f.write(priv.export_key())


def load_private_key():
    with open("private.pem", "rb") as f:
        return RSA.import_key(f.read())


def encrypt_rsa(msg, pub):
    cipher = PKCS1_OAEP.new(pub)
    return base64.b64encode(cipher.encrypt(msg)).decode()


def decrypt_rsa(ciphertext, priv):
    cipher = PKCS1_OAEP.new(priv)
    return cipher.decrypt(base64.b64decode(ciphertext))