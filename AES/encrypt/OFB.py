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
    def encryptOFB(pt, key):
        nonce = '0123456789abcdeffedcba9876543210'
        pt = aes.text_to_hex(pt)    #chuyển kí tự ASCII sang hexa
        pt = pt.upper()
        key = key.upper()
        nonce = nonce.upper()
        out = nonce
        p = divide(pt, 32)          #chia thành các khối 128bit
        cp = ''
        for i in range(len(p)):
            if i == len(p) - 1:     #đối với khối cuối (chứa < 128bit)
                out = aes.encrypt(out, key)         
                c = aes.xor_hex(out[:len(p[i])], p[i]) #xor khối cuối với số bit
                cp += c                                 #tương ứng của thanh ghi
                break
            out = aes.encrypt(out, key)         #mã hóa thanh ghi 
            c = aes.xor_hex(p[i], out)      #xor từng khối bản rõ với
            cp += c                         #thanh ghi đã mã hóa
        return cp
    cp = encryptOFB(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)

#print(encryptOFB(pt, key))








