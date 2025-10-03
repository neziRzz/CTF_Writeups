from Crypto.Cipher import AES
import os

# Input file
in_path = "Important_Note.txt"

with open(in_path, "rb") as f:
    blob = f.read()

ciphertext = blob[:-48]
key = blob[-48:-16]
iv = blob[-16:]

print("File size:", len(blob))
print("Ciphertext size:", len(ciphertext))
print("Key size:", len(key))
print("IV size:", len(iv))


cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(ciphertext)

print("Decrypted size:", len(decrypted))

out_path = os.path.splitext(in_path)[0] + "_decrypted.bin"
with open(out_path, "wb") as f:
    f.write(decrypted)

print(f"Decrypted file written to: {out_path}")
