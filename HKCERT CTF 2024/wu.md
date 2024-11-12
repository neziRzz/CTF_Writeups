# Void
## Misc
- Đề cho 1 web template như sau
![image](https://github.com/user-attachments/assets/b6733924-fc1e-4931-9056-2f3b85762018)
## Detailed Analysis
- Thường đối với nhưng chall rev web, ta có thể thấy được source kiểm tra input sẽ nằm ở bên trong mục script, khi mình check bên trong, có vẻ như code đã bị obfuscate

![image](https://github.com/user-attachments/assets/6ae4dd6c-646d-4c47-8e84-86f58a1fdc66)

- May thay khi mình kéo xuống dưới thì có thể thấy được reference của tác giả về kĩ thuật obfuscate này

![image](https://github.com/user-attachments/assets/1d761bb3-ad12-416d-b86d-551b43162fc0)

- Sau một hồi đọc qua, thì ta tìm thấy tác giả có đề cập đến cơ chế decode và thực thi script

![image](https://github.com/user-attachments/assets/731d5793-801d-4634-9845-eb9f56bd2a57)

- Đoạn code này sẽ có nhiệm vụ decode đống javascript bị tàng hình kia và thực thi chúng với method `eval()`. Vậy để có thể xem được source sau khi đã được decode, ta chỉ cần thay method `eval()` bằng `console.log()`
![image](https://github.com/user-attachments/assets/edb64720-2a3c-46b7-9991-44b8b4153a71)

- Test thử flag trên template

![image](https://github.com/user-attachments/assets/0553d7a8-d3bc-460d-a6ac-63e462e4e2fc)

## Script and Flag
**Flag:** `hkcert24{j4v4scr1p7_1s_n0w_alm0s7_y3t_4n0th3r_wh173sp4c3_pr09r4mm1n9_l4ngu4g3}`

# Yet another crackme
## Misc
- Đề cho 1 file APK

![image](https://github.com/user-attachments/assets/7bdf78a1-4345-4aa6-b512-0f5768377281)
## Detailed Analysis
- Với những chall liên quan đến Java hay APK, ta có thể decompile bằng [JADX](https://github.com/skylot/jadx), nhưng sau khi kiểm tra hàm hoạt động chính của chương trình thì không đem lại kết quả gì

![image](https://github.com/user-attachments/assets/6930eaaf-0bcd-4bb7-b9fa-8e800db13cef)

- Khi kiểm tra các package lân cận ta có thể đoán rằng chương trình được build bằng `.NET MAUI` framework và cụ thể hơn là `Xamarin`

![image](https://github.com/user-attachments/assets/ad3967a6-d2aa-46f3-960a-5380e8e47c03)

- Với dữ kiện là chương trình được build bằng `.NET` framework, ta sẽ phải dump được các DLLs .NET từ trong APK package trong thư mục `assemblies`(APK thực chất chỉ là một file đóng gói nên ta có thể sử dung `WinRar` để extract những file cần thiểt), để làm điều đó có thể sử dụng tool [này](https://github.com/jakev/pyxamstore)

- Sau khi unpack xong, sử dụng `dnSpy` để phân tích DLL `CrackMe.dll`

- hàm `checkFlag`
```C#
// CrackMe.MainPage
// Token: 0x0600000B RID: 11 RVA: 0x00018548 File Offset: 0x00016748
[NullableContext(1)]
private bool checkFlag(string f)
{
	int[] array = new int[]
	{
		9,
		10,
		11,
		12,
		13,
		32,
		33,
		34,
		35,
		36,
		37,
		38,
		39,
		40,
		41,
		42,
		43,
		44,
		45,
		46,
		47,
		48,
		49,
		50,
		51,
		52,
		53,
		54,
		55,
		56,
		57,
		58,
		59,
		60,
		61,
		62,
		63,
		64,
		65,
		66,
		67,
		68,
		69,
		70,
		71,
		72,
		73,
		74,
		75,
		76,
		77,
		78,
		79,
		80,
		81,
		82,
		83,
		84,
		85,
		86,
		87,
		88,
		89,
		90,
		91,
		92,
		93,
		94,
		95,
		96,
		97,
		98,
		99,
		100,
		101,
		102,
		103,
		104,
		105,
		106,
		107,
		108,
		109,
		110,
		111,
		112,
		113,
		114,
		115,
		116,
		117,
		118,
		119,
		120,
		121,
		122,
		123,
		124,
		125,
		126
	};
	int[] array2 = new int[]
	{
		58,
		38,
		66,
		88,
		78,
		39,
		80,
		125,
		64,
		106,
		48,
		49,
		98,
		32,
		42,
		59,
		126,
		93,
		33,
		56,
		112,
		120,
		60,
		117,
		111,
		45,
		87,
		35,
		10,
		68,
		61,
		77,
		11,
		55,
		121,
		74,
		107,
		104,
		65,
		63,
		46,
		110,
		34,
		41,
		102,
		97,
		81,
		12,
		47,
		51,
		103,
		89,
		115,
		75,
		54,
		92,
		90,
		76,
		113,
		122,
		114,
		52,
		72,
		70,
		50,
		94,
		91,
		73,
		84,
		95,
		36,
		82,
		124,
		53,
		108,
		101,
		9,
		13,
		44,
		96,
		67,
		85,
		116,
		123,
		100,
		37,
		43,
		119,
		71,
		105,
		118,
		69,
		99,
		79,
		86,
		109,
		62,
		83,
		40,
		57
	};
	ulong[] array3 = new ulong[]
	{
		16684662107559623091UL,
		13659980421084405632UL,
		11938144112493055466UL,
		17764897102866017993UL,
		11375978084890832581UL,
		14699674141193569951UL
	};
	ulong num = 14627333968358193854UL;
	int num2 = 8;
	Dictionary<int, int> dictionary = new Dictionary<int, int>();
	for (int i = 0; i < array.Length; i++)
	{
		dictionary[array[i]] = array2[i];
	}
	StringBuilder stringBuilder = new StringBuilder();
	foreach (char c in f)
	{
		stringBuilder.Append((char)dictionary[(int)c]);
	}
	int num3 = num2 - f.Length % num2;
	string text = stringBuilder.ToString() + new string('\u0001', num3);
	List<ulong> list = new List<ulong>();
	for (int k = 0; k < text.Length - 1; k += num2)
	{
		ulong num4 = BitConverter.ToUInt64(Encoding.ASCII.GetBytes(text.Substring(k, num2)), 0);
		list.Add(num4);
	}
	List<ulong> list2 = new List<ulong>();
	foreach (ulong num5 in list)
	{
		ulong num6 = num ^ num5;
		list2.Add(num6);
	}
	for (int l = 0; l < array3.Length; l++)
	{
		if (array3[l] != list2[l])
		{
			return false;
		}
	}
	return true;
}

```
- Hàm này có nhiệm vụ kiểm tra input của player, cụ thể như sau
  + Khởi tạo một dictionary với `array[i]` làm index và `array2[i]` là các phần tử trong dictionary
  + Mỗi kí tự của input sẽ được map dựa theo dictionary vào `StringBulider`
  + Sau khi map xong, buffer được tạo bởi `StringBuilder` sẽ được chia ra làm các khối 32 bits, khối cuối cùng sẽ được append `0x01`
  + Mỗi khối trong buffer kể trên sẽ được XOR với `num` và lưu vào `list2`
  + Cuối cùng sẽ kiểm tra từng phần tử trong `list2` với `array3`, tiếp tục loop nếu thỏa mãn và thoát nếu ngược lại

- Với source khá rõ ràng như này, việc viết script sẽ không quá khó khăn, bên dưới là script giải của mình
## Script and Flag
```python
import struct

def reverse_check_flag(output):
    array = [
        9, 10, 11, 12, 13, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
        119, 120, 121, 122, 123, 124, 125, 126
    ]
    
    array2 = [
        58, 38, 66, 88, 78, 39, 80, 125, 64, 106, 48, 49, 98, 32, 42, 59, 126, 93, 33, 56, 112, 120, 60, 117, 111, 45, 87, 35, 10, 68, 61, 77,
        11, 55, 121, 74, 107, 104, 65, 63, 46, 110, 34, 41, 102, 97, 81, 12, 47, 51, 103, 89, 115, 75, 54, 92, 90, 76, 113, 122, 114, 52, 72, 70,
        50, 94, 91, 73, 84, 95, 36, 82, 124, 53, 108, 101, 9, 13, 44, 96, 67, 85, 116, 123, 100, 37, 43, 119, 71, 105, 118, 69, 99, 79, 86, 109,
        62, 83, 40, 57
    ]
    
    array3 = [
        16684662107559623091, 13659980421084405632, 11938144112493055466, 17764897102866017993,
        11375978084890832581, 14699674141193569951
    ]
    
    num = 14627333968358193854
    num2 = 8
    

    inverse_dict = {array2[i]: array[i] for i in range(len(array))}
    
    
    list2 = list(map(int, output.split(',')))  
    

    reversed_chunks = [num ^ chunk for chunk in list2]
    

    decoded_string = ''.join([struct.unpack('8s', struct.pack('Q', chunk))[0].decode('ascii') for chunk in reversed_chunks])
    

    result = decoded_string.rstrip('\x01')
    

    original_flag = ''.join([chr(inverse_dict[ord(c)]) for c in result])
    
    return original_flag

output = "16684662107559623091,13659980421084405632,11938144112493055466,17764897102866017993,11375978084890832581,14699674141193569951"  
original_flag = reverse_check_flag(output)
print(original_flag)

```
**Flag:** `hkcert24{f0r3v3r_r3m3mb3r_x4m4r1n_2024-5-1}`
# Baby Cracker
## Misc
- Đề cho 1 file ELF64

![image](https://github.com/user-attachments/assets/e933bee8-bd35-49d1-a9be-ee5ce0daa41e)
## Detailed Analysis
- IDA's Pseudocode
  + Hàm `main()`
```C
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int i; // [rsp+Ch] [rbp-124h]
  int v5; // [rsp+18h] [rbp-118h]
  int v6; // [rsp+1Ch] [rbp-114h]
  char haystack[256]; // [rsp+20h] [rbp-110h] BYREF
  char **v8; // [rsp+120h] [rbp-10h]
  int v9; // [rsp+128h] [rbp-8h]
  int v10; // [rsp+12Ch] [rbp-4h]

  v10 = 0;
  v9 = a1;
  v8 = a2;
  printf("Enter the flag: ");
  __isoc99_scanf("%s", haystack);
  if ( strstr(haystack, needle) != haystack )
    goto LABEL_15;
  v6 = strlen(haystack);
  if ( strchr(haystack, '}') != &haystack[v6 - 1]
    || haystack[v6 - 2] != 49
    || haystack[v6 - 5] + haystack[v6 - 4] + haystack[v6 - 3] != 300
    || 2 * haystack[v6 - 5] + haystack[v6 - 4] + 2 * haystack[v6 - 3] != 496
    || 2 * haystack[v6 - 5] + 3 * haystack[v6 - 4] + haystack[v6 - 3] != 607 )
  {
    goto LABEL_15;
  }
  v5 = 0;
  for ( i = 0; i < v6 - 14 && (*((char *)off_4058 + i) ^ haystack[i + 9]) == byte_2123[i]; ++i )
    ++v5;
  if ( v5 == 28 && i == v6 - 14 )
  {
    printf("You are now verified!\n");
    return 0;
  }
  else
  {
LABEL_15:
    printf("Bye\n");
    return (unsigned int)-1;
  }
}
```

- Ta có thể thấy rằng luồng hoạt động của chương trình như sau
  + Đầu tiên chương trình nhận input của user
  + Kiểm tra header của flag có phải là `hkcert24{` hay không (`strstr(haystack, needle) != haystack `)
  + Kiểm tra kí tự cuối cùng của flag có kết thúc với `}` cùng với 4 kí tự liên tiếp cho đến kí tự cuối của flag với một số điều kiện
  + Tiếp đến kiểm tra các kí tự còn lại bằng cách xor chúng với `off_4058` và so sánh với `byte_2123`. Nếu tất cả thỏa mãn thì in ra string `You are now verified!` và `Bye` nếu ngược lại

- Ta có thể tìm ra input chính xác bằng z3
## Script and Flag
```python
from z3 import *
flag = [BitVec('x[%d]'%i,8) for i in range(32)]
s = Solver()
xor1 = [  0xCE, 0x21, 0xDB, 0x64, 0xD1, 0x50, 0xE0, 0x1B, 0x0D, 0x3E, 
  0xFB, 0x0A, 0x52, 0x2F, 0x94, 0x9D, 0xAF, 0xB1, 0x58, 0x6B, 
  0x8A, 0xEE, 0xC1, 0xF0, 0xFC, 0x19, 0x0A, 0xE3, 0xE9, 0x1E, 
  0xD0, 0x4A, 0x62, 0xF2, 0x47, 0xA8, 0x20, 0x0B, 0xD3, 0x6C, 
  0x1C, 0x1C, 0x56, 0x5B, 0x9B, 0xB3, 0x4D, 0x3D, 0xCE, 0x83, 
  0x80, 0xC0, 0xE6, 0x7E, 0xE8, 0x09, 0xBD, 0x14, 0xC4, 0x47, 
  0xA1, 0xF6, 0x2F, 0xD1, 0x31, 0x5C, 0x1E, 0x10, 0xD1, 0x2A, 
  0xE0, 0x53, 0x45, 0xFE, 0x85, 0x58, 0xA6, 0xAD, 0x03, 0xCC, 
  0x10, 0x4B, 0xD3, 0x94, 0xFE, 0x62, 0x85, 0x4E, 0x4A, 0x27, 
  0x35, 0xE2, 0x94, 0x0F, 0x49, 0x91, 0x86, 0xD7, 0x80, 0x35, 
  0x4C, 0x67, 0xC3, 0xAA, 0x3C, 0x67, 0xE8, 0x3F, 0xE4, 0x67, 
  0x23, 0xDE, 0x8E, 0x2D, 0x46, 0x25, 0x36, 0xE1, 0xF3, 0x90, 
  0x7D, 0x0F, 0xB9, 0x14, 0x8C, 0xE7, 0xB6, 0xA6, 0x1A, 0x90, 
  0x80, 0x79, 0x85, 0x35, 0xFD, 0x51, 0x8C, 0x10, 0xE9, 0x3F, 
  0x32, 0xCC, 0x4B, 0xB5, 0x42, 0xDE, 0xF5, 0x57, 0x13, 0xC8, 
  0x09, 0x9B, 0x4D, 0x19, 0x84, 0x91, 0x5F, 0x9D, 0x77, 0x30, 
  0x31, 0xC7, 0x28, 0x8D, 0x1D, 0xF4, 0x71, 0xE4, 0xD1, 0xA3, 
  0x0C, 0x07, 0x59, 0xAA, 0x0D, 0xAD, 0x16, 0x35, 0x40, 0xB9, 
  0x28, 0x6A, 0xB5, 0x4C, 0x24, 0x5A, 0x8D, 0xA6, 0xA6, 0xC4, 
  0x56, 0xDD, 0xC0, 0x9B, 0xBF, 0xCC, 0xDE, 0x0C, 0x5B, 0xC1, 
  0x75, 0xDD, 0x77, 0xBB, 0xF6, 0x2B, 0x43, 0x1D, 0x13, 0x03, 
  0xAD, 0x73, 0xA3, 0xAC, 0x4D, 0xEA, 0xA5, 0x2F, 0xC2, 0x3E, 
  0x4A, 0x1A, 0xF5, 0x65, 0x72, 0xE5, 0x4A, 0x10, 0x10, 0x8C, 
  0xFB, 0x10, 0x0A, 0x4D, 0x79, 0x71, 0xF6, 0xC7, 0x80, 0x54, 
  0x64, 0xB0, 0x02, 0xAA, 0xD8, 0x7C, 0x39, 0x53, 0xEC, 0xAD, 
  0xB4, 0x4E, 0x2F, 0xEB, 0xE0, 0x47, 0x00]
dest = [  0xBD, 0x10, 0xB6, 0x50, 0xBD, 0x35, 0xBF, 0x78, 0x7F, 0x0A, 
  0x98, 0x61, 0x1F, 0x1C, 0xCB, 0xA9, 0xF0, 0xD9, 0x6C, 0x05, 
  0xEE, 0xAC, 0xB8, 0x98, 0x9D, 0x77, 0x3C, 0xBC, 0x81, 0x2E, 
  0xA0, 0x79, 0x3D, 0x8B, 0x77, 0xDD, 0x7F, 0x6F, 0xE3, 0x02, 
  0x2B, 0x43, 0x38, 0x68, 0xA8, 0xD7, 0x12, 0x0A, 0xA1, 0xDC, 
  0xF5, 0xF3, 0x83, 0x21, 0xDC, 0x67, 0xDA, 0x66, 0x9B, 0x77, 
  0xD3, 0xA9, 0x55, 0xE2, 0x6E, 0x3A, 0x2E, 0x62, 0x8E, 0x5E, 
  0x88, 0x62, 0x36, 0xA1, 0xE7, 0x2D, 0x91, 0xF2, 0x32, 0x93, 
  0x67, 0x7B, 0xBD, 0xF0, 0xCD, 0x10, 0xDA, 0x7F, 0x2C, 0x78, 
  0x56, 0x8A, 0xA0, 0x38, 0x2E, 0xE1, 0xB1, 0x88, 0xB0, 0x47, 
  0x13, 0x04, 0xF7, 0xC4, 0x63, 0x14, 0xDB, 0x0C, 0xBB, 0x13, 
  0x4B, 0xEF, 0xBB, 0x72, 0x24, 0x14, 0x59, 0x83, 0x90, 0xA4, 
  0x09, 0x69, 0xCC, 0x7A, 0xE2, 0x9E, 0x8C, 0x8F, 0x69, 0xA1, 
  0xED, 0x4D, 0xE9, 0x50, 0xA2, 0x32, 0xFE, 0x24, 0x8A, 0x54, 
  0x7F, 0xFF, 0x14, 0x81, 0x1D, 0xB6, 0xC1, 0x39, 0x77, 0x8A, 
  0x70, 0xF3, 0x2C, 0x77, 0xB2, 0xCE, 0x37, 0xAD, 0x07, 0x03, 
  0x6E, 0xBE, 0x18, 0xF8, 0x42, 0x90, 0x41, 0x8A, 0xE6, 0xFC, 
  0x62, 0x34, 0x6A, 0xCE, 0x52, 0x9A, 0x79, 0x6A, 0x35, 0x8A, 
  0x4D, 0x35, 0x81, 0x22, 0x43, 0x28, 0xD2, 0x96, 0xD4, 0x9B, 
  0x2C, 0xEE, 0x9F, 0xFD, 0x8F, 0xBE, 0x81, 0x78, 0x33, 0xF0, 
  0x06, 0x82, 0x15, 0xCE, 0xC1, 0x74, 0x72, 0x42, 0x64, 0x33, 
  0xC3, 0x17, 0x90, 0xDE, 0x12, 0xDB, 0xC3, 0x70, 0xA1, 0x56, 
  0x7E, 0x2D, 0x92, 0x15, 0x45, 0xBA, 0x7A, 0x62, 0x4F, 0xEF, 
  0xCF, 0x7E, 0x55, 0x3E, 0x4A, 0x42, 0xA9, 0xB3, 0xE8, 0x65, 
  0x51, 0xEF, 0x60, 0x9B, 0xB7, 0x1E, 0x5A, 0x67, 0x98, 0xCB, 
  0xC1, 0x20, 0x41, 0x92, 0xDA, 0x6E, 0x00]
for i in range(len(flag)):
    s.add(flag[i] >= 0x20)
    s.add(flag[i] <= 0x7F)
s.add(flag[len(flag)-1] == 49)
s.add(flag[len(flag)-4] + flag[len(flag)-3] + flag[len(flag)-2] == 300 ) 
s.add(2*flag[len(flag)-4] + flag[len(flag)-3] + 2*flag[len(flag)-2] == 496 ) 
s.add(2*flag[len(flag)-4] + 3*flag[len(flag)-3] + flag[len(flag)-2] == 607 )
for i in range(28):
    s.add(flag[i] ^ xor1[i] == dest[i]) 
if(s.check()==sat):
    model = s.model()
    flag_string = ''.join([chr(model[flag[i]].as_long()) for i in range(32)])
    print("hkcert24{"+flag_string+"}")
```
**Flag:** `hkcert24{s1m4le_cr4ckM3_4_h4ndByhan6_cha1}`
# Cyp.ress
## Misc
- Đề cho một file .PYC

![image](https://github.com/user-attachments/assets/9ad4e05f-0bf8-4748-91a0-772ddc7ab93b)
## Detailed Analysis
- Thường đối với những challange dạng này ta sẽ sử dụng những tool như `uncompyle6` hoặc `Decompyle++` để decompile file `.pyc` về dạng python source. Nhưng khi thử sử dụng 2 tool trên lên file `sser.cpython-312.pyc` thì đều bị lỗi

![image](https://github.com/user-attachments/assets/93ce9a7b-0c11-4703-a6ea-5c181dd04d0c)
![image](https://github.com/user-attachments/assets/2881bb16-4e4e-4ead-898d-0651233a2ad4)

- Vậy từ đây ta sẽ phải đổi hướng tiếp cận đó chính là sử dụng thư viện `dis` của python để lấy ra bytecode và từ đó build lại chương trình. Bên dưới là script để biến đổi
```python
import dis
import marshal

pyc_file = 'sser.cpython-312.pyc'

with open(pyc_file, 'rb') as f:
    f.read(16)  # Skip the header bytes
    code_obj = marshal.load(f)

dis.dis(code_obj)
```
- Chạy đoạn code trên ta có output như sau
```python
 1           0 RESUME                   0
              2 LOAD_CONST               0 (0)
              4 LOAD_CONST               1 (None)
              6 IMPORT_NAME              0 (os)
              8 STORE_NAME               0 (os)
             10 LOAD_CONST               0 (0)
             12 LOAD_CONST               1 (None)
             14 IMPORT_NAME              1 (requests)
             16 STORE_NAME               1 (requests)
             18 LOAD_CONST               0 (0)
             20 LOAD_CONST               2 (('AES',))
             22 IMPORT_NAME              2 (Crypto.Cipher)
             24 IMPORT_FROM              3 (AES)
             26 STORE_NAME               3 (AES)
             28 POP_TOP
             30 LOAD_CONST               0 (0)
             32 LOAD_CONST               1 (None)
             34 IMPORT_NAME              4 (hashlib)
             36 STORE_NAME               4 (hashlib)
             38 LOAD_CONST               4 ('What is the flag?> ')
             40 CALL_INTRINSIC_1         1 (INTRINSIC_PRINT)
             42 POP_TOP
             44 LOAD_CONST               3 (<code object get_nonce at 0x00000202C11F4420, file "sser.py", line 6>)
             46 MAKE_FUNCTION            0
             48 STORE_NAME               5 (get_nonce)
             50 PUSH_NULL
             52 LOAD_NAME                6 (input)
             54 BUILD_STRING             0
             56 CALL                     1
             64 LOAD_ATTR               15 (NULL|self + encode)
             84 CALL                     0
             92 STORE_NAME               8 (flag)
             94 PUSH_NULL
             96 LOAD_NAME                5 (get_nonce)
             98 CALL                     0
            106 STORE_NAME               9 (nonce)
            108 PUSH_NULL
            110 LOAD_NAME                1 (requests)
            112 LOAD_ATTR               20 (post)
            132 LOAD_CONST               5 ('https://c12-cypress.hkcert24.pwnable.hk/')
            134 LOAD_CONST               6 ('nonce')
            136 LOAD_NAME                9 (nonce)
            138 LOAD_ATTR               23 (NULL|self + hex)
            158 CALL                     0
            166 BUILD_MAP                1
            168 KW_NAMES                 7 (('json',))
            170 CALL                     2
            178 STORE_NAME              12 (r)
            180 LOAD_NAME               13 (bytes)
            182 LOAD_ATTR               29 (NULL|self + fromhex)
            202 LOAD_NAME               12 (r)
            204 LOAD_ATTR               30 (text)
            224 CALL                     1
            232 STORE_NAME              16 (c0)
            234 PUSH_NULL
            236 LOAD_NAME                4 (hashlib)
            238 LOAD_ATTR               34 (sha256)
            258 LOAD_CONST               8 (b'key/')
            260 LOAD_NAME                9 (nonce)
            262 BINARY_OP                0 (+)
            266 CALL                     1
            274 LOAD_ATTR               37 (NULL|self + digest)
            294 CALL                     0
            302 LOAD_CONST               1 (None)
            304 LOAD_CONST               9 (16)
            306 BINARY_SLICE
            308 STORE_NAME              19 (key)
            310 PUSH_NULL
            312 LOAD_NAME                4 (hashlib)
            314 LOAD_ATTR               34 (sha256)
            334 LOAD_CONST              10 (b'iv/')
            336 LOAD_NAME                9 (nonce)
            338 BINARY_OP                0 (+)
            342 CALL                     1
            350 LOAD_ATTR               37 (NULL|self + digest)
            370 CALL                     0
            378 LOAD_CONST               1 (None)
            380 LOAD_CONST               9 (16)
            382 BINARY_SLICE
            384 STORE_NAME              20 (iv)
            386 PUSH_NULL
            388 LOAD_NAME                3 (AES)
            390 LOAD_ATTR               42 (new)
            410 LOAD_NAME               19 (key)
            412 LOAD_NAME                3 (AES)
            414 LOAD_ATTR               44 (MODE_CFB)
            434 LOAD_NAME               20 (iv)
            436 CALL                     3
            444 STORE_NAME              23 (cipher)
            446 LOAD_NAME               23 (cipher)
            448 LOAD_ATTR               49 (NULL|self + encrypt)
            468 LOAD_NAME                8 (flag)
            470 CALL                     1
            478 STORE_NAME              25 (c1)
            480 PUSH_NULL
            482 LOAD_NAME               26 (print)
            484 LOAD_CONST              11 ('🙆🙅')
            486 LOAD_NAME               16 (c0)
            488 LOAD_NAME               25 (c1)
            490 COMPARE_OP              55 (!=)
            494 BINARY_SUBSCR
            498 CALL                     1
            506 POP_TOP
            508 RETURN_CONST             1 (None)

Disassembly of <code object get_nonce at 0x00000202C11F4420, file "sser.py", line 6>:
  6           0 RESUME                   0

  7           2 NOP

  8     >>    4 LOAD_GLOBAL              1 (NULL + os)
             14 LOAD_ATTR                2 (urandom)
             34 LOAD_CONST               1 (16)
             36 CALL                     1
             44 STORE_FAST               0 (nonce)

  9          46 LOAD_GLOBAL              5 (NULL + hashlib)
             56 LOAD_ATTR                6 (sha256)
             76 LOAD_CONST               2 (b'pow/')
             78 LOAD_FAST                0 (nonce)
             80 BINARY_OP                0 (+)
             84 CALL                     1
             92 LOAD_ATTR                9 (NULL|self + digest)
            112 CALL                     0
            120 LOAD_CONST               0 (None)
            122 LOAD_CONST               3 (3)
            124 BINARY_SLICE
            126 LOAD_CONST               4 (b'\x00\x00\x00')
            128 COMPARE_OP              40 (==)
            132 POP_JUMP_IF_FALSE        2 (to 138)
            134 LOAD_FAST                0 (nonce)
            136 RETURN_VALUE

  7     >>  138 JUMP_BACKWARD           68 (to 4)
```

- Tuy hơi mất não nhưng ta có thể đưa đoạn code trên lên ChatGPT và nhờ nó convert về lại python source 💀

```python
import os
import requests
from Crypto.Cipher import AES
import hashlib

def get_nonce():
    while True:
        nonce = os.urandom(16)  # Generate a random 16-byte nonce
        # Hash with a prefix and check if the first three bytes are zero
        if hashlib.sha256(b'pow/' + nonce).digest()[:3] == b'\x00\x00\x00':
            return nonce

# Ask for user input
print("What is the flag?> ")
flag = input().encode()

# Get the nonce value using the get_nonce function
nonce = get_nonce()

# Make a request with the nonce as part of a JSON payload
r = requests.post("https://c12-cypress.hkcert24.pwnable.hk/", json={"nonce": nonce.hex()})

# Convert the response text from hex to bytes
c0 = bytes.fromhex(r.text)

# Generate keys for AES encryption using SHA-256 digests of nonce and different prefixes
key = hashlib.sha256(b'key/' + nonce).digest()[:16]
iv = hashlib.sha256(b'iv/' + nonce).digest()[:16]

# Create AES cipher in CFB mode with the generated key and IV
cipher = AES.new(key, AES.MODE_CFB, iv)

# Encrypt the flag with the cipher
c1 = cipher.encrypt(flag)

# Check if c0 (received ciphertext) is different from c1 (locally encrypted flag)
print("🙆🙅"[c0 != c1])  # Print different emoji based on comparison

```
- Từ đây ta có thể suy ra flow của chương trình như sau
  + Đầu tiên chương trình nhận input của user
  + Tạo request đến `https://c12-cypress.hkcert24.pwnable.hk/` để lấy ra flag data đã bị mã hóa
  + Thực hiện encrypt input của user bằng thuật toán `AES` với mode `CFB`, key là `key/` được hash bằng thuật toán `SHA-256`, IV là `iv/` và so sánh với cyphertext nhận được từ `https://c12-cypress.hkcert24.pwnable.hk/`

- Biết cách thức mã hóa, ta có thể viết script giải mã hoặc sửa luôn trong script trên từ `cipher.encrypt(flag)` thành `cipher.decrypt(c0)` và in kết quả ra màn hình
## Script and Flag
```python
import os
import requests
from Crypto.Cipher import AES
import hashlib

def get_nonce():
    while True:
        nonce = os.urandom(16) 
        if hashlib.sha256(b'pow/' + nonce).digest()[:3] == b'\x00\x00\x00':
            return nonce

print("What is the flag?> ")
flag = input().encode()

nonce = get_nonce()

r = requests.post("https://c12-cypress.hkcert24.pwnable.hk/", json={"nonce": nonce.hex()})

c0 = bytes.fromhex(r.text)

key = hashlib.sha256(b'key/' + nonce).digest()[:16]
iv = hashlib.sha256(b'iv/' + nonce).digest()[:16]

cipher = AES.new(key, AES.MODE_CFB, iv)

c1 = cipher.decrypt(c0)


print("🙆🙅"[c0 != c1])  
print(c1)
```
**Flag:** `hkcert24{y0u_c4n_h00k_func710ns_t0_35c4p3_fr0m_r3v3r5e_3n9e3r1n9}`
# ISA 101
