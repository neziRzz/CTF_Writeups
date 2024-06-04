ELF64 executable
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/f50dfb72-16dd-46cd-9120-90520159aa6a)
Put in IDA
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/6f19d980-6c63-49a0-8712-d0b454864285)
For the sake of simplicity, we will not analyze the above routine in asm but instead in pseudo C
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/8fbb8f29-a1f9-4fc4-a4d6-a61212ca0147)
The program compare each character of the user's input with the following values and if they are valid and the input's lenght is equal to 23 then we get the flag.
This is a python script for this challenge
```python
s=["lmaommb"]*23
s[22] = 125
s[21] = 116
s[20] = 78
s[19] = 49
s[18] = 95
s[17] = 115
s[16] = 116
s[15] = 105
s[14] = 98
s[13] = 56
s[12] = 95
s[11] = 115
s[10] = 49
s[9] = 95
s[8] = 114
s[7] = 52
s[6] = 72
s[5] = 99
s[4] = 123
s[3] = 83
s[2] = 80
s[0] = 78
s[1] = 48
for i in range(23):
    print(chr(s[i]),end='')
```
**Flag:** `N0PS{cH4r_1s_8bits_1Nt}`

