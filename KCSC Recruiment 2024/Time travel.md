- Đề cho 2 file. PE64 và enc.txt

![image](https://github.com/user-attachments/assets/48c9788f-3c17-4a3f-8ea5-1816a788f8d4)

- Pseudocode của IDA
```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  FILE *v4; // rax
  int i; // [rsp+20h] [rbp-28h]
  unsigned __int64 v7; // [rsp+28h] [rbp-20h]

  v3 = call_time64(0i64);
  srand(v3);
  v4 = _acrt_iob_func(1u);
  freopen(FileName, Mode, v4);
  for ( i = 0; ; ++i )
  {
    v7 = -1i64;
    do
      ++v7;
    while ( aKcscOhNoTheFla[v7] );
    if ( i >= v7 )
      break;
    aKcscOhNoTheFla[i] ^= rand();
    call_fprintf("%c", (unsigned __int8)aKcscOhNoTheFla[i]);
  }
  return 0;
}
```
- Đây là một bài có sử dụng hàm `rand()` và `srand()`, điều mà chúng ta phải lưu ý cho những dạng bài như thế này là phải để ý là bài cho loại file thực thi nào. Ví dụ như PE32/64 sẽ là của Windows và ELF32/64 sẽ là của Linux bởi trên 2 hệ điều hành này thì giá trị trả về của 2 hàm trên sẽ khác nhau

- Về luồng chạy của chương trình sẽ như sau
  + Đầu tiên chương trình gọi hàm `call_time64(0i64)` để lấy thời gian hiện tại (khi bắt đầu chạy chương trình) rồi gán return value cho `v3`, `v3` sẽ được dùng để tạo seed  
  + Tiếp theo chương trình sẽ tiến hành mở file có tên là `enc.txt` với mode là `wb`, nếu trong trường hợp file không tồn tại thì sẽ tạo 1 file mới có tên như trên
  + Sau đó chương trình sẽ lấy từng phần tử của flag xor với return value của hàm `rand()` với seed được khởi tạo bởi `srand(v3)`, cuối cùng lấy LOBYTE của kết quả vừa rồi viết vào file. Ví dụ nếu kết quả của phép xor kể trên là 0xDEAD thì ta sẽ chỉ lấy 0xAD viết vào file

- Giải quyết xong vấn đề về luồng, để tìm ngược ra flag ta cũng sẽ sử dụng quy trình tương tự, lấy từng byte trong file `enc.txt` xor kết quả của hàm `rand()` (ta sẽ phải bruteforce để tìm seed) và AND với kết quả tìm được với 0xFF để lấy phần LOBYTE của kết quả. Tại sao lại bruteforce? Vì ta không biết giá trị cụ thể mà hàm `time64()` sẽ trả về là gì và hàm `time64()` sẽ trả về giá trị là số giây đã trôi qua tính từ Unix Epoch cho đến thời điểm hiện tại thế nên ta sẽ để giá trị bắt đầu là 0 (ban đầu mình cứ nghĩ là giá trị bắt đầu sẽ phải là số giây trôi qua tính từ 2024-09-04 03:56:06 //Timestamp của chương trình// nhưng nhờ hint của author nên mình mới biết rằng thời điểm bắt đầu và thời điểm kết thúc không hề cố định như thế kia )

- Hiểu rõ được quy trình, bây giờ ta có thể viết script
```C
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main() {

    unsigned int ciphertext[] = {
        0x68, 0x68, 0x7D, 0xC6, 0x37, 0x8E, 0xFD, 0xEB, 0x34, 0xFE,
        0x17, 0xFE, 0x9D, 0x28, 0xE0, 0x04, 0x70, 0x85, 0xB7, 0x44,
        0x68, 0x37, 0xC0, 0xFB, 0x22, 0xC9, 0xA0, 0x49, 0xBD, 0x2A,
        0xB6, 0xCF, 0xB8, 0x45, 0xBD, 0x44, 0x50, 0x87, 0xB1, 0x48,
        0xF3, 0xC9, 0x7C, 0x23, 0xB8, 0xF9, 0x2E, 0x83, 0xBD, 0xEE,
        0xA8, 0xD9, 0x08, 0xEF, 0x37, 0x98, 0x1C, 0x76, 0xC5, 0x13,
        0xF6, 0xF0, 0xDC, 0x0E, 0x2A, 0x51, 0xBD, 0xD4, 0x23, 0x64,
        0x84, 0x53, 0xE1, 0x4B
    };

    size_t cipher_len = sizeof(ciphertext)/sizeof(ciphertext[0]);
    unsigned int past = 0;
    unsigned int present = (unsigned int)_time64(NULL); 

    for (unsigned int i = past; i <= present; i++) { 
        srand(i);  
        
        unsigned char decrypted[74];  
        for (size_t j = 0; j < cipher_len; ++j) {
            int rand_val = rand(); 
            decrypted[j] = (ciphertext[j] ^ rand_val) & 0xFF;  
        }
        decrypted[cipher_len] = '\0';  

 
        if (strncmp((char*)decrypted, "KCSC{", 5) == 0) {
            printf("%s",decrypted);
            break;
        }
    }
    
    return 0;
}
```
**Flag:** `KCSC{0xffffff_is_1970-07-14,I_created_this_challenge_at_"the_end"_of_time}`
