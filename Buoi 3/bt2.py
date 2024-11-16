import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp + x0
    return x0


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_large_prime(bits):
    while True:
        num_random = random.getrandbits(bits)
        if is_prime(num_random):
            return num_random


def generate_keys():
    p = generate_large_prime(16)
    q = generate_large_prime(16)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 2
    while gcd(e, phi_n) != 1 and e < phi_n:
        e += 1

    d = mod_inverse(e, phi_n)

    return (e, n), (d, n)


def encrypt(public_key, message):
    e, n = public_key

    message_numbers = [ord(char) for char in message]

    encrypted_numbers = [pow(num, e, n) for num in message_numbers]
    return encrypted_numbers


def decrypt(private_key, encrypted_numbers):
    d, n = private_key

    decrypted_numbers = [pow(num, d, n) for num in encrypted_numbers]

    decrypted_message = ''.join(chr(num) for num in decrypted_numbers)
    return decrypted_message


if __name__ == "__main__":
    public_key, private_key = generate_keys()

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    message = input("Nhập thông điệp cần mã hóa: ")
    print(f"Original Message: {message}")

    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")