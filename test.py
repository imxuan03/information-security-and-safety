# def Char2Num(num):
#     return ord(num)-65


# def Num2Char(num):
#     return chr(num+65)


# def mahoa(text, buoc):
    
#     ciphertext =''
#     for i in text:
#         x =  (Char2Num(i)+buoc) % 26
#         ciphertext += Num2Char(x)

#     return ciphertext

# def giaima(text, buoc):
    
#     decrypted_text =''
#     for i in text:
#         x =  (Char2Num(i)-buoc) % 26
#         decrypted_text += Num2Char(x)

#     return decrypted_text


# mahoa = mahoa('ABCHELOOOO', 3)
# print(mahoa)
# giaima = giaima(mahoa, 3)
# print(giaima)


from sympy import Matrix

# Ma trận khóa K
K = Matrix([[17, 17, 5],
            [21, 18, 21],
            [2, 2, 19]])

import numpy as np

# Tính ma trận nghịch đảo theo mod 26
try:
    K_inv_mod = K.inv_mod(26)
    print("Ma trận nghịch đảo của K theo mod 26 là:")
    print(np.array(K_inv_mod))

except ValueError as e:
    print(e)