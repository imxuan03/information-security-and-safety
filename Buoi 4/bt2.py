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
    func = random.randint(0,3)
    if func == 0:
        result = MD5.new(password)
    if func == 1:
        result = SHA1.new(password)
    if func == 2:
        result = SHA256.new(password)
    if func == 3:
        result = SHA512.new(password)

    # Học viên tự cài đặt các phương thức cho SHA256 và SHA512
    return result.hexdigest().upper()
def createAccount():
    filename = 'account.csv'

    username = usernametxt.get()
    password = passwdtxt.get()
    # Kiểm tra xem tập tin đã tồn tại chưa
    file_exists = os.path.isfile(filename)

    # Nếu đã tồn tại, kiểm tra xem tài khoản đã có chưa
    if file_exists:
        with open(filename, mode='r', newline='') as file:
            users = csv.reader(file)
            for row in users:
                if row[0] == username:
                    print("Tài khoản đã tồn tại!")
                    return

    # Mã hóa mật khẩu
    hashed_password = hashing(password)

    # Thêm tài khoản vào tập tin
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password])

    print("Tài khoản đã được thêm thành công!")


# ===============================================
# Giao diện
# ===============================================
#khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="TẠO TÀI KHOẢN",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)


usernamelb = Label(window, text="Tên đăng nhập",font=("Arial", 14))
usernamelb.grid(column=0, row=2)
usernametxt = Entry(window,width=60)
usernametxt.grid(column=1, row=2)

passwdlb = Label(window, text="Mật khẩu",font=("Arial", 14))
passwdlb.grid(column=0, row=3)
passwdtxt = Entry(window,width=60)
passwdtxt.grid(column=1, row=3)


createAccountbtn = Button(window, text="Tạo tài khoản",command=createAccount )
createAccountbtn.grid(column=1, row=4)



window.geometry('600x200')
window.mainloop()
