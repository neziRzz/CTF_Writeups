This challange is rather simple
- First lets put it in IDA
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/fe3505cc-de77-484b-84f2-7cfcd0f481ac)
This function might seems intimidating but it actually just print out the string `Let's start out easy` and ask for your input by using `WriteFile` and `ReadFile` function

- Then comes the checking routine
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/d7b87237-8340-4785-8ad8-d92c52069c0c)
This routine functionality can be roughly tranlated to
  - Our input is stored in `byte_402158[ecx]` is move into `AL`
  - Our input then xor'ed with 0x7D
  - If its not equal to what is stored at `byte_402140[ecx]` the program then print `You are failure` and the program terminates else increment `ECX`
  by 1 and if `ECX` is greater or equal to 0x18 (which is 24 in decimal) the routine then loop back to the beginning

 And when i find what is stored at `byte_402140[ecx]`, this is what i found
 ![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/def902b2-a2ea-47c4-849b-23ac30e2e7de)
 Since xor operation is symmetric and reflexive, we can just take whatever is stored in `byte_402140[ecx]` 
 and xor it with 0x7D

**Flag:`bunny_sl0pe@flare-on.com`**
And this is a python script for this challange
```python
data="1F 08 13 13 04 22 0E 11 4D 0D 18 3D 1B 11 1C 0F 18 50 12 13 53 1E 12 10" 
b=bytes.fromhex(data)
for i in range(len(b)):
    print(chr((b[i])^0x7D),end='')
```
