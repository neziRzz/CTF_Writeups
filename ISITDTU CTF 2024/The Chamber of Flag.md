# Mics
- Đề cho 1 file PE64
![image](https://github.com/user-attachments/assets/2b254465-38fd-4a4d-b07c-9b231e7b5d39)

# Detailed analysis
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
