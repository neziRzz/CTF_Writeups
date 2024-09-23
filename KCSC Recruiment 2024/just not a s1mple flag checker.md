- Đề cho 1 file PE64

- Bài này làm mình nhớ đến hồi học lập trình căn bản...

![image](https://github.com/user-attachments/assets/ed0f09fb-bf4a-4059-bbf6-3439463044fb)


- Pseudocode của IDA ( mình đã đổi tên một số hàm và biến để tiện hơn cho việc phân tích

```C
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE *node_fake_flag; // rax
  __int64 v4; // rdx
  __int64 v5; // r8
  _BYTE *node_input; // rax
  _BYTE *node_binary; // rax
  _BYTE *node_binary2; // rax
  __int64 v9; // rdx
  __int64 v10; // r8
  char v11; // al
  __int64 v12; // rdx
  __int64 v13; // r8
  int k; // [rsp+20h] [rbp-108h]
  int m; // [rsp+24h] [rbp-104h]
  int i; // [rsp+28h] [rbp-100h]
  int j; // [rsp+2Ch] [rbp-FCh]
  int n; // [rsp+34h] [rbp-F4h]
  int v20; // [rsp+38h] [rbp-F0h]
  __int64 v21; // [rsp+40h] [rbp-E8h]
  int final; // [rsp+4Ch] [rbp-DCh]
  _BYTE *node; // [rsp+70h] [rbp-B8h]
  _QWORD *head2; // [rsp+78h] [rbp-B0h] BYREF
  _QWORD *head1; // [rsp+80h] [rbp-A8h] BYREF
  _QWORD *head3; // [rsp+88h] [rbp-A0h] BYREF
  char v27[16]; // [rsp+90h] [rbp-98h] BYREF
  char input[112]; // [rsp+A0h] [rbp-88h] BYREF

  head1 = 0i64;                                 // input
  head2 = 0i64;                                 // base2
  head3 = 0i64;                                 // fake_flag
  for ( i = 423; i >= 0; --i )
  {
    node_fake_flag = create_node(fake_flag[4 * i]);// this starts somewhere in the binary arr
    push_to_list(&head3, node_fake_flag);
  }
  call_printf(aShowYourSkill, argv, envp);
  call_scanf("%s", input);
  v21 = -1i64;
  do
    ++v21;
  while ( input[v21] );
  if ( (_DWORD)v21 == 53 )
  {
    for ( j = 0; j < 53; ++j )
    {
      node_input = create_node(input[j]);
      push_to_list(&head1, node_input);         // head1: K->C->S->C->...->NULL
    }
    base_convert(&head1, &head2, 10, 2);        // convert base10 to base 2, results push to head2:bin(})->....
    for ( k = 423; k >= 0; --k )
    {
      *(_DWORD *)&binary_arr[4 * k] ^= (unsigned __int8)get_node_from_head((__int64)head2);
      pop_node_from_list(&head2);
    }
    for ( m = 0; m < 424; m += 2 )
    {
      node_binary = create_node(binary_arr[4 * m + 4]);
      push_to_list(&head2, node_binary);
      node_binary2 = create_node(binary_arr[4 * m]);
      push_to_list(&head2, node_binary2);
    }
    base_convert(&head2, &head1, 2, 8);         // convert base2 to base10 then to base 8
    v20 = 0;
    while ( head1 )
    {
      for ( n = 0; n < 8; ++n )
      {
        v27[n] = get_node_from_head((__int64)head1);
        pop_node_from_list(&head1);
      }
      v11 = base10((__int64)v27);
      node = create_node(LOBYTE(dword_7FF7C9B24160[v20]) ^ v11);
      push_to_list(&head2, node);               // head2: K->C->S->C->......
      ++v20;
    }
    while ( head2 )
    {
      final = (unsigned __int8)get_node_from_head((__int64)head2);
      if ( final != (unsigned __int8)get_node_from_head((__int64)head3) )
      {
        call_printf(aNope, v12, v13);
        return 0;
      }
      pop_node_from_list(&head2);
      pop_node_from_list(&head3);
    }
    call_printf(aCorrect, v9, v10);
  }
  else
  {
    call_printf(aWrongInputLeng, v4, v5);
  }
  return 0;
}
```
- Đây là 1 bài sử dụng linked list để implement stack, tại sao lại như vậy? Bây giờ mình sẽ phân tích một số hàm sau để khẳng định điều này

- Hàm `create_node()`
```C
_BYTE *__fastcall create_node(char a1)
{
  _BYTE *result; // rax

  result = malloc(0x10ui64);
  result[8] = a1;
  *(_QWORD *)result = 0i64;
  return result;
}
```
- Đầu tiên malloc một vùng nhớ `0x10` byte

- Gán cho byte thứ 9 là giá trị của argument được truyền vào hàm

- Cuối cùng gán cho giá trị của 8 byte đầu là 0 (`NULL`) và trả về địa chỉ được malloc

- Ta có thể coi quá trình này như là việc tạo một node và sau đó cho con trỏ của node đó trỏ vào `NULL` (`node->NULL`)

- Hàm `push_to_list()`
```C
_QWORD *__fastcall push_to_list(_QWORD *a1, _QWORD *a2)
{
  _QWORD *result; // rax

  *a2 = *a1;
  result = a1;
  *a1 = a2;
  return result;
}
```
- Trước khi phân tích, ta có thể thấy rằng các arguments truyền vào hàm này đều có pattern như sau


![image](https://github.com/user-attachments/assets/93743e3f-33e9-4b5d-8445-e9aa5be46704)


- Đầu tiên hàm sẽ gán cho giá trị con trỏ của `a2` bằng `a1`

- Tiếp theo lưu lại giá trị của `a1`

- Cuối cùng cập nhật giá trị của con trỏ `a1` bằng với `a2`

- Trả về giá trị cũ của `a1`

- Dựa vào những dữ kiện trên ta có thể thấy rằng, hàm này sẽ update con trỏ `head` sao cho khi sau mỗi một lần gọi hàm `create_node()` thì node được tạo ra sẽ được `head` trỏ tới

- Hàm `remove_top_node()`
```
void __fastcall remove_top_node(_QWORD **a1)
{
  _QWORD *Block; // [rsp+20h] [rbp-18h]

  if ( *a1 )
  {
    Block = *a1;
    *a1 = (_QWORD *)**a1;
    free(Block);
  }
}
```
- Hàm này nhận các arguments có pattern như sau

![image](https://github.com/user-attachments/assets/5cf5908c-9ba1-46cf-b7c4-cec534841205)

- Đầu tiên hàm sẽ kiểm tra `*a1` có `NULL` hay không

- Tiếp theo, gán cho biến block giá trị là con trỏ đến `a1`

- Thực hiện dereference `*a1` và gắn giá trị cho `*a1` (để cho `a1` trỏ về giá trị mà nó trỏ trước đó)

- Cuối cùng là thực hiện free `Block`

- Vì vậy ta có thể kết luận rằng, đây là một implementation của stack bằng linked list, nó sẽ thực hiện 2 chức năng chính là đẩy value vào stack và pop value ra khỏi stack

------------------------------------------------------------------------------------------------------------------------------
- Quay về phân tích luồng của chương trình, ta có thể thấy rằng

- Đầu tiên chương trình sẽ bắt đầu lấy các phần tử với offsets tối đa là ở 1692 byte(bắt đầu ở byte thứ 1692) tính từ arr `fake_flag[]` và tiến hành lấy các phần tử ở đó push vào trong stack

- Tiếp đến chương trình sẽ thực hiện lấy input và kiểm tra độ dài của input có bằng 53 hay không, nếu không sẽ in ra chuỗi `Wrong input length` và thoát

- Nếu thỏa mãn điều kiện trên thì chương trình sẽ push từng phần tử của input vào trong stack với con trỏ `head1` con trỏ là head, gọi hàm `base_convert(&head1, &head2, 10, 2)` để đổi giá trị của từng phần tử của input sang hệ cơ số 2 (binary) và kết quả sẽ được đẩy vào stack `head2`

--------------------------------------------------------------------------------------------------------------------------------

- Hàm `base_convert()`
```C
_QWORD *__fastcall base_convert(_QWORD *a1, _QWORD *a2, int a3, int a4)
{
  _QWORD *result; // rax
  unsigned __int8 node_non_zero_val; // al
  unsigned __int8 v6; // al
  int i; // [rsp+20h] [rbp-28h]
  char v8[8]; // [rsp+28h] [rbp-20h] BYREF

  if ( a3 == 10 )
  {
    while ( 1 )
    {
      result = a1;
      if ( !*a1 )
        break;
      node_non_zero_val = get_node_from_head(*a1);
      base10_to(a2, node_non_zero_val, a4);
      pop_node_from_list((_QWORD **)a1);
    }
  }
  else
  {
    while ( 1 )
    {
      result = a1;
      if ( !*a1 )
        break;
      for ( i = 0; i < 8; ++i )
      {
        v8[i] = get_node_from_head(*a1);
        pop_node_from_list((_QWORD **)a1);
      }
      v6 = to_base10((__int64)v8, a3);
      base10_to(a2, v6, a4);
    }
  }
  return result;
}
```
- Đầu tiên hàm này sẽ check xem hệ ban đầu cần đổi có phải là hệ 10 hay không (`a3 == 10`), nếu có thì sẽ tiến hành kiểm tra con trỏ `a1` (head của stack) có `NULL` hay không, rồi sau đó lấy các node này đổi từ hệ 10 sang hệ được specified trong argument `a4`

- Nếu argument `a3 != 10` (hệ ban đầu không phải là 10), thì sẽ pop các giá trị trong stack có head là `a1` bỏ vào array `v8[]` (pop 8 node một lần), rồi thực hiện biến đổi các giá trị có trong array này sang hệ 10 bằng hàm `to_base10()`. Ví dụ nếu giá trị trong array lần lượt là [0,0,0,0,0,1,2,3] thì giá trị trả về của hàm sẽ là `123` , về cách biến đổi 1 hệ bất kì sang hệ 10, các bạn có thể tham khảo ở [đây](https://www.rapidtables.com/convert/number/base-converter.html)

- Hàm `base10_to()`
```C
__int64 __fastcall base10_to(_QWORD *a1, unsigned __int8 a2, int a3)
{
  __int64 result; // rax
  _BYTE *node; // rax
  _BYTE *v5; // rax
  int i; // [rsp+20h] [rbp-18h]

  for ( i = 0; ; ++i )
  {
    result = a2;
    if ( !a2 )
      break;
    node = create_node(a2 % a3);
    push_to_list(a1, node);
    a2 /= a3;
  }
  while ( i < 8 )
  {
    v5 = create_node(0);
    push_to_list(a1, v5);
    result = (unsigned int)++i;
  }
  return result;
}
```
-  Hàm này sẽ tiến hành lấy giá trị các node chia modulo cho argument `a3` (trong trường hợp này sẽ là 2), sau đó sẽ lấy các giá trị trả về của phép tính trên push vào stack có head là `a1` và tiếp tục chia cho đến khi `a2 = 0`. Bạn nào mà đã học kĩ môn lập trình căn bản từ hồi năm nhất thì sẽ có thể thấy rằng đây là thuật toán đổi một số từ hệ 10 sang 1 hệ bất kì sử dụng stack

-  Vòng `while i < 8` có nhiệm vụ đảm bảo rằng mỗi giá trị sau khi được biến đổi sẽ có độ lớn là 8 bit (or byte) bằng cách là nếu khi mà ở vòng lặp for phía trên khi mà số lượng giá trị của các node sau khi được biến đổi mà không đủ 8 thì sẽ fill các giá trị còn lại là 0

- Hàm `to_base10()`
```C
__int64 __fastcall to_base10(__int64 target, int base_of_target)
{
  unsigned __int8 v3; // [rsp+20h] [rbp-28h]
  int i; // [rsp+24h] [rbp-24h]
  double v5; // [rsp+30h] [rbp-18h]

  v3 = 0;
  for ( i = 0; i < 8; ++i )
  {
    v5 = (double)*(unsigned __int8 *)(target + i);
    v3 = (int)((double)v3 + v5 * pow((double)base_of_target, (double)(8 - i - 1)));
  }
  return v3;
}
```
- Hàm này thực chất chỉ biến đổi các giá trị trong array `target[]` về giá trị base10 theo công thức được đề cập trong [đây](https://www.rapidtables.com/convert/number/base-converter.html) với 2 parameters là array `target[]` và base hiện tại của array `target[]`

--------------------------------------------------------------------------------------------------------------------------------

- Quay lại về luồng hoạt động của chương trình, sau khi đã biến đổi các giá trị của `input` về base2 và push kết quả vào trong stack có head là `head2` thì tiến hành xor các giá trị có trong array `binary_arr[]` (bắt đầu từ cuối) với step là 4 byte với các giá trị được pop từ `head2` (là các giá trị của 8 bit của input)



```python
fake_flag = [
    0x24, 0x24, 0x24, 0x24, 0x24, 0x24, 0x24, 0x24, 0x24, 0x24,
    0x24, 0x24, 0x7d, 0x67, 0x61, 0x6c, 0x66, 0x20, 0x65, 0x6b,
    0x61, 0x66, 0x20, 0x61, 0x20, 0x74, 0x6f, 0x6e, 0x20, 0x74,
    0x73, 0x75, 0x6a, 0x20, 0x65, 0x72, 0x65, 0x68, 0x20, 0x67,
    0x6e, 0x69, 0x68, 0x74, 0x20, 0x74, 0x6f, 0x6e, 0x7b, 0x43,
    0x53, 0x43, 0x4b
]
rev_fake_flag = fake_flag[::-1]
dword_7FF7C9B24160 = [
    0x0c2, 0x03d, 0x029, 0x0cf, 0x134, 0x0de, 0x138, 0x110, 0x0cc, 0x075,
    0x13d, 0x154, 0x0f2, 0x047, 0x11b, 0x0b5, 0x087, 0x118, 0x0b6, 0x0a7,
    0x104, 0x001, 0x104, 0x134, 0x004, 0x128, 0x159, 0x0f0, 0x018, 0x0f7,
    0x019, 0x043, 0x10d, 0x000, 0x0e1, 0x08c, 0x0ad, 0x162, 0x153, 0x0eb,
    0x0e5, 0x0da, 0x0a0, 0x0d8, 0x04c, 0x068, 0x05c, 0x0a0, 0x034, 0x0c8,
    0x03e, 0x066, 0x150

]
flag = []
binary_arr = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
for i in range(len(rev_fake_flag)):
    rev_fake_flag[i] = rev_fake_flag[i] ^ dword_7FF7C9B24160[i]
decimal_list = [int(str(num), 8) for num in rev_fake_flag]
binary_list = [format(num, '08b') for num in decimal_list[::-1]]
bit_list = [bit for binary in binary_list for bit in binary]
bit_list_rev = bit_list[::-1]
for i in range(0,len(bit_list_rev),2):
    bit_list_rev[i], bit_list_rev[i+1] = bit_list_rev[i+1], bit_list_rev[i]
for i in range(len(bit_list)):
    binary_arr[4*i] ^= int(bit_list_rev[i])
for i in range(423,-1,-1):
    flag.append(binary_arr[4*i])
bytes_list = [flag[i:i + 8] for i in range(0, len(flag), 8)]
ascii_string = ''.join(chr(int(''.join(map(str, byte)), 2)) for byte in bytes_list)
print(ascii_string)
```
