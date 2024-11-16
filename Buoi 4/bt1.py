# Họ và tên sinh viên: Nguyễn Thanh Xuân
# Mã số sinh viên: B2106825
# STT: 26

from tkinter import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64

def hashing():
    content = plaintxt.get().encode()
    func = hashmode.get()
    if func == 0:
        result = MD5.new(content)
    if func == 1:
        result = SHA1.new(content)
    if func == 2:
        result = SHA256.new(content)
    if func == 3:
        result = SHA512.new(content)


    # Học viên tự cài đặt các phương thức cho SHA256 và SHA512
    rs = result.hexdigest().upper()
    hashtxt.delete(0,END)
    hashtxt.insert(INSERT,rs)
# ===============================================
# Giao diện
# ===============================================
#khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH BĂM",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)


plainlb = Label(window, text="Văn bản",font=("Arial", 14))
plainlb.grid(column=0, row=2)
plaintxt = Entry(window,width=60)
plaintxt.grid(column=1, row=2)



radioGroup= LabelFrame(window, text = "Hàm băm")
radioGroup.grid(row=3, column=1)
hashmode = IntVar()
hashmode.set(-1)

md5_func = Radiobutton(radioGroup, text="Hash MD5", font=("Times New Roman", 11), variable=hashmode, value=0, command=hashing)
md5_func.grid(row=4, column=0)

sha1_func = Radiobutton(radioGroup, text="Hash SHA1", font=("Times New Roman", 11), variable=hashmode, value=1, command=hashing)
sha1_func.grid(row=5, column=0)

# Tương tự đối với sha256 và sha512
sha256_func = Radiobutton(radioGroup, text="Hash SHA256", font=("Times New Roman", 11), variable=hashmode, value=2, command=hashing)
sha256_func.grid(row=6, column=0)

sha512_func = Radiobutton(radioGroup, text="Hash SHA512", font=("Times New Roman", 11), variable=hashmode, value=3, command=hashing)
sha512_func.grid(row=7, column=0)

hashlb = Label(window, text="Giá trị băm",font=("Arial", 14))
hashlb.grid(column=0, row=8)
hashtxt = Entry(window,width=60)
hashtxt.grid(column=1, row=8)


window.geometry('600x400')
window.mainloop()
