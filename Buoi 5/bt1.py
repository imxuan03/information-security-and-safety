# Ho va ten sinh vien: Nguyen Thanh Xuan
# Ma so sinh vien: B2106825
# STT: 26

# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# ========================================================
def pad(s):
    #Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

class MAHOA_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa AFFINE")
        self.geometry('800x600')
        self.lbl = Label(self,
                         text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)
        self.lb2 = Label(self,
                         text="MẬT MÃ ĐỐI XỨNG AFFINE",
                         font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)

        # ===================================
        self.plainlb3 = Label(self, text="PLAIN TEXT", font=("Arial", 14))
        self.plainlb3.grid(column=0, row=3)
        self.plaintxt = Entry(self, width=20)
        self.plaintxt.grid(column=1, row=3)
        self.KEYlb4 = Label(self, text="KEY PAIR", font=("Arial", 14))
        self.KEYlb4.grid(column=2, row=3)
        self.KEYA1 = Entry(self, width=3)
        self.KEYA1.grid(column=3, row=3)
        self.KEYB1 = Entry(self, width=5)
        self.KEYB1.grid(column=4, row=3)

        self.AFbtn = Button(self, text="Mã Hóa", command=self.mahoa)
        self.AFbtn.grid(column=5, row=3)

        self.cipherlb = Label(self, text="CIPHER TEXT", font=("Arial", 14))
        self.cipherlb.grid(column=0, row=4)
        self.ciphertxt = Entry(self, width=20)
        self.ciphertxt.grid(column=1, row=4)

        # Giai ma
        self.giaimabtn = Button(self, text="Giải mã", command=self.giaima)
        self.giaimabtn.grid(column=2, row=4)

        self.giaimatext = Entry(self, width=20)
        self.giaimatext.grid(column=3, row=4)

        #=================================================
        self.thoat = Button(self, text="Quay về màn hình chính",
                            command=self.destroy)
        self.thoat.grid(column=1, row=11)

    # =======================
    def Char2Num(self, c):
        if c.islower():
            return ord(c) - 97
        elif (c == ' '):
            return None
        elif c.isupper():
            return ord(c) - 65

    def Num2Char(self, n, isupper):
        if isupper:
            return chr(n + 65)  # Chữ hoa
        else:
            return chr(n + 97)  # Chữ thường

    def encryptAF(self, txt, a, b, m):
        r = ""
        for c in txt:
            if c == ' ':
                r += c  # Giữ nguyên khoảng trắng
            else:
                isupper = c.isupper()
                e = (a * self.Char2Num(c) + b) % m
                r = r + self.Num2Char(e, isupper)
        return r

    def mahoa(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        entxt = self.encryptAF(self.plaintxt.get(), a, b, m)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)

    def giaima(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        detxt = self.decryptAF(self.ciphertxt.get(), a, b, m)
        self.giaimatext.delete(0, END)  # Xóa nội dung ô nhập cũ
        self.giaimatext.insert(INSERT, detxt)  # Hiển thị kết quả giải mã

    def xgcd(self, a, m):
        temp = m
        x0, x1, y0, y1 = 1, 0, 0, 1
        while m != 0:
            q, a, m = a // m, m, a % m
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        if x0 < 0: x0 = temp + x0
        return x0

    def decryptAF(self, txt, a, b, m):
        r = ""
        a1 = self.xgcd(a, m)
        for c in txt:
            if c == ' ':
                r += c  # Giữ nguyên khoảng trắng
            else:
                isupper = c.isupper()
                e = (a1 * (self.Char2Num(c) - b)) % m
                r = r + self.Num2Char(e, isupper)
        return r



# ========================================================
class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry('800x600')
        self.lbl = Label(self,
        text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)
        self.lb2 = Label(self,
                         text="MẬT MÃ ĐỐI XỨNG DES",
                         font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)
        self.plainlb3 = Label(self,
                              text="Văn bản gốc", font=("Arial", 14))
        self.plainlb3.grid(column=0, row=4)
        self.plaintxt = Entry(self, width=100)
        self.plaintxt.grid(column=1, row=4)
        self.lb4 = Label(self, text="Khóa", font=("Arial", 14))
        self.lb4.grid(column=0, row=5)
        self.keytxt = Entry(self, width=100)
        self.keytxt.grid(column=1, row=5)
        self.lb5 = Label(self,
                         text="Văn bản được mã hóa", font=("Arial", 14))
        self.lb5.grid(column=0, row=6)
        self.ciphertxt = Entry(self, width=100)
        self.ciphertxt.grid(column=1, row=6)
        self.lb6 = Label(self,
                         text="Văn bản được giải mã", font=("Arial", 14))
        self.lb6.grid(column=0, row=7)
        self.denctxt = Entry(self, width=100)
        self.denctxt.grid(column=1, row=7)
        self.btn_enc = Button(self, text="Mã Hóa",
                              command=self.mahoa_DES)
        self.btn_enc.grid(column=1, row=9)
        self.btn_dec = Button(self, text="Giải Mã ",
                              command=self.giaima_DES)
        self.btn_dec.grid(column=1, row=10)
        self.thoat = Button(self, text="Quay về màn hình chính",
                            command=self.destroy)
        self.thoat.grid(column=1, row=11)

    def mahoa_DES(self):
        txt = pad(self.plaintxt.get()).encode()
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)

    def giaima_DES(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))
        self.denctxt.delete(0, END)
        self.denctxt.insert(INSERT, detxt)

