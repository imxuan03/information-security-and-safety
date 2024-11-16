# import random
# from sympy import mod_inverse, gcd, isprime

# def generate_large_prime(bits):
#     while True:
#         num_random = random.getrandbits(bits)
#         if isprime(num_random):
#             return num_random
        
# def generate_keys():
#     p = generate_large_prime(16)
#     q = generate_large_prime(16)

#     n = p*q
#     phi_n = (p-1)*(q-1)

#     e = 2
#     while gcd(e, phi_n)!=1 and e <phi_n:
#         e+=1

#     d = mod_inverse(e, phi_n)

#     return (e, n), (d, n)

# def mahoa(message, public_key):
#     e, n = public_key

#     message_numbers = [ord(char) for char in message ]
#     encrypted_message = [pow(num, e, n) for num in message_numbers]
#     return encrypted_message

# def giaima(encrypted_message, private_key):
#     d, n = private_key

#     decrypted_numbers = [pow(num, d, n) for num in encrypted_message]
#     decrypted_message = ''.join(chr(num) for num in decrypted_numbers)
#     return decrypted_message

# public_key, private_key = generate_keys()

# mess = "hello ne Moi Nguoi oi"

# mahoa = mahoa(mess, public_key)
# print(mahoa)
# giaima = giaima(mahoa, private_key)
# print(giaima)


import random 
from sympy import gcd, mod_inverse, isprime

def generate_large_prime(bits):
    while True:
        num_rand = random.getrandbits(bits)
        if isprime(num_rand):
            return num_rand
        
def generate_keys():
    p = generate_large_prime(16)
    q = generate_large_prime(16)
    n = p*q
    phi_n = (p-1)*(q-1)

    e = 2
    while gcd(e, phi_n)!=1 and e<phi_n:
        e+=1

    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def encrypt(public_key, message):
    e, n = public_key

    mess_num = [ord(c) for c in message]
    encrypt_mess = [pow(num, e, n) for num in mess_num]
    return encrypt_mess

def decrypt(private_key, encrypted_message):
    d, n = private_key

    encrypt_num = [pow(num, d, n) for num in encrypted_message]
    decrypt_mess = ''.join(chr(num) for num in encrypt_num)
    return decrypt_mess

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