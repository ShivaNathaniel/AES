import encrypt_aes

#Input
#pt = 'truong dai hoc bach khoa ha noi'
#cp = '8BF00825E78895F7DC0A8CD28F67D62C5C13F82B5E390F45DC837E917B5D0A'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-d.txt', 'r', encoding = 'UTF-8') as cipher,open('output-d.txt', 'w', encoding = 'UTF-8') as text, open('key-d.txt', 'r', encoding = 'UTF-8') as k:
    cp = cipher.read()
    key = k.read()
    #Chia thanh cac khoi 8-bit
    def divide(s):      
        a = []
        for i in range(0, len(s), 2):       
            a.append(s[i:i + 2])
        return a

    def decryptCFB(cp, key):
        IV = '0123456789abcdeffedcba9876543210' #vecto khởi tạo
        cp = cp.upper()
        key = key.upper()
        IV = IV.upper()
        reg = encrypt_aes.encrypt(IV, key)  #mã hóa vecto khởi tạo được thanh ghi
        c = divide(cp)
        pt = ''
        p = encrypt_aes.xor_hex(c[0], reg[0:2]) #xor khối bản mã đầu với 8bit của
        pt += p                              #thanh ghi được khối bản rõ đầu
        for i in range(1, len(c)):
            reg = reg[2:] + c[i-1]      #dịch vòng trái 8bit của thanh ghi
            reg = encrypt_aes.encrypt(reg, key) 
            p = encrypt_aes.xor_hex(c[i], reg[0:2]) #xor từng khối bản mã với 8 bit
            pt += p                         #đầu của thanh ghi
        pt = encrypt_aes.hex_to_text(pt)
        return pt
    pt = decryptCFB(cp, key)
    #pt = decrypt_aes.hex_to_text(pt)
    text.write(pt)

#print(decryptCFB(cp, key) + '!')

