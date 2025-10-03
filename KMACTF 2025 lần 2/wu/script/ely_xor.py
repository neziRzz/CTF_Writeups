import os

def decrypt_file(path):
    with open(path, "rb") as f:
        data = f.read()


    key = data[-40:]          
    cipher = data[:-40]       

    plain = bytearray(len(cipher))
    for i in range(len(cipher)):
        plain[i] = cipher[i] ^ key[i % len(key)]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "Important_Note_decrypted.txt")

    with open(output_path, "wb") as f:
        f.write(plain)

if __name__ == "__main__":
    input_path = r"D:\\KCSC RE\\kmactf_02\\Important_Note_decrypted.txt"
    decrypt_file(input_path)
