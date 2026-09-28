from crypto.aes import encrypt_aes, decrypt_aes
from crypto.rsa import generate_keys, encrypt_rsa, decrypt_rsa, save_keys, load_private_key


def hybrid_encrypt(text):
    aes_data = encrypt_aes(text)
    pub, priv = generate_keys()
    save_keys(pub, priv)

    enc_key = encrypt_rsa(aes_data['key'].encode(), pub)

    return {
        "cipher": aes_data,
        "encrypted_key": enc_key,
        "note": "Private key saved in private.pem"
    }


def hybrid_decrypt(data):
    priv = load_private_key()

    # Step 1: decrypt AES key using RSA
    decrypted_key = decrypt_rsa(data['encrypted_key'], priv).decode()

    # Step 2: replace key in AES data
    aes_data = data['cipher']
    aes_data['key'] = decrypted_key

    # Step 3: decrypt AES ciphertext
    return decrypt_aes(aes_data)