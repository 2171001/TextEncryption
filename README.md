# Text Encryption

A Python-based cybersecurity toolkit for encrypting and decrypting text using multiple cryptographic algorithms, including **AES, DES, RSA, and Hybrid Encryption**.

The project also includes educational attack simulations such as **Frequency Analysis** and **Brute Force / Dictionary Attack simulation** to demonstrate how weak cryptographic configurations can be analyzed or attacked.

---

## Project Description

The goal of this project is to demonstrate how different cryptographic techniques can be used to protect text and how encryption approaches differ in terms of key usage, performance, and security characteristics.

The toolkit provides a command-line interface where users can:

* Encrypt text using AES, DES, or RSA
* Decrypt previously encrypted text
* Perform hybrid encryption using AES and RSA together
* Analyze character frequencies
* Simulate brute-force attacks against weak DES keys
* Demonstrate the difference between weak and strong encryption scenarios

---

## Features

### AES Encryption

Encrypts text using the Advanced Encryption Standard (AES).

The encryption output contains the required cryptographic parameters, including:

* Ciphertext
* Encryption key
* Nonce
* Authentication tag

The complete encrypted data can then be supplied back to the toolkit for decryption.

---

### DES Encryption

Supports text encryption using the Data Encryption Standard (DES).

The output contains:

* Ciphertext
* DES key
* Initialization Vector (IV)

The toolkit can subsequently use these values to recover the original plaintext.

> **Note:** DES is included for educational and comparative purposes. DES is considered obsolete for modern secure applications because of its limited key size.

---

### RSA Encryption

Provides asymmetric encryption using RSA.

RSA uses a key pair:

* **Public key** for encryption
* **Private key** for decryption

The toolkit generates the RSA key pair locally and uses the corresponding private key to decrypt the ciphertext.

---

### Hybrid Encryption

Combines symmetric and asymmetric cryptography.

The toolkit uses:

1. AES to encrypt the actual plaintext.
2. RSA to encrypt the AES key.
3. The RSA-encrypted AES key and AES ciphertext are returned together.

The decryption process reverses this:

```text
RSA Private Key
       ↓
Decrypt AES Key
       ↓
AES Decryption
       ↓
Original Plaintext
```

This demonstrates the fundamental concept behind hybrid cryptographic systems: using symmetric encryption for data and asymmetric encryption for key protection.

---

## Attack Simulation

The toolkit also contains educational attack simulations to demonstrate weaknesses in cryptographic systems.

### Frequency Analysis

Frequency analysis counts how frequently each character occurs in the supplied text and calculates its percentage of the total.

For example:

```text
s: 2 (25.00%)
o: 3 (23.08%)
```

This technique is useful for understanding how statistical patterns can be exploited against certain weak or classical substitution-based ciphers.

It is not intended to break modern AES or RSA encryption.

---

### Brute Force / Dictionary Attack

The brute-force component demonstrates how weak DES keys can be vulnerable to key-guessing attacks.

The simulation:

* Generates a target ciphertext.
* Uses a deliberately weak key scenario.
* Attempts candidate keys.
* Decrypts the ciphertext with each candidate.
* Performs an exact plaintext comparison.
* Reports success only when the decrypted plaintext exactly matches the original plaintext.

This strict comparison prevents the simulation from treating random readable-looking data as a successful crack.

The project also demonstrates the contrast between a deliberately weak key scenario and a randomly generated stronger key scenario.

---

## Command-Line Interface

Run the toolkit with:

```bash
poetry run python main.py
```

The main menu provides:

```text
===== CipherX Toolkit =====

1. Encrypt Text
2. Decrypt Text
3. Hybrid Encryption
4. Attack Simulation
5. Exit
```

---

## Example Workflow

### AES

```text
Enter text: J35u5 15 L0rd
Choose: aes
```

The toolkit returns the encrypted ciphertext together with the required AES parameters.

The resulting JSON can then be supplied to the decryption functionality to recover:

```text
J35u5 15 L0rd
```

---

### DES

```text
Enter text: Awes0m3 G0d!
Choose: des
```

The ciphertext, key, and IV are generated.

The same information can subsequently be supplied to the decryption functionality to recover the original plaintext.

---

### RSA

```text
Enter text: Maran@tha
Choose: rsa
```

The plaintext is encrypted using the RSA public key.

The corresponding private key is then used to decrypt the ciphertext.

---

### Hybrid Encryption

```text
Enter text: Y@hw3h
```

The toolkit encrypts the plaintext with AES and protects the AES key using RSA.

The resulting package can then be supplied to the hybrid decryption functionality to recover:

```text
Y@hw3h
```

---

## Requirements

* Python 3
* Poetry
* PyCryptodome
* Linux, macOS, or Windows

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

Install the project dependencies:

```bash
poetry install
```

Run the toolkit:

```bash
poetry run python main.py
```

---

## Security & Educational Disclaimer

This project is primarily intended for **educational and cybersecurity demonstration purposes**.

AES, DES, and RSA are implemented to demonstrate different cryptographic concepts. In particular, DES is included because it is part of the project's algorithm comparison and attack-simulation objectives, not because it is recommended for protecting modern sensitive data.

The attack functionality is designed as a controlled demonstration of cryptographic weaknesses and key-guessing concepts.

Do not use this project as a replacement for professionally reviewed cryptographic software or as the sole protection mechanism for real-world sensitive communications.

---

## Technologies Used

* **Python**
* **PyCryptodome**
* **AES**
* **DES**
* **RSA**
* **Hybrid Cryptography**
* **Frequency Analysis**
* **Brute Force / Dictionary Attack Simulation**
* **Poetry**

---

## Learning Objectives

This project demonstrates:

* Symmetric encryption
* Asymmetric encryption
* Hybrid cryptography
* Key generation and management
* Nonces and initialization vectors
* Authentication tags
* RSA key pairs
* Cryptographic attack concepts
* Frequency-based analysis
* Weak-key attacks
* Command-line cybersecurity tooling

---

## Security Note

This project is intended for **educational and security-awareness purposes**.

The reported entropy, Markov score, crack time, and overall score are estimates produced by the tool's analysis model. They should not be interpreted as guarantees of how long a real-world attacker would require to recover a password.

For real-world password management, use unique passwords for every service and consider using a reputable password manager.

---

## License

This project is intended for educational and cybersecurity learning purposes.
