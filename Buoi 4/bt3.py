# Họ và tên sinh viên: Nguyễn Thanh Xuân
# Mã số sinh viên: B2106825
# STT: 26
import random
from tkinter import *
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
import os
import csv

def hashing(password):
    password = password.encode()

    resultMD5 = MD5.new(password).hexdigest().upper()
    resultSHA1 = SHA1.new(password).hexdigest().upper()
    resultSHA256 = SHA256.new(password).hexdigest().upper()
    resultSHA512 = SHA512.new(password).hexdigest().upper()

    return [resultMD5, resultSHA1, resultSHA256, resultSHA512]
def login():
    filename = 'account.csv'

    username = usernametxt.get()
    password = passwdtxt.get()

    # Kiểm tra xem tập tin đã tồn tại chưa
    file_exists = os.path.isfile(filename)

    # Nếu đã tồn tại, kiểm tra xem tài khoản đã có chưa
    accountExist = 0

    passwordInCSV = ''
    if file_exists:
        with open(filename, mode='r', newline='') as file:
            users = csv.reader(file)
            for row in users:
                if row[0] == username:
                    accountExist = 1
                    passwordInCSV = row[1]

    if accountExist == 1:
        passwdHashing = hashing(password)
        for passwd in passwdHashing:
            if passwd == passwordInCSV:
                print("Dang nhap thanh cong!")
                return
    else:
        print("Dang nhap khong thanh cong!")

    print("Dang nhap khong thanh cong!")
    return



# ===============================================
# Giao diện
# ===============================================
#khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="ĐĂNG NHẬP",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)


usernamelb = Label(window, text="Tên đăng nhập",font=("Arial", 14))
usernamelb.grid(column=0, row=2)
usernametxt = Entry(window,width=60)
usernametxt.grid(column=1, row=2)

passwdlb = Label(window, text="Mật khẩu",font=("Arial", 14))
passwdlb.grid(column=0, row=3)
passwdtxt = Entry(window,width=60)
passwdtxt.grid(column=1, row=3)


createAccountbtn = Button(window, text="Đăng nhập",command=login)
createAccountbtn.grid(column=1, row=4)



window.geometry('600x200')
window.mainloop()
