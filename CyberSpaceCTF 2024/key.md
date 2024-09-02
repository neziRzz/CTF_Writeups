- Given an ELF64 file

![image](https://github.com/user-attachments/assets/eaf666c4-0c91-4150-b079-9265306c438c)

- IDA's pseudocode
```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+8h] [rbp-138h]
  int v5[32]; // [rsp+10h] [rbp-130h]
  int v6[32]; // [rsp+90h] [rbp-B0h]
  char s[40]; // [rsp+110h] [rbp-30h] BYREF
  unsigned __int64 v8; // [rsp+138h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  v6[0] = 67;
  v6[1] = 164;
  v6[2] = 65;
  v6[3] = 174;
  v6[4] = 66;
  v6[5] = 252;
  v6[6] = 115;
  v6[7] = 176;
  v6[8] = 111;
  v6[9] = 114;
  v6[10] = 94;
  v6[11] = 168;
  v6[12] = 101;
  v6[13] = 242;
  v6[14] = 81;
  v6[15] = 206;
  v6[16] = 32;
  v6[17] = 188;
  v6[18] = 96;
  v6[19] = 164;
  v6[20] = 109;
  v6[21] = 70;
  v6[22] = 33;
  v6[23] = 64;
  v6[24] = 32;
  v6[25] = 90;
  v6[26] = 44;
  v6[27] = 82;
  v6[28] = 45;
  v6[29] = 94;
  v6[30] = 45;
  v6[31] = 196;
  printf("Enter the key: ");
  __isoc99_scanf("%32s", s);
  if ( (unsigned int)strlen(s) == 32 )
  {
    for ( i = 0; i < 32; ++i )
    {
      v5[i] = (i % 2 + 1) * (i ^ s[i]);
      if ( v5[i] != v6[i] )
        break;
      if ( i == 31 )
        printf("Success!");
    }
  }
  else
  {
    printf("Denied Access");
  }
  return 0;
}
```
- The program takes the users' input, do some calculation on it and assign it to `v5` then compare `v5` with `v6`
- This can be easily solved with z3
```python
from z3 import*
flag = [BitVec('x[%d]' % i,8) for i in range(32)]
s = Solver()
v6 = [0]*32
v6[0] = 67
v6[1] = 164
v6[2] = 65
v6[3] = 174
v6[4] = 66
v6[5] = 252
v6[6] = 115
v6[7] = 176
v6[8] = 111
v6[9] = 114
v6[10] = 94
v6[11] = 168
v6[12] = 101
v6[13] = 242
v6[14] = 81
v6[15] = 206
v6[16] = 32
v6[17] = 188
v6[18] = 96
v6[19] = 164
v6[20] = 109
v6[21] = 70
v6[22] = 33
v6[23] = 64
v6[24] = 32
v6[25] = 90
v6[26] = 44
v6[27] = 82
v6[28] = 45
v6[29] = 94
v6[30] = 45
v6[31] = 196
v5 = [0]*32
for i in range(32):
    s.add(flag[i] >= 0x20)
    s.add(flag[i] <= 0x7F)
for i in range(32):
    v5[i] = (i % 2 + 1) * (i ^ flag[i])
    s.add(v5[i] == v6[i])
if(s.check() == sat):
    res = ''
    for i in range(len(flag)):
        last = int(str(s.model()[flag[i]]))
        res += chr(last)
else:
    print("Failed")
print(res)
```
**Flag:** `CSCTF{u_g0T_it_h0OrAy6778462123}`
