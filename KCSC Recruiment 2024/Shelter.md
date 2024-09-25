- Đề cho 1 file PE32

![image](https://github.com/user-attachments/assets/03f411b9-7a5d-4314-ac4c-82f010f14ed0)

- Pseudocode của IDA (mình đã rename lại một số hàm và biến để tiện hơn cho việc phân tích)
```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  get_input();
  pad();
  init_sha256_key();
  init_MD5_IV();
  start_encrypt();
  check();
  return 0;
}
```
- Hàm main không có gì nhiều và chức năng của các hàm cũng không quá phức tạp, sau đây mình sẽ phân tích từng hàm

- Hàm `get_input()`
```C
char *get_input()
{
  FILE *v0; // eax
  char savedregs; // [esp+0h] [ebp+0h]

  sub_921040("Enter Your Flag: ", savedregs);
  v0 = _acrt_iob_func(0);
  return fgets(input, 80, v0);
}
```
- Hàm này đơn thuần chỉ là lấy input

- Hàm `pad()`
```C
unsigned int sub_9210B0()
{
  unsigned int result; // eax
  unsigned int v1; // [esp+Ch] [ebp-14h]
  unsigned int v2; // [esp+10h] [ebp-10h]
  unsigned int i; // [esp+14h] [ebp-Ch]

  v1 = strlen(input);
  result = 16 - v1 % 16;
  v2 = result;
  if ( result != 16 )
  {
    for ( i = 0; i < v2; ++i )
    {
      result = i + v1;
      if ( i + v1 >= 80 )
        sub_921756();
      input[i + v1] = 0;
    }
  }
  return result;
}
```
- Hàm này có nhiệm vụ kiểm tra độ dài input của chúng ta có phải là bội của 16 hay không, nếu không sẽ tiến hành pad thêm các byte 0 vào để phục vụ cho việc mã hóa, tại sao lại vậy bởi vì phần lớn các thuật toán mã hóa hiện nay sẽ thực hiện mã hóa 128 bit (16 byte) cho mỗi một round mã hõa, cụ thể như trong bài này sẽ là mã hóa AES, các bạn có thể tìm hiểu thêm về thuật toán này tại [đây](https://vi.wikipedia.org/wiki/Advanced_Encryption_Standard)

- Hàm `init_sha256_key()`
```C
BOOL sub_921150()
{
  BOOL result; // eax
  DWORD pdwDataLen; // [esp+14h] [ebp-10h] BYREF
  HCRYPTPROV phProv; // [esp+18h] [ebp-Ch] BYREF
  HCRYPTHASH phHash; // [esp+1Ch] [ebp-8h] BYREF

  result = CryptAcquireContextW(&phProv, 0, 0, 0x18u, 0xF0000000);
  if ( result )
  {
    if ( CryptCreateHash(phProv, CALG_SHA_256, 0, 0, &phHash) )
    {
      if ( CryptHashData(phHash, key, strlen((const char *)key), 0) )
      {
        pdwDataLen = 32;
        CryptGetHashParam(phHash, 2u, &pbData, &pdwDataLen, 0);
        CryptDestroyHash(phHash);
        return CryptReleaseContext(phProv, 0);
      }
      else
      {
        CryptDestroyHash(phHash);
        return CryptReleaseContext(phProv, 0);
      }
    }
    else
    {
      return CryptReleaseContext(phProv, 0);
    }
  }
  return result;
}
```
- Hàm này sử dụng crypto api của Microsoft để thực hiện hash string `https://www.youtube.com/watch?v=fzQ6gRAEoy0` (MV Shelter) bằng thuật toán SHA-256, dữ liệu sau khi được hash sẽ được sử dụng làm key cho việc mã hóa (cụ thể tại sao mình sẽ phân tích trong hàm `start_encrypt()`)

- Hàm `init_MD5_IV()`
```C
BOOL sub_921280()
{
  BOOL result; // eax
  DWORD pdwDataLen; // [esp+14h] [ebp-10h] BYREF
  HCRYPTPROV phProv; // [esp+18h] [ebp-Ch] BYREF
  HCRYPTHASH phHash; // [esp+1Ch] [ebp-8h] BYREF

  result = CryptAcquireContextW(&phProv, 0, 0, 0x18u, 0xF0000000);
  if ( result )
  {
    if ( CryptCreateHash(phProv, CALG_MD5, 0, 0, &phHash) )
    {
      if ( CryptHashData(phHash, key, strlen((const char *)key), 0) )
      {
        pdwDataLen = 16;
        CryptGetHashParam(phHash, 2u, &IV, &pdwDataLen, 0);
        CryptDestroyHash(phHash);
        return CryptReleaseContext(phProv, 0);
      }
      else
      {
        CryptDestroyHash(phHash);
        return CryptReleaseContext(phProv, 0);
      }
    }
    else
    {
      return CryptReleaseContext(phProv, 0);
    }
  }
  return result;
}
```
- Hàm này có nhiệm vụ hash string `https://www.youtube.com/watch?v=fzQ6gRAEoy0` bằng thuật toán MD5 sử dụng crypto api của Microsoft, dữ liệu sau khi hash sẽ được sử dụng làm IV (Initialization Vector) cho việc mã hóa, các bạn có thể tìm hiểu thêm về IV tại [đây](https://en.wikipedia.org/wiki/Initialization_vector), về tại sao dữ liệu sau khi hash lại được sử dụng làm IV mình xin phép phân tích tại hàm `start_encrypt()` 

- Hàm `start_encrypt()`
```C
BOOL start_encrypt()
{
  BOOL result; // eax
  BYTE pbData[2]; // [esp+18h] [ebp-40h] BYREF
  __int16 v2; // [esp+1Ah] [ebp-3Eh]
  int v3; // [esp+1Ch] [ebp-3Ch]
  int v4; // [esp+20h] [ebp-38h]
  char v5[32]; // [esp+24h] [ebp-34h] BYREF
  BYTE v6[4]; // [esp+44h] [ebp-14h] BYREF
  DWORD pdwDataLen; // [esp+48h] [ebp-10h] BYREF
  HCRYPTPROV phProv; // [esp+4Ch] [ebp-Ch] BYREF
  HCRYPTKEY phKey; // [esp+50h] [ebp-8h] BYREF

  result = CryptAcquireContextW(&phProv, 0, L"Microsoft Enhanced RSA and AES Cryptographic Provider", 24u, 0);
  if ( result )
  {
    pbData[0] = 8;
    pbData[1] = 2;
    v2 = 0;
    v3 = 0x6610;
    v4 = 0x20;
    qmemcpy(v5, &::pbData, sizeof(v5));
    if ( CryptImportKey(phProv, pbData, 44u, 0, 0, &phKey) )
    {
      *(_DWORD *)v6 = 1;
      if ( CryptSetKeyParam(phKey, KP_MODE, v6, 0) && CryptSetKeyParam(phKey, KP_IV, &IV, 0) )
      {
        pdwDataLen = strlen(input);
        if ( CryptEncrypt(phKey, 0, 1, 0, 0, &pdwDataLen, 0) )
        {
          dword_924418 = pdwDataLen;
          memcpy(&byte_924430, input, pdwDataLen);
          CryptEncrypt(phKey, 0, 1, 0, &byte_924430, &pdwDataLen, 0x400u);
        }
      }
      CryptDestroyKey(phKey);
      return CryptReleaseContext(phProv, 0);
    }
    else
    {
      return CryptReleaseContext(phProv, 0);
    }
  }
  return result;
}
```
- Đầu tiên hàm gọi `CryptAcquireContextW()` để set context mã hóa, với một trong những parameters là `Microsoft Enhanced RSA and AES Cryptographic Provider`, thì ta có thể chắc chắn rằng bài này sẽ sử dụng thuật toán AES cho việc mã hóa

- Tiếp theo gọi hàm `CryptImportKey()` để lấy key sau khi đã được hash bằng SHA-256, để kiểm chứng các bạn có thể debug xong đối chiếu data sau khi mã hóa tại hàm `init_sha256_key()` và parameter `pbData` (đôi chút về debug thì trong lúc thi vì một lí do nào đó mà máy mình không thể debug được bài này nên sau giải thì mình phải làm lại bài này bằng cách phân tích tĩnh...)

- Sau đó gọi 2 lần hàm `CryptSetKeyParam()` để set mode mã hóa và IV cho việc mã hóa bằng 2 parameters `KP_MODE`, và `KP_IV` với `KP_MODE` là CBC (`v6 = 1`) và `KP_IV` được set là dữ liệu sau khi được hash ở hàm `init_MD5_IV()`

- Cuối cùng là thực hiện encrypt input với context đã được nêu trên bằng hàm `CryptEncrypt()`

- Hàm `check()`
```C
int check()
{
  unsigned int i; // [esp+0h] [ebp-4h]

  for ( i = 0; i < dword_924418; ++i )
  {
    if ( *(&byte_924430 + i) != (unsigned __int8)byte_924068[i] )
    {
      sub_921040("Wrong Flag!!!\n", i);
      exit(0);
    }
  }
  return sub_921040("Correct!!! You are awesome <3\n", i);
}
```
- Hàm này có nhiệm vụ so sánh các byte sau khi được mã hóa với `byte_924068`, nếu đúng thì in ra string `Correct!!! You are awesome <3` ngược lại in ra string `Wrong Flag!!!` (Tại sao khi mình nhập input là gì đi nữa thì chương trình đều in ra correct nhỉ?...)

- Vậy với các dữ kiện trên ta có thể viết script giải mã theo 2 cách, một là viết script C bằng cách dùng các API cần thiết hoặc là dùng thư viện `pycryptodome` của python, mình dùng `pycryptodome` vì viết script nó ngắn hơn :v
```python 
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, MD5
from Crypto.Util.Padding import unpad

def decrypt_aes_cbc(encrypted_data, key):
    sha256 = SHA256.new()
    sha256.update(key)
    aes_key = sha256.digest()
    md5 = MD5.new()
    md5.update(key)
    iv = md5.digest()
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    try:
        decrypted_data = unpad(decrypted_data, AES.block_size)
    except ValueError:
        print("Invalid padding")

    return decrypted_data

if __name__ == '__main__':
    encrypted_data = bytes([
        0x5D, 0xDE, 0x8C, 0xAC, 0xAE, 0xE2, 0x2D, 0x9F, 0xF2, 0x49,
        0x3F, 0x18, 0x35, 0x09, 0x3C, 0x9E, 0xEF, 0xC5, 0xD1, 0x14,
        0xA5, 0x78, 0x02, 0x97, 0x18, 0x5A, 0xE8, 0xA0, 0x8E, 0x4C,
        0xDD, 0x19, 0x74, 0x5C, 0xE4, 0x9B, 0x29, 0x95, 0xB8, 0xD7,
        0xB9, 0x7D, 0xD0, 0x56, 0xBD, 0x94, 0x99, 0x72, 0xFF, 0x58,
        0xB9, 0x1E, 0x57, 0xE9, 0xDA, 0x27, 0xD5, 0xA9, 0x4D, 0xF5,
        0xB6, 0x3B, 0x07, 0x46, 0xC8, 0xDB, 0x37, 0x6E, 0x77, 0x95,
        0x97, 0xFA, 0x7F, 0x5D, 0x4D, 0x54, 0x86, 0xDA, 0xE3, 0x17
    ])
    key = b"https://www.youtube.com/watch?v=fzQ6gRAEoy0"
    decrypted_data = decrypt_aes_cbc(encrypted_data, key)
    print(decrypted_data.decode('utf-8'))

```
**Flag:** `KCSC{md5_4nd_5h4256_4nd_435_w17h_w1n4p1_YXV0aG9ybm9vYm1hbm5uZnJvbWtjc2M=}`
