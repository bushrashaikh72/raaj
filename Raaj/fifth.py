def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def diffie_hellman():
    P = int(input("Enter a prime number (P): "))
    while not is_prime(P):
        print("The number you entered is not prime. Please enter a prime number.")
        P = int(input("Enter a prime number (P): "))
        
    G = int(input("Enter a primitive root (G): "))
    
    private_key_A = int(input("Enter Alice's private key (a): "))
    private_key_B = int(input("Enter Bob's private key (b): "))

    public_key_A = int(pow(G, private_key_A, P))
    public_key_B = int(pow(G, private_key_B, P))

    shared_secret_key_A = int(pow(public_key_B, private_key_A, P))
    shared_secret_key_B = int(pow(public_key_A, private_key_B, P))

    print("\nPublic Key for Alice (A):", public_key_A)
    print("Public Key for Bob (B):", public_key_B)
    print("\nShared Secret Key for Alice (Ka):", shared_secret_key_A)
    print("Shared Secret Key for Bob (Kb):", shared_secret_key_B)

if __name__ == '__main__':
    diffie_hellman()
