import numpy as np
def pad(s):
    # Them vao dau so con thieu de du boi 8 bit
    return (8 - len(s)% 8)* "0" + s

def lay_cot_thanh_hang(cot,bang):
    list_cot= []
    for row in range(8):
        for col in range(8):
            if cot == col:
                list_cot.append(bang[row][col])
    cot_nguoc = "".join(list_cot[::-1]) #reverse
    return cot_nguoc

def lay_cot_thanh_hang_Decrypt(cot,bang):
    list_cot= []
    for row in range(4):
        for col in range(8):
            if cot == col:
                list_cot.append(bang[row][col])
    cot= "".join(list_cot)
    return cot

def Encrypt_IP(plaintxt):
    # tao bang cho plaintext
    txt = plaintxt
    tach_64bit_txt= []
    PLaintext = []
    IP=[]
    while len(txt)>= 8:
        tach_64bit_txt.append(txt[:8])
        txt= txt[8:]
    tach_64bit_txt.append(txt)

    for i in tach_64bit_txt[0]:
        nhi_phan = pad(format(ord(i),"b"))
        PLaintext.append(nhi_phan)
    print("plain text:\n",PLaintext)
    for i in range(8):
        if i%2 !=0:
            IP.append(lay_cot_thanh_hang(i,PLaintext))
    for i in range(8):
        if i%2 ==0:
            IP.append(lay_cot_thanh_hang(i,PLaintext))
    return IP

def Decrypt_IP(bang_nhi_phan):
    IP_temp=[]
    IP_rs=[]
    for row in range(4):
        hang1 = np.array(list(bang_nhi_phan[row+4][:]))
        hang2 = np.array(list(bang_nhi_phan[row][:]))
        IP_1 = np.stack((hang1,hang2),axis=1)
        a = ["".join(i) for i in IP_1]
        IP_temp.append(a)
    for i in range(8):
        IP_rs.append(lay_cot_thanh_hang_Decrypt(i,IP_temp))
    return IP_rs[::-1] #reverse



pltxt = "Xin chao toi ten la Nguyen Thanh Hieu"

IP= Encrypt_IP(pltxt)
print(IP)

de = Decrypt_IP(IP)
print(de)
