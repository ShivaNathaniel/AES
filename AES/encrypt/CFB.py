import aes

#input
#pt = 'truong dai hoc bach khoa ha noi'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-e.txt', 'r', encoding = 'UTF-8') as text,open('output-e.txt', 'w', encoding = 'UTF-8') as cipher, open('key-e.txt', 'r', encoding = 'UTF-8') as k:
    pt = text.read()
    key = k.read()
    #Chia thanh cac khoi 8-bit
    def divide(s):
        a = []
        for i in range(0, len(s), 2):
            a.append(s[i:i + 2])
        return a

    #Encrypt
    def encryptCFB(pt, key):
        IV = '0123456789abcdeffedcba9876543210'         #vecto khởi tạo
        pt = aes.text_to_hex(pt)        #chuyển kí tự ASCII về hexa
        pt = pt.upper()
        key = key.upper()
        IV = IV.upper()
        reg = aes.encrypt(IV, key)      #mã hóa aes tạo thanh ghi 128bit
        p = divide(pt)
        cp = ''
        c = aes.xor_hex(p[0], reg[0:2]) #xor 8bit đầu của tnh ghi với khối bản rõ đầu
        cp += c                         #được khối bản mã đầu tiên
        for i in range(1, len(p)):
            reg = reg[2:] + c           #dịch vòng trái 8 bit của thanh ghi
            reg = aes.encrypt(reg, key)
            c = aes.xor_hex(p[i], reg[0:2]) #xor từng khối bản rõ với
            cp += c                         #8bit đầu của thanh ghi
        return cp
    cp = encryptCFB(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)

#print(encryptCFB(pt, key))





