import os
import sys
import random as rnd
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import base64
import customtkinter as ctk


def aes_encrypt_decrypt(key, iv, text, action):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

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


def sha256_hash(text):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(text.encode())
    return digest.finalize().hex()


def generate_password(level):
    if level == "Simple":
        return "user123"
    elif level == "Strong":
        return "user@Strong123"
    elif level == "Secure":
        return "S3cur3!@#User123"
    else:
        return ""


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Advanced Encryption and Password Manager Tool")
app.geometry("800x600")


menu_frame = ctk.CTkFrame(app, width=200, corner_radius=0)
menu_frame.pack(side="left", fill="y")

content_frame = ctk.CTkFrame(app)
content_frame.pack(side="right", expand=True, fill="both")


def show_password_manager():
    for widget in content_frame.winfo_children():
        widget.destroy()

    label = ctk.CTkLabel(content_frame, text="Password Manager", font=("Arial", 20))
    label.pack(pady=10)

    level_label = ctk.CTkLabel(content_frame, text="Select Password Level:")
    level_label.pack(pady=5)

    level_combo = ctk.CTkComboBox(content_frame, values=["Simple", "Strong", "Secure"])
    level_combo.pack(pady=5)

    result_label = ctk.CTkLabel(content_frame, text="")
    result_label.pack(pady=10)

    def generate():
        level = level_combo.get()
        password = generate_password(level)
        result_label.configure(text=f"Generated Password: {password}")

    generate_button = ctk.CTkButton(
        content_frame, text="Generate Password", command=generate
    )
    generate_button.pack(pady=10)


def show_encryption_tool():
    for widget in content_frame.winfo_children():
        widget.destroy()

    label = ctk.CTkLabel(
        content_frame, text="AES Encryption/Decryption", font=("Arial", 20)
    )
    label.pack(pady=10)

    text_label = ctk.CTkLabel(content_frame, text="Enter Text:")
    text_label.pack(pady=5)
    text_entry = ctk.CTkEntry(content_frame, width=400)
    text_entry.pack(pady=5)

    key_label = ctk.CTkLabel(content_frame, text="Enter Key (16 bytes):")
    key_label.pack(pady=5)
    key_entry = ctk.CTkEntry(content_frame, width=400)
    key_entry.pack(pady=5)

    iv_label = ctk.CTkLabel(content_frame, text="Enter IV (16 bytes):")
    iv_label.pack(pady=5)
    iv_entry = ctk.CTkEntry(content_frame, width=400)
    iv_entry.pack(pady=5)

    result_label = ctk.CTkLabel(content_frame, text="")
    result_label.pack(pady=10)

    def encrypt():
        try:
            text = text_entry.get()
            key = key_entry.get().encode()
            iv = iv_entry.get().encode()
            result = aes_encrypt_decrypt(key, iv, text, "encrypt")
            result_label.configure(text=f"Encrypted: {result}")
        except Exception as e:
            result_label.configure(text=f"Error: {e}")

    def decrypt():
        try:
            text = text_entry.get()
            key = key_entry.get().encode()
            iv = iv_entry.get().encode()
            result = aes_encrypt_decrypt(key, iv, text, "decrypt")
            result_label.configure(text=f"Decrypted: {result}")
        except Exception as e:
            result_label.configure(text=f"Error: {e}")

    encrypt_button = ctk.CTkButton(content_frame, text="Encrypt", command=encrypt)
    encrypt_button.pack(pady=5)

    decrypt_button = ctk.CTkButton(content_frame, text="Decrypt", command=decrypt)
    decrypt_button.pack(pady=5)


def show_hashing_tool():
    for widget in content_frame.winfo_children():
        widget.destroy()

    label = ctk.CTkLabel(content_frame, text="SHA-256 Hashing", font=("Arial", 20))
    label.pack(pady=10)

    text_label = ctk.CTkLabel(content_frame, text="Enter Text:")
    text_label.pack(pady=5)

    text_entry = ctk.CTkEntry(content_frame, width=400)
    text_entry.pack(pady=5)

    result_label = ctk.CTkLabel(content_frame, text="")
    result_label.pack(pady=10)

    def hash_text():
        text = text_entry.get()
        hashed = sha256_hash(text)
        result_label.configure(text=f"SHA-256 Hash: {hashed}")

    hash_button = ctk.CTkButton(content_frame, text="Hash Text", command=hash_text)
    hash_button.pack(pady=10)


password_manager_button = ctk.CTkButton(
    menu_frame, text="Password Manager", command=show_password_manager
)
password_manager_button.pack(pady=10, padx=10, fill="x")

encryption_tool_button = ctk.CTkButton(
    menu_frame, text="Encryption Tool", command=show_encryption_tool
)
encryption_tool_button.pack(pady=10, padx=10, fill="x")

hashing_tool_button = ctk.CTkButton(
    menu_frame, text="Hashing Tool", command=show_hashing_tool
)
hashing_tool_button.pack(pady=10, padx=10, fill="x")

exit_button = ctk.CTkButton(menu_frame, text="Exit", command=sys.exit)
exit_button.pack(pady=10, padx=10, fill="x")

app.mainloop()
