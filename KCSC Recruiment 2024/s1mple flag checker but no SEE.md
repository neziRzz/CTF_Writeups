- Đề cho 1 file source bằng Java (Mình đã rename các hàm `check()` để tiện hơn cho việc phân tích)

- Tuy bài này không quá khó nhưng mình lại mất quá nhiều thời gian ngồi sửa script xong cuối cùng không giải được trong lúc thi :(

```Java
import java.util.*;

public class Flag_Checker {
	static int[] pos = { 10, 15, 19, 28, 30, 44, 49 };
	static int[] f1nal = { 18, 20, 22, 23, 25, 26, 27, 31, 33, 34, 36, 37, 39, 40 };

	public static boolean check1(boolean ret, String s) {
		if ((!s.substring(0, 5).equals("KCSC{")) || !(s.charAt(s.length() - 1) == '}'))
			ret = false;
		return ret;
	}

	public static boolean check3(boolean ret, String s, int[] arr) {
		for (int i = 0; i < arr.length; ++i) {
			if (s.charAt(arr[i]) != 95)
				return false;
		}
		return ret;
	}

	public static boolean check2(boolean ret, String s, boolean[] arr) {
		int[] num = new int[10];

		for (int i = 0; i < s.length(); ++i) {
			if (Character.isDigit(s.charAt(i)) != arr[i])
				ret = false;
		}
		for (int i = 0; i < pos.length; ++i) {
			num[i] = s.charAt(pos[i]) - 0x30;
		}
		if ((num[1] != num[6])
				|| (num[0] != num[1] - num[6])
				|| (num[3] + num[4] != num[1])
				|| (num[6] * num[5] != 20)
				|| (num[0] != num[2])
				|| (Math.pow(num[3], num[5]) != 256)
				|| ((num[1] ^ num[4]) != 4)
				|| (num[1] != 5)) {
			ret = false;
		}
		return ret;
	}

	public static boolean check4(boolean ret, String s, char[] arr) {
		int l = 5, r = 55, cnt = 0;
		while (cnt < arr.length) {
			while (!Character.isLetter(s.charAt(l)))
				l++;
			while (!Character.isLetter(s.charAt(r)))
				r--;
			if (s.charAt(r) != arr[cnt] || s.charAt(l) != arr[cnt + 1]) {
				ret = false;
			}
			cnt += 2;
			l++;
			r--;
		}
		return ret;
	}

	public static boolean check5(boolean ret, String s, String tmp) {
		for (int i = 0; i < f1nal.length; ++i)
			tmp += s.charAt(f1nal[i]);

		if (((tmp.charAt(2) ^ tmp.charAt(0)) != 32)
				|| (tmp.charAt(0) + tmp.charAt(5) + tmp.charAt(6) != 294)
				|| (tmp.charAt(1) * tmp.charAt(3) != 8160)
				|| ((tmp.charAt(3) ^ tmp.charAt(4)) != 44)
				|| ((tmp.charAt(2) ^ tmp.charAt(3)) != 9)
				|| (tmp.charAt(0) * tmp.charAt(3) != 8058)
				|| (tmp.charAt(3) - tmp.charAt(4) != 28)
				|| ((tmp.charAt(2) ^ tmp.charAt(7)) != 28)
				|| (tmp.charAt(12) - tmp.charAt(13) + tmp.charAt(9) - tmp.charAt(8) != 38)
				|| (tmp.charAt(3) - tmp.charAt(4) != 28)
				|| ((tmp.charAt(2) ^ tmp.charAt(11)) != 0)
				|| (tmp.charAt(4) - tmp.charAt(6) != -44)
				|| ((tmp.charAt(6) ^ tmp.charAt(8)) != 19)
				|| (tmp.charAt(9) - tmp.charAt(5) != 25)
				|| (tmp.charAt(0) + tmp.charAt(5) + tmp.charAt(7) != 291)
				|| ((tmp.charAt(10) ^ tmp.charAt(5)) != 21)
				|| (tmp.charAt(1) != tmp.charAt(13))
				|| (tmp.charAt(11) != 111)
				|| (s.charAt(s.length() - 2) != 63)) {
			ret = false;
		}
		return ret;
	}

	public static void main(String[] args) {
		boolean[] isDigit = { false, false, false, false, false, false, false, false, false, false, true, false,
				false, false, false, true, false, false, false, true, false, false, false, false, false, false, false,
				false, true, false, true, false, false, false, false, false, false, false, false, false, false, false,
				false, false, true, false, false, false, false, true, false, false, false, false, false, false, false };
		int[] pos = { 17, 21, 24, 29, 32, 35, 38, 47, 52 };
		char[] let = { 't', 'P', 'i', 'o', 't', 'L', 'n', 'y', 'i', 'm', 'h', 'r', 'c', 'p', 'o', 'h', 'r', 'i',
				'P', 'm' };
		Scanner inp = new Scanner(System.in);
		System.out.print("Enter flag: ");
		String input = inp.next();
		boolean ret = true;
		if (check(check(check(check(check(ret, input), input, isDigit), input, pos), input, let), input, ""))
			System.out.println("Flag is correct");
		else
			System.out.println("Try another one");
	}
}

```
- Như ta có thể thấy rằng chương trình sẽ kiểm tra input bằng cách lồng rất nhiều hàm `check()` với parameters là input, một số các predefined array và các hàm `check()` khác . Để mà biết rõ được luồng kiểm tra như thế nào khi mà chỉ phân tích tĩnh thì thật sự rất khó, vì vậy ta sẽ phải debug file java này (VSCode có cung cấp extension giúp chúng ta debug )

- Sau khi debug, chúng ta có thể biết được thứ tự gọi các hàm `check()` và các parameters tương ứng
  	+ Hàm `check1(ret,input)`
  	  + Kiểm tra 5 kí tự đầu có phải là `KCSC{` và kí tự cuối có phải là `}` hay không
  	+ Hàm `check2(ret,input,isDigit[])`
  	  + Kiểm tra input tại các vị trí được đánh `true` trong mảng `isDigit[]` (từ mảng này ta có thể suy ra độ dài input là 57 kí tự) xem tại đấy có phải là kí tự số hay không, sau đó tiến hành biến đổi các kí tự số này từ ASCII sang số thuần bằng cách lấy giá trị đó trừ cho 0x30. Ví dụ `0x32` là biểu diễn của kí tự `2` trong bảng ASCII nên khi trừ cho 0x30 thì giá trị còn lại sẽ là 0x2
  	  + Tiếp đến gán các giá trị đã được biến đổi vào array `num` rồi thực hiện kiểm tra (đoạn này mình bắt buộc phải giải tay tìm các giá trị trong mảng `num` vì khi thử z3 thì không ra flag)
  	+ Hàm `check3(ret,input,pos[17,...])`
  	  + Kiểm tra input tại các index theo mảng `pos[]` có chứa kí tự `_` hay không
  	+ Hàm `check4(ret,input,let[])`
  	  + Thực hiện duyệt phần content (`{content_ở_đây}`) của flag từ 2 đầu nếu như gặp phải kí tự nào **không thuộc bảng chữ cái** thì bỏ qua chúng, ngược lại sẽ đối chiếu chúng với một số kí tự có trong mảng `let[]`
  	+ Hàm `check5(ret,input,"")`
  	  + Thực hiện concat vào string `tmp` các kí tự trong input với index được duyệt theo mảng `f1nal[]`
  	  + Lấy các kí tự trong string tmp thực hiện tính toán rồi kiểm tra với các constants
  	  + Kiểm tra kí tự cuối cùng trong content của flag xem có phải là `?` hay không

- Vậy để giải bài này mình sẽ chia ra làm 2 phase:
  + Phase 1: Dùng z3 để giải các constraints có trong hàm `check5()`
  + Phase 2: Lấy kết quả từ Phase 1 rồi hoàn thiện nốt script

Phase 1
```python
from z3 import *

tmp = [BitVec(f'tmp{i}', 8) for i in range(14)]


s = Solver()


s.add((tmp[2] ^ tmp[0]) == 32)
s.add(tmp[0] + tmp[5] + tmp[6] == 294)
s.add(tmp[1] * tmp[3] == 8160)
s.add((tmp[3] ^ tmp[4]) == 44)
s.add((tmp[2] ^ tmp[3]) == 9)
s.add(tmp[0] * tmp[3] == 8058)
s.add(tmp[3] - tmp[4] == 28)
s.add((tmp[2] ^ tmp[7]) == 28)
s.add(tmp[12] - tmp[13] + tmp[9] - tmp[8] == 38)
s.add((tmp[2] ^ tmp[11]) == 0)
s.add(tmp[4] - tmp[6] == -44)
s.add((tmp[6] ^ tmp[8]) == 19)
s.add(tmp[9] - tmp[5] == 25)
s.add(tmp[0] + tmp[5] + tmp[7] == 291)
s.add((tmp[10] ^ tmp[5]) == 21)
s.add(tmp[1] == tmp[13])
s.add(tmp[11] == 111)  


if s.check() == sat:

    model = s.model()
    solution = [model[tmp[i]] for i in range(14)]
    print(solution) #[79, 80, 111, 102, 74, 97, 118, 115, 101, 122, 116, 111, 97, 80]

else:
    print("No")

```

Phase 2 
```python
tmp_flag = ['K', 'C', 'S', 'C', '{', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '}']
underscoreIndices = [ 17, 21, 24, 29, 32, 35, 38, 47, 52 ]
digitIndices = [ 10, 15, 19, 28, 30, 44, 49 ]
let =[ 't', 'P', 'i', 'o', 't', 'L', 'n', 'y', 'i', 'm', 'h', 'r', 'c', 'p', 'o', 'h', 'r', 'i',
				'P', 'm' ]
f1nal = [ 18, 20, 22, 23, 25, 26, 27, 31, 33, 34, 36, 37, 39, 40 ]
f1nal_res = [79, 80, 111, 102, 74, 97, 118, 115, 101, 122, 116, 111, 97, 80]
tmp_flag[len(tmp_flag) - 2] = chr(63)
tmp_flag[digitIndices[0]] = chr(0 + 0x30)
tmp_flag[digitIndices[1]] = chr(5 + 0x30)
tmp_flag[digitIndices[2]] = chr(0 + 0x30)
tmp_flag[digitIndices[3]] = chr(4 + 0x30)
tmp_flag[digitIndices[4]] = chr(1 + 0x30)
tmp_flag[digitIndices[5]] = chr(4 + 0x30)
tmp_flag[digitIndices[6]] = chr(5 + 0x30)
for pos in underscoreIndices:
    tmp_flag[pos] = '_'
l = 5 
r = 55
cnt=0
while(cnt<len(let)):
    if(tmp_flag[l].isalpha() == False ):
        l +=1
    if(tmp_flag[r].isalpha() == False):
        r -= 1 
    tmp_flag[r] = let[cnt]
    tmp_flag[l] = let[cnt+1]
    cnt +=2 
    l +=1
    r -=1
for i in range(len(f1nal)):
    tmp_flag[f1nal[i]] = chr(f1nal_res[i])

for i in tmp_flag:
    print(i,end='')

```
**Flag:** `KCSC{PoLym0rphi5m_O0P_of_Jav4_1s_ez_to_aPPro4ch_i5nt_it?}`
  	
