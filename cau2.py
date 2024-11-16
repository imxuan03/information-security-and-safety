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
    if 0 <= n <= 25:
        return chr(n + 65)  # A-Z
    elif 26 <= n <= 51:
        return chr(n - 26 + 97)  # a-z
    elif 52 <= n <= 61:
        return chr(n - 52 + 48)  # 0-9
    elif n == 62:
        return ' '  # Space
    
    
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
m = 63
mahoa = encryptAF('Hell ba da 123 231134421 he moi nuoi oi he', 5,11, m)
print(mahoa)


giaima = decryptAF(mahoa,5,11 ,m)
print(giaima)

