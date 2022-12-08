import encrypt_aes

#input
#pt = 'dai hoc bach khoa ha noi he thong nhung iot'
#cp = '9B6AED6A603CDC5C0B55C82B447FE7D680C5B2910045FD78262A11310F9EBC3EF982B066BF555A64379FD0'
#key = '0f1571c947d9e8590cb7add6af7f6798'

with open('input-d.txt', 'r', encoding = 'UTF-8') as cipher,open('output-d.txt', 'w', encoding = 'UTF-8') as text, open('key-d.txt', 'r', encoding = 'UTF-8') as k:
    cp = cipher.read()
    key = k.read()
    #Chia thanh cac khoi n-byte (8*n-bit)
    def divide(s, n):
        a = []
        for i in range(0, len(s), n):           #Chia thanh cac khoi n-bit
            a.append(s[i:i + n])                ##khoi cuoi < n-bit khong padding
        return a

    #decrypt
    def decryptCTR(cp, key):
        ctr = '0123456789abcdeffedcba9876543210'    #thanh ghi khởi tạo
        cp = cp.upper()
        key = key.upper()
        ctr = ctr.upper()
        c = divide(cp, 32)  #chia bản mã thành các khối 128bit (32 số hexa)
        out_ctr = ctr
        pt = ''
        for i in range(len(c)):
            if i == len(c) - 1:     #xử lí với khối bản mã cuối( < 128bit)
                out_ctr = encrypt_aes.encrypt(out_ctr, key)
                p = encrypt_aes.xor_hex(out_ctr[:len(c[i])], c[i])
                pt += p
                break
            out_ctr = encrypt_aes.encrypt(out_ctr, key) #mã hóa thanh ghi rồi xor với
            p = encrypt_aes.xor_hex(c[i], out_ctr)      #khối bản mã tương ứng thứ i
            pt += p
            out_ctr = encrypt_aes.add_hex(out_ctr, '1') #cộng thanh ghi thêm 1bit
        pt = encrypt_aes.hex_to_text(pt)
        return pt
    pt = decryptCTR(cp, key)
    #pt = decrypt_aes.hex_to_text(pt)
    text.write(pt)

#print(decryptCTR(cp, key) + '!')
