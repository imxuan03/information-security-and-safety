# Ho va ten sinh vien: Nguyễn Thanh Xuân
# Ma so sinh vien: B2106825
# STT: 26
from tkinter import *
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

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    entxt = encryptAF(plaintxt.get(),a,b,m)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    detxt = decryptAF(ciphertxt.get(),a,b,m)
    giaimatext.delete(0, END)  # Xóa nội dung ô nhập cũ
    giaimatext.insert(INSERT, detxt)  # Hiển thị kết quả giải mã

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

#khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)

AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)


cipherlb = Label(window, text="CIPHER TEXT",font=("Arial", 14))
cipherlb.grid(column=0, row=4)
ciphertxt = Entry(window,width=20)
ciphertxt.grid(column=1, row=4)

# Giai ma
giaimabtn = Button(window, text="Giải mã", command=giaima)
giaimabtn.grid(column=2, row=4)

giaimatext = Entry(window,width=20)
giaimatext.grid(column=3, row=4)


window.geometry('800x600')
window.mainloop()



