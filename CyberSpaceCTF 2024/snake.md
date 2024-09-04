- Given a ELF64 file

![image](https://github.com/user-attachments/assets/ca712c7d-7e25-4888-b2c5-5a91fbdcc7bf)


- As the title suggested, this is a game similar to `Snake Xenzia` on Nokia phones back in the 2000s 

![image](https://github.com/user-attachments/assets/1d50140a-fc2d-4fdb-b5d3-b5ca607bebba)

- Use WASD to move, for each `food` we eat, we gain 10 points, when we reach 16525 pts, we clear the game, but if we touch the outer border we lose

![image](https://github.com/user-attachments/assets/deb0d772-8b89-410b-a3aa-c345811532b8)

- When dealing with these types of games, it is rather troublesome to actually put it in a disassembler and reverse the game's algorithm instead we should load the game into a debugger (mem-scanner) like Cheat Engine(Windows) or Game Conqueror(Linux)
- For this challenge, we will use Game Counqueror ```$ sudo apt install gameconqueror```
- Game Counqueror interface

 ![image](https://github.com/user-attachments/assets/741e7b9f-13aa-4f73-8a47-17794dd07dd8)

- Using Game Conqueror is really simple:
  + First press `CTRL+F` to attach the debugger to a desired process (./snake)
  + To find the value that we want to modify simply enter that current value into the value field, for every time that value changes, simply update it inside Game Conqueror, Here is a example
  + Here our score is currently 0, we enter 0 into the value field
   
  ![image](https://github.com/user-attachments/assets/3936e4ec-88c3-4f20-b900-571d35625f5e)

  ![image](https://github.com/user-attachments/assets/0811719a-0ef0-4902-9d36-ca6cb2e29c85)

  + To change the score value, we will need to eat some foods
  
  ![image](https://github.com/user-attachments/assets/ef324faa-a724-4f7c-9536-44be585e6d2c)
  
  + Update the value accordingly in the debugger
 
  ![image](https://github.com/user-attachments/assets/3b1675b5-d990-461b-ab6b-e27756a6bc06)

  + However there are 4 `20` values, we just need to eat more food so that the debugger can eliminate the wrong ones
 
  ![image](https://github.com/user-attachments/assets/f54e06c4-ff8f-41e8-918a-8e3cc10c2278)

  + There are only 2 left, one of those is definitely the one we want (in this case it is `7ffc35fd1640`)
  
  + To change the value at that address, simply click on the value field (bottom) and change to our desired value

  ![image](https://github.com/user-attachments/assets/1a2f703f-078a-446a-b43b-439c5493f213)

  
![image](https://github.com/user-attachments/assets/10925b6a-18dc-4b8b-a7bc-1c9f5f23a12f)

**Flag:** `CSCTF{Y0u_b34T_My_Sl1th3r_G4m3!}`
