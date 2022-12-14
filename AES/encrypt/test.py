import aes
import cv2

a = [123, 356, 48, 56, 82, 104, 58, 90]
for i in a:
    cipher_hex = ''  # đưa từ dec về hex của chuỗi trước giải mã
    cipher_hex += (aes.bin_to_hex(aes.dec_to_bin(i)))
b = []
for i in range(0, len(cipher_hex), 32):  # chia thành các khối n phần tử đưa vào list
    b.append(cipher_hex[i:i + 32])
print(cipher_hex)
print(b)