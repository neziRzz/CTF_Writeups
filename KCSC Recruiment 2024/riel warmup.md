- Đề cho 1 file PE64

![image](https://github.com/user-attachments/assets/f99eea59-85a5-48ef-826b-b4578944bae4)

- Pseudocode của IDA

 ![image](https://github.com/user-attachments/assets/f5deefd9-eed9-4465-8751-49f841a489a2)

- Hàm Hide

![image](https://github.com/user-attachments/assets/0b0ba9d0-91f4-4a48-aeff-12d2b8de18b7)

- Chúng ta có thể thấy rằng bài sẽ bắt ta phải tự tìm flag được giấu đâu đó trong code, hàm hide đã cho ta một phần nhỏ của flag là `_how_to_use`
- Bài này đã khiến mình submit sai liên tục vì mình đã quá chú tâm vào mã giả mà không kiểm tra kĩ mã asm của bài, vì vậy để tiếp tục việc phân tích thì từ đây ta sẽ phân tích mã asm của bài

![image](https://github.com/user-attachments/assets/659ede89-2009-4362-a045-882acad43213)

- Ta có thể thấy được tiếp là `flag4` sẽ là phần cuối cùng của flag, nếu như chỉ có từng này thì flag sẽ không thể tạo thành 1 string có nghĩa nhưng chúng ta hãy để ý đến các instruction sau `mov     rax, 7661687B4353434Bh`, `mov     rdx, 776F6E6B5F755F65h`, `mov     [rbp+var_10], 6Eh`, các instruction này gán cho 2 register `rax`  `rdx` và `[rbp+var_10]` những giá trị kì lạ nhưng các giá trị ấy lại không được sử dụng ở đâu cả, tuy 2 register `rax` và `rdx` có thể sẽ là các arguments cho hàm hide nhưng kiểu calling convention của hàm này không hề thuộc kiểu `__fastcall` nên ta có thể chắc chắn rằng các giá trị trên không hề được sử dụng ở đâu hết, khi mình bấm chuột phải lên các giá trị này thì sẽ thấy 1 điều bất ngờ

![image](https://github.com/user-attachments/assets/fde701a9-80bc-45cd-b210-c98034e58879)

- Hóa ra đây chính là những giả trị ASCII của flag nhưng ở dưới dạng hex, nhưng mà tại sao chúng lại bị in ngược thì để giải thích cho điều này thì bởi đây là một file sử dụng kiểu Endian là `LE`(Little Endian) tức là những byte nằm ở cuối sẽ được đọc trước những byte ở đầu
- Với những dữ kiện trên, ta chỉ cần chuột phải (hoặc trỏ vào các value trên rồi bấm r) để convert hết các value về string rồi viết script
```python
x1 = 'vah{CSCK'
x2 = 'nwonk_u_e'
x3 = '_how_to_use'
x4 = 'ADI_'
x5 = '^^}pumraw_laer_siht_retfa_'
print(x1[::-1]+x2[::-1]+x3+x4[::-1]+x5[::-1])
```
**Flag:KCSC{have_u_known_how_to_use_IDA_after_this_real_warmup}**
