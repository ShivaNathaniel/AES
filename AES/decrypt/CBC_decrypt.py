import decrypt_aes

#Input
#pt = 'truong dai hoc bach khoa ha noi'
#cp = '79FC846713BD338C765B2F82003E1A4FACB5F32ED763343263E10AAEF27789D6'
#key = '0f1571c947d9e8590cb7add6af7f6798'
#count = 2

with open('input-d.txt', 'r', encoding = 'UTF - 8') as cipher,open('output-d.txt', 'w', encoding = 'UTF - 8') as text, open('key-d.txt', 'r', encoding = 'UTF - 8') as k:
    cp = cipher.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        for i in range(0, len(s), n):   #chia thành các khối n phần tử
            a.append(s[i:i + n])
        return a

    def decryptCBC(cp, key):
        cp = cp.upper()
        key = key.upper()
        IV = '0123456789abcdeffedcba9876543210' #vecto khởi tạo
        IV = IV.upper()
        c = divide(cp, 32)
        pre_p = decrypt_aes.decrypt(c[0], key)  #giải mã khối bản mã đầu tiên
        p = []                                  #sau đó xor với vecto khởi tạo 
        pt = ''                                 #để được khối bản mã đầu
        pr = decrypt_aes.xor_hex(pre_p, IV)
        p.append(pr)
        for i in range(1, len(c)):
            pre_p = decrypt_aes.decrypt(c[i], key)      #giải mã từng khối bản mã thứ i
            pr = decrypt_aes.xor_hex(pre_p, c[i - 1])   #xor với khối bản mã thứ i-1
            p.append(pr)                                #để được từng khối bản rõ
        for i in range(len(p)):
            pt += p[i]
        #pt = pt[:len(pt) - count]
        pt = decrypt_aes.hex_to_text(pt)
        return pt
    pt = decryptCBC(cp, key)
    #pt = decrypt_aes.hex_to_text(pt)
    text.write(pt)

#print(decryptCBC(cp, key) + '!')