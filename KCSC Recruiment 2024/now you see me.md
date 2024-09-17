- Đề cho 1 template web như sau

  ![image](https://github.com/user-attachments/assets/4f25e34e-a46b-4464-9b11-ec2703ea03c7)

- Khi ta nhập input vào thì sẽ bị chuyển hướng đến [đây](http://157.15.86.73:3004/register), và giao diện web trông như thế này

 ![image](https://github.com/user-attachments/assets/81b2ed70-6175-4ea0-9a03-002bd2d47860)

- Với một người chỉ có kiến thức mảng web newbie như mình, thì sẽ cần phải biết sử dụng Burpsuite ở mức cơ bản, đây là một công cụ có thể giúp chúng ta xem các responses và edit các requests một cách dễ dàng

- Đây là giao diện của Burpsuite

  ![image](https://github.com/user-attachments/assets/eada5d57-e9f3-49e2-b77b-e151bfcc6924)

- Ta chọn `Target` và nhấn `Open Browser` để mở trình duyệt built-in của Burpsuite rồi sau đó paste đường link của web target của mình vào URL

- Sau đó dùng browser nêu trên để nhập input rồi quan sát sự thay đổi trong giao diện của `Target`

![image](https://github.com/user-attachments/assets/64a40b9a-7d06-4f9c-80c1-418cd1639770)

- Ta có thể thấy chỉ có mỗi Method `POST` là có response nên mình sẽ nhấn vào đấy và đưa nó vào repeater để phân tích

![image](https://github.com/user-attachments/assets/009d4241-8975-477f-9a66-1763e3542b58)

- Bài bắt ta phải tìm được file `flag.txt`, và tùy thuộc vào input mà mình nhập vào thì response sẽ khác, sau một hồi thử các payload cơ bản thì mình phát hiện ra web này dính lỗi SSTI với payload `{{7*7}}` cho ra response `49`

 ![image](https://github.com/user-attachments/assets/582e3f9a-76ef-45cb-ae9f-523edb6dc92e)


- Với payload như trên thì ta có thể xác định được rằng template của web có thể là `Twig` hoặc là `Jinja2` trong trường hợp này template sẽ là `Jinja2` vì khi mình thử thêm payload `{{7*'7'}}` thì response là `7777777`

![68747470733a2f2f692e696d6775722e636f6d2f47565a655671362e706e67](https://github.com/user-attachments/assets/ebb0760f-d364-4034-9988-7efd96b72621)

- Sau đó mình lấy flag với payload `{{get_flashed_messages.__globals__.__builtins__.open("/flag.txt").read()}}` 

![image](https://github.com/user-attachments/assets/df91cd2a-3940-4276-bb0b-e4b8df42af72)

**Flag:** `KCSC{flagrandomngaunhienlagicungdu0c}`
