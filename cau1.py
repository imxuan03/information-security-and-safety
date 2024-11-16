import random

def generate_cipher(plaintext, salt):
    len_plaintext = len(plaintext)

    while len(salt) < len_plaintext - 1:
        char = chr(random.randint(65, 90))  
        if char not in salt: 
            salt += char

    cipher = []


    for i in range(len_plaintext):
        cipher.append(plaintext[i])

        if i < len(salt):
            cipher.append(salt[i])
                    
    return ''.join(cipher)

plaintext = "ATBMTT"
salt = "DHCT"
cipher = generate_cipher(plaintext, salt)
print("Cipher:", cipher)