def generate_key_table(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key = key.replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_table = []
    for char in key:
        if char not in key_table:
            key_table.append(char)
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
    return [key_table[i:i+5] for i in range(0, 25, 5)]

def format_message(message):
    message = message.upper().replace("J", "I")
    formatted_message = ""
    i = 0
    while i < len(message):
        formatted_message += message[i]
        if i+1 < len(message) and message[i] == message[i+1]:
            formatted_message += 'X'
        elif i+1 < len(message):
            formatted_message += message[i+1]
            i += 1
        i += 1
    if len(formatted_message) % 2 != 0:
        formatted_message += 'X'
    return formatted_message

def find_position(char, key_table):
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char:
                return i, j
    return None

def playfair_encrypt(plaintext, key_table):
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row_a, col_a = find_position(a, key_table)
        row_b, col_b = find_position(b, key_table)
        if row_a == row_b:
            ciphertext += key_table[row_a][(col_a + 1) % 5]
            ciphertext += key_table[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += key_table[(row_a + 1) % 5][col_a]
            ciphertext += key_table[(row_b + 1) % 5][col_b]
        else:
            ciphertext += key_table[row_a][col_b]
            ciphertext += key_table[row_b][col_a]
    return ciphertext

def playfair_decrypt(ciphertext, key_table):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row_a, col_a = find_position(a, key_table)
        row_b, col_b = find_position(b, key_table)
        if row_a == row_b:
            plaintext += key_table[row_a][(col_a - 1) % 5]
            plaintext += key_table[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += key_table[(row_a - 1) % 5][col_a]
            plaintext += key_table[(row_b - 1) % 5][col_b]
        else:
            plaintext += key_table[row_a][col_b]
            plaintext += key_table[row_b][col_a]
    return plaintext

def main():
    key = input("Enter the key: ").upper().replace("J", "I")
    message = input("Enter the message: ").upper().replace("J", "I")
    
    key_table = generate_key_table(key)
    formatted_message = format_message(message)
    
    print("Key Table:")
    for row in key_table:
        print(" ".join(row))
    
    encrypted_message = playfair_encrypt(formatted_message, key_table)
    decrypted_message = playfair_decrypt(encrypted_message, key_table)
    
    print(f"Formatted Message: {formatted_message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()

