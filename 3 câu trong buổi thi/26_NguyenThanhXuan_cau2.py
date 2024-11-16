# Đề 1
# STT: 26
# Họ tên: Nguyễn Thanh Xuân
# MSSV: B2106825
def Char2Num(c):
    if c.isupper():
        return ord(c)-65
    if c.islower():
        return ord(c)-97 + 26
    if c == ' ':
        return 52
    if c.isdigit():
        return ord(c) - 48 + 53
def Num2Char(n):
    if 0<=n<=25:
        return chr(n+65)
    if 26<=n<=51:
        return chr(n+97-26)
    if n == 52:
        return ' '
    if 53<=n<=62:
        return chr(n+48-53)

def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r

# Chương trình Euclid Extended để tìm ước số chung lớn nhất của 2 số
def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp+x0
    return x0

def decryptAF(txt,a,b,m):
    r = ""
    a1 = xgcd(a,m)
    for c in txt:
        e = (a1*(Char2Num(c)-b)) % m
        r = r+Num2Char(e)
    return r

def gcd(a, b):
    while b != 0:
        temp = a%b
        a = b
        b = temp
    return a

def find_keys(ciphertext, text):
    m = 63
    for a in range(1,m):
        if gcd(a, m)!=1:
            continue

        for b in range(0, m):
            decryptedtext = decryptAF(ciphertext, a, b, m)
            if text in decryptedtext:
                return a,b, decryptedtext

    print("Không có cặp khóa (a, b) nào thỏa điều kiện.")
    return None, None, None




ciphertext = 'zHliaxlvWgIYl3lEHHnlw0l2emloHOYu'
text = 'Book'

a,b, decryptedtext = find_keys(ciphertext, text)

print(f"Cap khoa (a,b) = ({a}, {b})")
print("Thong diep goc la: ",decryptedtext)