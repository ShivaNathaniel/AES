#from PIL import Image
import numpy as np
import cv2
import aes
key = '0f1571c947d9e8590cb7add6af7f6798'
key = key.upper()

img = cv2.imread('anh_test.jpg',0)

#cv2.imshow('original',img)
#cv2.waitKey(0)

lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        lst.append((np.binary_repr(img[i][j],width = 8))) #tra ve 8 bit nhi phan

print(len(lst))
eight_b_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128 ).reshape(img.shape[0],img.shape[1])
seven_b_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64 ).reshape(img.shape[0],img.shape[1])
six_b_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32 ).reshape(img.shape[0],img.shape[1])
five_b_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16 ).reshape(img.shape[0],img.shape[1])
four_b_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8 ).reshape(img.shape[0],img.shape[1])
three_b_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4 ).reshape(img.shape[0],img.shape[1])
two_b_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2 ).reshape(img.shape[0],img.shape[1])
one_b_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1 ).reshape(img.shape[0],img.shape[1])

cv2.imshow('bit plain 7',cv2.normalize(eight_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 6',cv2.normalize(seven_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 5',cv2.normalize(six_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 4',cv2.normalize(five_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 3',cv2.normalize(four_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 2',cv2.normalize(three_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 1',cv2.normalize(two_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.imshow('bit plain 0',cv2.normalize(one_b_img,np.zeros(img.shape),0,255,cv2.NORM_MINMAX))
cv2.waitKey(0)

