import json
from crypto.aes import encrypt_aes, decrypt_aes
from crypto.des import encrypt_des, decrypt_des
from crypto.rsa import generate_keys, encrypt_rsa, decrypt_rsa, save_keys, load_private_key
from crypto.hybrid import hybrid_encrypt, hybrid_decrypt
from attacks.frequency_analysis import analyze_frequency
from attacks.brute_force import brute_force_demo


def menu():
    print("""
    ===== CipherX Toolkit =====
    1. Encrypt Text
    2. Decrypt Text (AES/DES/RSA/Hybrid)
    3. Hybrid Encryption
    4. Attack Simulation
    5. Exit
    """)


while True:
    menu()
    choice = input("Select option: ")

    if choice == '1':
        text = input("Enter text: ")
        algo = input("Choose (aes/des/rsa): ").lower()

        if algo == 'aes':
            data = encrypt_aes(text)
            print(json.dumps(data, indent=2))

        elif algo == 'des':
            data = encrypt_des(text)
            print(json.dumps(data, indent=2))

        elif algo == 'rsa':
            pub, priv = generate_keys()
            save_keys(pub, priv)
            ct = encrypt_rsa(text.encode(), pub)
            print(f"Cipher (base64): {ct}")
            print("Private key saved locally.")

    elif choice == '2':
        algo = input("Choose (aes/des/rsa/hybrid): ").lower()

        if algo in ['aes', 'des']:
            print("Paste the FULL JSON output (copy everything between { and })")
            raw = input("Paste encrypted JSON: ")
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                print("[ERROR] Invalid JSON. Make sure you paste the COMPLETE output.")
                continue

            if algo == 'aes':
                print(decrypt_aes(data))
            else:
                print(decrypt_des(data))

        elif algo == 'rsa':
            priv = load_private_key()
            ct = input("Paste ciphertext (base64): ")
            print(decrypt_rsa(ct, priv).decode())

        elif algo == 'hybrid':
            print("Paste FULL hybrid JSON output")
            raw = input("Paste encrypted JSON: ")
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                print("[ERROR] Invalid JSON.")
                continue

            print(hybrid_decrypt(data))

    elif choice == '3':
        text = input("Enter text: ")
        data = hybrid_encrypt(text)
        print(json.dumps(data, indent=2))

    elif choice == '2':
        algo = input("Choose (aes/des/rsa/hybrid): ").lower()

        if algo in ['aes', 'des']:
            print("Paste the FULL JSON output (copy everything between { and })")
            raw = input("Paste encrypted JSON: ")
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                print("[ERROR] Invalid JSON. Make sure you paste the COMPLETE output.")
                continue

            if algo == 'aes':
                print(decrypt_aes(data))
            else:
                print(decrypt_des(data))

        elif algo == 'rsa':
            priv = load_private_key()
            ct = input("Paste ciphertext (base64): ")
            print(decrypt_rsa(ct, priv).decode())

        elif algo == 'hybrid':
            print("Paste FULL hybrid JSON output")
            raw = input("Paste encrypted JSON: ")
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                print("[ERROR] Invalid JSON.")
                continue

            print(hybrid_decrypt(data))

    elif choice == '4':
        sub = input("1. Frequency Analysis\n2. Brute Force Demo\nChoose: ")

        if sub == '1':
            text = input("Enter text: ")
            analyze_frequency(text)

        elif sub == '2':
            brute_force_demo()

    elif choice == '5':
        break