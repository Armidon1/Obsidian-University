from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad

def encrypt(plaintext):
    key = os.getenv("KEY", "keykeykeykeykeyk")
    nonce = os.getenv("NONCE", "noncenon")

    cipher = AES.new(key.encode(), AES.MODE_CTR, nonce=nonce.encode())
    ciphertext = cipher.encrypt(plaintext.encode())

    return ciphertext.hex()

def main():
    print("******************************************")
    print("*          Encrypt and Conquer!          *")
    print("******************************************")
    print("I've asked my friend to create a secure encryption scheme for me. He knows what he's doing.")
    print("Who cares it's impossible to make mistakes with crypto")

    while True:
        try:
            choice = int(input("Choose an option:\n1: Encrypt flag\n2: Encrypt custom message\n3: Exit\nEnter your choice: "))
            if choice == 1:
                # TODO: remove flag from here
                flag = os.getenv("FLAG", "ccit{fake_flag}")
                encrypted_flag = encrypt(flag)
                print(f"\nEncrypted Flag (as hex): {encrypted_flag}")
            elif choice == 2:
                user_input = input("Enter the message you want to encrypt: ")
                encrypted_user_text = encrypt(user_input)
                print(f"\nEncrypted User Text: {encrypted_user_text}\n")
            elif choice == 3:
                print("Exiting the AES CTR Challenge. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer choice.")

if __name__ == "__main__":
    main()
