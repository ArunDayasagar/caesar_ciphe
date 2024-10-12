def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter 'E' or 'D'.")
        return
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (0-25): "))
    shift = shift % 26
    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, -shift)
        print(f"Decrypted message: {decrypted_message}")
if __name__ == "__main__":
    main()