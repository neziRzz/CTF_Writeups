- Đề cho 1 file PE32

- Mình không thể giải được bài này trong lúc thi nhưng sau khi được author `noobmannn` hint thì mình đã có thể giải được

![image](https://github.com/user-attachments/assets/71237fe9-bb4a-4450-9bfc-3f2f18415184)

- Pseudocode của IDA (mình đã đổi tên một số hàm để tiện hơn cho việc phân tích)

```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4; // [esp+0h] [ebp-10h]
  unsigned int v5; // [esp+0h] [ebp-10h]
  unsigned __int8 i; // [esp+Fh] [ebp-1h]

  sub_401050("Enter Your Flag: ", v4);
  sub_4010C0("%s", (char)input);
  v5 = strlen(input);
  if ( v5 != 32 )
  {
    sub_401050("Wrong Length!!!\n", v5);
    exit(0);
  }
  encrypt1(input);
  encrypt2(input);
  encrypt3(input);
  for ( i = 0; i < 32u; ++i )
  {
    if ( input[i] != check[i] )
    {
      sub_401050("Wrong Flag!!!\n", 32);
      exit(0);
    }
  }
  sub_401050("Correct :3\n", 32);
  return 0;
}
```
- Ta có thể thấy được luồng của chương trình sẽ như sau
    + Đầu tiên, chương trình sẽ kiểm tra số lượng kí tự nhập vào có phải là 32 hay không, nếu không sẽ in ra `Wrong Length!!!` và kết thúc chương trình
    + Nếu thỏa mãn điều kiện, chương trình sẽ tiến hành encrypt input thông qua 3 hàm `encrypt1()`, `encrypt2()` và `encrypt3()`
    + Cuối cùng kiểm tra input sau khi đã được encrypt với array `check[]` và in ra `Correct :3` hoặc `Wrong Flag!!!` tương ứng

- Trước khi đi vào cụ thể các hàm encrypt sẽ làm gì, ta sẽ phải kiểm tra rằng có hàm nào được gọi trước hàm `main()` hay không, để kiểm tra thì các bạn có thể vào cửa sổ `Exports` của IDA

- Ta có thể thấy rằng hàm `TlsCallback_0` và hàm `start` được gọi trước hàm `main()`

  ![image](https://github.com/user-attachments/assets/aa07345a-4c7a-4efe-a6b5-24ca5b452a9b)

- Hàm `TlsCallback_0()`

```C
NTSTATUS __stdcall TlsCallback_0(int a1, int a2, int a3)
{
  NTSTATUS result; // eax
  ULONG NtGlobalFlag; // [esp+8h] [ebp-Ch]
  int ProcessInformation; // [esp+Ch] [ebp-8h] BYREF

  NtGlobalFlag = NtCurrentPeb()->NtGlobalFlag;
  ProcessInformation = 0;
  result = NtQueryInformationProcess((HANDLE)0xFFFFFFFF, ProcessDebugPort, &ProcessInformation, 4u, 0);
  if ( !result && ProcessInformation )
  {
    result = NtGlobalFlag & 0x70;
    if ( (NtGlobalFlag & 0x70) != 0 )
      qmemcpy(&byte_4041A8, &unk_4040A8, 0x100u);
  }
  return result;
}
```
- Hàm này thực hiện gọi  `NtQueryInformationProcess()` để lấy các thông tin về tiến trình, sau đó kiểm tra flag `NtGlobalFlag` có được set là 0x70 hay không (kiểm tra debugger), nếu flag này là 0x70 thì sẽ tiến hành overwrite `byte_1641A8` (byte array này sẽ được sử dụng cho hàm `encrypt2()`) thành `unk_1640A8` và điều này sẽ làm ảnh hưởng đến cách mà input được xử lí, [các bạn có thể tìm hiểu thêm về kĩ thuật anti-debug trên ở đây](https://anti-debug.checkpoint.com/techniques/debug-flags.html#manual-checks-ntglobalflag)

- Để bỏ qua đoạn check debug này, các bạn chỉ cần patch lại instruction `jnz  short loc_161161` thành jmp là được

    ![image](https://github.com/user-attachments/assets/2f97e6f5-59c1-4a1f-bbf9-0130a0861584)
    ![image](https://github.com/user-attachments/assets/e7cdb2f6-daf5-4092-a6d0-d58b45862567)

- Bây giờ thì mình sẽ bắt đầu việc phân tích các hàm encrypt

- Hàm `encrypt1()`
```C
unsigned __int8 __cdecl encrypt1(int a1)
{
  unsigned __int8 result; // al
  unsigned __int8 mm; // [esp+2h] [ebp-Ah]
  unsigned __int8 kk; // [esp+3h] [ebp-9h]
  unsigned __int8 jj; // [esp+4h] [ebp-8h]
  unsigned __int8 n; // [esp+5h] [ebp-7h]
  unsigned __int8 m; // [esp+6h] [ebp-6h]
  unsigned __int8 k; // [esp+7h] [ebp-5h]
  unsigned __int8 i; // [esp+8h] [ebp-4h]
  unsigned __int8 nn; // [esp+9h] [ebp-3h]
  unsigned __int8 ii; // [esp+Ah] [ebp-2h]
  unsigned __int8 j; // [esp+Bh] [ebp-1h]

  for ( i = 0; i < 0x20u; ++i )
    *(_BYTE *)(a1 + i) ^= 0xABu;
  for ( j = 0; j < 0x20u; ++j )
    *(_BYTE *)(a1 + j) ^= j - 85;
  for ( k = 0; k < 0x20u; k += 4 )
    *(_DWORD *)(a1 + k) ^= 0xC0FEBEEF;
  for ( m = 0; m < 0x20u; m += 4 )
    *(_DWORD *)(a1 + m) ^= 0xDEADBABE;
  for ( n = 0; n < 0x20u; ++n )
    *(_BYTE *)(a1 + n) ^= 0xCDu;
  for ( ii = 0; ii < 0x20u; ++ii )
    *(_BYTE *)(a1 + ii) ^= ii - 51;
  for ( jj = 0; jj < 0x20u; jj += 4 )
    *(_DWORD *)(a1 + jj) ^= 0xC0FEBABE;
  for ( kk = 0; kk < 0x20u; kk += 4 )
    *(_DWORD *)(a1 + kk) ^= 0xDEADBEEF;
  for ( mm = 0; ; ++mm )
  {
    result = mm;
    if ( mm >= 0x20u )
      break;
    *(_BYTE *)(a1 + mm) ^= 0xEFu;
  }
  for ( nn = 0; nn < 0x20u; ++nn )
  {
    *(_BYTE *)(a1 + nn) ^= nn - 17;
    result = nn + 1;
  }
  return result;
}    
 ```


- Hàm này thực hiện phép xor lên input của chúng ta với một số giá trị theo 2 pattern như sau, 1 là xor từng byte và 2 là xor 4 byte một   


- Hàm `encrypt2()`
```C
int __cdecl encrypt2(int a1)
{
  char v2; // [esp+4h] [ebp-4h]
  unsigned __int8 i; // [esp+5h] [ebp-3h]
  unsigned __int8 v4; // [esp+6h] [ebp-2h]
  unsigned __int8 v5; // [esp+7h] [ebp-1h]

  v5 = 0;
  v4 = 0;
  for ( i = 0; i < 0x20u; ++i )
  {
    v4 += sus[++v5];
    v2 = sus[v5];
    sus[v5] = sus[v4];
    sus[v4] = v2;
    *(_BYTE *)(a1 + i) ^= sus[((unsigned __int8)sus[v4] + (unsigned __int8)sus[v5]) % 256];
  }
  return enum_process_to_find_if_debugged();
}
```


- Hàm này sẽ xor input của chúng ta sau khi đã biến đổi qua hàm `encrypt1()` với array `sus[]`(array này là `byte_1641A8` nhưng mà mình đã đổi tên) với index của array `sus[]` được duyệt theo `((unsigned __int8)sus[v4] + (unsigned __int8)sus[v5]) % 256` cùng với `v4`, `v5` và `v2`

- Trước khi kết thúc hàm này thì nó sẽ gọi hàm `enum_process_to_find_if_debugged()` để tiến hành check for debugger



- Hàm `enum_process_to_find_if_debugged()`
```C
int enum_process_to_find_if_debugged()
{
  DWORD CurrentProcessId; // eax
  int v2; // [esp+10h] [ebp-288h]
  int v3; // [esp+1Ch] [ebp-27Ch]
  int v4; // [esp+20h] [ebp-278h]
  int v5; // [esp+24h] [ebp-274h]
  HANDLE hSnapshot; // [esp+28h] [ebp-270h]
  unsigned __int8 v7; // [esp+57h] [ebp-241h]
  PROCESSENTRY32W pe; // [esp+5Ch] [ebp-23Ch] BYREF
  DWORD flOldProtect; // [esp+288h] [ebp-10h] BYREF
  char Src[6]; // [esp+28Ch] [ebp-Ch] BYREF

  v7 = 0;
  GetCurrentProcessId();
  CurrentProcessId = GetCurrentProcessId();
  v2 = check_parent_process_pid(CurrentProcessId);
  memset(&pe, 0, sizeof(pe));
  pe.dwSize = 556;
  hSnapshot = CreateToolhelp32Snapshot(2u, 0);
  if ( Process32FirstW(hSnapshot, &pe) )
  {
    while ( 1 )
    {
      if ( pe.th32ProcessID == v2 )
      {
        v5 = wcscmp(pe.szExeFile, (const unsigned __int16 *)sub_161180(aFlagchecker4Ex));
        if ( v5 )
          v5 = v5 < 0 ? -1 : 1;
        if ( v5 )
        {
          v4 = wcscmp(pe.szExeFile, (const unsigned __int16 *)sub_161180(aCmdExe));
          if ( v4 )
            v4 = v4 < 0 ? -1 : 1;
          if ( v4 )
          {
            v3 = wcscmp(pe.szExeFile, (const unsigned __int16 *)sub_161180(aExplorerExe));
            if ( v3 )
              v3 = v3 < 0 ? -1 : 1;
            if ( v3 )
              break;
          }
        }
      }
      if ( !Process32NextW(hSnapshot, &pe) )
        goto LABEL_14;
    }
    v7 = 1;
  }
LABEL_14:
  if ( !v7 )
  {
    v7 = 0;
    Src[0] = 104;
    Src[5] = -61;
    *(_DWORD *)&Src[1] = riel_encrypt;
    VirtualProtect(encrypt3, 6u, 0x40u, &flOldProtect);
    memcpy(encrypt3, Src, 6u);
  }
  CloseHandle(hSnapshot);
  return v7;
}
```
- Trước tiên hàm này gọi `GetCurrentProcessId()` để lấy PID hiện tại của tiến trình

- Tiếp theo gọi hàm `check_parent_process_pid(CurrentProcessId)` để lấy parent process pid của tiến trình `FlagChecker4.exe` (có nghĩa là tiến trình nào đang chạy `FlagChecker4.exe` thì sẽ lấy PID của tiến trình đó) sau đó gắn vào `v2`

- Tiếp đến gọi hàm `CreateToolhelp32Snapshot(2u, 0)` để tạo ra handle đến snapshot chứa thông tin của các tiến trình đang chạy trên hệ thống (với 2 arguments 2u = TH32CS_SNAPPROCESS và 0 là để include tiến trình hiện tại vào trong snapshot)

- Enumerate snapshot cho đến khi gặp parent process của `FlagChecker4.exe`, tiến hành kiểm tra tên của tiến trình này xem nó có là ``FlagChecker4.exe``, `cmd.exe` hoặc  `explorer.exe`, nếu tên không thuộc 1 trong 3 tiến trình này thì có nghĩa là chương trình bị debug, sau đó sẽ set flag `v7`, đóng handle và thoát khỏi hàm, ngược lại thì sẽ thực hiện dùng hàm `VirtualProtect()` để thực hiện thay đổi quyền truy cập cho hàm `encrypt3()` thành `PAGE_EXECUTE_READWRITE`(0x40) nhằm cấp quyền có thể ghi và đọc hàm này, cuối cùng là overwrite hàm này thành hàm `riel_encrypt()`

- Để bypass đoạn check này, các bạn chỉ cần patch instructions `jnz  loc_16160E` thành `jmp` là được

![image](https://github.com/user-attachments/assets/f61604e6-8d25-46ca-884f-d2ebbc0042e6)
![image](https://github.com/user-attachments/assets/4b7970c9-0eaf-4d5e-8e40-84d5d2337ecc)



- Hàm `encrypt3()`(bây giờ đã thành hàm `riel_encrypt()`)
```C
int __usercall riel_encrypt@<eax>(int a1@<ebp>, const void *a2)
{
  int result; // eax
  unsigned __int8 k; // [esp-47h] [ebp-53h]
  unsigned __int8 j; // [esp-46h] [ebp-52h]
  unsigned __int8 jj; // [esp-45h] [ebp-51h]
  unsigned __int8 ii; // [esp-44h] [ebp-50h]
  unsigned __int8 n; // [esp-43h] [ebp-4Fh]
  unsigned __int8 m; // [esp-42h] [ebp-4Eh]
  unsigned __int8 i; // [esp-41h] [ebp-4Dh]
  __int128 KCSC_extend_128_bits_key; // [esp-40h] [ebp-4Ch] BYREF
  _BYTE v11[36]; // [esp-24h] [ebp-30h] BYREF
  int v12; // [esp+0h] [ebp-Ch]
  int v13; // [esp+4h] [ebp-8h]
  int retaddr; // [esp+Ch] [ebp+0h]

  v12 = a1;
  v13 = retaddr;
  qmemcpy(v11, a2, 0x20u);
  for ( i = 0; i < 0x20u; ++i )
    v11[i] = (0x88 - i) ^ i;
  for ( j = 0; j < 0x20u; ++j )
    v11[j] = dec136_pow_v11_mod_251(136u, v11[j]);
  KCSC_extend_128_bits_key = xmmword_163180;
  for ( k = 0; k < 0x58u; ++k )
  {
    aes_enc(v11, &KCSC_extend_128_bits_key);
    aes_enc(&v11[16], &KCSC_extend_128_bits_key);
  }
  for ( m = 0; m < 0x20u; ++m )
    *((_BYTE *)a2 + m) = rol(*((_BYTE *)a2 + m), m & 7);
  for ( n = 0; n < 0x20u; ++n )
    *((_BYTE *)a2 + n) ^= v11[n];
  for ( ii = 0; ii < 0x20u; ++ii )
    *((_BYTE *)a2 + ii) = rol(*((_BYTE *)a2 + ii), 8 - (ii & 7));
  for ( jj = 0; ; ++jj )
  {
    result = jj;
    if ( jj >= 0x20u )
      break;
    *((_BYTE *)a2 + jj) ^= 0xFF - v11[jj];
  }
  return result;
}
```
- Đầu tiên gán từng phần tử `v11` với `(0x88 - i) ^ i`

- Sau đó gán các giá trị trả về của hàm `dec136_pow_v11_mod_251(136u, v11[j])` cho từng phần tử của `v11` qua 2 dữ kiện đầu tiên thì ta có thể thấy rằng v11 không hề phụ thuộc vào a2) (**qmemcpy chỉ để đánh lạc hướng**)

- Tiếp đến thực hiện mã hóa AES bằng cách sử dụng 2 inline asm instructions là `aesenc` và `aesenclast` 

- Tiến hành rotate left `a2` (`a2` là input đã được xử lí ở 2 hàm `encrypt1()` và `encrypt2()`)   `m & 7` bit 

- Xor input với array `v11[]`(là `v11` đã được mã hóa AES)
 
- Tiếp tục rotate left `a2`  `8 - (ii & 7)` bit 

- Cuối cùng là xor các phần tử của `a2` với `0xFF - v11[jj]`


- Vậy để tìm được lại input ban đầu, mình sẽ rev các hàm `encrypt()` theo thứ tự từ `riel_encrypt()` trở về `encrypt1()`, và mình sẽ chia quá trình này ra làm 2 phase ( khả thi vì trong hàm `riel_encrypt()` thì `a2` sẽ được xor với key `v11` chứa các giá trị constants sau khi được encrypt bằng AES và để xử lí 2 phép `rol` kia thì ta chỉ cần làm ngược lại là sử dụng phép `ror`, `encrypt1()` và `encrypt2()` thì chỉ là các phép xor, ta chỉ cần lưu ý vào hàm `encrypt1()` hơn một chút vì cách chúng sử dụng phép xor sẽ có chút đặc biệt là xor 1 byte 1 và xor 4 byte 1)
  
- Phase 1 mình sẽ thực hiện rev 2 hàm `riel_encrypt()` và `encrypt2()`

- Phase 2 sẽ là để rev `encrypt1()` (mình code bằng C phase này vì để mà implement xor 4 byte 1 trong python khá là loằng ngoằng)


- Phase 1
```python
def _ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))
cyphertext = [0]*32
v5 = 0
v4 = 0
v11 = [
    0xA4, 0xA9, 0x01, 0xFF, 0x22, 0xD3, 0xA3, 0x06, 0xDE, 0x2C, 0x17, 0x81, 0xA6, 
    0x70, 0xA6, 0xE6, 0x7B, 0xB6, 0x47, 0x02, 0x7B, 0x8D, 0x2C, 0x0C, 0x4A, 0x17, 
    0x21, 0x91, 0x60, 0x72, 0x08, 0xE4
]
a2 = [
    0x9C, 0x87, 0x9C, 0x6E, 0x64, 0x27, 0x3B, 0x78, 0x71, 0x53, 0x2B, 0x6D, 0xD4, 
    0x0E, 0x82, 0x22, 0x5D, 0xC4, 0xE2, 0xE8, 0x07, 0xB9, 0x85, 0xA7, 0x49, 
    0x9A, 0x6D, 0xD4, 0xFC, 0x64, 0xBA, 0x02
]
sus = [
    0x89, 0xCD, 0x32, 0x41, 0x9A, 0x7C, 0xE5, 0x51,
    0xF1, 0xC2, 0xA1, 0x76, 0x96, 0x59, 0x5F, 0x7A,
    0x4F, 0x47, 0x88, 0x70, 0x4C, 0x63, 0x28, 0xA4,
    0x21, 0x90, 0xEA, 0x00, 0x09, 0xB0, 0x8F, 0x16,
    0x3A, 0x8D, 0x3E, 0x9F, 0x8B, 0xE6, 0x74, 0x33,
    0x40, 0xA2, 0xA8, 0x39, 0x2A, 0x36, 0xC7, 0x5B,
    0xF0, 0xB4, 0xD7, 0x87, 0xDE, 0xF7, 0x4A, 0x8A,
    0x77, 0x30, 0x75, 0xAF, 0x94, 0x5A, 0xDF, 0x67,
    0x48, 0xDD, 0x52, 0x93, 0xA3, 0x2F, 0xFE, 0xA6,
    0x03, 0xD9, 0x4B, 0xC5, 0x5D, 0x62, 0x17, 0x66,
    0xC6, 0x1E, 0xE4, 0xCA, 0x46, 0x19, 0xD6, 0x92,
    0x78, 0xEC, 0xB5, 0x4D, 0xF4, 0xF2, 0x7B, 0x27,
    0x8C, 0x31, 0xA9, 0x3B, 0x12, 0xAA, 0x73, 0x9D,
    0x05, 0xE9, 0xB6, 0xAB, 0x0B, 0x08, 0x97, 0x7E,
    0xBA, 0x9E, 0x20, 0x25, 0x71, 0x38, 0x80, 0x0E,
    0x64, 0xEB, 0xE2, 0xCC, 0xFA, 0xCE, 0xAD, 0x44,
    0x61, 0xF6, 0xFF, 0x69, 0xD0, 0x13, 0x99, 0xFD,
    0xDA, 0x6B, 0x3C, 0x22, 0x56, 0x6E, 0xB2, 0x45,
    0x26, 0x7F, 0xF8, 0x0C, 0xBC, 0x1B, 0x6D, 0xC4,
    0x42, 0xD8, 0x84, 0x72, 0xB3, 0x8E, 0x43, 0x1D,
    0xB9, 0x5C, 0xBE, 0x5E, 0x53, 0x83, 0xCB, 0x85,
    0x95, 0x9B, 0xAE, 0xE8, 0x15, 0xB7, 0xD5, 0xE3,
    0xBF, 0xCF, 0x6C, 0xD3, 0xC3, 0xC1, 0x14, 0x0D,
    0x01, 0xE1, 0xC9, 0x3F, 0xEF, 0x18, 0x68, 0xA7,
    0xE0, 0xC8, 0x2C, 0x86, 0x1F, 0xF5, 0xFB, 0x6A,
    0xDB, 0x54, 0xD4, 0xBB, 0xD2, 0x49, 0x37, 0x23,
    0xD1, 0xEE, 0x2D, 0xAC, 0x60, 0x4E, 0xE7, 0x79,
    0x1C, 0xB1, 0x98, 0x0F, 0x6F, 0x02, 0x7D, 0x0A,
    0xED, 0xA5, 0xA0, 0x06, 0x55, 0x24, 0x58, 0xC0,
    0xBD, 0x91, 0x2B, 0xF3, 0x2E, 0x9C, 0x07, 0xDC,
    0xF9, 0x29, 0x35, 0x05, 0x81, 0x57, 0x82, 0xB8,
    0x50, 0x3D, 0x65, 0x11, 0x34, 0xFC, 0x10, 0x1A
]
print(len(v11))
for i in range(len(v11)):
    a2[i] ^= (0xFF - v11[i])&0xFF
for j in range(len(v11)):
    a2[j] = _ror(a2[j],(8-(j & 7)),8)
for k in range(len(v11)):
    a2[k] ^= v11[k] 
for l in range(len(v11)):
    a2[l] = _ror(a2[l],l&7,8)
for m in range(len(v11)):
    v4 = (v4+sus[v5+1]) &0xFF
    v5 +=1
    v2 = sus[v5]
    sus[v5] = sus[v4]
    sus[v4] = v2
    cyphertext[m] = a2[m] ^ sus[((sus[v4] + sus[v5])&0xFF) % 256]
for i in cyphertext:
    print(hex(i),end= ' ')
```
- Phase 2
  
```C
#include <stdint.h>
#include <stdio.h>

void reverse() {

    uint8_t a1[] = {
        0x4b, 0x58, 0x49, 0x46, 0x7f, 0x29, 0x6c, 0x2a,
        0x2c, 0x24, 0x33, 0x3c, 0x3d, 0x6e, 0x26, 0x64,
        0x4f, 0xdf, 0x98, 0xe6, 0x8b, 0xd8, 0x9f, 0xc7,
        0xc6, 0x90, 0xd0, 0x97, 0x9f, 0x94, 0x95, 0xdc
    };
    for (uint8_t nn = 0; nn < 0x20; ++nn) {
        a1[nn] ^= nn - 17;
    }


    for (uint8_t mm = 0; mm < 0x20; ++mm) {
        a1[mm] ^= 0xEF;
    }


    for (uint8_t kk = 0; kk < 0x20; kk += 4) {
        *(uint32_t*)(a1 + kk) ^= 0xDEADBEEF;
    }


    for (uint8_t jj = 0; jj < 0x20; jj += 4) {
        *(uint32_t*)(a1 + jj) ^= 0xC0FEBABE;
    }


    for (uint8_t ii = 0; ii < 0x20; ++ii) {
        a1[ii] ^= ii - 51;
    }


    for (uint8_t n = 0; n < 0x20; ++n) {
        a1[n] ^= 0xCD;
    }


    for (uint8_t m = 0; m < 0x20; m += 4) {
        *(uint32_t*)(a1 + m) ^= 0xDEADBABE;
    }

    for (uint8_t k = 0; k < 0x20; k += 4) {
        *(uint32_t*)(a1 + k) ^= 0xC0FEBEEF;
    }


    for (uint8_t j = 0; j < 0x20; ++j) {
        a1[j] ^= j - 85;
    }


    for (uint8_t i = 0; i < 0x20; ++i) {
        a1[i] ^= 0xAB;
    }
    printf("%s",a1);
}
int main(){
    reverse();
    return 0;
}
```
**Flag:** `KCSC{6r347!!!y0u_4r3_w1nn3r:333}`
