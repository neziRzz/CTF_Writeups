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

- Có lẽ trong lúc decrypt flag thì chương trình đã bị lỗi ở đâu đó, nên mình quyết định tìm hàm decrypt và trace ngược lại hàm nào đã gọi nó

- Hàm `sub_1400010C8` (decrypt)
```C
__int64 __fastcall sub_1400010C8(PUCHAR pbInput, __int64 a2, __int64 a3, UCHAR *a4, PUCHAR a5)
{
  phAlgorithm = 0i64;
  phKey = 0i64;
  *(_DWORD *)pbOutput = 0;
  v7 = 98;
  pcbResult = 0;
  wcscpy(pszAlgId, L"b#'1");                    // AES
  v8 = 0i64;
  while ( 1 )
  {
    pszAlgId[++v8] ^= v7;
    if ( v8 >= 3 )
      break;
    v7 = pszAlgId[0];
  }
  pszAlgId[4] = 0;
  if ( BCryptOpenAlgorithmProvider(&phAlgorithm, &pszAlgId[1], 0i64, 0) )
    return 0i64;
  v9 = 0i64;
  *(_DWORD *)pbInputa = 6881346;
  v10 = 1;
  v23 = 0;
  v22 = 1;
  v25 = 6815840;
  v11 = 111;
  v26 = 6815855;
  v27 = 6684783;
  v28 = 7209036;
  v29 = 6553701;
  v30 = 4390978;
  v31 = 66;
  while ( 1 )
  {
    *(_WORD *)&pbInputa[2 * v9++] ^= v10;
    if ( v9 >= 0xF )
      break;
    v10 = v22;
  }
  HIWORD(v31) = 0;
  v12 = 41;
  wcscpy(pszProperty, L")jAH@G@GNdFML");        // ChainingMode - CBC
  v13 = 0i64;
  while ( 1 )
  {
    pszProperty[++v13] ^= v12;
    if ( v13 >= 0xC )
      break;
    v12 = pszProperty[0];
  }
  pszProperty[13] = 0;
  if ( BCryptSetProperty(phAlgorithm, &pszProperty[1], pbInputa, 0x20u, 0) )
    return 0i64;
  wcscpy(pszProperty, L"o \r\x05\n\f\x1B#\n\x01\b\x1B\a");// ObjectLength
  v14 = 0i64;
  while ( 1 )
  {
    pszProperty[++v14] ^= v11;
    if ( v14 >= 0xC )
      break;
    v11 = pszProperty[0];
  }
  pszProperty[13] = 0;
  if ( BCryptGetProperty(phAlgorithm, &pszProperty[1], pbOutput, 4u, &pcbResult, 0) )
    return 0i64;
  v15 = *(_DWORD *)pbOutput;
  ProcessHeap = GetProcessHeap();
  v17 = (UCHAR *)HeapAlloc(ProcessHeap, 0, v15);
  if ( !v17 )
    return 0i64;
  if ( BCryptGenerateSymmetricKey(phAlgorithm, &phKey, v17, *(ULONG *)pbOutput, &pbSecret, 0x20u, 0) )
    return 0i64;
  v36 = 16;
  if ( BCryptDecrypt(phKey, pbInput, 0x10u, 0i64, a4, 0x10u, a5, 0x10u, &v36, 0) )
    return 0i64;
  BCryptDestroyKey(phKey);
  BCryptCloseAlgorithmProvider(phAlgorithm, 0);
  v18 = GetProcessHeap();
  HeapFree(v18, 0, v17);
  return 1i64;
}
```
- Hàm này có nhiệm vụ decrypt flag cho chúng ta bằng thuật toán `AES` với mode là `CBC`, sử dụng cửa sổ xref của IDA, ta có thể thấy có 1 hàm gọi đến hàm này

![image](https://github.com/user-attachments/assets/62213cbc-cb03-45f2-91b7-97539f82fcbd)

- Hàm `sub_140001A00`
```C
int sub_140001A00()
{
///......
 if ( VirtualQuery(v14, &Buffer, 0x30ui64) )
      {
        if ( Buffer.BaseAddress )
        {
          memset(v13, 0, 0x200ui64);
          v15 = *((_QWORD *)v13 + 67);
          v16 = 0;
          v17 = 0;
          if ( v15 != *((_QWORD *)v13 + 68) )
          {
            v18 = _mm_load_si128((const __m128i *)&xmmword_140004E50);
            v19 = (UCHAR *)(v15 + 4);
            do
            {
              memset(v35, 0, sizeof(v35));
              if ( !(unsigned int)sub_1400010C8(v19, v35) )
                *(__m128i *)v35 = v18;
              v20 = 0;
              v21 = v35;
              do
///......
```
- Hàm decrypt của chúng ta được gọi tại đây, tiến hành debug để kiểm tra thì mình thấy rằng chương trình không hề chạy vào luồng này, và khi mình thử patch lại chương trình thì xuất hiện lỗi như sau

![image](https://github.com/user-attachments/assets/3775ec4e-ca6e-4eab-bfed-2a2d8b383476)

- Lí do cho điều này là bởi một trong những arguments (cyphertext) của hàm decrypt `sub_1400010C8` không trỏ đến một vùng nhớ hợp lệ

![image](https://github.com/user-attachments/assets/c21bbd64-fbf8-4b60-bd04-abd73036c928)
![image](https://github.com/user-attachments/assets/224a81b4-6d20-4a33-8a87-18c3798a4f61)

- Ta có thể thấy rằng register `RCX` không trỏ đến 1 vùng nhớ không hợp lệ, nhưng giờ kể cả có tìm được vùng nhớ hợp lệ đi chăng nữa thì liệu đó có đúng là vùng nhớ chứa cyphertext?
Sau khi mò xung quanh vùng nhớ chứa giá trị của RCX thì mình có tìm được một chuỗi hex khá đáng nghi

![image](https://github.com/user-attachments/assets/b7b65c85-ba45-4000-b5cf-bb1de4c8b9d9)

- Mình thử set lại cho `RCX` trỏ vào vùng này thì ra flag được in ra màn hình

![image](https://github.com/user-attachments/assets/a6d8f94a-33e7-4134-86c7-e5aa93f07c5c)

# Script and Flag
**Flag:**: `ISITDTU{STATIC_STRUCt_INITIALIZATION_FAiLED}`
