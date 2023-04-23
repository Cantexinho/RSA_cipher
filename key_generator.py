class KeyGenerator:
    def __init__(self) -> None:
        self.pq = self.select_pq()
        self.public_key, self.private_key = self.generate_key_pair(self.pq)

    def select_pq(self) -> tuple:
        while True:
            p = int(input("Enter a prime number for p: "))
            if not self.is_prime(p):
                print(f"Error: Your entered number is not prime.")
            else:
                break

        while True:
            q = int(input("Enter a prime number for q: "))
            if not self.is_prime(q):
                print(f"Error: Your entered number is not prime.")
            elif p == q:
                    print(f"Error: p and q cannot be equal.")
            else:
                return [p, q]

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    def greatest_common_divisor(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def extended_greatest_common_divisor(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_greatest_common_divisor(b % a, a)
            return gcd, y - (b // a) * x, x

    def mod_inverse(self, a, m):
        gcd, x, _ = self.extended_greatest_common_divisor(a, m)
        if gcd != 1:
            raise Exception("Modular inverse does not exist")
        else:
            return x % m

    def generate_key_pair(self, pq):
        p, q = pq
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537

        if self.greatest_common_divisor(e, phi) != 1:
            raise ValueError("e and phi are not coprime")

        d = self.mod_inverse(e, phi)
        return (e, n), (d, n)