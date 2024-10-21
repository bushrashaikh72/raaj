import hashlib
import hmac

def generate_mac(key, message):
    
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    
    mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    return mac

def verify_mac(key, message, mac_to_verify):
   
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    
    calculated_mac = hmac.new(key, message, hashlib.sha256).hexdigest()

   
    return hmac.compare_digest(calculated_mac, mac_to_verify)


key = input("Enter the secret key: ")
message = input("Enter the message: ")


mac = generate_mac(key, message)
print("Generated MAC:", mac)


mac_to_verify = input("Enter the MAC to verify: ")
if verify_mac(key, message, mac_to_verify):
    print("MAC is valid. The message is authentic.")
else:
    print("MAC is invalid. The message may have been tampered with.")



