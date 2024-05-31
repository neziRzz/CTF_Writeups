def swapNibbles(x):
    return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 )
encrypt = ["a"]*24
dest = "44 93 51 42 24 45 2E 9B 01 99 7F 05 4D 47 25 43 A2 E2 3E AA 85 99 18 7E"
key = "reversing_is_pretty_cool"
b = bytes.fromhex(dest)
for i in range(len(b)):
    encrypt[i] = b[i] ^ ord(key[i])
    encrypt[i] = swapNibbles(encrypt[i])
print("KCSC{",end='')    
for i in range(len(encrypt)):
    print(chr(encrypt[i]),end='')    
print("}")
