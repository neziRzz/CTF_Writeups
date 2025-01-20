# Hidden 
## Misc 
- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/2a7ff778-c8c3-44e1-b903-676ccf81ac96)

## Detailed Analysis

- Hàm `main`

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _main();
  printf_0("KCSC{can_you_see_me??}\n");
  return 0;
}
```
- Vì đây là 1 chal warmup nên thoặt qua thấy flag ngay trong `main` như này thì ngỡ rằng đây là flag đúng nhưng thực ra không phải, hàm chuẩn sẽ là hàm `printFlag`

- Hàm `printFlag`
```C
int printFlag()
{
  int result; // eax
  unsigned int v1; // eax
  __int64 v2[3]; // [rsp+20h] [rbp-20h]
  int i; // [rsp+3Ch] [rbp-4h]

  v2[0] = 0xFDE7F1F3CBDBCBC3ui64;
  v2[1] = 0xFBD7FCAFE6E9EBD7ui64;
  result = 0xE5D7EDED;
  v2[2] = 0xF5FEB2EDE5D7EDEDui64;
  for ( i = 0; i <= 0x17; ++i )
  {
    v1 = *((char *)v2 + i);
    LOBYTE(v1) = *((_BYTE *)v2 + i) ^ 0x88;
    result = printf_0("%c", v1);
  }
  return result;
}
```

- Hàm này sẽ có nhiệm vụ xor từng byte của đống data kia với 0x88 và in kết quả ra màn hình, việc viết script sẽ không quá khó khăn
## Script and Flag
```python
def print_flag():
    # Initialize the 64-bit values (little-endian encoding)
    v2 = [
        0xFDE7F1F3CBDBCBC3,
        0xFBD7FCAFE6E9EBD7,
        0xF5FEB2EDE5D7EDED
    ]
    
    # Convert the 64-bit values into a byte array with little-endian order
    byte_array = bytearray()
    for value in v2:
        byte_array.extend(value.to_bytes(8, 'little'))
    
    # XOR each byte with 0x88 and decode to characters
    flag = ''.join(chr(byte ^ 0x88) for byte in byte_array[:24])
    return flag

# Print the flag
flag = print_flag()
print("Flag:", flag)

```
**Flag:** `KCSC{you_can't_see_me:v}`

# easyre
## Misc
- Đề cho 1 file PE64

  ![image](https://github.com/user-attachments/assets/3f407fb9-d11d-45cd-b401-b85cdafb462f)

# Detailed Analysis
- Hàm `main`
```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  size_t v4; // rax
  __int64 v5; // rax
  unsigned int v6; // edx
  unsigned int v7; // r8d
  unsigned __int64 v8; // rax
  __m128 v9; // xmm0
  __m128 v10; // xmm1
  __int64 v11; // rcx
  __int64 v12; // rax
  char *v13; // rcx
  char Buffer[16]; // [rsp+20h] [rbp-68h] BYREF
  __int128 v16; // [rsp+30h] [rbp-58h] BYREF
  int v17; // [rsp+40h] [rbp-48h]
  __int128 v18[2]; // [rsp+48h] [rbp-40h] BYREF
  __int64 v19; // [rsp+68h] [rbp-20h]
  int v20; // [rsp+70h] [rbp-18h]
  char v21; // [rsp+74h] [rbp-14h]

  LOBYTE(v17) = 0;
  v19 = 0i64;
  *(_OWORD *)Buffer = 0i64;
  v20 = 0;
  v16 = 0i64;
  v21 = 0;
  memset(v18, 0, sizeof(v18));
  sub_140001010("Enter flag: ");
  v3 = _acrt_iob_func(0);
  fgets(Buffer, 33, v3);
  v4 = strcspn(Buffer, "\n");
  if ( v4 >= 0x21 )
    sub_140001558();
  Buffer[v4] = 0;
  v5 = -1i64;
  do
    ++v5;
  while ( Buffer[v5] );
  if ( v5 == 32 )
  {
    base64((__int64)Buffer, v18);
    v6 = 0;
    v7 = 0;
    v8 = 0i64;
    do
    {
      v9 = (__m128)_mm_loadu_si128((const __m128i *)&byte_140005078[v8]);
      v7 += 32;
      v10 = (__m128)_mm_loadu_si128((const __m128i *)&v18[v8 / 0x10]);
      v8 += 32i64;
      *(__m128 *)&dword_140005058[v8 / 4] = _mm_xor_ps(v10, v9);
      *(__m128 *)&qword_140005068[v8 / 8] = _mm_xor_ps(
                                              (__m128)_mm_loadu_si128((const __m128i *)((char *)&v16 + v8 + 8)),
                                              (__m128)_mm_loadu_si128((const __m128i *)&qword_140005068[v8 / 8]));
    }
    while ( v7 < 0x20 );
    v11 = (int)v7;
    if ( (unsigned __int64)(int)v7 < 0x2C )
    {
      do
      {
        ++v7;
        byte_140005078[v11] ^= *((_BYTE *)v18 + v11);
        ++v11;
      }
      while ( v7 < 0x2C );
    }
    v12 = 0i64;
    while ( byte_1400032F0[v12] == byte_140005078[v12] )
    {
      ++v6;
      ++v12;
      if ( v6 >= 0x2C )
      {
        v13 = "Correct!\n";
        goto LABEL_13;
      }
    }
  }
  v13 = "Incorrect!\n";
LABEL_13:
  sub_140001010(v13);
  return 0;
}
```
- Đầu tiên hàm `main` sẽ kiểm tra độ dài của input có phải là 32 hay không, nếu thỏa mãn thì sẽ tiến hành encode input bằng base64, sau đó sẽ xor input với `byte_7FF6A9F35078`, đoạn xor này sẽ được chia ra làm 2 phần, phần đầu là xor 16 bytes và phần cuối sẽ xor từng byte một. Cuối cùng input sẽ được kiểm tra với `byte_7FF6A9F332F0` nếu thỏa mãn sẽ in ra string `Correct!` hoặc `Incorrect!` tương ứng

- Với các dữ kiện như trên, ta có thể dễ dàng viết script

## Script and Flag
```python
key =[ 0x92, 0xA1, 0x27, 0xE0, 0x37, 0xCA, 0x70, 0x7E, 0xE6, 0xBE, 
  0x33, 0x1D, 0x5D, 0xFE, 0x29, 0x93, 0xB6, 0x66, 0xF9, 0x02, 
  0x6A, 0x74, 0x0D, 0xDF, 0xD6, 0xEC, 0x5A, 0x71, 0xC8, 0xA3, 
  0xFD, 0x84, 0xC5, 0x13, 0x1E, 0x87, 0xC7, 0x52, 0x50, 0x55, 
  0x01, 0x16, 0xFD, 0xCF]
cypher = [0xC1, 0x91, 0x69, 0xB4, 0x66, 0xF9, 0x04, 0x12, 0xB2, 0xD3, 
  0x7D, 0x6B, 0x0F, 0xB9, 0x7F, 0xF5, 0xD2, 0x1C, 0xBF, 0x32, 
  0x0B, 0x32, 0x34, 0x9C, 0x98, 0xA4, 0x14, 0x37, 0x86, 0xC9, 
  0xAF, 0xE2, 0x9C, 0x46, 0x2B, 0xEC, 0x9F, 0x63, 0x38, 0x23, 
  0x54, 0x78, 0xCD, 0xF2]
for i in range (len(cypher)):
    print(chr(cypher[i]^key[i]),end='') //Remember to decode it back from b64
```
**Flag:** `KCSC{eNcoDe_w1th_B4sE64_aNd_XoR}`
