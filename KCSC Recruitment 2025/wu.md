# Hidden 
## Misc 
- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/2a7ff778-c8c3-44e1-b903-676ccf81ac96)

## Detailed Analysis

- Hàm `main`

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _main();
  printf_0("KCSC{can_you_see_me??}\n");
  return 0;
}
```
- Vì đây là 1 chal warmup nên thoặt qua thấy flag ngay trong `main` như này thì ngỡ rằng đây là flag đúng nhưng thực ra không phải, hàm chuẩn sẽ là hàm `printFlag`

- Hàm `printFlag`
```C
int printFlag()
{
  int result; // eax
  unsigned int v1; // eax
  __int64 v2[3]; // [rsp+20h] [rbp-20h]
  int i; // [rsp+3Ch] [rbp-4h]

  v2[0] = 0xFDE7F1F3CBDBCBC3ui64;
  v2[1] = 0xFBD7FCAFE6E9EBD7ui64;
  result = 0xE5D7EDED;
  v2[2] = 0xF5FEB2EDE5D7EDEDui64;
  for ( i = 0; i <= 0x17; ++i )
  {
    v1 = *((char *)v2 + i);
    LOBYTE(v1) = *((_BYTE *)v2 + i) ^ 0x88;
    result = printf_0("%c", v1);
  }
  return result;
}
```

- Hàm này sẽ có nhiệm vụ xor từng byte của đống data kia với 0x88 và in kết quả ra màn hình, việc viết script sẽ không quá khó khăn
## Script and Flag
```python
def print_flag():
    # Initialize the 64-bit values (little-endian encoding)
    v2 = [
        0xFDE7F1F3CBDBCBC3,
        0xFBD7FCAFE6E9EBD7,
        0xF5FEB2EDE5D7EDED
    ]
    
    # Convert the 64-bit values into a byte array with little-endian order
    byte_array = bytearray()
    for value in v2:
        byte_array.extend(value.to_bytes(8, 'little'))
    
    # XOR each byte with 0x88 and decode to characters
    flag = ''.join(chr(byte ^ 0x88) for byte in byte_array[:24])
    return flag

# Print the flag
flag = print_flag()
print("Flag:", flag)

