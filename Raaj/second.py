
import random
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 if x1 >= 0 else x1 + m0


def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose public exponent (usually 65537)
    e = 65537

    # Calculate private exponent using modular inverse
    d = mod_inverse(e, phi)

    return ((n, e), (n, d))

def encrypt(message, public_key):
    n, e = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    n, d = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

if __name__ == "__main__":
    bits = 16  # You can increase the key size for stronger encryption (e.g., 1024)
    
    public_key, private_key = generate_keypair(bits)
    print("Public Key (n, e):", public_key)
    print("Private Key (n, d):", private_key)

    plaintext = input("Enter the plaintext message: ")
    ciphertext = encrypt(plaintext, public_key)
    print("Encrypted Message:", ciphertext)

    decrypted_text = decrypt(ciphertext, private_key)
    print("Decrypted Message:", decrypted_text)

