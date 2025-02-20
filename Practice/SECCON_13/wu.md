# Packed
## Mics 
- Given a UPX-packed ELF64 executable

![image](https://github.com/user-attachments/assets/b29d2e1a-7fea-4bc3-bb6e-af4bc25e4d4f)

## Detailed Analysis
- When i try to unpack the file using the upx tool, the flag checking routine seems to be stripped, the program only print out `Wrong` then exit

![image](https://github.com/user-attachments/assets/45250d94-9641-4ca3-90ef-c651dc452c7a)

- This means that the code is somehow being modified during the unpacking process, we will have to unpack the file manually

- After a bit of debugging, we can identify where the true main function is

![image](https://github.com/user-attachments/assets/6aa1ccf5-b8ce-47bc-8114-8d91ab3fac5a)


## Script and Flag
```python
key = [232, 74, 0, 0, 0, 131, 249, 73, 117, 68, 83, 87, 72, 141, 76, 55, 253, 94, 86, 91, 235, 47, 72, 57, 206, 115, 50, 86, 94, 172, 60, 128, 114, 10, 60, 143, 119, 6, 128, 126, 254, 15, 116, 6, 44, 232, 60, 1]
cypher = [187, 15, 67, 67, 79, 205, 130, 28, 37, 28, 12, 36, 127, 248, 46, 104, 204, 45, 9, 58, 180, 72, 120, 86, 170, 44, 66, 58, 106, 207, 15, 223, 20, 58, 78, 208, 31, 55, 228, 23, 144, 57, 43, 101, 28, 140, 15, 124]
for i in range(len(key)):
    print(chr(cypher[i]^key[i]),end='')
```
**Flag:** `SECCON{UPX_s7ub_1s_a_g0od_pl4c3_f0r_h1din6_c0d3}`



