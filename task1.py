def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
    
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
    
        else:
            decrypted_text += char
    return decrypted_text

def main():
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
