from key_generator import KeyGenerator


if __name__ == "__main__":
    keys = KeyGenerator()
    public_key = keys.public_key
    private_key = keys.private_key
    print("Public Key:", public_key)
    print("Private Key:", private_key)
