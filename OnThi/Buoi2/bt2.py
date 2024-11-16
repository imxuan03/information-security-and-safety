from tkinter import *
from Crypto.Cipher import DES
import base64

def pad(s):
    # Them vao cuoi so con thieu, cho du boi cua 8
    return s + (8-len(s)%8) * chr(8-len(s)%8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES(inputfile, outputfile, key):
    with open(inputfile, 'r') as f:
        txt = f.read()
        
    
    txt = pad(txt).encode("utf8")
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)

    with open(outputfile, 'wb') as f:
        f.write(entxt)

def giaima_DES(inputfile, outputfile, key):
   
    
    
    with open(inputfile, 'r') as f:
        ciphertext = f.read()

    txt = base64.b64decode(ciphertext)
    key = pad(key).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))

    with open(outputfile, 'wb') as f:
        f.write(detxt)




# Sử dụng chương trình
input_file = 'text.txt'  # Đường dẫn tới file văn bản gốc
output_file = 'mahoa.txt'  # Đường dẫn tới file chứa văn bản đã mã hóa
key = 'ascadfs'  # Khóa bí mật (phải có độ dài 8 bytes)
output_file_giaima = 'giaima.txt'

mahoa_DES(input_file, output_file, key)
giaima_DES(output_file, output_file_giaima, key)