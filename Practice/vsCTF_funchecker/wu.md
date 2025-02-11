# Mics
# Detailed Analysis
# Script and Flag
```python
def rol(val, bits, bit_size):
    return (val << bits % bit_size) & (2 ** bit_size - 1) | \
           ((val & (2 ** bit_size - 1)) >> (bit_size - (bits % bit_size)))
def ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))
dest = [0xFA97D8710C8B9B54, 0xEB82CC74589FDA54, 0xEE928C654D8BDF01, 0x5A35D0732E291BFE, 0xFF879860199F9E01, 0x690AEC7CD215D8FE, 0x7D0FB86893159CAB, 0x0F30C0333F3C0FFF, 0xBEC388645CDA9F54, 0x0F30C0333F3C0FFF,
0x5F2590623B3D1EAB, 0xC9A8E47EF0B75854, 0x226E7C5ABD78D301, 0xDDADB06AB1B71C01, 0x5F61C4322E6D4FAA, 0x6C1AAC6DC701DDAB, 0x0F7494632A6C5EFE, 0xEB82CC74589FDA54, 0x226E7C5ABD78D301, 0xBBD3C87549CE9A01,
0xFFC3CC300CCFCF00, 0xFA97D8710C8B9B54, 0xFFC3CC300CCFCF00, 0xBBD3C87549CE9A01, 0xEB82CC74589FDA54, 0x5F61C4322E6D4FAA, 0x7D0FB86893159CAB, 0xAFD69C6108CEDE54, 0x226E7C5ABD78D301, 0x7D0FB86893159CAB,
0x4E3084676F295FAB, 0x5A35D0732E291BFE, 0x5F61C4322E6D4FAA, 0xFA97D8710C8B9B54, 0x0F7494632A6C5EFE, 0x226E7C5ABD78D301, 0x4E3084676F295FAB, 0x0F30C0333F3C0FFF, 0x5A35D0732E291BFE, 0x88ECF47AB5F25901]
count = 0
while(count<len(dest)):
    for i in range(0x20,0x7f):
        input = i 
        v15 = 4
        v13 = 6
        for j in range(5):
            input ^= ror(input,v13,64) ^ rol(input,v15,64)
            v15 *= 2
            v13 = (2 * v13)
        if(input == dest[count]):
            print(chr(i),end='')
            count+=1
            break
```
**Flag:** `vsctf{n0b0dy_l1kes_r3v3rs1ng_nat1ve_a0t}`
