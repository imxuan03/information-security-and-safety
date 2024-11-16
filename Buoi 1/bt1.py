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

print(encryptAF('HELLO', 3, 5, 26))