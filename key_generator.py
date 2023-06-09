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
            elif p * q < 128:
                print(f"Error: p times q must be more than 127.")
            else:
                return [p, q]

    def is_prime(self, number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    
    def greatest_common_divisor(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def extended_greatest_common_divisor(self, a: int, b: int) -> list:
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.extended_greatest_common_divisor(b % a, a)
            return gcd, y - (b // a) * x, x

    def mod_inverse(self, a: int, m: int) -> int:
        gcd, x, _ = self.extended_greatest_common_divisor(a, m)
        if gcd != 1:
            raise Exception("Modular inverse does not exist")
        else:
            return x % m

    def generate_key_pair(self, pq: list) -> tuple:
        p, q = pq
        n = p * q
        phi = (p - 1) * (q - 1)

        for e in range(2, phi):
            if self.greatest_common_divisor(e, phi) == 1:
                break

        d = self.mod_inverse(e, phi)
        return (e, n), (d, n)