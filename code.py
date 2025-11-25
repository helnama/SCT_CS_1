def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def main():
    print("Caesar Cipher Program")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))
    action = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if action not in ['encrypt', 'decrypt']:
        print("Invalid action. Please choose 'encrypt' or 'decrypt'.")
        return

    output = caesar_cipher(message, shift, action)
    print(f"Result: {output}")

if __name__ == "__main__":
    main()
