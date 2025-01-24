# 1. frog
## Mics
- Given a PE32 executable built with Python and a Python source

![image](https://github.com/user-attachments/assets/00ab4f42-9ef5-441c-8aa4-aff15de100e1)

## Detailed Analysis
- The goal is to get to the statue and win, but the paths are blocked

![image](https://github.com/user-attachments/assets/109d9d4e-36ed-46bb-939c-708136433817)

- Since we already have source code, we can just analyze it instead, take a close look at the `GenerateFlagText` function

```python
def GenerateFlagText(x, y):
    key = x + y*20
    encoded = "\xa5\xb7\xbe\xb1\xbd\xbf\xb7\x8d\xa6\xbd\x8d\xe3\xe3\x92\xb4\xbe\xb3\xa0\xb7\xff\xbd\xbc\xfc\xb1\xbd\xbf"
    return ''.join([chr(ord(c) ^ key) for c in encoded])
```
- This function generate decryption key using the player's current coordinate with the following formula `x + y*20`, then use it as the xor key 
- We also know the winning condition is `x = 10` and `y = 10`

![image](https://github.com/user-attachments/assets/7c6f02ec-b5bb-4148-befc-1ad96cbe7c66)

- With this, we can easily write a solve script (At the time i solve this, i was kinda lazy so i solved it by brute-forcing the key instead)
## Script and Flag
```python
encoded = "\xa5\xb7\xbe\xb1\xbd\xbf\xb7\x8d\xa6\xbd\x8d\xe3\xe3\x92\xb4\xbe\xb3\xa0\xb7\xff\xbd\xbc\xfc\xb1\xbd\xbf"
flag = ""
for i in range(801):
    for j in range(601):
        key = i +j*20
        flag = ''.join([chr(ord(c) ^ key) for c in encoded])
        if(flag[:-14:-1][::-1] == "@flare-on.com"):
            print(i,j)
            print(flag)
            exit()
        else:
            flag = ''
            continue
```
**Flag:** `welcome_to_11@flare-on.com`
# 2. Checksum
## Mics
- Given a PE64 executable built with Go

![image](https://github.com/user-attachments/assets/645769ac-e026-45f4-86f8-0f6a0bc91811)

## Detailed Analysis
- 
