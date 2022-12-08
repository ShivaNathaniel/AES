#from PIL import Image
import numpy as np
import cv2
import aes_function
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()
img = cv2.imread('tiger_gray.jpg',0)
#cv2.imshow('original',img)
#cv2.waitKey(0)

lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append((np.binary_repr(img[i][j],width = 8)))#tra ve 8 bit nhi phan

#eight_b_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128 ).reshape(img.shape[0],img.shape[1])
seven_b_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64 ).reshape(img.shape[0],img.shape[1])
#six_b_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32 ).reshape(img.shape[0],img.shape[1])
#five_b_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16 ).reshape(img.shape[0],img.shape[1])
#four_b_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8 ).reshape(img.shape[0],img.shape[1])
#three_b_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4 ).reshape(img.shape[0],img.shape[1])
#two_b_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2 ).reshape(img.shape[0],img.shape[1])
#one_b_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1 ).reshape(img.shape[0],img.shape[1])

#enjoy the show
#cv2.imshow('bit plain 7',cv2.normalize(eight_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 6',cv2.normalize(seven_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.imshow('bit plain 5',cv2.normalize(six_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.imshow('bit plain 4',cv2.normalize(five_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.imshow('bit plain 3',cv2.normalize(four_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.imshow('bit plain 2',cv2.normalize(three_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.imshow('bit plain 1',cv2.normalize(two_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.imshow('bit plain 0',cv2.normalize(one_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
#cv2.waitKey(0)

# test encrypt one bit image
b_lst = '' # chuoi bit
for i in range(seven_b_img.shape[0]):
    for j in range(seven_b_img.shape[1]):
        b_lst += np.binary_repr(seven_b_img[i][j],width = 7)

h_lst =[]  #list de luu cac block 128 bit
for i in range(0,len(b_lst),8):
    h_lst.append(b_lst[i:i+8])
#padding turn 1
m = len(h_lst) - 1
n = len(h_lst[m])
if(n!=8):
    h_lst[m] = h_lst[m] + '1'
    for i in range(8 - n - 1):
        h_lst[m] = h_lst[m] + '0'
#chuyen ve hexa
q_lst =''#chuoi hexa
for i in range(len(h_lst)):
   q_lst += aes_function.bintohex(h_lst[i])

#chia thanh cac block 128 bit
block =[]
for i in range(0,len(q_lst),32):
    block.append(q_lst[i:i+32])

m = len(block)-1
#padding turn 2
n = len(block[m])
if n != 32:
    block[m] += '8'
    for i in range(32 - n - 1):
        block[m] += '0'

#aes encryption
e_lst ='' #cipher string
for i in block :
    e_lst += aes_function.encrypt(i,key)
# go padding
e_lst = e_lst[:len(e_lst) - (32 - n)]

#chia ve cac khoi hexa
he_lst =''
for i in range(0,len(e_lst),2):
    he_lst += aes_function.hextobin(e_lst[i:i+2])
#go paddig #2
he_lst = he_lst[:len(he_lst) -(8 - n)]
#test
test_lst =[]
for i in range(0,len(he_lst),7):
    test_lst.append(int(he_lst[i:i+7]))
print(test_lst)
#khoi cuoi cung
cipher_lst =[]
for i in range(0,len(he_lst),7):
    cipher_lst.append(aes_function.bintodec(int(he_lst[i:i+7])))

e_one_b_img = (np.array([int(i) for i in cipher_lst],dtype = np.uint8) ).reshape(img.shape[0],img.shape[1])
print(e_one_b_img)
cv2.imshow('encrypt bit plain 8',cv2.normalize(e_one_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.waitKey(0)