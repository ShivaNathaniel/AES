import aes

with open('input-e.txt', 'r', encoding = 'UTF-8') as text,open('output-e.txt', 'w', encoding = 'UTF-8') as cipher, open('key-e.txt', 'r', encoding = 'UTF-8') as k:
    pt = text.read()
    #chuyển từ text về hex
    def text_to_hex(s):
        d = ''
        c = []
        for i in s:
            c.append(hex(ord(i)))
        for i in range(len(c)):
            c[i] = c[i].replace('0x', '')
        for i in range(len(c)):
            if len(c[i]) == 1:
                c[i] = '0' + c[i]
        d = []                          #viết hoa hexa
        for i in c:
            d.append(i.upper())
        return d

    #chuyển từ hex về text
    def hex_to_text(s):
        hex_pt = []
        text = ''
        for i in s:
            hex_pt.append(aes.bin_to_dec(int(aes.hex_to_bin(s))))
        for i in range(len(hex_pt)):
            text += chr(hex_pt[i])
        return text

    # hexa lưu dưới dạng list để đánh dấu chữ có dấu
    b = text_to_hex(pt)

    # đếm chiều dài 1 phần tử trong list hexa
    count_index = []
    for i in b:
        count_index.append(len(i))

    #lưu hex dưới dạng str
    str_hex = ''
    for i in b:
        str_hex += i

    #cắt str theo chiều dài đã lưu trước đó
    #trả về lst_cut
    #cut sai :))
    lst_cut = []
    for j in count_index:
        f = slice(j)
        lst_cut.append(str_hex[f])
        str_hex = str_hex.replace(str_hex[f], '')


    print(count_index)


   # c = hex_to_text(b)
   # print(l)
