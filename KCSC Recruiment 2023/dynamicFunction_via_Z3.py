from z3 import *
dest = "44 93 51 42 24 45 2E 9B 01 99 7F 05 4D 47 25 43 A2 E2 3E AA 85 99 18 7E"
key = "reversing_is_pretty_cool"
b = bytes.fromhex(dest)
flag = [BitVec("x[%d]" %i,8) for i in range(len(b))]
temp=0
s = Solver()
for i in range(len(b)):
    s.add(flag[i]>=0x20)
    s.add(flag[i]<=0x7f)
for i in range(len(b)):
    temp = 16*(flag[i]%16)+flag[i]/16
    s.add(b[i] == temp ^ ord(key[i]))
if s.check() == unsat:
    print("Failed") 
else:
    print(s.model())   

