import numpy as np
import cv2
import decrypt_aes
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()        #viết hoa key

#tách thành 3 channel RGB của ảnh mã hóa
img = cv2.imread('anh_ma_hoa.png',1)
de_red = img[:, :, 2]
de_green = img[:, :, 1]
de_blue = img[:, :, 0]

def decrypt_image(s, n):
    lst_str = ''                                                 #đưa từ dec về hex của chuỗi trước giải mã
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            lst_str += decrypt_aes.bin_to_hex(np.binary_repr(s[i][j], width=8))
    a = []
    for i in range(0, len(lst_str), n):                          #chia thành các khối n phần tử đưa vào list
        a.append(lst_str[i:i + n])
    cp_decrypt = ''                                              #string lưu trữ cipher text sau giải mã
    for i in a:
        cp_decrypt += decrypt_aes.decrypt(i, key)
    dec_decrypt = []
    for i in range(0, len(cp_decrypt), 2):
        dec_decrypt.append(decrypt_aes.bin_to_dec(int(decrypt_aes.hex_to_bin(cp_decrypt[i:i+2]))))
    return dec_decrypt

#đưa về dạng dec của rgb
r = decrypt_image(de_red, 32)
g = decrypt_image(de_green, 32)
b = decrypt_image(de_blue, 32)

#đưa về dạng ảnh rgb greyscale
img_red_de = (np.array([int(i) for i in r],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
img_green_de = (np.array([int(i) for i in g],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
img_blue_de = (np.array([int(i) for i in b],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])

#merge 3 ảnh sau giải mã
img_de = cv2.merge([img_red_de, img_blue_de, img_green_de])

#lưu ảnh sau giải mã
cv2.imwrite('anh_giai_ma.png', img_de)

#cv2.imshow('', img_de)
#cv2.waitKey(0)