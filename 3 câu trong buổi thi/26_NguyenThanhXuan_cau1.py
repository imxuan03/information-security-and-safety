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

a = int(input('Nhap a:'))
b = int(input('Nhap b:'))
m = 63

message = input("Nhap thong diep goc:")
mahoa = encryptAF(message, a, b, m)
print("Ban ma la:", mahoa)
giaima = decryptAF(mahoa, a,b,m)
print("Giai ma la:", giaima)