```
**Flag:** `KCSC{you_can't_see_me:v}`

# easyre
## Misc
- Đề cho 1 file PE64

  ![image](https://github.com/user-attachments/assets/3f407fb9-d11d-45cd-b401-b85cdafb462f)

## Detailed Analysis
- Hàm `main`
```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  size_t v4; // rax
  __int64 v5; // rax
  unsigned int v6; // edx
  unsigned int v7; // r8d
  unsigned __int64 v8; // rax
  __m128 v9; // xmm0
  __m128 v10; // xmm1
  __int64 v11; // rcx
  __int64 v12; // rax
  char *v13; // rcx
  char Buffer[16]; // [rsp+20h] [rbp-68h] BYREF
  __int128 v16; // [rsp+30h] [rbp-58h] BYREF
  int v17; // [rsp+40h] [rbp-48h]
  __int128 v18[2]; // [rsp+48h] [rbp-40h] BYREF
  __int64 v19; // [rsp+68h] [rbp-20h]
  int v20; // [rsp+70h] [rbp-18h]
  char v21; // [rsp+74h] [rbp-14h]

  LOBYTE(v17) = 0;
  v19 = 0i64;
  *(_OWORD *)Buffer = 0i64;
  v20 = 0;
  v16 = 0i64;
  v21 = 0;
  memset(v18, 0, sizeof(v18));
  sub_140001010("Enter flag: ");
  v3 = _acrt_iob_func(0);
  fgets(Buffer, 33, v3);
  v4 = strcspn(Buffer, "\n");
  if ( v4 >= 0x21 )
    sub_140001558();
  Buffer[v4] = 0;
  v5 = -1i64;
  do
    ++v5;
  while ( Buffer[v5] );
  if ( v5 == 32 )
  {
    base64((__int64)Buffer, v18);
    v6 = 0;
    v7 = 0;
    v8 = 0i64;
    do
    {
      v9 = (__m128)_mm_loadu_si128((const __m128i *)&byte_140005078[v8]);
      v7 += 32;
      v10 = (__m128)_mm_loadu_si128((const __m128i *)&v18[v8 / 0x10]);
      v8 += 32i64;
      *(__m128 *)&dword_140005058[v8 / 4] = _mm_xor_ps(v10, v9);
      *(__m128 *)&qword_140005068[v8 / 8] = _mm_xor_ps(
                                              (__m128)_mm_loadu_si128((const __m128i *)((char *)&v16 + v8 + 8)),
                                              (__m128)_mm_loadu_si128((const __m128i *)&qword_140005068[v8 / 8]));
    }
    while ( v7 < 0x20 );
    v11 = (int)v7;
    if ( (unsigned __int64)(int)v7 < 0x2C )
    {
      do
      {
        ++v7;
        byte_140005078[v11] ^= *((_BYTE *)v18 + v11);
        ++v11;
      }
      while ( v7 < 0x2C );
    }
    v12 = 0i64;
    while ( byte_1400032F0[v12] == byte_140005078[v12] )
    {
      ++v6;
      ++v12;
      if ( v6 >= 0x2C )
      {
        v13 = "Correct!\n";
        goto LABEL_13;
      }
    }
  }
  v13 = "Incorrect!\n";
LABEL_13:
  sub_140001010(v13);
  return 0;
}
```
- Đầu tiên hàm `main` sẽ kiểm tra độ dài của input có phải là 32 hay không, nếu thỏa mãn thì sẽ tiến hành encode input bằng base64, sau đó sẽ xor input với `byte_7FF6A9F35078`, đoạn xor này sẽ được chia ra làm 2 phần, phần đầu là xor 16 bytes và phần còn lại sẽ xor từng byte một. Cuối cùng input sẽ được kiểm tra với `byte_7FF6A9F332F0` nếu thỏa mãn sẽ in ra string `Correct!` hoặc `Incorrect!` tương ứng

- Với các dữ kiện như trên, ta có thể dễ dàng viết script

## Script and Flag
```python
key =[ 0x92, 0xA1, 0x27, 0xE0, 0x37, 0xCA, 0x70, 0x7E, 0xE6, 0xBE, 
  0x33, 0x1D, 0x5D, 0xFE, 0x29, 0x93, 0xB6, 0x66, 0xF9, 0x02, 
  0x6A, 0x74, 0x0D, 0xDF, 0xD6, 0xEC, 0x5A, 0x71, 0xC8, 0xA3, 
  0xFD, 0x84, 0xC5, 0x13, 0x1E, 0x87, 0xC7, 0x52, 0x50, 0x55, 
  0x01, 0x16, 0xFD, 0xCF]
cypher = [0xC1, 0x91, 0x69, 0xB4, 0x66, 0xF9, 0x04, 0x12, 0xB2, 0xD3, 
  0x7D, 0x6B, 0x0F, 0xB9, 0x7F, 0xF5, 0xD2, 0x1C, 0xBF, 0x32, 
  0x0B, 0x32, 0x34, 0x9C, 0x98, 0xA4, 0x14, 0x37, 0x86, 0xC9, 
  0xAF, 0xE2, 0x9C, 0x46, 0x2B, 0xEC, 0x9F, 0x63, 0x38, 0x23, 
  0x54, 0x78, 0xCD, 0xF2]
for i in range (len(cypher)):
    print(chr(cypher[i]^key[i]),end='') #Remember to decode it back from b64
```
**Flag:** `KCSC{eNcoDe_w1th_B4sE64_aNd_XoR}`

# Spy Room
## Misc
- Đề cho 1 file .NET 32-bit

  ![image](https://github.com/user-attachments/assets/ddace5f7-63fe-4818-991f-bae77ca7d459)

## Detailed Analysis

- Với những file được build bằng .NET, ta sẽ phải phân tích bằng `dnSpy`, các bạn có thể tải tại [đây](https://github.com/dnSpy/dnSpy)

- Hàm `Main`
```C#
// TestEzDotNET.Program
// Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
private static void Main()
{
	Console.Write("Enter Something: ");
	char[] array = Console.ReadLine().ToCharArray();
	int num = array.Length;
	char[] array2 = array.Take(num / 4).ToArray<char>();
	char[] array3 = array.Skip(num / 4).Take(num / 4).ToArray<char>();
	char[] array4 = array.Skip(2 * num / 4).Take(num / 4).ToArray<char>();
	char[] array5 = array.Skip(3 * num / 4).ToArray<char>();
	array2 = Program.Xor(array2, array3);
	array3 = Program.Xor(array3, array4);
	array4 = Program.Xor(array4, array5);
	array5 = Program.Xor(array5, array2);
	char[] array6 = array2.Concat(array3).Concat(array4).Concat(array5).ToArray<char>();
	string text = "https://www.youtube.com/watch?v=L8XbI9aJOXk";
	array6 = Program.Xor(array6, text.ToCharArray());
	byte[] source = new byte[]
	{
		85,
		122,
		105,
		71,
		17,
		94,
		71,
		24,
		114,
		78,
		107,
		11,
		108,
		106,
		107,
		113,
		121,
		51,
		91,
		117,
		86,
		110,
		100,
		18,
		124,
		104,
		71,
		66,
		123,
		3,
		111,
		99,
		74,
		107,
		69,
		77,
		111,
		2,
		120,
		125,
		83,
		99,
		62,
		99,
		109,
		76,
		119,
		111,
		59,
		32,
		1,
		93,
		69,
		117,
		84,
		106,
		73,
		85,
		112,
		66,
		114,
		92,
		61,
		80,
		80,
		104,
		111,
		72,
		98,
		28,
		88,
		94,
		27,
		120,
		15,
		76,
		15,
		67,
		86,
		117,
		81,
		108,
		18,
		37,
		34,
		101,
		104,
		109,
		23,
		30,
		62,
		78,
		88,
		10,
		2,
		63,
		43,
		72,
		102,
		38,
		76,
		23,
		34,
		62,
		21,
		97,
		1,
		97
	};
	if (!array6.SequenceEqual((from e in source
	select (char)e).ToArray<char>()))
	{
		Console.WriteLine("Wrong!!");
		return;
	}
	Console.WriteLine("Decode It!!");
}
```

- Chương trình thực hiện chia input của chúng ta ra làm 4 phần, tiếp đến sẽ sử dụng một hàm `Xor` custom để xor từng block này với nhau theo dạng `block1^block2`, `block2^block3`,... Cuối cùng thì sẽ gộp lại các block trên lại với nhau và xor với string `https://www.youtube.com/watch?v=L8XbI9aJOXk` và kiểm tra với `source`

- Hàm `Xor`
```C#
private static char[] Xor(char[] a, char[] b)
{
	int num = Math.Max(a.Length, b.Length);
	char[] array = new char[num];
	for (int i = 0; i < num; i++)
	{
		if (a.Length >= b.Length)
		{
			array[i] = (a[i] ^ b[i % b.Length]);
		}
		else
		{
			array[i] = (a[i % a.Length] ^ b[i]);
		}
	}
	return array;
}
```
- Hàm này chỉ là kiểm tra xem độ dài của 2 array để xor. Nếu độ dài arr1 lớn hơn arr2 thì khi arr1 xor hết các phần tử của arr2 thì lúc này phần tử tiếp đến của arr1 sẽ được xor lại từ phần tử đầu tiên của arr2
- Vậy để giải ta chỉ cần đảo ngược lại quá trình trên, output sau khi tìm được sẽ là 1 string b64 được encode 3 lần nên ta cần phải chú ý
## Script and Flag
```python
import base64 as b64


def xor(a, b):
    #Performs XOR operation on two character arrays.
    max_len = max(len(a), len(b))
    result = []
    for i in range(max_len):
        if len(a) >= len(b):
            result.append(chr(ord(a[i]) ^ ord(b[i % len(b)])))
        else:
            result.append(chr(ord(a[i % len(a)]) ^ ord(b[i])))
    return ''.join(result)

def solve():
    # Source byte array
    source = [
        85, 122, 105, 71, 17, 94, 71, 24, 114, 78, 107, 11, 108, 106, 107, 113,
        121, 51, 91, 117, 86, 110, 100, 18, 124, 104, 71, 66, 123, 3, 111, 99,
        74, 107, 69, 77, 111, 2, 120, 125, 83, 99, 62, 99, 109, 76, 119, 111,
        59, 32, 1, 93, 69, 117, 84, 106, 73, 85, 112, 66, 114, 92, 61, 80,
        80, 104, 111, 72, 98, 28, 88, 94, 27, 120, 15, 76, 15, 67, 86, 117,
        81, 108, 18, 37, 34, 101, 104, 109, 23, 30, 62, 78, 88, 10, 2, 63,
        43, 72, 102, 38, 76, 23, 34, 62, 21, 97, 1, 97
    ]
    source_chars = ''.join(chr(e) for e in source)

    # The URL used in the XOR process
    text = "https://www.youtube.com/watch?v=L8XbI9aJOXk"

    # Reverse XOR with the URL text
    temp_array = xor(source_chars, text)

    # Calculate the length of the original input
    n = len(temp_array)

    # Split the reversed XOR result back into parts
    num = n // 4
    array2 = temp_array[:num]
    array3 = temp_array[num:2*num]
    array4 = temp_array[2*num:3*num]
    array5 = temp_array[3*num:]

    # Reverse the sequence of XOR operations
    array5 = xor(array5, array2)
    array4 = xor(array4, array5)
    array3 = xor(array3, array4)
    array2 = xor(array2, array3)

    # Combine the parts to reconstruct the original input
    original_input = array2 + array3 + array4 + array5

    return original_input

if __name__ == "__main__":
    result = solve()
    for _ in range(3):
        result = b64.b64decode(result)
    print(result)
```
**Flag:** `KCSC{Easy_Encryption_With_DotNET_Program:3}`
# EzRev
## Mics
- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/c5d6c30a-1b51-47b3-8f27-6c0d5412f2cc)

## Detailed Analysis
- Hàm `main`

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+20h] [rbp-28h]
  __int64 v5; // [rsp+28h] [rbp-20h]

  sub_140001200("Enter Something: ", argv, envp);
  sub_1400012D0("%s", byte_1400047A8);
  if ( (unsigned int)sub_140001100(byte_1400047A8) == 0x89D5B562 )
  {
    v5 = -1i64;
    do
      ++v5;
    while ( byte_1400047A8[v5] );
    if ( v5 == 40 )
    {
      sub_140001000((__int64)byte_1400047A8);
      dword_1400047A0 = 1;
      for ( i = 0; i < 40; ++i )
      {
        if ( dword_140004080[i] != dword_140004700[i] )
          dword_1400047A0 = 0;
      }
    }
  }
  if ( dword_1400047A0 )
    sub_140001200("Excellent!! Here is your flag: KCSC{%s}", byte_1400047A8);
  else
    sub_140001200("You're chicken!!!");
  return 0;
}
```
- Đầu tiên chương trình sẽ kiểm tra hash `FNV-1a` bằng hàm `sub_140001100` của input, nếu hash thỏa mãn thì input sẽ tiếp tục được biến đổi tại `sub_140001000`, cuối cùng kiểm tra input sau khi được biến đổi với `dword_140004080`, thỏa mãn thì in ra flag và ngược lại in ra string `You're chicken!!!`

- Hàm `sub_140001000`

```C
__int64 __fastcall sub_140001000(__int64 a1)
{
  __int64 result; // rax
  unsigned int v2; // [rsp+0h] [rbp-38h]
  unsigned int i; // [rsp+4h] [rbp-34h]
  int j; // [rsp+8h] [rbp-30h]
  int v5; // [rsp+Ch] [rbp-2Ch]
  int v6; // [rsp+10h] [rbp-28h]
  __int64 v7; // [rsp+18h] [rbp-20h]

  v7 = -1i64;
  do
    ++v7;
  while ( *(_BYTE *)(a1 + v7) );
  for ( i = 0; ; ++i )
  {
    result = (unsigned int)v7;
    if ( i >= (unsigned int)v7 )
      break;
    v5 = 4;
    v6 = 6;
    v2 = *(unsigned __int8 *)(a1 + (int)i);
    for ( j = 0; j < 5; ++j )
    {
      v2 ^= __ROL4__(v2, v5) ^ __ROR4__(v2, v6);
      v5 *= 2;
      v6 *= 2;
    }
    dword_140004700[i] = v2;
  }
  return result;
}
```
- Hàm này biến đổi input của chúng ta bằng các phép rol4, ror4 và Xor. Có điều phải chú ý rằng các phép rol và ror thực hiện trên trường số 32 bit. Bởi hàm này chỉ xử lí từng kí tự 1 của input nên để giải ta có thể build lại hàm này và viết script bằng cách bruteforce

## Script and Flag
```python
def rol(val, bits, bit_size):
    return (val << bits % bit_size) & (2 ** bit_size - 1) | \
           ((val & (2 ** bit_size - 1)) >> (bit_size - (bits % bit_size)))
def ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))
dest = [0xF30C0330, 0x340DDE9D, 0x750D9AC9, 0x391FBC2A, 0x9F16AF5B, 0xE6180661, 0x6C1AAC6B, 0x340DDE9D, 0xB60D5635, 0x9F16AF5B,
0xA3195364, 0x681BBD3A, 0xF30C0330, 0xA3195364, 0xAB1B71C6, 0xF30C0330, 0xF21D5274, 0x9F16AF5B, 0xE6180661, 0x300CCFCC,
0xF21D5274, 0x9F16AF5B, 0xAB1B71C6, 0xA3195364, 0x750D9AC9, 0xA3195364, 0x9F16AF5B, 0xF21D5274, 0xF30C0330, 0xA3195364,
0xF21D5274, 0x351C8FD9, 0x710C8B98, 0xF70D1261, 0x2D1AE83F, 0xF30C0330, 0xEE1A24C3, 0xF70D1261, 0x6108CEDC, 0x6108CEDC,]
count = 0
while(count<len(dest)-1):
    for j in range(0x20,0x7f):
        v5 = 4
        v6 = 6
        v2 = j
        for i in range(5):

            v2 ^= rol(v2, v5,32) ^ ror(v2, v6,32)
            v5 *= 2
            v6 *= 2
        if(v2 == dest[count]):
            print(chr(j),end='')
            count +=1
```
**Flag:** `KCSC{345y_fl46_ch3ck3r_f0r_kc5c_r3cru17m3n7!}`
# Waiterfall
## Mics
- Đề cho 1 file PE64 🐧

![image](https://github.com/user-attachments/assets/83547248-353a-4e82-bcd0-6c807390472c)

## Detailed Analysis
