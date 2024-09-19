- Đề cho 3 file. txt, mini dmp và PE64

- Đáng ra sau khi được author `13r_ə_Rɪst` hint bài `Time travel` thì mình nên làm bài này sớm hơn...

![image](https://github.com/user-attachments/assets/8ee98a13-d7a9-4f71-b68d-74453255604f)

- Pseudocode của IDA
```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  __int64 i; // rbx
  HANDLE FileW; // rdi
  int FileSize; // ebp
  __int64 v7; // rbx
  void *v8; // rsi
  int v9; // r8d
  _BYTE *v10; // rdx
  int v11; // eax
  DWORD NumberOfBytesRead; // [rsp+40h] [rbp-28h] BYREF
  __int128 v14; // [rsp+48h] [rbp-20h]

  v14 = 0i64;
  v3 = time32(0i64);
  srand(v3);
  NumberOfBytesRead = 0;
  for ( i = 0i64; i < 16; ++i )
    *((_BYTE *)&v14 + i) = rand();
  BYTE12(v14) = dword_140005088;
  BYTE13(v14) = dword_140005080;
  BYTE14(v14) = dword_14000508C;
  HIBYTE(v14) = dword_140005084;
  FileW = CreateFileW(FileName, 0xC0000000, 3u, 0i64, 3u, 0x80u, 0i64);
  if ( FileW == (HANDLE)-1i64 )
    sub_140001010(aCannotOpenFile);
  FileSize = GetFileSize(FileW, 0i64);
  v7 = FileSize;
  v8 = malloc(FileSize);
  if ( !v8 )
  {
    CloseHandle(FileW);
    sub_140001010(aFileIsEmpty);
  }
  ReadFile(FileW, v8, FileSize, &NumberOfBytesRead, 0i64);
  v9 = 0;
  if ( FileSize > 0 )
  {
    v10 = v8;
    do
    {
      v11 = v9 % 16;
      ++v9;
      *v10++ ^= *((_BYTE *)&v14 + v11);
      --v7;
    }
    while ( v7 );
  }
  sub_140001010(aHayGiupBenjLol);
  SetFilePointer(FileW, 0, 0i64, 0);
  WriteFile(FileW, v8, FileSize, &NumberOfBytesRead, 0i64);
  CloseHandle(FileW);
  sub_140001010(aHoacGui200kVao);
  sub_140001010(aNoiDungChuyenK);
  sub_140001010(aNoteSaiCuPhapL);
  system(Command);
  return 0;
}
```
- Đầu tiên, chương trình sẽ gọi hàm `time32()` để lấy số giây tính từ Unix Epoch đến thời điểm bắt đầu chạy chương trình, gán vào `v3` rồi sử dụng `v3` làm seed
  
- Tiếp theo, chương trình khởi tạo mảng `v14` có độ dài 16 byte rồi cho gán cho giá trị của từng byte trong mảng là giá trị trả về của hàm `rand()`(**đã được AND với 0xFF**), sau khi gán hết thì thực hiện overwrite 4 byte cuối bằng các giá trị 0xCA, 0xFE, 0xBE, 0xEF (Có điều đặc biệt về 4 byte này, mình sẽ nói sau)

- Sau đó chương trình sẽ thực hiện mở file `important_note.txt`, thực hiện lưu content của file này vào `v8` và thực hiện mã hóa bằng phép xor với key là `v14` có index được duyệt theo `v11 = v9 % 16`

- Sau khi mã hóa và viết lại vào file xong, chương trình sẽ hiện lên ransom note với nội dung như sau @@

![image](https://github.com/user-attachments/assets/176cfa83-870c-4be7-b33f-8a7e6ea32fe0)

- Vậy để đảo ngược chu trình mã hóa, đầu tiên ta sẽ phải tìm seed đúng, vì `v14` là key cho việc mã hóa hơn nữa `v14` lại được gen ra từ hàm `rand()`. Sau khi tìm được seed đúng xong, ta chỉ cần lấy `v14` xor với cyphertext là sẽ ra được flag. Về mặt ý tưởng thì bài này khá giống bài `Time travel`.

- Mình đã có đề cập ở trên là 4 byte 0xCA, 0xFE, 0xBE, 0xEF có điều đặc biệt. Khi mình kiểm tra xem những byte này được truy cập ở những đâu (trỏ vào rồi bấm x để mở cửa sổ xrefs trên IDA) thì thấy có điều đặc biệt

![image](https://github.com/user-attachments/assets/4f90dc65-9ddc-42f8-a4e4-1306370c0272)

- Vào hàm `TlsCallback_0()`

```C
NTSTATUS TlsCallback_0()
{
  NTSTATUS result; // eax
  __int64 ProcessInformation; // [rsp+30h] [rbp-18h] BYREF

  ProcessInformation = 0i64;
  result = NtQueryInformationProcess((HANDLE)0xFFFFFFFFFFFFFFFFi64, ProcessDebugPort, &ProcessInformation, 8u, 0i64);
  if ( !result )
  {
    if ( ProcessInformation )
    {
      dword_140005088 = 222;
      dword_140005080 = 173;
      dword_14000508C = 186;
      dword_140005084 = 190;
    }
  }
  return result;
}
```
- Có thể thấy rắng hàm này sẽ thực hiện gọi 1 hàm là `NtQueryInformationProcess()`, hàm này có nhiệm vụ lấy những thông tin về process đang chạy [tham khảo ở đây](https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntqueryinformationprocess), sau đó kiểm tra giá trị trả về trong class `ProcessDebugPort` có trả về 0 (không bị debug) hay không, nếu trả về giá trị khác 0 ( cụ thể là 0xFFFFFFFF or -1 và có nghĩa tiến trình bị debug) thì sẽ thực hiện overwrite 4 byte mà mình vừa đề cập trước đó sang các giá trị khác ([các bạn có thể tham khảo thêm về kĩ thuật trên cũng như là các kĩ thuật anti debug khác ở đây](https://anti-debug.checkpoint.com/techniques/debug-flags.html#using-win32-api-ntqueryinformationprocess))

- Điều kì lạ ở đây là, khi mình kiểm tra xrefs đến hàm `TlsCallback_0()` thì không hề có hàm nào gọi tới nó cả, vậy thì tại sao chương trình lại chạy đến hàm này?

![image](https://github.com/user-attachments/assets/31e2bc29-5b45-458b-abc0-6baa913caaa7)

- Để giải thích cho câu hỏi này thì ta cần phải biết `TLS Callbacks` là gì. Để giải thích một cách ngắn gọn nhất thì `TLS Callbacks` là tập hợp các hàm được định nghĩa trong thư mục `TLS` của 1 file PE, Windows loader sẽ có trách nhiệm thực thi các hàm này trước mỗi lần tạo thread, điều này có nghĩa là chúng sẽ được gọi trước cả main thread [References](https://medium.com/@andreabocchetti88/tls-callbacks-to-bypass-debuggers-60409195ed76)

- Vậy để bypass đoạn check debug này, ta chỉ cần patch lại instruction `jnz  short loc_7FF63EB610E0` thành `jmp` là được (Các bạn patch bằng cách Edit-Patch program-Assemble)

  ![image](https://github.com/user-attachments/assets/c3e85f48-1344-4d34-98e6-d027b1ff66a3)

  
- Giải quyết xong anti debug, ta chỉ cần viết script brute seed và gen ra flag

```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main() {

unsigned int ciphertext[] = {
    0xF4, 0xB6, 0x74, 0x47, 0x38, 0x1A, 0xAE, 0x65,
    0xD4, 0x82, 0xA5, 0xBB, 0xEA, 0x9F, 0xD0, 0x87,
    0x9F, 0x97, 0x48, 0x6D, 0x63, 0x06, 0xA9, 0x65,
    0x9A, 0xC3, 0xAE, 0xBE, 0xEA, 0x8A, 0xD6, 0x9A,
    0xDE, 0xD5, 0x55, 0x6B, 0x2A, 0x54, 0xB2, 0x65,
    0xD7, 0x82, 0xA5, 0xBB, 0xEA, 0x92, 0xDF, 0x82,
    0x9F, 0x99, 0x48, 0x6D, 0x63, 0x15, 0xA8, 0x64,
    0x9A, 0xC1, 0xA8, 0xA3, 0xAB, 0xDE, 0xCA, 0x9A,
    0xD1, 0x92, 0x07, 0x60, 0x22, 0x19, 0xE6, 0x62,
    0xD5, 0xCB, 0xE0, 0xB7, 0xA4, 0x96, 0x9E, 0x96,
    0xDA, 0x80, 0x07, 0x69, 0x2C, 0x00, 0xE6, 0x6D,
    0xD3, 0x82, 0xB4, 0xBE, 0xAF, 0xDE, 0xD0, 0x8E,
    0xC6, 0xD4, 0x06, 0x79
};

    size_t cipher_len = sizeof(ciphertext)/sizeof(ciphertext[0]);
    unsigned int past = 0;
    unsigned int present = (unsigned int)_time32(NULL); 

for(int i = past; i <= present;i++){
    srand(i);
    unsigned char decrypted[100];
    unsigned int v14[16];
    for(int j = 0;j<16;j++){
        v14[j] = (rand()) & 0xFF;
    }
    v14[12] = 0xCA;
    v14[13] = 0xFE;
    v14[14] = 0xBE;
    v14[15] = 0xEF;
    for(int k = 0; k< cipher_len;k++){
        decrypted[k] = v14[k % 16] ^ ciphertext[k]; 
    }
    if (strncmp((char*)decrypted, "KCSC{", 5) == 0) {
            printf("%d ",i);
            printf("%s\n",decrypted);
            break;
        }
}  
    return 0;
}
```

- Flag được gen với seed `13973678`

![image](https://github.com/user-attachments/assets/26b32557-5616-4fc2-a931-6bd471cc6b09)

**Flag:** `KCSC{nhin em anh boi roi anh thua roi tim em lam loi anh chua tung dam noi anh yeu mot ai the nay!!}`
