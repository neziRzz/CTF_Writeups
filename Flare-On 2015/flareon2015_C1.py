data="1F 08 13 13 04 22 0E 11 4D 0D 18 3D 1B 11 1C 0F 18 50 12 13 53 1E 12 10" 
b=bytes.fromhex(data)
for i in range(len(b)):
    print(chr((b[i])^0x7D),end='')
