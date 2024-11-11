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

