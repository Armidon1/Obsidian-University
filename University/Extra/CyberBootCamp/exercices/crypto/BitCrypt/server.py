import os
from string import printable

key = os.urandom(500)

FLAG = os.environ.get('FLAG', 'ccit{FAKE_FLAG}')

def encrypt(key, m): #key and messaage to encrypt 
    bits_key = ''.join([bin(x)[2:].zfill(8) for x in key]) # transform the key (string) in a string of bits
    bits_m = ''.join([bin(x)[2:].zfill(8) for x in m])
    encrypted = ''
    for i in range(len(bits_m)):
        if bits_key[i] == bits_m[i]:
            encrypted += '0'
        else:
            encrypted += '1'
    encrypted = [int(encrypted[i:i+8], 2) for i in range(0, len(encrypted), 8)] #trasform the string encrypted = '10101010'
                                                                                #into a list of int = [170]
    return bytes(encrypted).hex() #e poi lo converto in bytes e poi lo invio in esadecimale 

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Encrypt the FLAG")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            if not all([x in printable for x in message]):
                print("You can only encrypt printable characters.")
                continue
            if len(message) > 500:
                print("The message is too long.")
                continue
            encrypted_message = encrypt(key, message.encode())
            print("Encrypted message:", encrypted_message)
        elif choice == '2':
            encrypted_flag = encrypt(key, FLAG.encode('utf-8'))
            print("Encrypted FLAG:", encrypted_flag)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
