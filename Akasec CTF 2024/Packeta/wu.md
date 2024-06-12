ELF 64 executables


![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/d18a9012-1d85-4b19-8308-edd368a6f96b)
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/08ac553b-c47f-419f-bc58-9a006deaebdf)

Open with IDA

- Packeta
```C++
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __int64 v3; // rdi
  __int64 v4; // rdx
  __int64 v5; // r8
  __int64 v6; // r9
  __int64 v7; // rdx
  __int64 v8; // r8
  __int64 v9; // r9
  __int64 v10; // rdx
  __int64 v11; // r8
  __int64 v12; // r9
  int fd; // [rsp+1Ch] [rbp-54h]
  __int64 v15; // [rsp+20h] [rbp-50h] BYREF
  void *v16; // [rsp+28h] [rbp-48h]
  size_t len; // [rsp+30h] [rbp-40h]
  _BYTE *v18; // [rsp+38h] [rbp-38h]
  void *v19; // [rsp+40h] [rbp-30h]
  void *v20; // [rsp+48h] [rbp-28h]
  unsigned __int64 v21; // [rsp+58h] [rbp-18h]

  v21 = __readfsqword(0x28u);
  v16 = 0LL;
  if ( a1 <= 1 )
  {
    printf("Usage:\n$> %s your_elf_binary", *a2);
    exit(1);
  }
  fd = open(a2[1], 0, a3);
  if ( !fd )
    exit(1);
  len = lseek(fd, 0LL, 2);
  if ( len == -1LL )
  {
    close(fd);
    exit(1);
  }
  v16 = mmap(0LL, len, 3, 2, fd, 0LL);
  if ( v16 == (void *)-1LL )
    exit(1);
  close(fd);
  v18 = malloc(0x40uLL);
  if ( !v18 )
    exit(1);
  if ( !sub_17CD(v16, v18) )
    exit(1);
  v19 = malloc(8LL * *((unsigned __int16 *)v18 + 30));
  if ( !v19 )
    exit(1);
  v3 = 8LL * *((unsigned __int16 *)v18 + 28);
  v20 = malloc(v3);
  if ( !v20 )
    exit(1);
  call_memcpy_1(v3, (__int64)v18, v4, (__int64)v19, v5, v6, v15, (__int64)v16, len, (__int64)v18, (__int64)v19);
  call_memcpy_2(
    v3,
    (__int64)v18,
    v7,
    (__int64)v19,
    v8,
    v9,
    v15,
    (__int64)v16,
    len,
    (__int64)v18,
    (int)v19,
    (__int64)v20);
  sub_1CE2();
  sub_1464(v3, (__int64)v18, v10, (__int64)v19, v11, v12, v15, (__int64)v16, len, (__int64)v18, (__int64)v19);
  sub_1FC9((__int64)&v15);
  return 0LL;
}
```
- The programs require the first argument to be an elf file that we want to decrypt (flag)
- sub_1CE2
```C++
unsigned __int64 sub_1CE2() //gen_key
{
  int i; // [rsp+8h] [rbp-68h]
  time_t timer; // [rsp+10h] [rbp-60h] BYREF
  __int64 v3; // [rsp+18h] [rbp-58h]
  char v4[72]; // [rsp+20h] [rbp-50h] BYREF
  unsigned __int64 v5; // [rsp+68h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  v3 = 4919LL;
  time(&timer);
  srand(v3 + timer % 500);
  strcpy(v4, "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ");
  for ( i = 0; i <= 15; ++i )
    byte_5020[i] = v4[rand() % 62];
  return v5 - __readfsqword(0x28u);
}
```  
- srand() is initialized by using `(current_time % 500) + 4919` which means that we can bruteforce the value since `current_time % 500` can be anything from 0 to 499
- sub_1464
```C++
unsigned __int64 __fastcall sub_1464(
        __int64 a1,
        __int64 a2,
        __int64 a3,
        __int64 a4,
        __int64 a5,
        __int64 a6,
        int a7,
        __int64 a8,
        int a9,
        __int64 a10,
        __int64 a11)
{
  unsigned __int64 result; // rax
  unsigned __int64 i; // [rsp+0h] [rbp-10h]
  void *ptr; // [rsp+8h] [rbp-8h]

  for ( i = 0LL; ; ++i )
  {
    result = *(unsigned __int16 *)(a10 + 60);
    if ( i >= result )
      break;
    ptr = sub_19C8(a8, *(_QWORD *)(a11 + 8LL * *(unsigned __int16 *)(a10 + 62)), **(_DWORD **)(8 * i + a11));
    if ( (unsigned int)sub_13F8(ptr) )
      sub_1C66(a8 + *(_QWORD *)(*(_QWORD *)(8 * i + a11) + 24LL), *(_QWORD *)(*(_QWORD *)(8 * i + a11) + 32LL)); //rc4
    free(ptr);
  }
  return result;
}
```
- The above function has a call to an rc4_decrypt implementation
- sub_1C66(rc4_func)
```C++
unsigned __int64 __fastcall sub_1C66(__int64 a1, __int64 a2)
{
  char v3[264]; // [rsp+10h] [rbp-110h] BYREF
  unsigned __int64 v4; // [rsp+118h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  sub_1A84(byte_5020, v3);
  sub_1B5C(v3, a1, a2);
  return v4 - __readfsqword(0x28u);
}
```
- We can see that `byte_1A84` is used as key for decrypion, to identify the cyphertext, we can use a debugger

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/70ef69bc-175d-41ed-bf68-dfa46fa5e51f)
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/6f3fa5aa-b69d-470d-83ac-d7ae962da97b)

- The cyphertext starts with 0x4D, 0x75 and 0x3C, we can see where are those bytes located in the `flag` binary

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/80794f08-6799-4ca0-a1e5-f95931fa6e99)

- Those bytes are located in the .text section, start function of the `flag` binary, we can write a bruteforce script to find the valid key and compare the decrypt instructions with a normal start function
```python
from Crypto.Cipher import ARC4
from ctypes import CDLL
from capstone import *
import string

md = Cs(CS_ARCH_X86, CS_MODE_64)

libc = CDLL("libc.so.6")
ct = [0x4d, 0x75, 0xac, 0xea, 0x75, 0xab, 0x78, 0x7, 0x90, 0x58, 0x8e, 0x25, 0x7, 0x84, 0x3f, 0x73, 0x2b, 0xa2, 0x70, 0x40, 0x78, 0x62, 0x4b, 0xfd, 0x65, 0xf0, 0x9b, 0x7, 0x58, 0x44, 0x9d, 0xca, 0x5a, 0x37]
v4 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(500):
	libc.srand(4919 + i)
	key = ""
	for j in range(16):
		key += v4[libc.rand() % 62]
	cipher = ARC4.new(key.encode())
	asm = cipher.decrypt(bytes(ct))
	for j in md.disasm(asm, 0x401000):
		print(i, j)
	print() 
```
- decrypted with `current_time % 500` = 127

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/fa3154a2-bada-4b19-b470-a9733a4fe435)

-Normal start function for comparison

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/e5d0ae4f-238e-401e-b85c-77d41fefe23a)

- Now knowing the key, we just need to modify the `current_time % 500` to 127 using a debugger to get the decrypted file

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/42020db2-2e10-4f3b-839a-848a32068666)

- Run the decrypted binary

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/7b63ceac-1cc7-4a66-a3c3-de7924604d40)

**Flag:** `AKASEC{h4lf_p4ck_h4lf_7h3_fl46}`

Reference: <https://kos0ng.gitbook.io/ctfs/write-up/2024/akasec-ctf/reverse-engineering#packeta-460-pts>










