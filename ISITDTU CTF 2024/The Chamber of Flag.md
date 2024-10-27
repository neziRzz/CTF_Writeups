# Mics
- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/2b254465-38fd-4a4d-b07c-9b231e7b5d39)

# Detailed analysis
## Basic dynamic analysis
- Khi mở chương trình sẽ xuất hiện cửa sổ sau

![image](https://github.com/user-attachments/assets/f86d6195-11f2-4a85-a269-ea379e070e54)

- Ta có 2 lựa chọn là `Login` và `About`, trong đó `Login` sẽ bắt ta nhập `Secret` và `About` hiện lên thông tin về challenge, đồng thời số lượng kí tự tối đa của `Secret` là 6. Nếu ta nhập sai thì chương trình sẽ tiếp tục luồng nhập `Secret`

![image](https://github.com/user-attachments/assets/1ff5542f-8b26-4ddb-869d-1258748a2531)
![image](https://github.com/user-attachments/assets/390f9589-8bae-44dc-bbbc-47d2789fe53b)

- Đến đây, mình sẽ tiếp tục phân tích qua IDA để hiểu rõ hơn về cách chương trình hoạt động

## Advanced analysis
- IDA's Pseudocode (Vì mã giả khá dài nên mình sẽ rút gọn và chỉ đề cập đến những hàm quan trọng)
- Hàm `WinMain`
```C
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
while ( 2 )
  {
    memset(&Buffer, 0, sizeof(Buffer));
    while ( 1 )
    {
      NumberOfEvents = 0;
      if ( !GetNumberOfConsoleInputEvents(hConsoleInput, &NumberOfEvents) || !NumberOfEvents )
        break;
      if ( !ReadConsoleInputA(hConsoleInput, &Buffer, 1u, &NumberOfEvents) || NumberOfEvents != 1 )
        break;
  \\\...........................
    return 0;
  }
}
```
- Hàm này chỉ đơn thuần lấy keystroke của player

- Hàm `sub_140001530`
```C
char __fastcall sub_140001530(double a1)
{
\\\........
      if ( v10 == 6 )
      {
        phAlgorithm = 0i64;
        *(_OWORD *)pbOutput = 0i64;
        phHash = 0i64;
        v13 = 77;
        v30 = 0i64;
        wcscpy(pszAlgId, L"M\x1E\x05\f\x7Fx{"); // sha-256
        v14 = 0i64;
        while ( 1 )
        {
          pszAlgId[++v14] ^= v13; // decrypt AlgId
          if ( v14 >= 6 )
            break;
          v13 = pszAlgId[0];
        }
        pszAlgId[7] = 0;
        LODWORD(v9) = BCryptOpenAlgorithmProvider(&phAlgorithm, &pszAlgId[1], 0i64, 0);
        if ( !(_DWORD)v9 )
        {
          LODWORD(v9) = BCryptCreateHash(phAlgorithm, &phHash, 0i64, 0, 0i64, 0, 0);
          if ( !(_DWORD)v9 )
          {
            LODWORD(v9) = BCryptHashData(phHash, &pbInput, 6u, 0);
            if ( !(_DWORD)v9 )
            {
              LODWORD(v9) = BCryptFinishHash(phHash, pbOutput, 0x20u, 0);
              if ( !(_DWORD)v9 )
              {
                BCryptDestroyHash(phHash);
                BCryptCloseAlgorithmProvider(phAlgorithm, 0);
                v9 = RtlCompareMemory(&unk_1400044B8, pbOutput, 0x20ui64);
                if ( v9 == 32 )
                {
                  qword_140008E08 = 3i64;
                  *(_OWORD *)&::pbSecret = *(_OWORD *)pbOutput;
                  LODWORD(qword_140008DF0) = 0;
                  xmmword_140008E28 = v30;
                  LOBYTE(v9) = (unsigned __int8)memset(&pbInput, 0, 0x400ui64);
                  dword_1400089E0 = 0;
                  dword_140008E00 = 1000;
                }
              }
            }
          }
        }
      }
    }
  }
  return v9;
```
- Hàm này có nhiệm vụ hash `Secret` mà player nhập vào sử dụng WINAPI bằng thuật toán `SHA-256` (pszAlgId bị encrypt bằng XOR) và sau đó kiểm tra chuỗi hash thu được sau khi mã hóa với `unk_1400044B8`. Như mình đã đề cập ở trên, độ dài tối đa của `Secret` là 6 và thuật toán hash là `SHA-256` ta có thể dễ dàng bruteforce `Secret` với hashcat với command như sau `hashcat.exe -a 3 -m 1400 26F2D45844BFDBC8E5A2AE67149AA6C50E897A2A48FBF479D1BFB9F0D4E24544 ?a?a?a?a?a?a` với `-a 3` là chế độ bruteforce, `-m 1400` là mode `SHA-256`, `26F2D45844BFDBC8E5A2AE67149AA6C50E897A2A48FBF479D1BFB9F0D4E24544` là chuỗi hash cần bruteforce (trong trường hợp này là `unk_1400044B8`) và cuối cùng là `?a?a?a?a?a?a` tượng trưng cho 6 kí tự printable ASCII, kết quả của command này sẽ là `808017`. Sau khi nhập chuỗi nhận được vào `Secret` thì menu của chương trình có sự thay đổi

![image](https://github.com/user-attachments/assets/164bc3ad-e39f-4784-ae52-ecb872929602)

- Khi chọn mục `Flag` thì mình nghĩ đến đây là xong nhưng chương trình lại in ra chuỗi sau

![image](https://github.com/user-attachments/assets/ef4fd0af-3172-44a4-9a59-a809f9e8bc96)
