# -*- coding: utf8 -*-
from tkinter import *
# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")


from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
import random
from tkinter import messagebox

def hashing(text):
    text = text.encode()
    func = random.choice([0, 1])
    if func == 0:
        result = MD5.new(text)
    if func == 1:
        result = SHA1.new(text)
    # Học viên tự cài đặt các phương thức cho SHA256 và SHA512
    return result.hexdigest().upper()

import csv
def createAccount():
    filename = 'csdl.csv'

    username = usernametxt.get()
    password = passwordtxt.get()


    stt = 0
    with open(filename, mode='r', newline='') as f:
        users = list(csv.reader(f))
        stt = len(users)
        for user in users:
            if user and user[1] == username:
                messagebox.showerror("That bai", "tai khoan da ton tai")
                return

            
    hasing_pass = hashing(password)
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([stt,username, hasing_pass])
        messagebox.showinfo('Thanh cong', 'Tài khoản đã được thêm thành công!')





# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="Tạo tài khoản",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)


usernamelb = Label(window, text="Tên đăng nhập",font=("Arial", 14))
usernamelb.grid(column=0, row=2)
usernametxt = Entry(window,width=20)
usernametxt.grid(column=1, row=2)

passwordlb = Label(window, text="Mat Khau",font=("Arial", 14))
passwordlb.grid(column=0, row=3)
passwordtxt = Entry(window,width=20)
passwordtxt.grid(column=1, row=3)

dangkibtn = Button(window, text="Đăng ký", command=createAccount)
dangkibtn.grid(column=1, row=4)

# Hien thi cua so
window.geometry('500x300')
window.mainloop()

