def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_greatest_common_divisor(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_greatest_common_divisor(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, _ = extended_greatest_common_divisor(a, m)
    if gcd != 1:
        raise Exception("Modular inverse does not exist")
    else:
        return x % m

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537

    if greatest_common_divisor(e, phi) != 1:
        raise ValueError("e and phi are not coprime")

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


if __name__ == "__main__":
    p = 37
    q = 11
    public_key, private_key = generate_key_pair(p, q)
    print("Public Key:", public_key)
    print("Private Key:", private_key)
