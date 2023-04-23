from key_generator import KeyGenerator
from db_connection import DatabaseConnection as db


def select_cipher_decypher() -> str:
    while True:
        chosen_type = input("Choose Cipher/Decipher: ")
        if chosen_type.lower() in ["cipher", "decipher"]:
            return chosen_type
        else:
            print(f"Error: Your entered type must be Cipher or Decipher")

def encrypt(public_key: tuple, plaintext: str) -> list:
    e, n = public_key
    ciphertext = [pow(ord(character), e, n) for character in plaintext]
    return ciphertext

def decrypt(private_key: tuple, ciphertext: list) -> str:
    d, n = private_key
    plaintext = "".join([chr(pow(character, d, n)) for character in ciphertext])
    return plaintext

def write_to_db(public_key: tuple, encrypted_text: list) -> None:
    while True:
        answer = input("Do you want to put this public key and text to database? (Yes/No) ")
        if answer.lower() not in ["yes", "no"]:
            print(f"Error: Your must say Yes or No!")
        else:
            if answer.lower() == "yes":
                database = db()
                database.upload_to_db({"Public Key": public_key, "Encrypted Text": encrypted_text})
                return
            if answer.lower() == "no":
                return 
            
def decrypt_user_input() -> None:
    while True:
        answer = input("Do you want to read the text from database? (Yes/No) ")
        if answer.lower() not in ["yes", "no"]:
            print(f"Error: Your must say Yes or No!")
        else:
            if answer.lower() == "yes":
                database = db()
                database_data = database.retrieve_from_db("Encrypted Text")
                return database_data
            if answer.lower() == "no":
                user_input = input("Enter a list of integers separated by spaces: ")
                int_list = [int(x) for x in user_input.split()]
                return int_list


if __name__ == "__main__":

    chosen_type = select_cipher_decypher()

    keys = KeyGenerator()
    public_key = keys.public_key
    private_key = keys.private_key

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    if chosen_type.lower() == "cipher":
        user_input = input("Type in the text you want to encrypt: ")
        encrypted_text = encrypt(public_key, user_input)
        print("Encrypted message:", encrypted_text)
        write_to_db(public_key, encrypted_text)
    elif chosen_type.lower() == "decipher":
        user_input = decrypt_user_input()
        print("Decrypted message:", decrypt(private_key, user_input))