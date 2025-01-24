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
- Luckily, the symbols are not stripped, in case they are you can use [this](https://github.com/mandiant/GoReSym) tool to recover them 

![image](https://github.com/user-attachments/assets/949ef992-0f60-4531-b731-a5766a6754ba)

- `main_main` function
```C
// main.main
// local variable allocation has failed, the output may be wrong!
void __fastcall main_main()
{
  // [COLLAPSED LOCAL DECLARATIONS. PRESS KEYPAD CTRL-"+" TO EXPAND]

  while ( (unsigned __int64)&v218 <= *(_QWORD *)(v5 + 16) )
    runtime_morestack_noctxt();
  v231 = math_rand_v2__ptr_Rand_uint64n((_DWORD)math_rand_v2_globalRand, 5, v0, v1, v2, v3, v4);
  p_int = (int *)runtime_newobject(&RTYPE_int);
  for ( i = 0LL; ; i = v223 + 1 )
  {
    v16 = v231 + 3;
    if ( i >= v231 + 3 )
      break;
    v223 = i;
    v230 = math_rand_v2__ptr_Rand_uint64n((_DWORD)math_rand_v2_globalRand, 10000, i, v1, v16, v7, v8);
    v229 = math_rand_v2__ptr_Rand_uint64n(
             (_DWORD)math_rand_v2_globalRand,
             10000,
             (_DWORD)math_rand_v2_globalRand,
             v1,
             v16,
             v17,
             v18);
    v244 = v6;
    v245 = v6;
    v24 = runtime_convT64(v230, 10000, v19, v1, v16, v20, v21, v22, v23, v145);
    *(_QWORD *)&v244 = &RTYPE_int;
    *((_QWORD *)&v244 + 1) = v24;
    v29 = runtime_convT64(v229, 10000, (unsigned int)&RTYPE_int, v1, v16, v25, v26, v27, v28, v146);
    *(_QWORD *)&v245 = &RTYPE_int;
    *((_QWORD *)&v245 + 1) = v29;
    v228 = v230 + v229;
    fmt_Fprintf(
      (unsigned int)go_itab__os_File_io_Writer,
      os_Stdout,
      (unsigned int)"Check sum: %d + %d = ",
      21,
      (unsigned int)&v244,
      2,
      2,
      v30,
      v31,
      v147,
      v166,
      v185,
      v201,
      v208,
      v213,
      v216);
    v243[0] = &RTYPE__ptr_int;
    v243[1] = p_int;
    v32 = os_Stdin;
    fmt_Fscanf(
      (unsigned int)go_itab__os_File_io_Reader,
      os_Stdin,
      (unsigned int)"%d\n%s\nnil01_\\\\?adxaesshaavxfmaEOF m=125625nanNaNintmapptr...finobjgc %: gp  *(in  n= )\n -   P  MPC= < end > ]:\n???pc=  Gopenread",
      3,
      (unsigned int)v243,
      1,
      1,
      v33,
      v34,
      v148,
      v167,
      v186,
      v199,
      v202,
      v206,
      v209,
      v211,
      v214,
      v215,
      v216);
    v1 = 21;
    v40 = main_b(
            v32,
            v35,
            (unsigned int)"Not a valid answer...",
            21,
            (unsigned int)v243,
            v36,
            v37,
            v38,
            v39,
            v149,
            v168,
            v187);
    if ( *(_QWORD *)p_int != v228 )
    {
      runtime_printlock(v40);
      v46 = runtime_printstring(
              (unsigned int)"Try again! ;)\nis a directoryunexpected EOFinvalid syntax1907348632812595367431640625unsafe.Pointer on zero Valueunknown methodOpenSCManagerWModule32FirstWuserArenaStateread mem statsallocfreetracegcstoptheworldGC assist waitfinalizer waitsync.Cond.Waits.allocCount= nil elem type! to finalizer GC worker initruntime: full=runtime: want=MB; allocated timeEndPeriod",
              14,
              v41,
              21,
              (unsigned int)v243,
              v42,
              v43,
              v44,
              v45,
              v150,
              v169);
      runtime_printunlock(v46);
      return;
    }
    runtime_printlock(v40);
    v15 = runtime_printstring(
            (unsigned int)"Good math!!!\n------------------------------\n",
            44,
            v10,
            21,
            (unsigned int)v243,
            v11,
            v12,
            v13,
            v14,
            v150,
            v169);
    runtime_printunlock(v15);
  }
  p_string = (string *)runtime_newobject(&RTYPE_string);
  p_string->ptr = 0LL;
  v242[0] = &RTYPE_string;
  v242[1] = &off_4EDAB0;
  fmt_Fprint(
    (unsigned int)go_itab__os_File_io_Writer,
    os_Stdout,
    (unsigned int)v242,
    1,
    1,
    v47,
    v48,
    v49,
    v50,
    v145,
    v166,
    v185,
    v201,
    v208);
  v241[0] = &RTYPE__ptr_string;
  v241[1] = p_string;
  v51 = os_Stdin;
  fmt_Fscanf(
    (unsigned int)go_itab__os_File_io_Reader,
    os_Stdin,
    (unsigned int)"%s\nnil01_\\\\?adxaesshaavxfmaEOF m=125625nanNaNintmapptr...finobjgc %: gp  *(in  n= )\n -   P  MPC= < end > ]:\n???pc=  Gopenread",
    3,
    (unsigned int)v241,
    1,
    1,
    v52,
    v53,
    v151,
    v170,
    v188,
    v200,
    v203,
    v207,
    v210,
    v212,
    v213,
    HIDWORD(v213),
    v216);
  main_b(
    v51,
    v54,
    (unsigned int)"Fail to read checksum input...",
    30,
    (unsigned int)v241,
    v55,
    v56,
    v57,
    v58,
    v152,
    v171,
    v189);
  ptr = p_string->ptr;
  v234 = (chacha20poly1305_xchacha20poly1305 *)runtime_stringtoslicebyte(
                                                 (unsigned int)&v219,
                                                 p_string->ptr,
                                                 p_string->len,
                                                 30,
                                                 (unsigned int)v241,
                                                 v60,
                                                 v61,
                                                 v62,
                                                 v63,
                                                 v153,
                                                 v172,
                                                 v190);
  v221 = v64;
  v68 = encoding_hex_Decode(
          (_DWORD)v234,
          (_DWORD)ptr,
          v64,
          (_DWORD)v234,
          (_DWORD)ptr,
          v64,
          v65,
          v66,
          v67,
          v154,
          v173,
          v191,
          v204);
  if ( v68 > v221 )
    runtime_panicSliceAcap(v68, ptr, v68);
  v222 = v68;
  main_b(
    (_DWORD)ptr,
    v69,
    (unsigned int)"Not a valid checksum...",
    23,
    (_DWORD)ptr,
    v70,
    v71,
    v72,
    v73,
    v155,
    v174,
    v192);
  v78 = runtime_makeslice((unsigned int)&RTYPE_uint8, 24, 24, 23, (_DWORD)ptr, v74, v75, v76, v77, v156, v175, v193);
  v83 = v222;
  v84 = v234;
  for ( j = 0LL; v83 > (__int64)j; ++j )
  {
    v79 = v84->key[j];
    if ( j == 24 )
      break;
    if ( j >= 0x18 )
      runtime_panicIndex(j, 24LL, 24LL, 23LL);
    *(_BYTE *)(v78 + j) = v79;
  }
  v237.cap = v78;
  if ( v83 == 32 )
  {
    p_chacha20poly1305_xchacha20poly1305 = (chacha20poly1305_xchacha20poly1305 *)runtime_newobject(&RTYPE_chacha20poly1305_xchacha20poly1305);
    if ( p_chacha20poly1305_xchacha20poly1305 != v234 )
    {
      v235 = p_chacha20poly1305_xchacha20poly1305;
      runtime_memmove(p_chacha20poly1305_xchacha20poly1305, v234, 32LL, 23LL, v84);
      p_chacha20poly1305_xchacha20poly1305 = v235;
    }
    v86 = go_itab__golang_org_x_crypto_chacha20poly1305_xchacha20poly1305_crypto_cipher_AEAD;
    LODWORD(v87) = 0;
    v88 = p_chacha20poly1305_xchacha20poly1305;
    LODWORD(v89) = 0;
  }
  else
  {
    v240[1] = 32LL;
    v240[0] = "chacha20poly1305: bad key length";
    v86 = 0LL;
    v87 = go_itab__errors_errorString_error;
    v88 = 0LL;
    v89 = v240;
  }
  v233 = v88;
  v220 = v86;
  main_b(
    (_DWORD)v87,
    (_DWORD)v89,
    (unsigned int)"Maybe it's time to analyze the binary! ;)",
    41,
    (_DWORD)v89,
    v79,
    v80,
    v81,
    v82,
    v157,
    v176,
    v194);
  v158 = main_encryptedFlagData;
  v177 = qword_59A4F8;
  v195 = qword_59A500;
  *(_OWORD *)&v196[8] = v6;
  cap = v237.cap;
  v237.ptr = (uint8 *)((__int64 (__golang *)(chacha20poly1305_xchacha20poly1305 *, _QWORD, _QWORD, _QWORD, size_t, __int64, __int64))v220[4])(
                        v233,
                        0LL,
                        0LL,
                        0LL,
                        v237.cap,
                        24LL,
                        24LL);
  *(_QWORD *)v225 = 0LL;
  *(_QWORD *)v226 = v92;
  main_b(
    0,
    cap,
    (unsigned int)"Maybe it's time to analyze the binary! ;)",
    41,
    cap,
    v93,
    v94,
    v95,
    v96,
    (__int64)v158,
    v177,
    v195);
  *(_OWORD *)v232.h = v6;
  ((void (__fastcall *)(__int64 *))loc_463086)(&v231);
  crypto_sha256__ptr_digest_Reset(&v232);
  v248.ptr = v237.ptr;
  v248.len = *(_QWORD *)v225;
  v248.cap = *(_QWORD *)v226;
  crypto_sha256__ptr_digest_Write(&v232, v248);
  v248.ptr = 0LL;
  v248.len = 0LL;
  v97 = 0LL;
  v248 = crypto_sha256__ptr_digest_Sum(&v232, *(_slice_uint8 *)(&v97 - 2));
  v224 = v248.ptr;
  v236 = v98;
  v228 = 2 * (__int64)v248.ptr;
  v103 = runtime_makeslice(
           (unsigned int)&RTYPE_uint8,
           2 * LODWORD(v248.ptr),
           2 * LODWORD(v248.ptr),
           0,
           cap,
           v99,
           v100,
           v101,
           v102,
           v159,
           v178,
           *(__int64 *)v196);
  v107 = v224;
  v108 = v228;
  v109 = v236;
  v110 = 0LL;
  v111 = 0LL;
  while ( (__int64)v107 > v110 )
  {
    v112 = *(_BYTE *)(v109 + v110);
    v105 = "0123456789abcdef";
    v113 = (unsigned __int8)a0123456789abcd[v112 >> 4];
    if ( v111 >= v108 )
      runtime_panicIndex(v111, v111, v108, v113);
    *(_BYTE *)(v103 + v111) = v113;
    v97 = v111 + 1;
    v104 = (unsigned __int8)a0123456789abcd[v112 & 0xF];
    if ( v108 <= v111 + 1 )
      runtime_panicIndex(v111 + 1, v111, v108, v97);
    *(_BYTE *)(v111 + v103 + 1) = v104;
    ++v110;
    v111 += 2LL;
  }
  len = v103;
  v115 = runtime_slicebytetostring(
           (unsigned int)&v217,
           v103,
           v108,
           v97,
           v108,
           v109,
           v104,
           (_DWORD)v105,
           v106,
           v160,
           v179,
           *(__int64 *)v196);
  if ( len == p_string->len )
  {
    len = (__int64)p_string->ptr;
    if ( (unsigned __int8)runtime_memequal(v115, p_string->ptr) )
    {
      len = p_string->len;
      v119 = main_a(p_string->ptr, len, (_DWORD)p_string, v97, v108, v120, v116, v117, v118, v161, v180);
    }
    else
    {
      v119 = 0;
    }
  }
  else
  {
    v119 = 0;
  }
  if ( !v119 )
  {
    v239[0] = &RTYPE_string;
    v239[1] = &off_4EDAC0;
    len = os_Stdout;
    LODWORD(v97) = 1;
    LODWORD(v108) = 1;
    fmt_Fprintln(
      (unsigned int)go_itab__os_File_io_Writer,
      os_Stdout,
      (unsigned int)v239,
      1,
      1,
      (unsigned int)&off_4EDAC0,
      v116,
      v117,
      v118,
      v161,
      v180,
      *(__int64 *)v196,
      v6);
  }
  v237.len = os_UserCacheDir();
  v227 = len;
  main_b(v121, v97, (unsigned int)"Fail to get path...", 19, v108, v122, v123, v124, v125, v161, v180, *(__int64 *)v196);
  v126 = v237.len;
  v131 = runtime_concatstring2(
           0,
           v237.len,
           v227,
           (unsigned int)"\\REAL_FLAREON_FLAG.JPG",
           22,
           v127,
           v128,
           v129,
           v130,
           v162,
           v181,
           *(__int64 *)v196,
           *(__int64 *)&v196[8]);
  v132 = v226[0];
  v136 = os_WriteFile(
           v131,
           v126,
           (int)v237.ptr,
           v225[0],
           v226[0],
           420,
           v133,
           v134,
           v135,
           v163,
           v182,
           *(_slice_uint8 *)v196,
           0);
  main_b(v136, v126, (unsigned int)"Fail to write file...", 21, v132, v137, v138, v139, v140, v164, v183, v197);
  v238[0] = &RTYPE_string;
  v238[1] = &off_4EDAD0;
  fmt_Fprintln(
    (unsigned int)go_itab__os_File_io_Writer,
    os_Stdout,
    (unsigned int)v238,
    1,
    1,
    v141,
    v142,
    v143,
    v144,
    v165,
    v184,
    v198,
    v205);
}
```
- Since this is Golang, the pseudocode is obnoxiously hard to read, to somewhat understand what the program is doing we will have to debug
- After some debugging, we can deduce the program functionality as following
  + First it generates two random numbers and users will have to calculate the sum of those numbers
  + After some calculation, we will have to enter some kind of `checksum` (with this clue we can at least guess that some kind of hashing algorithm will be used)
  + If the checksum is correct, the program will decrypt a file name `REAL_FLAREON_FLAG.JPG` and drop it into the `temp` directory of the operating system
 
- Now what we have to do is find where the checking is being done. After some digging, I came across a function called `main_a`
```C
// main.a
__int64 __golang main_a(void *a1, __int64 a2, __int64 a3, int a4, __int64 a5, int a6, int a7, int a8, int a9)
{
  __int64 v9; // r14
  __int64 v10; // rax
  const char *v11; // r8
  int v12; // r9d
  int v13; // r10d
  int v14; // r11d
  _BYTE *v16; // rdx
  __int64 i; // rbx
  _BYTE *v18; // rdi
  unsigned __int64 v19; // rax
  char v20; // dl
  __int64 v21; // rbx
  __int64 v22; // rax
  __int64 v24; // [rsp-20h] [rbp-28h]
  __int64 v25; // [rsp-18h] [rbp-20h]
  __int64 v26; // [rsp-10h] [rbp-18h]
  _BYTE *v27; // [rsp+0h] [rbp-8h]
  void *retaddr; // [rsp+10h] [rbp+8h] BYREF
  void *v30; // [rsp+18h] [rbp+10h]

  while ( (unsigned __int64)&retaddr <= *(_QWORD *)(v9 + 16) )
  {
    v30 = a1;
    runtime_morestack_noctxt();
    a1 = v30;
  }
  if ( !a1 )
    a1 = &runtime_noptrbss;
  v27 = a1;
  v10 = runtime_makeslice((unsigned int)&RTYPE_uint8, a2, a2, a4, a5, a6, a7, a8, a9);
  v16 = v27;
  for ( i = 0LL; a2 > i; ++i )
  {
    a5 = v10;
    v18 = v16;
    v19 = i - 11 * ((__int64)((unsigned __int128)(i * (__int128)0x5D1745D1745D1746LL) >> 64) >> 2);
    v20 = v16[i];
    if ( v19 >= 0xB )
      runtime_panicIndex(v19, i, 11LL, v18);
    v11 = "FlareOn2024bad verb '%0123456789_/dev/stdout/dev/stderrCloseHandleOpenProcessGetFileTypeshort write30517578125bad argSizemethodargs(reflect.SetProcessPrngMoveFileExWNetShareAddNetShareDeluserenv.dllassistQueuenetpollInitreflectOffsglobalAllocmSpanManualstart traceclobberfreegccheckmarkscheddetailcgocall nilunreachable s.nelems=   of size  runtime: p  ms clock,  nBSSRoots=runtime: P  exp.) for minTrigger=GOMEMLIMIT=bad m value, elemsize= freeindex= span.list=, npages = tracealloc( p->status= in status  idleprocs= gcwaiting= schedtick= timerslen= mallocing=bad timedivfloat64nan1float64nan2float64nan3float32nan2GOTRACEBACK) at entry+ (targetpc= , plugin: runtime: g : frame.sp=created by broken pipebad messagefile existsbad addressRegCloseKeyCreateFileWDeleteFileWExitProcessFreeLibrarySetFileTimeVirtualLockWSARecvFromclosesocketgetpeernamegetsocknamecrypt32.dllmswsock.dllsecur32.dllshell32.dlli/o timeoutavx512vnniwavx512vbmi2LocalAppDatashort buffer152587890625762939453125OpenServiceWRevertToSelfCreateEventWGetConsoleCPUnlockFileExVirtualQueryadvapi32.dlliphlpapi.dllkernel32.dllnetapi32.dllsweepWaiterstraceStringsspanSetSpinemspanSpecialgcBitsArenasmheapSpecialgcpacertracemadvdontneedharddecommitdumping heapchan receivelfstack.push span.limit= span.state=bad flushGen MB stacks, worker mode  nDataRoots= nSpanRoots= wbuf1=<nil> wbuf2=<nil> gcscandone runtime: gp= found at *( s.elemsize= B (";
    v12 = (unsigned __int8)aTrueeeppfilepi[v19 + 3060];
    *(_BYTE *)(a5 + i) = v12 ^ v20;
    v10 = a5;
    v16 = v18;
  }
  v21 = v10;
  v22 = encoding_base64__ptr_Encoding_EncodeToString(
          runtime_bss,
          v10,
          a2,
          a2,
          a5,
          (_DWORD)v11,
          v12,
          v13,
          v14,
          v24,
          v25,
          v26);
  if ( v21 == 88 )
    return runtime_memequal(
             v22,
             "cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA==");
  else
    return 0LL;
}
```
- This function xor our checksum input with string `FlareOn2024` and then encode it with base64, then compare it to a hardcoded base64 string. With these clue, i wrote a script to find the original checksum value

```python
import base64
base64_string = "cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA=="
flare_on="FlareOn2024"
byte_data = base64.b64decode(base64_string)
byte_list = list(byte_data)
for i in range(len(byte_list)):
    byte_list[i]^=ord(flare_on[i%len(flare_on)])
for i in range(len(byte_list)):
    print(chr(byte_list[i]),end='')
```
- We got the checksum value as `7fd7dd1d0e959f74c133c13abb740b9faa61ab06bd0ecd177645e93b1e3825dd`

![image](https://github.com/user-attachments/assets/cb49152d-bc32-4fae-b3bb-8af155855f04)

- Find the decrypted file in the `temp` directory and open it

![image](https://github.com/user-attachments/assets/b4d07600-828e-469d-8cae-fb3a71690981)

## Script and Flag
**Flag:** `Th3_M4tH_Do_b3_mAth1ng@flare-on.com`

# 3. aray
## Mics
- Given a Yara rule
## Detailed Analysis

![image](https://github.com/user-attachments/assets/8c9abd33-7e56-47f8-84ce-67f3cf302928)

- This seems like a normal flag checker with some hashing conditions being used, also there are some unnecessary conditions like `>`, `<` and `!=`. We can use z3 to solve this, for some hashing conditions, we will need to write a different script to bruteforce the hash value.

- After filtering out some unnecessary conditions, we have a z3 script like this (not account for some hashing conditions)
```python
from z3 import *
s = Solver()
uint8 = [BitVec("x[%d]"%i,8)for i in range(85)] 
uint32_52 = Concat(uint8[55], uint8[54], uint8[53], uint8[52])
uint32_17 = Concat(uint8[20], uint8[19], uint8[18], uint8[17])
uint32_59 = Concat(uint8[62], uint8[61], uint8[60], uint8[59])
uint32_28 = Concat(uint8[31], uint8[30], uint8[29], uint8[28])
uint32_66 = Concat(uint8[69], uint8[68], uint8[67], uint8[66])
uint32_10 = Concat(uint8[13], uint8[12], uint8[11], uint8[10])
uint32_37 = Concat(uint8[40], uint8[39], uint8[38], uint8[37])
uint32_22 = Concat(uint8[25], uint8[24], uint8[23], uint8[22])
uint32_46 = Concat(uint8[49], uint8[48], uint8[47], uint8[46])
uint32_70 = Concat(uint8[73], uint8[72], uint8[71], uint8[70])
uint32_80 = Concat(uint8[83], uint8[82], uint8[81], uint8[80])
uint32_3 = Concat(uint8[6], uint8[5], uint8[4], uint8[3])
uint32_41 = Concat(uint8[44], uint8[43], uint8[42], uint8[41])
s.add(uint8[55] & 128 == 0 )
s.add(uint8[58] + 25 == 122 )
s.add(uint8[7] & 128 == 0 )
s.add(uint32_52 ^ 425706662 == 1495724241)
s.add(uint8[3] & 128 == 0)
s.add(uint8[56] & 128 == 0)
s.add(uint8[15] & 128 == 0)
s.add(uint8[54] & 128 == 0)
s.add(uint32_17 - 323157430 == 1412131772)
#hash.crc32(8, 2] == 0x61089c5c)
#hash.crc32(34, 2] == 0x5888fc1b)
s.add(uint8[36] + 4 == 72)
s.add(uint8[28] & 128 == 0)
s.add(uint8[48] & 128 == 0)
s.add(uint8[27] ^ 21 == 40)
s.add(uint8[16] & 128 == 0)
s.add(uint8[14] & 128 == 0)
s.add(uint32_59 ^ 512952669 == 1908304943)
s.add(uint8[65] - 29 == 70)
s.add(uint8[27] & 128 == 0)
s.add(uint8[73] & 128 == 0)
s.add(uint8[45] ^ 9 == 104)
s.add(uint8[45] & 128 == 0)
s.add(uint8[36] & 128 == 0)
s.add(uint8[10] & 128 == 0)
s.add(uint8[33] & 128 == 0)
s.add(uint32_28 - 419186860 == 959764852)
s.add(uint8[74] + 11 == 116)
#hash.crc32(63, 2] == 0x66715919)
s.add(uint8[43] & 128 == 0)
s.add(uint8[24] & 128 == 0)
s.add(uint8[78] & 128 == 0)
#hash.sha256(14, 2] == "403d5f23d149670348b147a15eeb7010914701a7e99aad2e43f90cfa0325c76f")
s.add(uint8[81] & 128 == 0)
s.add(uint8[60] & 128 == 0)
s.add(uint8[34] & 128 == 0)
s.add(uint8[21] & 128 == 0)
s.add(uint8[65] & 128 == 0)
s.add(uint8[57] & 128 == 0)
s.add(uint8[37] & 128 == 0)
s.add(uint8[67] & 128 == 0)
s.add(uint8[69] & 128 == 0)
s.add(uint8[18] & 128 == 0)
s.add(uint8[76] & 128 == 0)
s.add(uint8[68] & 128 == 0)
#hash.sha256(56, 2] == "593f2d04aab251f60c9e4b8bbc1e05a34e920980ec08351a18459b2bc7dbf2f6")
s.add(uint8[1] & 128 == 0)
s.add(uint8[38] & 128 == 0)
s.add(uint8[5] & 128 == 0)
s.add(uint8[75] - 30 == 86)
s.add(uint8[30] & 128 == 0)
s.add(uint32_66 ^ 310886682 == 849718389)
s.add(uint32_10 + 383041523 == 2448764514)
s.add(uint8[79] & 128 == 0)
s.add(uint8[61] & 128 == 0)
s.add(uint8[77] & 128 == 0)
s.add(uint8[13] & 128 == 0)
s.add(uint8[35] & 128 == 0)
s.add(uint8[59] & 128 == 0)
s.add(uint8[80] & 128 == 0)
s.add(uint8[23] & 128 == 0)
s.add(uint8[32] & 128 == 0)
s.add(uint32_37 + 367943707 == 1228527996)
s.add(uint8[29] & 128 == 0)
s.add(uint32_22 ^ 372102464 == 1879700858)
s.add(uint8[26] & 128 == 0)
s.add(uint8[0] & 128 == 0)
s.add(uint8[66] & 128 == 0)
s.add(uint8[71] & 128 == 0)
s.add(uint8[75] & 128 == 0)
s.add(uint8[2] + 11 == 119)
#hash.md5(0, 2] == "89484b14b36a8d5329426a3d944d2983")
s.add(uint32_46 - 412326611 == 1503714457)
#hash.crc32(78, 2] == 0x7cab8d64)
s.add(uint8[83] & 128 == 0)
s.add(uint8[9] & 128 == 0)
s.add(uint8[49] & 128 == 0)
s.add(uint8[62] & 128 == 0)
s.add(uint8[4] & 128 == 0)
s.add(uint8[72] & 128 == 0)
s.add(uint8[53] & 128 == 0)
s.add(uint8[7] - 15 == 82)
s.add(uint32_70 + 349203301 == 2034162376)
s.add(uint8[25] & 128 == 0)
s.add(uint8[42] & 128 == 0)
#hash.md5(76, 2] == "f98ed07a4d5f50f7de1410d905f1477f")
s.add(uint8[44] & 128 == 0)
s.add(uint8[50] & 128 == 0)
s.add(uint8[22] & 128 == 0)
s.add(uint8[82] & 128 == 0)
s.add(uint32_80 - 473886976 == 69677856)
s.add(uint8[63] & 128 == 0)
s.add(uint8[8] & 128 == 0)
s.add(uint8[46] & 128 == 0)
s.add(uint32_3 ^ 298697263 == 2108416586)
s.add(uint8[21] - 21 == 94)
s.add(uint8[16] ^ 7 == 115)
s.add(uint8[47] & 128 == 0)
s.add(uint8[6] & 128 == 0)
s.add(uint32_41 + 404880684 == 1699114335)
s.add(uint8[70] & 128 == 0)
s.add(uint8[74] & 128 == 0)
s.add(uint8[51] & 128 == 0)
#hash.md5(50, 2] == "657dae0913ee12be6fb2a6f687aae1c7")
s.add(uint8[84] & 128 == 0)
s.add(uint8[26] - 7 == 25)
s.add(uint8[64] & 128 == 0)
s.add(uint8[12] & 128 == 0)
s.add(uint8[20] & 128 == 0)
s.add(uint8[17] & 128 == 0)
s.add(uint8[19] & 128 == 0)
s.add(uint8[58] & 128 == 0)
s.add(uint8[41] & 128 == 0)
#hash.md5(32, 2] == "738a656e8e8ec272ca17cd51e12f558b")
s.add(uint8[11] & 128 == 0)
s.add(uint8[40] & 128 == 0)
s.add(uint8[31] & 128 == 0)
s.add(uint8[2] & 128 == 0)
s.add(uint8[84] + 3 == 128)
s.add(uint8[39] & 128 == 0)
s.add(uint8[52] & 128 == 0)

if(s.check() == sat):
    print(s.model())
else:
    print("Failed")
```
- After bruteforcing the remaining hashing conditions, we got the flag

![image](https://github.com/user-attachments/assets/eabd8bfa-a4e6-45e1-a67f-9f0ec67d1d3e)

## Script and Flag
**Flag:** `1RuleADayK33p$Malw4r3Aw4y@flare-on.com`

# 4. FLARE Meme Maker 3000
## Mics
- Given a HTML template

![image](https://github.com/user-attachments/assets/4c224802-fb47-4ced-9d68-1d0c47deca92)

## Detailed Analysis
- As the name suggested, it is indeed a `Meme Maker`

![image](https://github.com/user-attachments/assets/4729bb2d-3843-41b1-a71c-a5fa32ca0439)

- Usually, you can find the `script` header when you try to inspect the HTML's source code, it is where the javascript code of the template is. Sadly, the javascript code is obfuscated

![image](https://github.com/user-attachments/assets/8a8c1c9b-38c1-4c00-b513-c7a89293aae1)

- To deobfuscate, i used [this](https://deobfuscate.relative.im/) website and find the flag validating function
```javascript
    function a0k() {
      const a = a0g.alt.split('/').pop();
      const b = a0l.textContent;
      const c = a0m.textContent;
      const d = a0n.textContent;
    
      var f =
        d[3] +
        'h' +
        a[10] +
        b[2] +
        a[3] +
        c[5] +
        c[c.length - 1] +
        '5' +
        a[3] +
        '4' +
        a[3] +
        c[2] +
        c[4] +
        c[3] +
        '3' +
        d[2] +
        a[3] +
        'j4' +
        a0c[1][2] +
        d[4] +
        '5' +
        c[2] +
        d[5] +
        '1' +
        c[11] +
        '7' +
        a0c[21][1] +
        b.replace(' ', '-') +
        a[11] +
        a0c[4].substring(12, 15);
    
      f = f.toLowerCase();
      alert(atob('Q29uZ3JhdHVsYXRpb25zISBIZXJlIHlvdSBnbzog') + f);
    }
      }
      const b = a0l.textContent,
        c = a0m.textContent,
        d = a0n.textContent
      if (
        a0c.indexOf(b) == 14 &&
        a0c.indexOf(c) == a0c.length - 1 &&
        a0c.indexOf(d) == 22
      ) {
        var e = new Date().getTime()
        while (new Date().getTime() < e + 3000) {}
        var f =
          d[3] +
          'h' +
          a[10] +
          b[2] +
          a[3] +
          c[5] +
          c[c.length - 1] +
          '5' +
          a[3] +
          '4' +
          a[3] +
          c[2] +
          c[4] +
          c[3] +
          '3' +
          d[2] +
          a[3] +
          'j4' +
          a0c[1][2] +
          d[4] +
          '5' +
          c[2] +
          d[5] +
          '1' +
          c[11] +
          '7' +
          a0c[21][1] +
          b.replace(' ', '-') +
          a[11] +
          a0c[4].substring(12, 15)
        f = f.toLowerCase()
        alert(atob('Q29uZ3JhdHVsYXRpb25zISBIZXJlIHlvdSBnbzog') + f)
      }
```
- This function will display the flag in an alert box if the meme's caption and image meet certain conditions. With the help of ChatGPT, it generated for me the solve script as following
```python
import base64
a0c = [
    'When you find a buffer overflow in legacy code',
    'Reverse Engineer',
    'When you decompile the obfuscated code and it makes perfect sense',
    'Me after a week of reverse engineering',
    'When your decompiler crashes',
    "It's not a bug, it's a feature",
    "Security 'Expert'",
    'AI',
    "That's great, but can you hack it?",
    'When your code compiles for the first time',
    "If it ain't broke, break it",
    "Reading someone else's code",
    'EDR',
    'This is fine',
    'FLARE On',
    "It's always DNS",
    'strings.exe',
    "Don't click on that.",
    'When you find the perfect 0-day exploit',
    'Security through obscurity',
    'Instant Coffee',
    'H@x0r',
    'Malware',
    '$1,000,000',
    'IDA Pro',
    'Security Expert',
]

a = "boy_friend0.jpg"
b = 'FLARE On'
c = 'Security Expert'
d = 'Malware'

def gen_string():

        f = (
            d[3] + 'h' + a[10] + b[2] + a[3] + c[5] + c[-1] + '5' + a[3] +
            '4' + a[3] + c[2] + c[4] + c[3] + '3' + d[2] + a[3] + 'j4' +
            a0c[1][2] + d[4] + '5' + c[2] + d[5] + '1' + c[11] + '7' +
            a0c[21][1] + b.replace(' ', '-') + a[11] + a0c[4][12:15]
        ).lower()

        message = base64.b64decode('Q29uZ3JhdHVsYXRpb25zISBIZXJlIHlvdSBnbzog').decode('utf-8')
        final_message = message + f

        print(final_message)
        
gen_string()

```
## Script and Flag
**Flag:** `wh0a_it5_4_cru3l_j4va5cr1p7@flare-on.com`

# 5. sshd
## Mics
- Given a container of a Linux server

 ![image](https://github.com/user-attachments/assets/8da3fe77-4b40-40c8-9998-3a1acd3044bb)

## Detailed Analysis
- We were given a hint that the server crashed and it is related to `sshd`. So i decided to find the `sshd` coredump (equivalent of memdump) in `/var/lib/systemd/coredump/` which is `sshd.core.93794.0.0.11.1725917676`

- Before loading the coredump in GDB, we need to either tell GDB where the is library located (not of your own system but of the given Linux server container) or use Docker to emulate the server
- In my case I use Docker with these commands
```bash
docker import '/home/kali/Desktop/ssh_container.tar' # this will generate a hash for the below command
```
```bash
sudo docker run --rm -it <hash> /bin/bash
```

- Load the coredump into GDB and use the `bt` command to identify where it crashed
```bash
root@1729c7775492:/sbin# gdb sshd /var/lib/systemd/coredump/sshd.core.93794.0.0.11.1725917676
```
![image](https://github.com/user-attachments/assets/7b5ae448-215b-4a0a-980f-2f1c349ea87c)

- It crashed in `liblzma.so.5`, which leads us to the infamous [CVE-2024-3094](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)
- According to [Wikipedia](https://en.wikipedia.org/wiki/XZ_Utils_backdoor#Mechanism), the compromised code is in `RSA_public_decrypt`
```C
__int64 __fastcall sub_9820(unsigned int a1, _DWORD *a2, __int64 a3, __int64 a4, unsigned int a5)
{
  const char *v9; // rsi
  void *v10; // rax
  void *v12; // rax
  void (*v13)(void); // [rsp+8h] [rbp-120h]
  char v14[200]; // [rsp+20h] [rbp-108h] BYREF
  unsigned __int64 v15; // [rsp+E8h] [rbp-40h]

  v15 = __readfsqword(0x28u);
  v9 = "RSA_public_decrypt";
  if ( !getuid() )
  {
    if ( *a2 == 0xC5407A48 )
    {
      chacha20_init(v14, a2 + 1, a2 + 9, 0LL);
      v12 = mmap(0LL, size, 7, 0x22, 0xFFFFFFFF, 0LL);
      v13 = (void (*)(void))memcpy(v12, &shellcode, size);
      chacha20_encrypt_decrypt(v14, v13, size);
      v13();
      chacha20_init(v14, a2 + 1, a2 + 9, 0LL);
      chacha20_encrypt_decrypt(v14, v13, size);
    }
    v9 = "RSA_public_decrypt ";
  }
  v10 = dlsym(0LL, v9);
  return ((__int64 (__fastcall *)(_QWORD, _DWORD *, __int64, __int64, _QWORD))v10)(a1, a2, a3, a4, a5);
}
``` 
- It use `ChaCha20` algorithm to decrypt the shellcode, then execute it. Now we will have to find key and nonce for `ChaCha20` to decrypt the shellcode. Luckily, we can trace back to the coredump file to find those. Since `ChaCha20` use the string `expand 32-byte k` as constant, we can just find that string in the hex editor

![image](https://github.com/user-attachments/assets/d6dacadd-0d69-49a2-9829-fc6be14bca01)

- Knowing that ChaCha20's state consist of a 32 bytes constant, 32 bytes key, 4 bytes counter and 12 bytes nonce we can a Python script to decrypt as following

```python
import struct

# ChaCha20 quarter-round function
def quarter_round(state, a, b, c, d):
    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    state[d] ^= state[a]
    state[d] = ((state[d] << 16) | (state[d] >> 16)) & 0xFFFFFFFF

    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    state[b] ^= state[c]
    state[b] = ((state[b] << 12) | (state[b] >> 20)) & 0xFFFFFFFF

    state[a] = (state[a] + state[b]) & 0xFFFFFFFF
    state[d] ^= state[a]
    state[d] = ((state[d] << 8) | (state[d] >> 24)) & 0xFFFFFFFF

    state[c] = (state[c] + state[d]) & 0xFFFFFFFF
    state[b] ^= state[c]
    state[b] = ((state[b] << 7) | (state[b] >> 25)) & 0xFFFFFFFF

# ChaCha20 block function
def chacha20_block(state):
    # Copy the state
    working_state = state[:]

    # Perform 20 rounds (10 column rounds + 10 diagonal rounds)
    for _ in range(10):
        # Column rounds
        quarter_round(working_state, 0, 4, 8, 12)
        quarter_round(working_state, 1, 5, 9, 13)
        quarter_round(working_state, 2, 6, 10, 14)
        quarter_round(working_state, 3, 7, 11, 15)

        # Diagonal rounds
        quarter_round(working_state, 0, 5, 10, 15)
        quarter_round(working_state, 1, 6, 11, 12)
        quarter_round(working_state, 2, 7, 8, 13)
        quarter_round(working_state, 3, 4, 9, 14)

    # Add the original state to the working state
    for i in range(16):
        working_state[i] = (working_state[i] + state[i]) & 0xFFFFFFFF

    # Serialize the state into bytes
    return b''.join(struct.pack("<I", word) for word in working_state)

# Custom state setup
constants = struct.unpack("<4I", b"expand 32-byte k")  # Constants
key = struct.unpack("<8I", bytes.fromhex(
    "943DF638A81813E2DE6318A507F9A0BA"
    "2DBB8A7BA63666D08D11A65EC914D66F"
))  # Key
nonce = struct.unpack("<3I", bytes.fromhex(
    "F236839F4DCD711A52862955"
))  # Nonce (split into 3 integers)
counter = 0  # Custom counter(KCSC)

# Initial state (combine constants, key, counter, and nonce)
initial_state = list(constants) + list(key) + [counter] + list(nonce)

# Decrypt ciphertext
def chacha20_decrypt(custom_state, ciphertext):
    plaintext = bytearray()
    for i in range(0, len(ciphertext), 64):
        # Generate block for current position
        block = chacha20_block(custom_state)
        custom_state[12] += 1  # Increment counter
        chunk = ciphertext[i:i + 64]
        plaintext.extend(a ^ b for a, b in zip(chunk, block))
    return plaintext

# Read ciphertext from file
with open("D:\\KCSC RE\\sshd (1)\\encrypted_payload", "rb") as file:
    ciphertext = file.read()

# Decrypt
plaintext = chacha20_decrypt(initial_state, ciphertext)

# Write the decrypted plaintext to a file
with open("D:\\KCSC RE\\sshd (1)\\decrypted_output.bin", "wb") as file:
    file.write(plaintext)

print("Decrypted text saved to 'decrypted_output.bin'")

```
- As expected, the result gave us a shellcode like program

![image](https://github.com/user-attachments/assets/320e31ad-e57f-4531-b732-993c7329caac)
![image](https://github.com/user-attachments/assets/5b4c0072-0ea3-48b7-8536-8c28bb9b4729)

- Open the string window, I noticed that instead of `expand 32-byte k`, the string is `expand 32-byte K`, this suggest that this shellcode may use a custom constant variation of `ChaCha20`

![image](https://github.com/user-attachments/assets/6a686dcc-2161-4403-8b33-8ac0b8c8476c)

- When we get to the main function of the shellcode, there are a bunch of syscalls
```C
__int64 __fastcall sub_DC2(__int64 a1, __int64 a2)
{
  __int64 v2; // rcx
  __int64 v3; // rcx
  char v5[32]; // [rsp+410h] [rbp-1278h] BYREF
  char v6[272]; // [rsp+430h] [rbp-1258h] BYREF
  char v7[4224]; // [rsp+540h] [rbp-1148h] BYREF
  unsigned int v8; // [rsp+15C4h] [rbp-C4h]

  LOWORD(a2) = 1337;
  sub_1A(a1, a2);
  __asm
  {
    syscall; Low latency system call
    syscall; Low latency system call
    syscall; Low latency system call
    syscall; Low latency system call
  }
  v6[61] = 0;
  __asm
  {
    syscall; Low latency system call
    syscall; Low latency system call
  }
  v8 = strlen(v7);
  chacha20_init((__int64)v6, (__int64)v5, 0i64);
  chacha20_encrypt_decrypt(v8, (__int64)v7);
  __asm
  {
    syscall; Low latency system call
    syscall; Low latency system call
  }
  sub_B(v2, v8, 0i64, 0i64);
  sub_8F(v3, 0i64);
  return 0i64;
}
```
- So instead of reading the assembly to know what those syscalls does, I wrote a shellcode loader in C and use `strace` to trace the loader instead

![image](https://github.com/user-attachments/assets/6bc8f629-b88d-4052-ac27-3aa234526250)

- This shellcode functionality can be roughly deduce as
  + Connect to `10.0.2.15` with port `1337`
  + Receive data from the above adress
  + Open a file and then send that file back
- Since the received data size is 32,12 and 4 respectively, It is mostly certain that those data will be used as key, nonce and counter for `ChaCha20`. What we will need to find next is the cyphertext. It is known that the shellcode was open a file, we can try and find a filename inside the coredump (txt)

![image](https://github.com/user-attachments/assets/6ca4d40e-562e-4559-a7ea-8e4d9443aae0)

- There are some wierd value right above the path to the file, my guess is that those values are related to `ChaCha20` somehow (key :8D EC 91 12 EB 76 0E DA 7C 7D 87 A4 43 27 1C 35 D9 E0 CB 87 89 93 B4 D9 04 AE F9 34 FA 21 66 D7, nonce:11 11 11 11 11 11 11 11 11 11 11 11), and as for the file, i guess that was the path to cyphertext and indeed there was a file name `flag.txt` there but lo and behold

```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
if only it were that easy......
```
