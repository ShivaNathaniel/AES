import numpy as np
import cv2
import decrypt_aes
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()        #viết hoa key

def decrypt_image(s):
    cipher_hex = []
    for i in s:
        cipher_hex.append(decrypt_aes.bin_to_hex(decrypt_aes.dec_to_bin(s)))
    return cipher_hex
b = [12345679098]
a = decrypt_image(b)
print(a)