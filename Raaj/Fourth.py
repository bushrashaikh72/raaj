import hashlib
import rsa

public_key, private_key = rsa.newkeys(512)  

def create_signature(private_key, message):
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = rsa.sign(message_hash, private_key, 'SHA-256')
    return signature

def verify_signature(public_key, message, signature):
    message_hash = hashlib.sha256(message.encode()).digest()
    try:
        rsa.verify(message_hash, signature, public_key)
        return True
    except rsa.VerificationError:
        return False

def is_valid_hex(s):
    if len(s) % 2 != 0:
        return False  
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

message = input("Enter the message: ")

signature = create_signature(private_key, message)
print("Digital Signature:", signature.hex())

verify_input = input("Do you want to verify the signature? (yes/no): ")
if verify_input.lower() == 'yes':
    verify_signature_input = input("Enter the digital signature to verify: ")
    
    if not is_valid_hex(verify_signature_input):
        print("Invalid signature format. Please enter a valid hexadecimal signature.")
    else:
        verify_result = verify_signature(public_key, message, bytes.fromhex(verify_signature_input))
        if verify_result:
            print("Digital Signature is valid. The message is authentic.")
        else:
            print("Digital Signature is invalid. The message may have been tampered with.")
else:
    print("Verification skipped.")
