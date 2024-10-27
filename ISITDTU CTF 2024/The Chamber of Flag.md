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
