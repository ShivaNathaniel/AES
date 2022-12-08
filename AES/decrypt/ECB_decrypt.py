import decrypt_aes

#Input
#pt = 'dai hoc bach khoa ha noi'
#cp = '6AFD9025724CECFB672A5354FA37D324BF5D97AF37C51E193C912E7DB1F28C59'
#key = '0f1571c947d9e8590cb7add6af7f6798'
#count = 16

with open('input-d.txt', 'r', encoding = 'UTF-8') as cipher,open('output-d.txt', 'w', encoding = 'UTF-8') as text, open('key-d.txt', 'r', encoding = 'UTF-8') as k:
    cp = cipher.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        for i in range(0, len(s), n):      #chia thành các khối n phần tử
            a.append(s[i:i + n])
        return a

    #decrypt
    def decryptECB(cp, key):
        cp = cp.upper()
        key = key.upper()
        c = divide(cp, 32)          #chia bản mã thành các khối 128bit
        p = []
        pt = ''
        for i in range(len(c)):     #giải mã từng khối bản mã để được bản rõ
            p.append(decrypt_aes.decrypt(c[i], key))
        for i in range(len(p)):
            pt += p[i]
        #pt = pt[:len(pt) - count]
        pt = decrypt_aes.hex_to_text(pt)    #chuyển kí tự hex về ASCII
        return pt
    pt = decryptECB(cp, key)
    #pt = decrypt_aes.hex_to_text(pt)
    text.write(pt)

#print(decryptECB(cp, key) + '!')
