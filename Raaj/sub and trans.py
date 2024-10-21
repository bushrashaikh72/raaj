def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Keep punctuation and spaces unchanged
    return result

# Get input from user
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift (an integer): "))

# Encrypt the plaintext using Caesar cipher
encrypted_text = caesar_cipher(plaintext, shift)

# Print the results
print("Plaintext:", plaintext)
print("Shift:", shift)
print("Encrypted text:", encrypted_text)

