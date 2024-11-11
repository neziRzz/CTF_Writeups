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
