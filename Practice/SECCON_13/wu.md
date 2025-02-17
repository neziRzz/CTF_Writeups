# Packed
## Mics 
- Given a UPX-packed ELF64 executable

![image](https://github.com/user-attachments/assets/b29d2e1a-7fea-4bc3-bb6e-af4bc25e4d4f)

## Detailed Analysis
- When i try to unpack the file using the upx tool, the flag checking routine seems to be stripped, the program only print out `Wrong` then exit

![image](https://github.com/user-attachments/assets/45250d94-9641-4ca3-90ef-c651dc452c7a)

- This means that the code is somehow being modified during the unpacking process, we will have to unpack the file manually





