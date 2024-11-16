import math
def Char2Num(c):
    if c.isupper():
        return ord(c)-65
    if c.islower():
        return ord(c)-97+26
    if c.isdigit():
        return ord(c)-48+52
    if c==' ':
        return 62
def Num2Char(n):
    if n == 62:
        return ' '
    if 0<=n<=25:
        return chr(n+65)
    if 26<=n<=51:
        return chr(n+97-26)
    if 52<=n<=61:
        return chr(n+48-52)
    
# Chương trình Euclid Extended để tìm ước số chung lớn nhất của 2 số
def xgcd(a,m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a ,m = a//m, m, a%m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0

def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r


def decryptAF(txt,a,b,m):
    r = ""
    a1 = xgcd(a,m)
    for c in txt:
        e = (a1*(Char2Num(c)-b )) % m
        r = r+Num2Char(e)
    return r

# def find_message(encypted_text):
#     m = 63

#     for a in range(1,m):
#         if math.gcd(a, m)==1:
#             for b in range(m):
#                 mess = decryptAF(encypted_text,a, b, m)
#                 if 'LAMUOI' in mess:
#                     print("a,b la: ", a, b)
#                     print(mess)
#                     return

#     print("Khong tim ra kq")

# find_message('LOLYLTQOLTHDZTDC')

def calculate_gcd(a, b):
    return math.gcd(a, b)

def find_original_message(cipher_message):
    m = 63

    for a in range(1,m):
        if math.gcd(a, m)!=1:
            continue

        for b in range(m):
            decrypted_message = decryptAF(cipher_message, a, b, m)
            if 'LAMUOI' in decrypted_message:
                return decrypted_message, a, b
    return None, None, None

original_message, a, b  = find_original_message('LOLYLTQOLTHDZTDC')
if original_message:
    print(f"Thông điệp gốc: {original_message}")
    print(f"Cặp khóa (a, b): ({a}, {b})")
else:
    print("Không tìm thấy thông điệp gốc với từ đã biết.")
