import os
import sys
import time
import random as rnd
from colorama import Fore, Style
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
    Encoding,
    PrivateFormat,
    PublicFormat,
)
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend
import base64


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.05):
    for char in text + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def show_usage():
    clear_screen()
    usage_text = """
    ================================================
    🔐 Advanced Encryption and Password Manager Tool 🔐
    ================================================

    This tool provides the following features:

    1️⃣ Password Management:
       - Create Simple, Strong, or Secure passwords based on user input.
       - Generate professional password lists and save them to files.

    2️⃣ Encryption and Decryption:
       - AES, RSA, ChaCha20, and Blowfish encryption and decryption.
       - Hashing text using SHA-256.

    3️⃣ Utility Features:
       - Timer for task management.

    🚀 Easy-to-use interface with advanced security features.

    ================================================
    """
    slow_print(Fore.CYAN + usage_text + Fore.RESET, delay=0.01)


def aes_encrypt_decrypt(key, iv, text, action):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

    if action == "encrypt":
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(text.encode()) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(encrypted_data).decode()

    elif action == "decrypt":
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(base64.b64decode(text)) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data.decode()


def rsa_generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def rsa_encrypt_decrypt(key, text, action):
    if action == "encrypt":
        encrypted = key.encrypt(
            text.encode(),
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return base64.b64encode(encrypted).decode()

    elif action == "decrypt":
        decrypted = key.decrypt(
            base64.b64decode(text),
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return decrypted.decode()


def chacha_encrypt_decrypt(key, nonce, text, action):
    chacha = ChaCha20Poly1305(key)
    if action == "encrypt":
        encrypted = chacha.encrypt(nonce, text.encode(), None)
        return base64.b64encode(encrypted).decode()

    elif action == "decrypt":
        decrypted = chacha.decrypt(nonce, base64.b64decode(text), None)
        return decrypted.decode()


def blowfish_encrypt_decrypt(key, iv, text, action):
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=default_backend())

    if action == "encrypt":
        padder = padding.PKCS7(algorithms.Blowfish.block_size).padder()
        padded_data = padder.update(text.encode()) + padder.finalize()
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(encrypted_data).decode()

    elif action == "decrypt":
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(base64.b64decode(text)) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.Blowfish.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data.decode()


def sha256_hash(text):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(text.encode())
    return digest.finalize().hex()


def create_password():
    clear_screen()
    print(Fore.CYAN + "\nCreate a password in three levels:\n")
    print("1. Simple Password")
    print("2. Strong Password")
    print("3. Secure Password")
    print("4. Generate Professional Password List")
    print(Fore.RESET)
    level = input(Fore.YELLOW + "Choose the level (1/2/3/4): ").strip()

    if level == "1":
        name = input(Fore.GREEN + "Enter your first name: ")
        last_name = input(Fore.GREEN + "Enter your last name: ")
        birth_year = input(Fore.GREEN + "Enter your birth year: ")
        password = f"{name[:4]}{last_name[0]}{birth_year[-2:]}"
        print(Fore.CYAN + f"Generated Simple Password: {password}")

    elif level == "2":
        name = input(Fore.GREEN + "Enter your first name: ")
        last_name = input(Fore.GREEN + "Enter your last name: ")
        birth_year = input(Fore.GREEN + "Enter your birth year: ")
        phone = input(Fore.GREEN + "Enter your phone number: ")
        password = f"{name[:3]}{rnd.choice(['!', '@', '#'])}{last_name[:2]}{birth_year[-2:]}{phone[-4:]}"
        print(Fore.CYAN + f"Generated Strong Password: {password}")

    elif level == "3":
        name = input(Fore.GREEN + "Enter your first name: ")
        last_name = input(Fore.GREEN + "Enter your last name: ")
        birth_year = input(Fore.GREEN + "Enter your birth year: ")
        phone = input(Fore.GREEN + "Enter your phone number: ")
        national_id = input(Fore.GREEN + "Enter your national ID: ")
        random_string = "".join(
            rnd.choices(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*",
                k=4,
            )
        )
        password = f"{name[:2]}{last_name[-2:]}{rnd.choice(['$', '%', '&'])}{birth_year[-2:]}{phone[-3:]}{random_string}{national_id[:3]}"
        print(Fore.CYAN + f"Generated Secure Password: {password}")

    elif level == "4":
        create_password_list()
    else:
        print(Fore.RED + "Invalid option. Please try again.")
        return create_password()

    if level in ["1", "2", "3"]:
        save_option = input(
            Fore.YELLOW + "\nDo you want to save the password to a file? (yes/no): "
        ).lower()
        if save_option == "yes":
            file_name = input(Fore.GREEN + "Enter the file name: ")
            with open(file_name, "w") as file:
                file.write(password)
            print(Fore.CYAN + f"Password saved in {file_name}")


def create_password_list():
    """Generates a list of passwords and saves them to a text file."""
    clear_screen()
    print(Fore.CYAN + "\nGenerate a Custom Password List:\n")

    try:
        count = int(input(Fore.GREEN + "Enter the number of passwords to generate: "))
        length = int(input(Fore.GREEN + "Enter the desired password length: "))

        if count <= 0 or length <= 0:
            print(Fore.RED + "Count and length must be positive integers.")
            return

        characters = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
        )
        passwords = ["".join(rnd.choices(characters, k=length)) for _ in range(count)]

        file_name = input(
            Fore.GREEN
            + "Enter the file name to save the passwords (e.g., passwords.txt): "
        ).strip()

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        with open(file_name, "w") as file:
            for password in passwords:
                file.write(password + "\n")

        print(
            Fore.CYAN
            + f"\n{count} passwords of length {length} have been saved in '{file_name}'."
        )

    except ValueError:
        print(
            Fore.RED
            + "Invalid input. Please enter numeric values for count and length."
        )
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")


def main():
    show_usage()
    while True:
        print(Fore.MAGENTA + "\nPassword Manager and Encryption Tool")
        print(Fore.BLUE + "1. Create Password")
        print(Fore.GREEN + "2. Generate Password List")
        print(Fore.YELLOW + "3. Encryption/Decryption")
        print(Fore.RED + "4. Hashing (SHA-256)")
        print(Fore.RED + "0. Exit")
        choice = input(Fore.YELLOW + "Choose an option: ").strip()

        if choice == "1":
            create_password()
        elif choice == "2":
            create_password_list()
        elif choice == "3":
            print(Fore.CYAN + "Encryption and Decryption Module Coming Soon!")
        elif choice == "4":
            text = input(Fore.GREEN + "Enter the text to hash: ")
            hashed = sha256_hash(text)
            print(Fore.CYAN + f"SHA-256 Hashed text: {hashed}")
        elif choice == "0":
            print(Fore.RED + "Exiting the program...")
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid option. Please try again.")


if __name__ == "__main__":
    main()
