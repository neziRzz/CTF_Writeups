- Đề cho 1 file python

```python
b64 = {
    "000000": "/",
    "000001": "+",
    "000010": "0",
    "000011": "1",
    "000100": "2",
    "000101": "3",
    "000110": "4",
    "000111": "5",
    "001000": "6",
    "001001": "7",
    "001010": "8",
    "001011": "9",
    "001100": "a",
    "001101": "b",
    "001110": "c",
    "001111": "d",
    "010000": "e",
    "010001": "f",
    "010010": "g",
    "010011": "h",
    "010100": "i",
    "010101": "j",
    "010110": "k",
    "010111": "l",
    "011000": "m",
    "011001": "n",
    "011010": "o",
    "011011": "p",
    "011100": "q",
    "011101": "r",
    "011110": "s",
    "011111": "t",
    "100000": "u",
    "100001": "v",
    "100010": "w",
    "100011": "x",
    "100100": "y",
    "100101": "z",
    "100110": "A",
    "100111": "B",
    "101000": "C",
    "101001": "D",
    "101010": "E",
    "101011": "F",
    "101100": "G",
    "101101": "H",
    "101110": "I",
    "101111": "J",
    "110000": "K",
    "110001": "L",
    "110010": "M",
    "110011": "N",
    "110100": "O",
    "110101": "P",
    "110110": "Q",
    "110111": "R",
    "111000": "S",
    "111001": "T",
    "111010": "U",
    "111011": "V",
    "111100": "W",
    "111101": "X",
    "111110": "Y",
    "111111": "Z",
}


def encode(string):
    s = ""
    for i in string:
        s += bin(ord(i))[2:].zfill(8)
    
    pad = ""
    if len(s) % 6 == 4:
        pad = "="
        s += "11"
    elif len(s) % 6 == 2:
        pad = "=="
        s += "1111"
    
    ret = ""
    for i in range(0,len(s),6):
        ret += b64[s[i:i+6]]
    return ret+pad

from secret import FLAG
print(encode(FLAG))
# gObheRHIpN+wlQ7vqQiQb3XzpAbJn4iv6lR=
```
- Đây là một bài sử dụng một thuật toán base64 encode custom
  + Đầu tiên chương trình sẽ lấy từng kí tự của input và biến chúng thành dạng binary tương ứng và gắn các string binary đấy lại với nhau
  + Sau đó để đảm bảo độ dài của binary string là bội của 6 thì chương trình sẽ pad `=` (`11` nếu như đấy là string binary) vào cuối chuỗi base64_encoded nếu modulo với 6 của độ dài string là 4. Pad `==` (`1111` nếu như đấy là string binary) vào cuối chuỗi base64_encoded nếu modulo với 6 của độ dài string là 2
  + Chương trình sẽ tra bảng `b64` với 6 bit một để tạo ra char tương ứng, concat chúng với nhau rồi pad `=` hoặc `==` và in ra chuỗi đã được encode

- Vậy để viết thuật toán giải mã, ta sẽ làm như sau
  + Đảo ngược lại cách tra bảng `b64` (ban đầu ta tra binary to char thì bây giờ ta sẽ tra char to binary)
  + Bỏ các kí tự `=` và `==` có trong string bị encode và xóa số bit tương ứng với 2 ki tự này
  + Biến các kí tự có trong string bị encode về dạng binary (bằng cách tra bảng `b64`)
  + Biến đổi 8 bit một về các kí tự ASCII tương ứng

- Dưới đây là script decode của mình
```python
b64 = {
    "000000": "/",
    "000001": "+",
    "000010": "0",
    "000011": "1",
    "000100": "2",
    "000101": "3",
    "000110": "4",
    "000111": "5",
    "001000": "6",
    "001001": "7",
    "001010": "8",
    "001011": "9",
    "001100": "a",
    "001101": "b",
    "001110": "c",
    "001111": "d",
    "010000": "e",
    "010001": "f",
    "010010": "g",
    "010011": "h",
    "010100": "i",
    "010101": "j",
    "010110": "k",
    "010111": "l",
    "011000": "m",
    "011001": "n",
    "011010": "o",
    "011011": "p",
    "011100": "q",
    "011101": "r",
    "011110": "s",
    "011111": "t",
    "100000": "u",
    "100001": "v",
    "100010": "w",
    "100011": "x",
    "100100": "y",
    "100101": "z",
    "100110": "A",
    "100111": "B",
    "101000": "C",
    "101001": "D",
    "101010": "E",
    "101011": "F",
    "101100": "G",
    "101101": "H",
    "101110": "I",
    "101111": "J",
    "110000": "K",
    "110001": "L",
    "110010": "M",
    "110011": "N",
    "110100": "O",
    "110101": "P",
    "110110": "Q",
    "110111": "R",
    "111000": "S",
    "111001": "T",
    "111010": "U",
    "111011": "V",
    "111100": "W",
    "111101": "X",
    "111110": "Y",
    "111111": "Z",
}
b64_reverse = {v: k for k, v in b64.items()}

def decode(encoded_string):

    padding = encoded_string.count("=")
    encoded_string = encoded_string.rstrip("=")
    
    binary_string = ""
    
    for char in encoded_string:
        binary_string += b64_reverse[char]

    if padding == 1:
        binary_string = binary_string[:-2]  
    elif padding == 2:
        binary_string = binary_string[:-4]  
  
    decoded_string = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        decoded_string += chr(int(byte, 2))

    return decoded_string

encoded_flag = "gObheRHIpN+wlQ7vqQiQb3XzpAbJn4iv6lR="
print(decode(encoded_flag))

```
**Flag:** `KCSC{no0b_base64_encode!!}`
