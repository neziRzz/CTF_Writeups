- Đề cho 1 file PE64 được code bằng Go

![image](https://github.com/user-attachments/assets/d77e878b-caab-4ae3-aef9-3c7509c7c2b9)


- Thường đối với những bài được code bằng Go, khi load vào trong IDA thì các tên biến và hàm sẽ rất khó nhìn và để phần nào đó khắc phục được điều này ta có thể sử dụng một tool được viết bằng python tên là `GoReSym` được phát triển bởi Mandiant [GoReSym's repo](https://github.com/mandiant/GoReSym) (may thay là bài này các tên hàm đã được rename)

- Và một điểm nữa khi debug những bài được code bằng Go(những bài có pseudocode phức tạp nói chung) là ta không nên nhìn vào mỗi pseudocode để debug mã hãy debug mã asm và pseudocode một cách song song (step qua các asm instruction ) để có cái nhìn chính xác nhất về cách mà input được xử lý

- Pseudocode của hàm main 
```C
  void __cdecl main_main()
  {
  __int64 v0; // r14
  __int128 v1; // xmm15
  _QWORD *v2; // rcx
  __int64 i; // rax
  __int64 v4; // r9
  unsigned __int64 v5; // r8
  __int64 v6; // rax
  __int64 v7; // [rsp+38h] [rbp-200h]
  __int64 v8; // [rsp+40h] [rbp-1F8h]
  char v9; // [rsp+90h] [rbp-1A8h] BYREF
  _QWORD *v10; // [rsp+1D8h] [rbp-60h]
  __int128 v11; // [rsp+1E0h] [rbp-58h]
  void *v12; // [rsp+1F0h] [rbp-48h]
  char **v13; // [rsp+1F8h] [rbp-40h]
  void *v14; // [rsp+200h] [rbp-38h]
  char **v15; // [rsp+208h] [rbp-30h]
  const char *v16; // [rsp+210h] [rbp-28h]
  _QWORD *v17; // [rsp+218h] [rbp-20h]
  void *v18; // [rsp+220h] [rbp-18h]
  char **v19; // [rsp+228h] [rbp-10h]

  if ( (unsigned __int64)&v9 <= *(_QWORD *)(v0 + 16) )
    runtime_morestack_noctxt_abi0();
  v8 = 18LL;
  sub_AFF062();
  v10 = (_QWORD *)runtime_newobject();
  *v10 = 0LL;
  v18 = &unk_B45580;
  v19 = &off_B7BBF0;
  fmt_Fprint();
  v16 = "\b";
  v17 = v10;
  fmt_Fscanln();
  v2 = v10;
  if ( v10[1] != 51LL )
  {
    v14 = &unk_B45580;
    v15 = &off_B7BC00;
    fmt_Fprintln();
    os_Exit();
    v2 = v10;
  }
  for ( i = 0LL; i < 51; i = v4 + 1 )
  {
    if ( (unsigned __int64)i >= v2[1] )
      runtime_panicIndex();
    v4 = i;
    v5 = i - (i & 0xFFFFFFFFFFFFFFE0LL);
    if ( v5 >= 0x20 )
      runtime_panicIndex();
    if ( *(&v8 + i) != ((unsigned __int8)aYxv0ag9ybm9vym[v5] ^ (unsigned __int64)*(unsigned __int8 *)(i + *v2)) )
    {
      v7 = i;
      v12 = &unk_B45580;
      v13 = &off_B7BC10;
      fmt_Fprintln();
      os_Exit();
      v2 = v10;
      v4 = v7;
    }
  }
  v11 = v1;
  runtime_concatstring2();
  v6 = runtime_convTstring();
  *(_QWORD *)&v11 = &unk_B45580;
  *((_QWORD *)&v11 + 1) = v6;
  fmt_Fprintln();
  os_Exit();
  }
```
- Khi nhìn vào pseudocode của hàm main, ta có thể thấy được chương trình sẽ nhận input, kiểm tra độ dài của input có bằng 51 hay không, nếu không sẽ in ra chuỗi `Wrong Length!!!` và thoát, tiếp theo chương trình sẽ lấy từng kí tự của input xor với một array base64 với các index của array này được duyệt theo `v5 = i - (i & 0xFFFFFFFFFFFFFFE0LL);` để mỗi khi `v5` > 31 thì v5 sẽ duyệt array này từ đầu (tương tự với việc lấy i % 32), sau đó sẽ kiểm tra kết quả được xor với `v8` và nếu như sai ở bất kì một index nào thì chương trình sẽ in ra chuỗi `Wrong Flag!!!` và thoát

- Như mình đã nói ở trên thì lí do cụ thể hơn cho việc debug song song pseudocode và asm code trong bài này nếu ta debug trong cửa sổ pseudocode, khi ta trỏ chuột vào các biến như `v10`, `v2`,... thì nó sẽ không hiện lên những giá trị như mong đợi, và với những bài mà số lượng các phép tính nhiều và phức tạp thì việc phân tích sẽ dường như là không thể

![image](https://github.com/user-attachments/assets/33090f85-a420-49a2-967f-84187454d6d5)

![image](https://github.com/user-attachments/assets/78abd627-393b-4a28-b6d6-b1b3ed754785)

**Note** : **Đây là địa chỉ nhưng khi tìm giá trị của chúng trong hex viewer thì chúng không cho ra giá trị như mong đợi**

- `v8` trong built-in hex viewer của IDA

![image](https://github.com/user-attachments/assets/480b4511-4af7-4ff8-9dff-095f6fb909d9)


- Ta có thể thấy rằng v8 là một array chứa các DWORD (mình đã bôi xanh những DWORD thuộc `v8`) , ta chỉ nhặt những byte khác 0 rồi viết script giải

```python
from z3 import *
key = 'YXV0aG9ybm9vYm1hbm5uZnJvbWtjc2M='
flag = [BitVec('x[%d]'%i,8) for i in range(51)]
hex = [
    0x12, 0x1B,
    0x05, 0x73,
    0x1A, 0x70,
    0x51, 0x48,
    0x57, 0x32,
    0x08, 0x43,
    0x06, 0x5E,
    0x05, 0x5D,
    0x1B, 0x5B,
    0x05, 0x19,
    0x6E, 0x00,
    0x7C, 0x29,
    0x01, 0x3F,
    0x40, 0x06,
    0x0F, 0x01,
    0x23, 0x0B,
    0x6A, 0x07,
    0x61, 0x55,
    0x00, 0x75,
    0x5D, 0x18,
    0x53, 0x5A,
    0x66, 0x4A,
    0x6A, 0x51,
    0x02, 0x49,
    0x43, 0x4C,
    0x48
]
s = Solver()
for i in range(51):
    s.add(flag[i]>=0x20)
    s.add(flag[i]<=0x7F)
for i in range(51):
    v5 = i % 32
    s.add(hex[i] == ord(key[v5]) ^ flag[i])
if(s.check()==sat):
    model = s.model()
    flag_string = ''.join([chr(model[flag[i]].as_long()) for i in range(51)])
    print(flag_string)
```
**Flag:** `KCSC{7h15_15_345y60l4n6_ch4ll3n63_7ea2da17_<3<3!!!}`
