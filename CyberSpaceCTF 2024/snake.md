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
  + To find the value that we want to modify simply   

![image](https://github.com/user-attachments/assets/10925b6a-18dc-4b8b-a7bc-1c9f5f23a12f)

**Flag:** `CSCTF{Y0u_b34T_My_Sl1th3r_G4m3!}`
