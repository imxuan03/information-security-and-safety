# -*- coding: utf8 -*-
from tkinter import *
# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

from tkinter import messagebox
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
import random

def hashing(text):
    text = text.encode()

    resultMD5 = MD5.new(text).hexdigest().upper()
    resultSHA1 = SHA1.new(text).hexdigest().upper()
    # Học viên tự cài đặt các phương thức cho SHA256 và SHA512
    return [resultMD5, resultSHA1]

import csv
def login():
    filename = 'csdl.csv'

    username = usernametxt.get()
    password = passwordtxt.get()

    with open(filename, mode='r', newline='') as f:
        users = csv.reader(f)
        
        for user in users:
            if user and  user[1] == username:
                hasing_pass = hashing(password)


                for passwd in hasing_pass:
                    if passwd == user[2]:
                        messagebox.showinfo('Thanh Cong', 'dang nhap thanh cong')
                        return
                



    messagebox.showerror('That bai', 'dang nhap khong thanh cong')
    return
            


# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="Đăng nhập",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)


usernamelb = Label(window, text="Tên đăng nhập",font=("Arial", 14))
usernamelb.grid(column=0, row=2)
usernametxt = Entry(window,width=20)
usernametxt.grid(column=1, row=2)

passwordlb = Label(window, text="Mat Khau",font=("Arial", 14))
passwordlb.grid(column=0, row=3)
passwordtxt = Entry(window,width=20)
passwordtxt.grid(column=1, row=3)

dangkibtn = Button(window, text="Đăng nhập", command=login)
dangkibtn.grid(column=1, row=4)

# Hien thi cua so
window.geometry('500x300')
window.mainloop()