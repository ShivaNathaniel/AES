import numpy as np
import cv2
import aes
import decrypt_aes
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()        #viết hoa key

#tách thành 3 channel RGB
img = cv2.imread('amongus.png',1)
red = img[:, :, 2]
green = img[:, :, 1]
blue = img[:, :, 0]

#lưu ma trận ảnh về chuỗi hex
def RGB_to_binl(n):
    lst_str = ''
    for i in range(n.shape[0]):
        for j in range(n.shape[1]):
            lst_str += aes.bin_to_hex(np.binary_repr(n[i][j], width=8))
    return lst_str

#chia thành các khối
def encypt_image(s, n):
    a = []
    for i in range(0, len(s), n):            #chia thành các khối n phần tử đưa vào list
        a.append(s[i:i + n])
    for i in range(len(a)):
        if len(a[i]) < n:                    #padding thêm bit, bit đầu là 1
            a[i] += '8'                      #các bit còn lại là o cho đến khi đủ 128bit
            for j in range(0, n):
                if len(a[i]) == n:
                    break
                a[i] += '0'
    cp_encrypt = ''                          #string lưu trữ cipher text sau mã hóa
    for i in a:
        cp_encrypt += aes.encrypt(i, key)
    dec_encrypt = []                         #đưa cipher text về dec
    for i in range(0, len(cp_encrypt), 2):
        dec_encrypt.append(aes.bin_to_dec(int(aes.hex_to_bin(cp_encrypt[i:i+2]))))
    return dec_encrypt

#1: ảnh sau khi mã hóa được cipher text
#2: chuyển cipher text về bin
#3: chuyển bin về dec

dec_red = []
dec_green = []
dec_blue = []
dec_red = encypt_image(RGB_to_binl(red), 32)        #dec của red
dec_green = encypt_image(RGB_to_binl(green), 32)    #dec của green
dec_blue = encypt_image(RGB_to_binl(blue), 32)      #dec của blue

#đưa về dạng ảnh
img_red = (np.array([int(i) for i in dec_red],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
img_green = (np.array([int(i) for i in dec_green],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
img_blue = (np.array([int(i) for i in dec_blue],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])

#merge 3 ảnh sau mã hóa
#img_en = cv2.merge([img_red, img_blue, img_green])

#show ảnh
#cv2.imshow('encrypt',cv2.normalize(img_en,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.waitKey(0)

#decrypt
#s là dạng ảnh
def decrypt_image(s, n):
    lst_str = ''                                                        #đưa từ dec về hex của chuỗi trước giải mã
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            lst_str += aes.bin_to_hex(np.binary_repr(s[i][j], width=8))
    a = []
    for i in range(0, len(lst_str), n):                         # chia thành các khối n phần tử đưa vào list
        a.append(lst_str[i:i + n])
    cp_decrypt = ''                                            # string lưu trữ cipher text sau giải mã
    for i in a:
        cp_decrypt += decrypt_aes.decrypt(i, key)
    dec_decrypt = []
    for i in range(0, len(cp_decrypt), 2):
        dec_decrypt.append(decrypt_aes.bin_to_dec(int(decrypt_aes.hex_to_bin(cp_decrypt[i:i+2]))))
    return dec_decrypt

#đưa về dạng dec của rgb
r = decrypt_image(img_red, 32)
g = decrypt_image(img_green, 32)
b = decrypt_image(img_blue, 32)

#đưa về dạng ảnh rgb greyscale
img_red_de = (np.array([int(i) for i in r],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
img_green_de = (np.array([int(i) for i in g],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
img_blue_de = (np.array([int(i) for i in b],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])

#merge 3 ảnh sau giải mã
img_de = cv2.merge([img_red_de, img_blue_de, img_green_de])

cv2.imshow('', img_de)
cv2.waitKey(0)
