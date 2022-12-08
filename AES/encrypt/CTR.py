import aes

#input
#pt = 'dai hoc bach khoa ha noi he thong nhung iot'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-e.txt', 'r', encoding = 'UTF-8') as text,open('output-e.txt', 'w', encoding = 'UTF-8') as cipher, open('key-e.txt', 'r', encoding = 'UTF-8') as k:
    pt = text.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        for i in range(0, len(s), n):           #Chia thanh cac khoi n-bit
            a.append(s[i:i + n])                ##khoi cuoi < n-bit khong padding
        return a

    #Encrypt
    def encryptCTR(pt, key):
        ctr = '0123456789abcdeffedcba9876543210'    #thanh ghi đầu
        pt = aes.text_to_hex(pt)        #chuyển kí tự ASCII về hexa
        pt = pt.upper()
        key = key.upper()
        ctr = ctr.upper()
        p = divide(pt, 32)              #chia thành các khối 128bit
        out_ctr = ctr
        cp = ''
        for i in range(len(p)):
            if i == len(p) - 1:         #xử lí khối cuối cùng (len < 128bit)
                out_ctr = aes.encrypt(out_ctr, key)
                c = aes.xor_hex(out_ctr[:len(p[i])], p[i])
                cp += c
                break
            out_ctr = aes.encrypt(out_ctr, key)     #mã hóa thanh ghi
            c = aes.xor_hex(p[i], out_ctr)          #từng khối bản rõ xor với
            cp += c                                 #thanh ghi đã mã hóa
            out_ctr = aes.add_hex(out_ctr, '1') #cộng thanh ghi thêm 1 bit
        return cp
    cp = encryptCTR(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)

#print(encryptCTR(pt, key))
