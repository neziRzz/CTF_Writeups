# Mics
- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/1ed449b6-a053-4e51-bbfe-06355346f053)

# Detailed Analysis

- Chương trình sẽ bắt ta nhập flag và nếu nhập sai thì....

![image](https://github.com/user-attachments/assets/756bb810-9824-4d4e-98d7-eab7d1321eca)
![image](https://github.com/user-attachments/assets/d800e4c1-59ec-424c-afed-5727ed83d1eb)

- Bởi đây là mội chương trình WinGUI, luồng hoạt động chính sẽ nằm bên trong hàm `WinProc`

![image](https://github.com/user-attachments/assets/e6fcb0de-1628-419f-a3d2-a4869fe1fff5)

- `sub_7FF69C441F90` (bởi trước đó mình có chạy debugger nên địa chỉ có thể sẽ khác so với các bạn)
```C
LRESULT __fastcall sub_7FF69C441F90(HWND a1, UINT a2, WPARAM a3, LPARAM a4)
{
  struct _LIST_ENTRY *RtlAddVectoredExceptionHandler; // [rsp+40h] [rbp-88h]
  tagPAINTSTRUCT Paint; // [rsp+60h] [rbp-68h] BYREF

  switch ( a2 )
  {
    case 2u:
      PostQuitMessage(0);
      ExitProcess(0);
    case 0xFu:
      BeginPaint(a1, &Paint);
      RtlAddVectoredExceptionHandler = api_hashing(0xFDE7F515, 0xF9D7E6D5);
      ((void (__fastcall *)(__int64, __int64 (__fastcall *)(__int64)))RtlAddVectoredExceptionHandler)(
        1LL,
        exception_handler);
      EndPaint(a1, &Paint);
      break;
    case 0x111u:
      switch ( (unsigned __int16)a3 )
      {
        case 'g':
          sub_7FF69C441A30(a1);
          break;
        case 'h':
          DialogBoxParamW(hInstance, (LPCWSTR)0x67, a1, DialogFunc, 0LL);
          break;
        case 'i':
          CloseHandle(hObject);
          DestroyWindow(a1);
          break;
        default:
          return DefWindowProcW(a1, a2, a3, a4);
      }
      break;
    default:
      return DefWindowProcW(a1, a2, a3, a4);
  }
  return 0LL;
}
```
- Hàm này cơ bản là sẽ xử lí một số thứ liên quan đến GUI và thao tác người dùng, một điều đáng chú ý là hàm này có sử dụng kĩ thuật `api_hashing` để resolve ra hàm `RtlAddVectoredExceptionHandler` và gắn hàm `exception_handler` làm luồng sử lí các ngoại lệ sau này. Đồng thời hàm này cũng lấy input của user và input sẽ được xử lí tại `sub_7FF69C441A30`

- `sub_7FF69C441A30`

```C
void __fastcall __noreturn sub_7FF69C441A30(HWND a1)
{
  HWND DlgItem; // rax
  unsigned __int64 v2; // [rsp+20h] [rbp-248h]
  _BYTE *v3; // [rsp+28h] [rbp-240h]
  WCHAR String[256]; // [rsp+50h] [rbp-218h] BYREF

  DlgItem = GetDlgItem(a1, 0x66);
  GetWindowTextW(DlgItem, String, 0x100);
  v2 = 0xFFFFFFFFFFFFFFFFuLL;
  do
    ++v2;
  while ( String[v2] );
  if ( v2 < 46 )
  {
    MessageBoxW(a1, L"Khong du dai", L"Khong du dai", 0);
    v3 = operator new(1uLL);
    *v3 = 0x55;
    pipe_handling(v3, 1u);
    ExitProcess(0);
  }
  sub_7FF69C441350(String);
  sub_7FF69C441520();
}
```
- Trước tiên thì hàm này sẽ kiểm tra độ dài của input, nếu nhỏ hơn 47 thì hiện MSGBOX và gửi `0x55` qua pipe thông qua hàm `pipe_handling` ngược lại thì input sẽ tiếp tục được xử lí tại `sub_7FF69C441350`

- Hàm `pipe_handling`
```C
BOOL __fastcall pipe_handling(void *a1, DWORD a2)
{
  DWORD NumberOfBytesWritten; // [rsp+40h] [rbp-18h] BYREF
  DWORD NumberOfBytesRead; // [rsp+44h] [rbp-14h] BYREF

  while ( 1 )
  {
    hObject = CreateFileW(L"\\\\.\\pipe\\KMACTF", 0xC0000000, 0, 0LL, 3u, 0, 0LL);
    if ( hObject != (HANDLE)-1LL )
      break;
    Sleep(0x64u);
  }
  WriteFile(hObject, a1, a2, &NumberOfBytesWritten, 0LL);
  ReadFile(hObject, a1, a2, &NumberOfBytesRead, 0LL);
  return CloseHandle(hObject);
}
```
- Hàm này sẽ thực hiện mở pipe và data sẽ được trao đổi qua đây. Bởi pipe là một kĩ thuật cho phép 2 tiến trình có thể giao tiếp với nhau nên ta có thể đoán chương trình này có thể sẽ spawn ra một chương trình khác, bằng việc xref đến hàm `CreateProcess`, ta có thể thấy chương trình này spawn ra một chương trình khác có tên `Windows Update Checker 2.exe` và chương trình này được dropped tại thư mục `TEMP` của hệ điều hành

![image](https://github.com/user-attachments/assets/ec4196be-8291-47e1-8109-b4a3b04f76dc)
![image](https://github.com/user-attachments/assets/1daab832-3401-4b76-9c6f-31d1f49fca51)

- Bây giờ ta sẽ tiếp tục phân tích file `Windows Update Checker 2.exe` (luồng hoạt động của chương trình này nằm hết ở bên trong `sub_7FF7B5FD1560`)

```C
void __noreturn sub_7FF7B5FD1560()
{
  char base64_char_before_tranformation; // [rsp+40h] [rbp-B8h]
  char v1; // [rsp+41h] [rbp-B7h]
  int m; // [rsp+44h] [rbp-B4h]
  int v3; // [rsp+48h] [rbp-B0h]
  int k; // [rsp+4Ch] [rbp-ACh]
  int n; // [rsp+50h] [rbp-A8h]
  int i; // [rsp+58h] [rbp-A0h]
  int ii; // [rsp+5Ch] [rbp-9Ch]
  HANDLE hNamedPipe; // [rsp+68h] [rbp-90h]
  int j; // [rsp+70h] [rbp-88h]
  unsigned __int64 v10; // [rsp+78h] [rbp-80h]
  unsigned __int64 v11; // [rsp+80h] [rbp-78h]
  unsigned __int64 v12; // [rsp+88h] [rbp-70h]
  DWORD NumberOfBytesWritten; // [rsp+C8h] [rbp-30h] BYREF
  DWORD NumberOfBytesRead; // [rsp+CCh] [rbp-2Ch] BYREF

  while ( 1 )
  {
    hNamedPipe = CreateNamedPipeW(L"\\\\.\\pipe\\KMACTF", 3u, 6u, 1u, 0x6000u, 0x6000u, 0, 0LL);
    if ( ConnectNamedPipe(hNamedPipe, 0LL) || GetLastError() == 0x217 )
    {
      memset((void *)lpBuffer, 0, 0x600uLL);
      ReadFile(hNamedPipe, (LPVOID)lpBuffer, 0x600u, &NumberOfBytesRead, 0LL);
      switch ( *(_BYTE *)lpBuffer )
      {
        case 5:
          v3 = *(_DWORD *)((char *)lpBuffer + 1);
          if ( exception_codes[counter] != v3 )
            exception_flag = 0;
          base64_char_before_tranformation = *(_BYTE *)(base64_string + counter);
          switch ( v3 )
          {
            case 0x80000003:
              dword_7FF7B5FD5880[counter] = 0x80000003;
              for ( i = 0; i < 0xA; ++i )
                *(_BYTE *)(base64_string + counter) = 7 * (i ^ base64_char_before_tranformation)
                                                    + ((i + 0x33) ^ (*(_BYTE *)(base64_string + counter) + 0x45));
              ++counter;
              ++*(_QWORD *)((char *)lpBuffer + 0x191);
              break;
            case 0xC0000005:
              dword_7FF7B5FD5880[counter] = 0xC0000005;
              for ( j = 0; j < 0xA; ++j )
                *(_BYTE *)(base64_string + counter) = (*(_BYTE *)(base64_string + counter) + j + 0x55) ^ 7;
              ++counter;
              *(_QWORD *)((char *)lpBuffer + 0x191) += 7LL;
              break;
            case 0xC000001D:
              dword_7FF7B5FD5880[counter] = 0xC000001D;
              for ( k = 0; k < 0xA; ++k )
                *(_BYTE *)(base64_string + counter) = (*(char *)(base64_string + counter) << (k % 3))
                                                    & 0x4F
                                                    ^ (0x5B
                                                     * ((k + base64_char_before_tranformation)
                                                      ^ *(_BYTE *)(base64_string + counter))
                                                     + k
                                                     + (base64_char_before_tranformation >> (((k >> 0x1F) ^ k & 1)
                                                                                           - (k >> 0x1F))));
              ++counter;
              *(_QWORD *)((char *)lpBuffer + 0x191) += 2LL;
              break;
            case 0xC0000094:
              dword_7FF7B5FD5880[counter] = 0xC0000094;
              for ( m = 0; m < 0xA; ++m )
                *(_BYTE *)(base64_string + counter) = (m ^ base64_char_before_tranformation)
                                                    + 0x5D
                                                    * ((m + base64_char_before_tranformation)
                                                     ^ (3 * base64_char_before_tranformation
                                                      + m
                                                      + *(_BYTE *)(base64_string + counter)
                                                      + 4 * m));
              ++counter;
              *(_QWORD *)((char *)lpBuffer + 0x191) += 3LL;
              break;
            case 0xC0000096:
              dword_7FF7B5FD5880[counter] = 0xC0000096;
              for ( n = 0; n < 0xA; ++n )
                *(_BYTE *)(base64_string + counter) = (0x4D
                                                     * ((7 * n)
                                                      ^ (*(char *)(base64_string + counter)
                                                       + (base64_char_before_tranformation << (n % 3))
                                                       + 0x2D))
                                                     + n
                                                     + base64_char_before_tranformation)
                                                    % 0xFF;
              ++counter;
              *(_QWORD *)((char *)lpBuffer + 0x191) += 3LL;
              break;
          }
          WriteFile(hNamedPipe, lpBuffer, 0x600u, &NumberOfBytesWritten, 0LL);
          break;
        case 1:
          memset(byte_7FF7B5FD5C80, 0, sizeof(byte_7FF7B5FD5C80));
          v10 = 0xFFFFFFFFFFFFFFFFuLL;
          do
            ++v10;
          while ( *((_BYTE *)lpBuffer + v10 + 1) );
          qmemcpy(byte_7FF7B5FD5C80, (char *)lpBuffer + 1, v10);
          memset((void *)base64_string, 0, 0x100uLL);
          v11 = 0xFFFFFFFFFFFFFFFFuLL;
          do
            ++v11;
          while ( byte_7FF7B5FD5C80[v11] );
          base64_string = (__int64)base64_convert((__int64)byte_7FF7B5FD5C80, v11);
          v12 = 0xFFFFFFFFFFFFFFFFuLL;
          do
            ++v12;
          while ( *(_BYTE *)(base64_string + v12) );
          dword_7FF7B5FD5870 = v12;
          WriteFile(hNamedPipe, lpBuffer, 0x600u, &NumberOfBytesWritten, 0LL);
          break;
        case 8:                                 // check
          if ( counter >= dword_7FF7B5FD5870 )
          {
            v1 = 1;
            for ( ii = 0; ; ++ii )
            {
              if ( ii >= 0x40 )
                goto LABEL_52;
              if ( *(char *)(base64_string + ii) != dest[ii] )
                break;
            }
            v1 = 0;
LABEL_52:
            *(_BYTE *)lpBuffer = 0xCC;
            WriteFile(hNamedPipe, lpBuffer, 1u, &NumberOfBytesWritten, 0LL);
            exception_flag = 1;
            counter = 0;
            if ( v1 )
            {
              MessageBoxW(0LL, L"Correct", L"Correct", 0x40000u);
            }
            else
            {
              MessageBoxW(0LL, L"Wrong", L"Wrong", 0x40000u);
              sub_7FF7B5FD1550();
            }
          }
          else
          {
            *(_BYTE *)lpBuffer = *(_BYTE *)(base64_string + counter);
            if ( !exception_flag )
            {
              *(_BYTE *)lpBuffer = 0xCC;
              WriteFile(hNamedPipe, lpBuffer, 1u, &NumberOfBytesWritten, 0LL);
              counter = 0;
              exception_flag = 1;
              CloseHandle(hNamedPipe);
              MessageBoxW(0LL, L"Wrong", L"Wrong", 0x40000u);
              sub_7FF7B5FD1550();
            }
            WriteFile(hNamedPipe, lpBuffer, 1u, &NumberOfBytesWritten, 0LL);
          }
          break;
        case 0x54:
          ExitProcess(0);
        case 0x55:
          sub_7FF7B5FD1550();
          ExitProcess(0);
      }
    }
    CloseHandle(hNamedPipe);
  }
}
```
- Đầu tiên chương trình sẽ tiến hành mở và tạo kết nối đên pipe để kết nối đến chương trình cha. Chương trình sẽ có 5 case chính, ta sẽ lần lượt phân tích qua các case này

  + `Case 5` : Biến đổi lần lượt các kí tự của string base64 được gen ra từ `case 1` dựa trên các mã lỗi tương ứng của các kí tự (mã lỗi được gen ra từ tiến trình cha, mình sẽ phân tích hàm đó sau)
  + `Case 1` : Biến đổi input đầu vào của user thành base64 và gửi lại data qua pipe
  + `Case 8` : Kiểm tra input sau khi biến đổi hoàn tất
  + `Case 0x54`: Thoát tiến trình con
  + `Case 0x55`: Tạo tiến trình để troll user
- Vậy để solve ta sẽ cần phải tìm lại string base64 trước khi bị biến đổi (bruteforce bởi string được biến đổi từng byte một), việc này tương đối dễ dàng bởi author đã cho ta các mã lỗi tương ứng cho từng kí tự tại `Case 5`, bây giờ ta sẽ quay lại `sub_7FF69C441520` ở tiến trình cha để tìm các mã lỗi cho các kí tự
```C
void __noreturn sub_7FF69C441520()
{
  __int64 v0; // rdx
  _BYTE *v1; // [rsp+28h] [rbp-30h]

  while ( 1 )
  {
    v1 = operator new(1u);
    *v1 = 8;
    pipe_handling(v1, 1u);
    switch ( *v1 )
    {
      case '+':
        stat_illg_inst();                       // 0xC000001D
      case '/':
      case 'C':
      case 'D':
      case 'F':
      case 'N':
      case 'P':
      case 'c':
      case 'j':
      case 'k':
      case 'p':
      case 'q':
      case 't':
      case 'w':
        stat_breakpoint();                      // 0x80000003
        break;
      case '0':
      case '6':
      case '7':
      case 'A':
      case 'B':
      case 'K':
      case 'L':
      case 'O':
      case 'T':
      case 'b':
      case 'g':
      case 'y':
      case 'z':
        stat_access_violation();                // 0xC0000005
        break;
      case '1':
      case '4':
      case '5':
      case '8':
      case '=':
      case 'I':
      case 'J':
      case 'U':
      case 'W':
      case 'd':
      case 'f':
      case 'r':
      case 'u':
        stat_priv_ins();                        // 0xC0000096
        break;
      case '2':
        stat_illg_inst();                       // 0xC000001D
      case '3':
      case '9':
      case 'E':
      case 'G':
      case 'M':
      case 'Q':
      case 'S':
      case 'V':
      case 'Y':
      case 'e':
      case 'h':
      case 'i':
      case 'n':
        stat_div_0(0x7FF69C440000LL, v0);       // 0xC0000094
        break;
      case 'H':
        stat_illg_inst();                       // 0xC000001D
      case 'R':
        stat_illg_inst();                       // 0xC000001D
      case 'X':
        stat_illg_inst();                       // 0xC000001D
      case 'Z':
        stat_illg_inst();                       // 0xC000001D
      case 'a':
        stat_illg_inst();                       // 0xC000001D
      case 'l':
        stat_illg_inst();                       // 0xC000001D
      case 'm':
        stat_illg_inst();                       // 0xC000001D
      case 'o':
        stat_illg_inst();                       // 0xC000001D
      case 's':
        stat_illg_inst();                       // 0xC000001D
      case 'v':
        stat_illg_inst();                       // 0xC000001D
      case 'x':
        stat_illg_inst();                       // 0xC000001D
      case '\xCC':
        *v1 = 0x54;
        pipe_handling(v1, 1u);
        ExitProcess(0);
      default:
        break;
    }
    j_j_free(v1);
  }
}
```
- Từ đây ta có thể thấy được các kí tự tương ứng với một số mã lỗi như `STATUS_ILLEGAL_INSTRUCTION`, `STATUS_PRIVILEGED_INSTRUCTION`,.... Từ những dữ kiện này, mình đã viết script giải (đề ở một file riêng trong cùng folder) và nhận được kết quả như sau

![image](https://github.com/user-attachments/assets/79864e89-a8f4-49ee-a167-d982f369a8bd)

- Decode string trên ta được flag

# Script and Flag
**Flag:** `KMACTF{how_many_times_are_you_died_today?huh?}`

  
