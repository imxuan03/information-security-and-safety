from tkinter import *
from Crypto.Cipher import DES
import base64

def pad(s):
    # Them vao cuoi so con thieu, cho du boi cua 8
    return s + (8-len(s)%8) * chr(8-len(s)%8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def mahoa_DES(plaintxt, key):
    key = pad(key).encode("utf-8")
    plaintxt = pad(plaintxt).encode("utf-8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(plaintxt)
    entxt = base64.b64encode(entxt)
    return entxt.decode("utf-8")
def giaima_DES(ciphertxt, key):
    key = pad(key).encode("utf-8")
    ciphertxt = base64.b64decode(ciphertxt)
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(ciphertxt))
    return detxt.decode("utf-8")

# Doc file tu du lieu country vao
def read_file(input_file):
    with open(input_file, 'r') as f:
        countries = f.read()

    results = []
    text = countries.split('\n')
    
    for ten in text:
        if len(ten)>0:
            c = ten.split(',')[1]
            if len(c)<8 :
                results.append(c)
    return results[1:]

countries = read_file('country.csv')
plaintext1 = 'The treasure is under the coconut tree'
encryt1 = 'lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=='

encryt2 = 'LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=='
encryt3 = '5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9'

key = ''
for country in countries:
    if mahoa_DES(plaintext1, country) == encryt1:
        key = country
        print("Key la: ", country)
        break


print("Giai ma van ban 2 la: ", giaima_DES(encryt2,key))
print("Giai ma van ban 3 la: ", giaima_DES(encryt3,key))


