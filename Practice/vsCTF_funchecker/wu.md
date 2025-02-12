   # Mics
- Given a PE64 file

![image](https://github.com/user-attachments/assets/05e335ea-b41e-47c5-8859-7fd1823b14b1)

# Detailed Analysis
- The `main` function
```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __int64 v5; // rsi

  if ( !(unsigned __int8)sub_140005020(0i64, argv, envp) )
    return -1;
  v5 = sub_14000B1F0((LPCWSTR)sub_14009E330);
  if ( !(unsigned __int8)sub_14000AD90(
                           v5,
                           (unsigned int)sub_140065000,
                           (unsigned int)sub_1400AB1D0 - (unsigned int)sub_140065000,
                           (unsigned int)sub_1400649C0,
                           (unsigned int)sub_140064DA0 - (unsigned int)sub_1400649C0,
                           (__int64)off_1400F6490,
                           14) )
    return -1;
  sub_1400930E0(v5, (int)&unk_1400CB5E8, (&unk_1400CB5F8 - &unk_1400CB5E8) >> 3, (int)off_1400F6490, 14);
  return sub_14009E330((unsigned int)argc, argv);// true main function here
}
```
- Nothing special here, the true main function is at the end (`sub_14009E330`), with arguments being passed are `argc` and `argv`
- After a bit of debugging, we can see that the function responsible for checking the flag is `sub_140065360`

![image](https://github.com/user-attachments/assets/e98016c6-270d-4ef3-abe9-71a9b68a8935)

- Function `sub_140065360`
```C
__int64 __fastcall sub_140065360(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
  __int64 v6; // rax
  __int64 v7; // rbx
  __int64 v8; // rcx
  __int64 v9; // rdx
  __int64 v10; // r8
  __int64 v11; // rdx
  __int64 v12; // r8
  __int64 v13; // r9
  unsigned int v14; // eax
  int v15; // r10d
  int i; // r11d

  if ( *(_DWORD *)(a1 + 8) != 1 )
    return sub_140065C10(&unk_1400B3350, a2, a3, a4);
  if ( *(&qword_1400B5398 - 1) )
    sub_140001348();
  v6 = sub_1400953C0(*(_QWORD *)(qword_14010C278 + 8), *(_QWORD *)(a1 + 16));
  v7 = v6;
  if ( v6 )
  {
    v8 = v6 + 16;
    v9 = *(unsigned int *)(v6 + 8);
  }
  else
  {
    v8 = 0i64;
    v9 = 0i64;
  }
  v10 = 0i64;
  if ( (_DWORD)v9 )
    v10 = v8;
  if ( custom_hash(v10, v9, 0i64) == 0xA8A85CFA9660DB0Fui64 && *(_DWORD *)(v7 + 8) == 40 )// check hash and input length
  {
    v14 = 0;
    while ( 1 )
    {
      v11 = v14;
      v12 = *(unsigned __int8 *)(v7 + v14 + 16);
      v15 = 4;
      LODWORD(v13) = 6;
      for ( i = 0; i < 5; ++i )                 // input transformation and validation here
      {
        v12 ^= __ROR8__(v12, v13) ^ __ROL8__(v12, v15);
        v15 *= 2;
        v13 = (unsigned int)(2 * v13);
      }
      if ( *(_QWORD *)(*(_QWORD *)(qword_14010C168 + 8) + 8i64 * v14 + 16) != v12 )
        break;
      if ( (int)++v14 >= 40 )
        return sub_140065C10(&unk_1400AFA00, v11, v12, v13);// print correct
    }
  }
  return sub_140065C10(&unk_1400B0C48, v11, v12, v13);// print incorrect
}
```
- To keep it simple, this function will first use a custom hashing algorithm to hash the user's input from `argv`, compare the hashed input to a certain hash value and check the pre-hashed input length with 40, if one of these conditions are not met, the program exit, else the program will transform the user's input with `XOR`, `ROL` and `ROR` and compare the result with values from `qword_14010C168`
, with `qword_14010C168` points to here

![image](https://github.com/user-attachments/assets/70a03dce-1c5c-435c-b0cd-261c7ff8eb41)

- To solve, we can write a bruteforce script (no need to bruteforce the hash function) as follows
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
