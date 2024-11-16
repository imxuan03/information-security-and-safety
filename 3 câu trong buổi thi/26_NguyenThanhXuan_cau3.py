# Đề 1
# STT: 26
# Họ tên: Nguyễn Thanh Xuân
# MSSV: B2106825
import random

def isprime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i== 0:
            return  False
    return True

def gcd(a, b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return  a

def mod_inverse(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0
def generate_large_prime(bits):
    while True:
        num_rand = random.getrandbits(bits)
        if isprime(num_rand):
            return num_rand

def generate_keys(p, q):
    n = p*q
    phi_n = (p-1)*(q-1)

    e = 2
    while gcd(e,phi_n)!=1 and e < phi_n:
        e+=1

    d = mod_inverse(e, phi_n)

    return (e, n), (d, n)

def mahoa(public_key, message):
    e, n = public_key

    message_num = [ord(c) for c in message]
    encrypted_message = [pow(num, e, n) for num in message_num]
    return encrypted_message


def giaima(private_key, encrypted_message):
    d, n = private_key

    encrypted_num = [pow(num, d, n) for num in encrypted_message]
    decrypted_message = ''.join(chr(num) for num in encrypted_num)

    return decrypted_message


p = int(input("Nhap p :"))
q = int(input("Nhap q :"))
public_key, private_key = generate_keys(p, q)

OTP = random.randrange(0000,9999)
print("OTP la:", OTP)
otp = str(OTP)


mahoa = mahoa(public_key, otp)
print("Chuoi da ma hoa la: ",mahoa)


giaima= giaima(private_key, mahoa)
print("Chuoi giai ma la: ",giaima)
