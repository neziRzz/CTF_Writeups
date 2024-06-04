DiE cant identify the file

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/2ac8d99b-d68a-4d53-aa7e-10368fe32050)

Using HxD(Hex editor), we can see something strange at the last couple bytes of the file.

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/766aa259-72ff-4417-abd9-5b7842a1416c)

As the title and the challenge description suggested, we can see that the bytes of this program was reversed (The magic bytes are ELF in reverse)

After restore the original bytes we can see that the file is a ELF64 executable

![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/f2226c0f-1113-4a2e-b463-5378d8d19e87)

Put it in IDA (For ELF files, it is better to use Binary Ninja on a Linux machine so that we can debug and have an easier time reversing)
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/5ed61752-f681-440b-9467-6ae7447e582f)
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/13f6359d-3948-4e59-8b78-13e9ce7a3a0d)

We can fix the parameters name for easier analysis
![image](https://github.com/neziRzz/CTF_Writeups/assets/126742756/9a9e5f65-a24a-483b-91a2-6d03c33e4bcb)





