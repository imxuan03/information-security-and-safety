# Họ và tên sinh viên: Nguyễn Thanh Xuân
# Mã số sinh viên: B2106825
# STT: 26

from tkinter import *

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64

def save_file(data, mode, filepath):
    with open(filepath, mode) as file:
        file.write(data)

def generate_key():
    key = RSA.generate(1024)

    # Đường dẫn tệp bạn muốn lưu
    private_key_path = "private_key.pem"
    public_key_path = "public_key.pem"

    # Ghi khóa cá nhân vào tệp chỉ định
    save_file(key.exportKey('PEM'), 'wb', private_key_path)

    # Ghi khóa công khai vào tệp chỉ định
    save_file(key.publickey().exportKey('PEM'), 'wb', public_key_path)

    privatekeytext.delete('1.0', END)
    privatekeytext.insert(END, key.exportKey('PEM'))
    publickeytext.delete('1.0', END)
    publickeytext.insert(END, key.publickey().exportKey('PEM'))

def get_key(filename,key_style):
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

def mahoa_rsa():
    txt = plaintxt.get().encode()
    pub_key = get_key("public_key.pem","Public Key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

def giaima_rsa():
    txt = ciphertxt.get().encode()
    ciphertext = base64.decodebytes(txt)
    pri_key = get_key("private_key.pem", "Private Key")


    cipher = PKCS1_v1_5.new(pri_key)
    message = cipher.decrypt(ciphertext, None)

    deciphertxt.delete(0, END)
    deciphertxt.insert(INSERT, message)

#khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")
# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ BẤT ĐỐI XỨNG RSA",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)


plainlb = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb.grid(column=0, row=3)
plaintxt = Entry(window,width=60)
plaintxt.grid(column=1, row=3)


cipherlb = Label(window, text="Văn bản được mã hóa",font=("Arial", 14))
cipherlb.grid(column=0, row=4)
ciphertxt = Entry(window,width=60)
ciphertxt.grid(column=1, row=4)


decipherlb = Label(window, text="Văn bản được giải mã",font=("Arial", 14))
decipherlb.grid(column=0, row=5)
deciphertxt = Entry(window,width=60)
deciphertxt.grid(column=1, row=5)

privatekeylb = Label(window, text="Khóa cá nhân",font=("Arial", 14))
privatekeylb.grid(column=0, row=6)
privatekeytext = Text(window,width=60, height=10)
privatekeytext.grid(column=1, row=6)

publickeylb = Label(window, text="Khóa công khai",font=("Arial", 14))
publickeylb.grid(column=0, row=7)
publickeytext = Text(window, width=60, height=10)  # height có thể điều chỉnh
publickeytext.grid(column=1, row=7)


taokhoabtn = Button(window, text="Tạo khóa", width=10, command=generate_key)
taokhoabtn.grid(column=1, row=8)

mahoabtn = Button(window, text="Mã hóa", width=10, command=mahoa_rsa)
mahoabtn.grid(column=1, row=9)

giaimabtn = Button(window, text="Giải mã", width=10, command=giaima_rsa)
giaimabtn.grid(column=1, row=10)


window.geometry('800x600')
window.mainloop()
