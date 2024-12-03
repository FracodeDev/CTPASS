import os
import sys
import time
import random as rnd
from colorama import Fore, Style
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
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
    ====================================
    Welcome to the Password Manager Tool
    ====================================
    This tool provides the following features:

    1. Create and manage passwords:
       - Generate Simple, Strong, or Secure passwords.
       - Create professional password lists and save them to files.

    2. Encryption and Decryption:
       - Encrypt any text using AES encryption.
       - Decrypt text back to its original form.

    3. Timer:
       - Use a countdown timer for time management tasks.

    Features include:
    - Easy-to-use interface.
    - Secure password generation and storage.
    - Advanced encryption for sensitive data.

    ====================================
    """
    slow_print(Fore.MAGENTA + usage_text + Fore.RESET, delay=0.01)


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
        random_string = ''.join(rnd.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", k=4))
        password = f"{name[:2]}{last_name[-2:]}{rnd.choice(['$', '%', '&'])}{birth_year[-2:]}{phone[-3:]}{random_string}{national_id[:3]}"
        print(Fore.CYAN + f"Generated Secure Password: {password}")

    elif level == "4":  
        count = int(input(Fore.GREEN + "Enter the number of passwords to generate: "))
        length = int(input(Fore.GREEN + "Enter the desired password length: "))
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
        passwords = [''.join(rnd.choices(characters, k=length)) for _ in range(count)]
        file_name = input(Fore.GREEN + "Enter the file name to save the passwords: ")

        with open(file_name, "w") as file:
            for password in passwords:
                file.write(password + "\n")
        
        print(Fore.CYAN + f"{count} passwords saved in {file_name}")

    else:
        print(Fore.RED + "Invalid option. Please try again.")
        return create_password()

    if level in ["1", "2", "3"]:
        save_option = input(Fore.YELLOW + "\nDo you want to save the password to a file? (yes/no): ").lower()
        if save_option == "yes":
            file_name = input(Fore.GREEN + "Enter the file name: ")
            with open(file_name, "w") as file:
                file.write(password)
            print(Fore.CYAN + f"Password saved in {file_name}")


def encrypt_decrypt():
    backend = default_backend()
    key = b'ThisIsA16ByteKey'
    iv = b'ThisIsA16ByteIV_'

    def aes_encrypt(text):
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(text.encode()) + padder.finalize()
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return base64.b64encode(encrypted_data).decode()

    def aes_decrypt(encrypted_text):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(base64.b64decode(encrypted_text)) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data.decode()

    while True:
        clear_screen()
        print(Fore.MAGENTA + "\nEncryption Options:\n")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("0. Back to Main Menu")
        choice = input(Fore.YELLOW + "Choose an option: ").strip()

        if choice == "1":
            text = input(Fore.GREEN + "Enter the text to encrypt: ")
            encrypted = aes_encrypt(text)
            print(Fore.CYAN + f"Encrypted Text: {encrypted}")

        elif choice == "2":
            encrypted_text = input(Fore.GREEN + "Enter the encrypted text to decrypt: ")
            try:
                decrypted = aes_decrypt(encrypted_text)
                print(Fore.CYAN + f"Decrypted Text: {decrypted}")
            except Exception as e:
                print(Fore.RED + f"Decryption failed: {e}")

        elif choice == "0":
            break

        else:
            print(Fore.RED + "Invalid option. Please try again.")
            time.sleep(2)


def timer(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        timer_str = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(Fore.MAGENTA, Style.BRIGHT, timer_str, end="\r")
        time.sleep(1)
        t -= 1


def main():
    show_usage()
    while True:
        print(Fore.MAGENTA + "\nPassword Manager")
        print(Fore.BLUE + "1. Create Password")
        print(Fore.GREEN + "2. Timer")
        print(Fore.YELLOW + "3. Encryption/Decryption")
        print(Fore.RED + "0. Exit")
        choice = input(Fore.YELLOW + "Choose an option: ").strip()

        if choice == "1":
            create_password()
        elif choice == "2":
            t = int(input(Fore.GREEN + "Enter time in seconds: "))
            timer(t)
        elif choice == "3":
            encrypt_decrypt()
        elif choice == "0":
            print(Fore.GREEN + "Exiting program. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
            time.sleep(2)

if __name__ == "__main__":
    main()
