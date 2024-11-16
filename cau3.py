def Char2Num(c):
    if c.isupper():
        return ord(c)-65
    elif c.islower():
        return ord(c)-97 +26
    elif c.isdigit():
        return ord(c)-48 + 52
    elif c == ' ':
        return 62
    
def Num2Char(n):
    if 0<=n<=25:
        return chr(n+65)
    elif 26<=n<=51:
        return chr(n+97 -26)
    elif 52<=n<=61:
        return chr(n+48-52)
    elif n==62:
        return ' '
    
    
def encryptAF(txt,a,b,m):
    r = ""
    for c in txt:
        e = (a*Char2Num(c)+b) % m
        r = r+Num2Char(e)
    return r

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
        e = (a1*(Char2Num(c)-b )) % m
        r = r+Num2Char(e)
    return r


import math

# Ciphertext từ đề bài
ciphertext = "LOLYLTQOLTHDZTDC"
m = 63  # Modulo 63
target_word = "LAMUOI"

# Brute-force tìm a và b
for a in range(1, m):  # a phải là số nguyên tố cùng nhau với m
    if math.gcd(a, m) == 1:  # Chỉ thử những giá trị a có nghịch đảo modulo
        for b in range(m):  # Dò b từ 0 đến m-1
            plaintext = decryptAF(ciphertext, a, b, m)
            if target_word in plaintext:  # Kiểm tra xem có chứa từ "Future" không
                print(f"Tìm thấy cặp (a, b): ({a}, {b})")
                print("Plaintext giải mã:", plaintext)
                break