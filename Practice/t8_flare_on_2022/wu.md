# Mics
- Given a PE32 executable and a PCAPNG file

![image](https://github.com/user-attachments/assets/99155344-8d2b-4d18-a42e-8e7c50ce20ca)

# Detailed Analysis
- First when I tried to determine whether any functions are called before `main`, I found a very suspicious looking function
```C
int sub_171020()
{
  struct _SYSTEMTIME SystemTime; // [esp+4h] [ebp-20h] BYREF
  int v2; // [esp+20h] [ebp-4h]

  v2 = 0;
  memmove_thing(&dword_1C0874, L"FO9", 3u);
  GetLocalTime(&SystemTime);
  srand(SystemTime.wMilliseconds + 1000 * (SystemTime.wSecond + 60 * SystemTime.wMinute));
  dword_1C0870 = rand();
  xmmword_1C088C = (__int128)SystemTime;
  return atexit(sub_1ADC50);
}
```
- This function gets the current time then use it as seed for `srand`, the generated random value then appended with `dword_1C0874`. This value will be used later so we will need to remember this

- The `main` function is rather long so I will only go into detail about functions that are crucial for analysis

```C
 for ( i = xmmword_1C088C; moon_phase_calc(i, DWORD1(i)) != 0xF; i = xmmword_1C088C )
    Sleep(0x2932E00u);
```
- First, the `main` function seems to calculate something related to the `moon phase`, when the current date does not corresponse to the full moon, It sleeps until the next full moon
- Then it initialize some strings like `flare-on.com`, `POST` and `ahoy`, based on these strings, we can somewhat guess that the program will be some kind of client that makes some kind of HTTP requests to `flare-on.com` using the `POST` method. One thing to take note is that these strings are in `UTF-16LE` format

![image](https://github.com/user-attachments/assets/5ee9b727-4d70-4460-b767-1afd341bcf06)
![image](https://github.com/user-attachments/assets/9158f6cd-5f1d-4265-95c8-c16cc8761ce7)
![image](https://github.com/user-attachments/assets/21c9a387-e8a1-461a-a33f-236f3e43f846)

