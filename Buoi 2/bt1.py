from tkinter import *
from Crypto.Cipher import DES
import base64

def pad(s):
    # Them vao cuoi so con thieu, cho du boi cua 8
    return s + (8-len(s)%8) * chr(8-len(s)%8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf8")
    key = pad(KEYA1.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)

def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(KEYA1.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    deciphertxt.delete(0, END)
    deciphertxt.insert(INSERT, detxt)


# ====================================================
# ====================================================
#khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)

plainlb3 = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=40)
plaintxt.grid(column=1, row=3)

KEYlb4 = Label(window, text="Khóa",font=("Arial", 14))
KEYlb4.grid(column=0, row=4)
KEYA1 = Entry(window,width=40)
KEYA1.grid(column=1, row=4)


cipherlb = Label(window, text="Văn bản được mã hóa",font=("Arial", 14))
cipherlb.grid(column=0, row=5)
ciphertxt = Entry(window,width=40)
ciphertxt.grid(column=1, row=5)

decipherlb = Label(window, text="Văn bản được giải mã",font=("Arial", 14))
decipherlb.grid(column=0, row=6)
deciphertxt = Entry(window,width=40)
deciphertxt.grid(column=1, row=6)

mahoabtn = Button(window, text="Mã Hóa", command=mahoa_DES)
mahoabtn.grid(column=0, row=7)


giaimabtn = Button(window, text="Giải mã", command=giaima_DES)
giaimabtn.grid(column=1, row=7)


window.geometry('800x600')
window.mainloop()


