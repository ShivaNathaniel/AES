import aes

#Input
#pt = 'dai hoc bach khoa ha noi'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-e.txt', 'r', encoding = 'UTF-8') as text,open('output-e.txt', 'w', encoding = 'UTF-8') as cipher, open('key-e.txt', 'r', encoding = 'UTF-8') as k:
    pt = text.read()
    key = k.read()
    #Chia thanh cac khoi
    def divide(s, n):
        a = []
        count = 0
        for i in range(0, len(s), n):   #chia thành các khối n phần tử đưa vào list
            a.append(s[i:i + n])        
        for i in range(len(a)):
            if len(a[i]) < n:           #padding thêm bit, bit đầu là 1 
                a[i] += '8'             #các bit còn lại là o cho đến khi đủ 128bit
                count += 1
                for j in range(0, n):
                    if len(a[i]) == n:
                        break
                    a[i] += '0'         
                    count += 1          #lưu lại giá trị count là số lượng đã
        return [a, count]               #padding thêm

    count = divide(aes.text_to_hex(pt), 32)[1]
    #Encrypt ECB
    def encryptECB(pt, key):
        pt = aes.text_to_hex(pt)        #chuyen ki tu ASCII về hexa
        pt = pt.upper()
        key = key.upper()
        p = divide(pt, 32)[0]           #chia input thành các khối 16byte
        c = []
        cp = ''
        for i in range(len(p)):         #mã hóa từng khối trong list p
            c.append(aes.encrypt(p[i], key))
        for i in range(len(c)):         #ghép các khối bản mã lại để được output
            cp += c[i]
        return cp
    cp = encryptECB(pt, key)
    #cp = aes.hex_to_text(cp)
    cipher.write(cp)

#print(encryptECB(pt, key))
#print(count)


