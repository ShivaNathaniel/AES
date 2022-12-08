import aes

#input
#pt = 'truong dai hoc bach khoa ha noi'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-e.txt', 'r', encoding = 'UTF-8') as text,open('output-e.txt', 'w', encoding = 'UTF-8') as cipher, open('key-e.txt', 'r', encoding = 'UTF-8') as k:
    pt = text.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):                  
        a = []
        count = 0
        for i in range(0, len(s), n):   #chia thành các khối n phần tử đưa vào list
            a.append(s[i:i + n])
        for i in range(len(a)):
            if len(a[i]) < n:
                a[i] += '8'             #padding thêm bit, bit đầu là 1
                count += 1              #các bit còn lại là 0
                for j in range(0, n):
                    if len(a[i]) == n:
                        break
                    a[i] += '0'
                    count += 1          #lưu lại count là giá trị bit
        return [a, count]               #đã padding thêm

    #count = divide(aes.text_to_hex(pt), 32)[1]

    #encrypt CBC
    def encryptCBC(pt, key):
        pt = aes.text_to_hex(pt)        #chuyển kí tự ASCII về hexa
        pt = pt.upper()
        key = key.upper()
        IV = '0123456789abcdeffedcba9876543210'     #vecto khởi tạo
        IV = IV.upper()
        p = divide(pt, 32)[0]            #chia bản rõ thành các khối 128bit     
        pre_c = aes.xor_hex(p[0], IV)    #xor khối bản rõ đầu với vecto khởi tạo
        cr = aes.encrypt(pre_c, key)     #khối bản mã đầu tiên  
        c = []
        c.append(cr)
        cp = ''
        for i in range(1, len(p)):      
            pr = aes.xor_hex(p[i], cr)  #xor từng khối của bản rõ với khối bản mã trước đó
            cr = aes.encrypt(pr, key)   #mã hóa khối bản mã mới sau khi xor
            c.append(cr)
        for i in range(len(c)):         #ghép các khối bản mã để được output
            cp += c[i]
        return cp
    cp = encryptCBC(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)
    #print(encryptCBC(pt, key))
    #print(count)




