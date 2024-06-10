9ELF64 executable

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/ee97d947-2188-4df0-98b3-a8951aaa95ca)

Put in IDA (pseudocode)

```C
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __int64 v3; // rbx
  __int64 v4; // rbx
  __int64 v5; // rbx
  __int64 v6; // rbx
  __int64 v7; // rbx
  __int64 v8; // rbx
  __int64 v9; // rbx
  __int64 v10; // rbx
  __int64 v11; // rbx
  unsigned __int64 i; // [rsp+18h] [rbp-C8h]
  _QWORD *v14; // [rsp+20h] [rbp-C0h]
  __int64 v15; // [rsp+30h] [rbp-B0h]
  __int64 v16; // [rsp+38h] [rbp-A8h]
  __int64 v17; // [rsp+40h] [rbp-A0h]
  __int64 v18; // [rsp+48h] [rbp-98h]
  __int64 v19; // [rsp+50h] [rbp-90h]
  __int64 v20; // [rsp+58h] [rbp-88h]
  __int64 v21; // [rsp+60h] [rbp-80h]
  __int64 v22; // [rsp+68h] [rbp-78h]
  __int64 v23; // [rsp+70h] [rbp-70h]
  __int64 v24; // [rsp+78h] [rbp-68h]
  __int64 v25; // [rsp+80h] [rbp-60h]
  __int64 v26; // [rsp+88h] [rbp-58h]
  __int64 v27; // [rsp+90h] [rbp-50h]
  __int64 v28; // [rsp+98h] [rbp-48h]
  __int64 v29; // [rsp+A0h] [rbp-40h]
  char v30[13]; // [rsp+A8h] [rbp-38h]
  __int64 v31; // [rsp+B5h] [rbp-2Bh]
  unsigned __int64 v32; // [rsp+C8h] [rbp-18h]

  v32 = __readfsqword(0x28u);
  v15 = 0xB21E71BA177BBAA7LL;
  v16 = 0xF2F2DAD7F679BA96LL;
  v17 = 0xBA32C30AB77BBAF2LL;
  v18 = 0xCBD3D5C3D1DBD14ALL;
  v19 = 0xC9C4C481D848BAC3LL;
  v20 = 0xBA22B77BBA84C0EFLL;
  v21 = 0xC0EFC94ABA2AA77BLL;
  v22 = 0xEF48BAD483DBD384LL;
  v23 = 0xBACDC9C284DE81D2LL;
  v24 = 0x3516A77BBA2EB77BLL;
  v25 = 0xEA19F2F2F2F23EB7LL;
  v26 = 0x22F7B644FD3EB779LL;
  v27 = 0x3EB779307BB00271LL;
  v28 = 0xF33EB77122F7A67ALL;
  v29 = 0xBA621084E93E8F71LL;
  *(_QWORD *)v30 = 0xD7F6D9BA960AB779LL;
  *(_QWORD *)&v30[5] = 0x86F2F2F2DAD7F6D9LL;
  v31 = 0x313BF2F2F2F21AF7LL;
  for ( i = 0LL; i <= 0x8C; ++i )
    *((_BYTE *)&v15 + i) ^= 0xF2u;
  v14 = mmap(0LL, 0x8DuLL, 6, 34, -1, 0LL);
  v3 = v16;
  *v14 = v15;
  v14[1] = v3;
  v4 = v18;
  v14[2] = v17;
  v14[3] = v4;
  v5 = v20;
  v14[4] = v19;
  v14[5] = v5;
  v6 = v22;
  v14[6] = v21;
  v14[7] = v6;
  v7 = v24;
  v14[8] = v23;
  v14[9] = v7;
  v8 = v26;
  v14[10] = v25;
  v14[11] = v8;
  v9 = v28;
  v14[12] = v27;
  v14[13] = v9;
  v10 = *(_QWORD *)v30;
  v14[14] = v29;
  v14[15] = v10;
  v11 = v31;
  *(_QWORD *)((char *)v14 + 125) = *(_QWORD *)&v30[5];
  *(_QWORD *)((char *)v14 + 133) = v11;
  ((void (__fastcall *)(_QWORD))v14)(0LL);
  puts(":3");
  return 0LL;
}
```
- We can see that `v14` is initiallized using `mmap` (`VirtualAlloc` equivalent) and there are a lot of value assignments for `v14` also the call to `v14` at the end of the program, it is safe to say that `v14` is the flag checking function and will be initialized at runtime

Put in Binary Ninja

   - When we try to put a bp at main, RIP never reaches there so there must be some kind of anti-debugging technique being use, after some debugging, we can identify the anti-debug function

  ![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/62bf95e4-84c2-4957-bc02-d24e727d349a)

  - We just need to patch out the instruction, set bp at main and press run

  ![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/5ddb2dab-850b-48ea-8e6f-fbc5452d426a)

  - Set bp at the last call to `v14` (`rdx`) and step into the call

  ![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/ef287dd0-2a90-4cdd-91fb-4c0a6a816db7)


  - Analyze the function in pseudocode
    
  ![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/1a8d2bf1-02b4-4e2a-9aa5-5f98067c4aab)

  - This is just a simple xor routine and can be easily scripted


```python
cypher_header="#)#1\'!91"
cypher_body_end="2a7336363b1d3276212971261d20732c76303b3f"
b=bytes.fromhex(cypher_body_end)
for i in range(len(cypher_header)):
    print(chr(ord(cypher_header[i])^0x42),end='')
for i in range(len(b)):
    print(chr(b[i]^0x42),end='')
```
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/ad7e72c8-1867-4166-8d15-c22858b33d66)

**Flag:** `akasec{sh1tty_p4ck3d_b1n4ry}`
