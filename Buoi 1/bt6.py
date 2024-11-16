
# Ho va ten sinh vien: Nguyễn Thanh Xuân
# Ma so sinh vien: B2106825
# STT: 26

# =============================================
# GIỐNG BÀI TẬP 5 NHƯNG CÓ THỂ IN HOA , IN THƯỜNG, KHOẢNG TRẮNG
# =============================================
# =============================================
import math
def Char2Num(c):
    if c.islower():
        return ord(c)-97
    elif (c== ' '):
        return None
    elif c.isupper():
        return ord(c)-65

def Num2Char(n, isupper):
    if isupper:
        return chr(n + 65)  # Chữ hoa
    else:
        return chr(n + 97)  # Chữ thường

def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        if c == ' ':
            r += c  # Giữ nguyên khoảng trắng
        else:
            isupper = c.isupper()
            e = (a*Char2Num(c)+b) % m
            r = r+Num2Char(e,isupper)
    return r


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
        if c == ' ':
            r += c  # Giữ nguyên khoảng trắng
        else:
            isupper = c.isupper()
            e = (a1*(Char2Num(c)-b )) % m
            r = r+Num2Char(e, isupper)
    return r




ciphertext = 'QBkkz Ub Rhr Mhu'



for a in range(1,26):
    if math.gcd(a, 26)!= 1:
        continue

    for b in range (1, 26):
        # print("(a,b)=", a, b)
        decrypttext = decryptAF(ciphertext, a, b, 26)
        if 'c Ban' in decrypttext:
            print(decrypttext, a, b)
            break