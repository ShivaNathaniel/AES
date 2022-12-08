import numpy as np
import cv2
import aes
import ECB
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

a = aes.hex_to_bin(ECB.encryptECB(RGB_to_binl(red), key))
#print(a)
#1: ảnh sau khi mã hóa được cipher text
#2: chuyển cipher text về bin
#3: chuyển bin về dec

#dec_red = aes.bin_to_dec(aes.hex_to_bin(ECB.encryptECB(RGB_to_binl(red), key)))     #dec của red
#dec_green = aes.bin_to_dec(aes.hex_to_bin(ECB.encryptECB(RGB_to_binl(red), key)))   #dec của green
#dec_blue = aes.bin_to_dec(aes.hex_to_bin(ECB.encryptECB(RGB_to_binl(red), key)))    #dec của blue

#đưa về dạng ảnh
#img_red = (np.array([int(i) for i in dec_red],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
#img_green = (np.array([int(i) for i in dec_green],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
#img_blue = (np.array([int(i) for i in dec_blue],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])

b = aes.bin_to_dec(101001001001)
print(a)
#cv2.imshow('', img_red)