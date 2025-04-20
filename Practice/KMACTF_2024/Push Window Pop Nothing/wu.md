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
