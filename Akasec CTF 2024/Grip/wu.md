ELF64 executable

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/ee97d947-2188-4df0-98b3-a8951aaa95ca)

Put in IDA

```python
cypher_header="#)#1\'!91"
cypher_body_end="2a7336363b1d3276212971261d20732c76303b3f"
b=bytes.fromhex(cypher_body_end)
for i in range(len(cypher_header)):
    print(chr(ord(cypher_header[i])^0x42),end='')
for i in range(len(b)):
    print(chr(b[i]^0x42),end='')
```
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/ad7e72c8-1867-4166-8d15-c22858b33d66)

**Flag:** `akasec{sh1tty_p4ck3d_b1n4ry}`
