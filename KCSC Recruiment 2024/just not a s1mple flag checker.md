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