# ================================================================
class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa RSA")
        self.geometry('800x600')
        self.lbl = Label(self,
        text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbl.grid(column=1, row=1)
        self.lb2 = Label(self,
                         text="MẬT MÃ ĐỐI XỨNG RSA",
                         font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)
        # =================================
        self.plainlb = Label(self, text="Văn bản gốc", font=("Arial", 14))
        self.plainlb.grid(column=0, row=3)
        self.plaintxt = Entry(self, width=60)
        self.plaintxt.grid(column=1, row=3)

        self.cipherlb = Label(self, text="Văn bản được mã hóa", font=("Arial", 14))
        self.cipherlb.grid(column=0, row=4)
        self.ciphertxt = Entry(self, width=60)
        self.ciphertxt.grid(column=1, row=4)

        self.decipherlb = Label(self, text="Văn bản được giải mã", font=("Arial", 14))
        self.decipherlb.grid(column=0, row=5)
        self.deciphertxt = Entry(self, width=60)
        self.deciphertxt.grid(column=1, row=5)

        self.privatekeylb = Label(self, text="Khóa cá nhân", font=("Arial", 14))
        self.privatekeylb.grid(column=0, row=6)
        self.privatekeytext = Text(self, width=60, height=10)
        self.privatekeytext.grid(column=1, row=6)

        self.publickeylb = Label(self, text="Khóa công khai", font=("Arial", 14))
        self.publickeylb.grid(column=0, row=7)
        self.publickeytext = Text(self, width=60, height=10)  # height có thể điều chỉnh
        self.publickeytext.grid(column=1, row=7)

        self.taokhoabtn = Button(self, text="Tạo khóa", width=10, command=self.generate_key)
        self.taokhoabtn.grid(column=1, row=8)

        self.mahoabtn = Button(self, text="Mã hóa", width=10, command=self.mahoa_rsa)
        self.mahoabtn.grid(column=1, row=9)

        self.giaimabtn = Button(self, text="Giải mã", width=10, command=self.giaima_rsa)
        self.giaimabtn.grid(column=1, row=10)

        self.thoat = Button(self, text="Quay về màn hình chính", command=self.destroy)
        self.thoat.grid(column=1, row=11)

    # Cac ham ====================================================
    def save_file(self, data, mode, filepath):
        with open(filepath, mode) as file:
            file.write(data)

    def generate_key(self):
        key = RSA.generate(1024)

        # Đường dẫn tệp bạn muốn lưu
        private_key_path = "private_key.pem"
        public_key_path = "public_key.pem"

        # Ghi khóa cá nhân vào tệp chỉ định
        self.save_file(key.exportKey('PEM'), 'wb', private_key_path)

        # Ghi khóa công khai vào tệp chỉ định
        self.save_file(key.publickey().exportKey('PEM'), 'wb', public_key_path)

        self.privatekeytext.delete('1.0', END)
        self.privatekeytext.insert(END, key.exportKey('PEM'))
        self.publickeytext.delete('1.0', END)
        self.publickeytext.insert(END, key.publickey().exportKey('PEM'))

    def get_key(self,filename, key_style):
        # Đọc khóa từ tệp
        with open(filename, "rb") as file:
            key_data = file.read()

        # Nhập khóa RSA từ dữ liệu đọc được
        if key_style == "Public Key":
            return RSA.importKey(key_data)
        elif key_style == "Private Key":
            return RSA.importKey(key_data)
        else:
            raise ValueError("Unknown key style")

    def mahoa_rsa(self):
        txt = self.plaintxt.get().encode()
        pub_key = self.get_key("public_key.pem", "Public Key")
        cipher = PKCS1_v1_5.new(pub_key)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)

    def giaima_rsa(self):
        txt = self.ciphertxt.get().encode()
        ciphertext = base64.decodebytes(txt)
        pri_key = self.get_key("private_key.pem", "Private Key")

        cipher = PKCS1_v1_5.new(pri_key)
        message = cipher.decrypt(ciphertext, None)

        self.deciphertxt.delete(0, END)
        self.deciphertxt.insert(INSERT, message)

class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)
        self.mahoa_Affine = Button(text="Mã hóa Affine", font=("Times New Roman", 11), command=self.affine)
        self.mahoa_Affine.pack()

        self.mahoa_DES = Button(text="Mã hóa DES", font=("Times New Roman", 11), command=self.des)
        self.mahoa_DES.pack()

        self.mahoa_RSA = Button(text="Mã hóa RSA", font=("Times New Roman", 11), command=self.rsa)
        self.mahoa_RSA.pack()

        self.thoat = Button(text="Kết Thúc", font=("Times New Roman", 11), command=quit)
        self.thoat.pack()

    def affine(self):
        MAHOA_AFFINE(self)
    def des(self):
        MAHOA_DES(self)

    def rsa(self):
        MAHOA_RSA(self)

def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry('300x200')
    MainWindow(window)
    window.mainloop()

main()