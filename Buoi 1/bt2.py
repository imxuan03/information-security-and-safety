
# Ho va ten sinh vien: Nguyễn Thanh Xuân
# Ma so sinh vien: B2106825
# STT: 26

def Char2Num(c):
    return ord(c)-65

def Num2Char(n):
    return chr(n+65)

def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r

mahoa = encryptAF('HELLO', 5, 7, 26)
print(mahoa)

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

def decryptAF(txt,a,b,m):
    r = ""
    a1 = xgcd(a,m)
    for c in txt:
        e = (a1*(Char2Num(c)-b )) % m
        r = r+Num2Char(e)
    return r

giaima = decryptAF(mahoa,5,7 ,26)
print(giaima)

