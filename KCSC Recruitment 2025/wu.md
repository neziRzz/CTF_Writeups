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
