from sympy import Matrix
import numpy as np

# Ma trận khóa K
K = Matrix([
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19]
])

K_inv_mod = K.inv_mod(26)

print(np.array(K_inv_mod))


def Char2Num(text):
    results = []
    for c in text:
        e =  ord(c)-65
        results.append(e)

    return results

def Num2Char(num):
    results = ''
    for c in num:
        results += chr(int(c) + 65)  # Chuyển đổi từng số thành ký tự
    return results

def mahoa(message, K):
    ciphertex = ''
    #Group 3
    for i in range(0, len(message), 3):

        group = message[i:i+3]

        while len(group)<3:
            group+='X'


        P = np.array(Char2Num(group)).reshape(3,1)
        dec = np.dot(K, P) % 26

        ciphertex += Num2Char(dec)
    return ciphertex
        
def giaima(message, K_inv_mod):
    decrypted_mess = ''
    #Group 3
    for i in range(0, len(message), 3):

        group = message[i:i+3]

        P = np.array(Char2Num(group)).reshape(3,1)
        dec = np.dot(K_inv_mod, P) % 26

        decrypted_mess += Num2Char(dec)
    return decrypted_mess



message = "HELLOEVERYONE"
mahoa = mahoa(message, K)
print(mahoa)
giaima = giaima(mahoa, K_inv_mod)
print(giaima)
