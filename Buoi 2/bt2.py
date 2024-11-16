from tkinter import *
from Crypto.Cipher import DES
import base64

def pad(s):
    # Them vao cuoi so con thieu, cho du boi cua 8
    return s + (8-len(s)%8) * chr(8-len(s)%8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES(plaintxt, key):
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(plaintxt)
    entxt = base64.b64encode(entxt)
    return entxt


def giaima_DES(ciphertxt, key):
    ciphertxt = base64.b64decode(ciphertxt)
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(ciphertxt))
    return detxt


def mahoa_file(input_file, output_file, key):
    with open(input_file, 'r') as f:
        plaintext = f.read()

    padded_text = pad(plaintext).encode("utf-8")
    key = pad(key).encode("utf-8")

    encrypted_text = mahoa_DES(padded_text, key)

    with open(output_file, 'wb') as f:
        f.write(encrypted_text)


def giaima_file(input_file, output_file, key):
    with open(input_file, 'r') as f:  # Đọc dưới dạng bytes
        ciphertext = f.read()

    key = pad(key).encode("utf-8")

    decrypted_text = giaima_DES(ciphertext, key)  # Gọi hàm giải mã đúng

    with open(output_file, 'wb') as f:  # Ghi dưới dạng chuỗi
        f.write(decrypted_text)

# Sử dụng chương trình
input_file = 'text.txt'  # Đường dẫn tới file văn bản gốc
output_file = 'mahoa.txt'  # Đường dẫn tới file chứa văn bản đã mã hóa
key = 'ascadfs'  # Khóa bí mật (phải có độ dài 8 bytes)

mahoa_file(input_file, output_file, key)

output_file_giaima = 'giaima.txt'
giaima_file(output_file, output_file_giaima, key)
print(f'Mã hóa xong. Kết quả đã được lưu vào {output_file}.')