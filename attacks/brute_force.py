import base64
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import time


def brute_force_demo():
    print("[Brute Force Demo - DES | Dictionary Attack Mode]")

    # Take plaintext from user
    user_text = input("Enter plaintext to simulate attack: ")

    # Pad text
    original = user_text
    while len(user_text) % 8 != 0:
        user_text += ' '

        # Encrypt with weak key if plaintext is simple (to allow cracking)
    weak_keys = [
        b'password', b'12345678', b'abcdefgh', b'87654321',
        b'letmein!', b'admin123', b'qwertyui', b'hello123'
    ]

    # If user plaintext is simple, simulate weak system
    if len(original) <= 8 and original.isalnum():
        real_key = weak_keys[0][:8]  # predictable weak key
        print("[!] Weak encryption detected (simulated)")
    else:
        real_key = get_random_bytes(8)

    iv = get_random_bytes(8)
    cipher = DES.new(real_key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(user_text.encode())

    print(f"Target Cipher (base64): {base64.b64encode(ciphertext).decode()}")

    # 🔥 Dictionary of weak keys (simulating weak passwords)
    weak_keys = [
        b'password', b'12345678', b'abcdefgh', b'87654321',
        b'letmein!', b'admin123', b'qwertyui', b'hello123'
    ]

    start = time.time()
    attempts = 0

    print("Trying weak keys...")

    found = False

    for key in weak_keys:
        attempts += 1
        try:
            test_cipher = DES.new(key[:8], DES.MODE_CBC, iv)
            decrypted = test_cipher.decrypt(ciphertext).decode(errors='ignore').strip()

            if decrypted == original:
                print(f"[+] Key cracked using weak key after {attempts} attempts!")
                print(f"Key used: {key[:8]}")
                print(f"Decrypted: {decrypted}")
                found = True
                break
        except:
            continue

    end = time.time()

    if not found:
        print("[-] Not found in weak dictionary (strong key used)")

    print(f"Attempts: {attempts}")
    print(f"Time: {end - start:.2f} sec")