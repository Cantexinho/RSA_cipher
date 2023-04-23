from key_generator import KeyGenerator
from db_connection import DatabaseConnection as db

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(character), e, n) for character in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = "".join([chr(pow(character, d, n)) for character in ciphertext])
    return plaintext

if __name__ == "__main__":
    keys = KeyGenerator()
    public_key = keys.public_key
    private_key = keys.private_key
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    database = db()
    database.upload_to_db({"Public Key": public_key})


    # message = "56"
    # encrypted_msg = encrypt(public_key, message)
    # print("Encrypted message:", encrypted_msg)

    # decrypted_msg = decrypt(private_key, encrypted_msg)
    # print("Decrypted message:", decrypted_msg)
