#KMACTF{32bit_heaven_crashed_into_64bit_hellish_syscalls}
import itertools
import string
ASCII_MIN, ASCII_MAX = 0x20, 0x7E

SBOX_INV = [
    0x52,0x09,0x6A,0xD5,0x30,0x36,0xA5,0x38,0xBF,0x40,0xA3,0x9E,0x81,0xF3,0xD7,0xFB,
    0x7C,0xE3,0x39,0x82,0x9B,0x2F,0xFF,0x87,0x34,0x8E,0x43,0x44,0xC4,0xDE,0xE9,0xCB,
    0x54,0x7B,0x94,0x32,0xA6,0xC2,0x23,0x3D,0xEE,0x4C,0x95,0x0B,0x42,0xFA,0xC3,0x4E,
    0x08,0x2E,0xA1,0x66,0x28,0xD9,0x24,0xB2,0x76,0x5B,0xA2,0x49,0x6D,0x8B,0xD1,0x25,
    0x72,0xF8,0xF6,0x64,0x86,0x68,0x98,0x16,0xD4,0xA4,0x5C,0xCC,0x5D,0x65,0xB6,0x92,
    0x6C,0x70,0x48,0x50,0xFD,0xED,0xB9,0xDA,0x5E,0x15,0x46,0x57,0xA7,0x8D,0x9D,0x84,
    0x90,0xD8,0xAB,0x00,0x8C,0xBC,0xD3,0x0A,0xF7,0xE4,0x58,0x05,0xB8,0xB3,0x45,0x06,
    0xD0,0x2C,0x1E,0x8F,0xCA,0x3F,0x0F,0x02,0xC1,0xAF,0xBD,0x03,0x01,0x13,0x8A,0x6B,
    0x3A,0x91,0x11,0x41,0x4F,0x67,0xDC,0xEA,0x97,0xF2,0xCF,0xCE,0xF0,0xB4,0xE6,0x73,
    0x96,0xAC,0x74,0x22,0xE7,0xAD,0x35,0x85,0xE2,0xF9,0x37,0xE8,0x1C,0x75,0xDF,0x6E,
    0x47,0xF1,0x1A,0x71,0x1D,0x29,0xC5,0x89,0x6F,0xB7,0x62,0x0E,0xAA,0x18,0xBE,0x1B,
    0xFC,0x56,0x3E,0x4B,0xC6,0xD2,0x79,0x20,0x9A,0xDB,0xC0,0xFE,0x78,0xCD,0x5A,0xF4,
    0x1F,0xDD,0xA8,0x33,0x88,0x07,0xC7,0x31,0xB1,0x12,0x10,0x59,0x27,0x80,0xEC,0x5F,
    0x60,0x51,0x7F,0xA9,0x19,0xB5,0x4A,0x0D,0x2D,0xE5,0x7A,0x9F,0x93,0xC9,0x9C,0xEF,
    0xA0,0xE0,0x3B,0x4D,0xAE,0x2A,0xF5,0xB0,0xC8,0xEB,0xBB,0x3C,0x83,0x53,0x99,0x61,
    0x17,0x2B,0x04,0x7E,0xBA,0x77,0xD6,0x26,0xE1,0x69,0x14,0x63,0x55,0x21,0x0C,0x7D
]
def has_repeating_pattern(b):
    n = len(b)
    if n == 0:
        return False

    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len != 0:
            continue  

        pattern = b[:pattern_len]
        if pattern * (n // pattern_len) == b:
            return True
    return False

def rol16(value: int, count: int) -> int:
    value &= 0xFFFF  
    count &= 0xF     
    return ((value << count) | (value >> (16 - count))) & 0xFFFF
def inv_shift_rows(state):
    out = [0]*16
    
    out[0],  out[4],  out[8],  out[12] = state[0],  state[4],  state[8],  state[12]
    
    out[1],  out[5],  out[9],  out[13] = state[13], state[1],  state[5],  state[9]

    out[2],  out[6],  out[10], out[14] = state[10], state[14], state[2],  state[6]

    out[3],  out[7],  out[11], out[15] = state[7],  state[11], state[15], state[3]
    return out
def inv_sub_bytes(state):
    return [SBOX_INV[b] for b in state]
def pxor(a,b):
    return [x^y for x,y in zip(a,b)]


def gf_mul(a, b):
    r = 0
    for _ in range(8):
        if b & 1:
            r ^= a
        carry = a & 0x80
        a = (a << 1) & 0xFF
        if carry:
            a ^= 0x1B
        b >>= 1
    return r

def inv_mix_column(col):
    return [
        gf_mul(col[0],0x0e) ^ gf_mul(col[1],0x0b) ^ gf_mul(col[2],0x0d) ^ gf_mul(col[3],0x09),
        gf_mul(col[0],0x09) ^ gf_mul(col[1],0x0e) ^ gf_mul(col[2],0x0b) ^ gf_mul(col[3],0x0d),
        gf_mul(col[0],0x0d) ^ gf_mul(col[1],0x09) ^ gf_mul(col[2],0x0e) ^ gf_mul(col[3],0x0b),
        gf_mul(col[0],0x0b) ^ gf_mul(col[1],0x0d) ^ gf_mul(col[2],0x09) ^ gf_mul(col[3],0x0e),
    ]
def aesimc(xmm):
    state = [
        [xmm[0], xmm[4], xmm[8],  xmm[12]],
        [xmm[1], xmm[5], xmm[9],  xmm[13]],
        [xmm[2], xmm[6], xmm[10], xmm[14]],
        [xmm[3], xmm[7], xmm[11], xmm[15]],
    ]
    out = [[0]*4 for _ in range(4)]
    for i in range(4):
        col = [state[0][i], state[1][i], state[2][i], state[3][i]]
        mixed = inv_mix_column(col)
        for j in range(4):
            out[j][i] = mixed[j]
    return [
        out[0][0], out[1][0], out[2][0], out[3][0],
        out[0][1], out[1][1], out[2][1], out[3][1],
        out[0][2], out[1][2], out[2][2], out[3][2],
        out[0][3], out[1][3], out[2][3], out[3][3],
    ]
def aesdec_round(xmm, roundkey):
    state = inv_sub_bytes(xmm)
    state = inv_shift_rows(state)
    state = aesimc(state) 
    state = pxor(state, roundkey)
    return state

def aesdeclast_round(xmm, roundkey):
    state = inv_sub_bytes(xmm)
    state = inv_shift_rows(state)
    state = pxor(state, roundkey)
    return state
def pslldq(x,n):
    return [0]*n + x[:16-n]

def psrldq(x,n):
    return x[n:] + [0]*n

def movd(val):
    return [(val>>i)&0xFF for i in (0,8,16,24)] + [0]*12

def pshufd(x, imm):
    return x[:4]*4

def build_xmm(val):
    return movd(val)

def inv_sub_bytes(state):
    return [SBOX_INV[b] for b in state]


def emulate_full(rsp_bytes, memory):
    rsp = list(rsp_bytes) + [0]*(0x42 - len(rsp_bytes))
    

    ax = rsp[0] | (rsp[1]<<8)
    bx = rsp[2] | (rsp[3]<<8)
    rsp[0x40] = bx & 0xFF
    rsp[0x41] = (bx>>8) & 0xFF

    xmm0 = pshufd(build_xmm(ax), 0)
    xmm1 = pslldq(xmm0, 2)
    xmm0 = pxor(xmm0, xmm1)
    xmm1 = pslldq(xmm1, 4)
    xmm0 = pxor(xmm0, xmm1)

    xmm2 = pshufd(build_xmm(0x9E3779B9),0)
    xmm5 = pxor(xmm0,xmm2)
    xmm3 = pshufd(build_xmm(0x7F4A7C15),0)
    xmm6 = psrldq(xmm0,1)
    xmm6 = pxor(xmm6,xmm3)
    xmm7 = pxor(xmm5,xmm6)
    xmm4 = aesimc(xmm6)


    dx = ax
    dx = rol16(dx,0x2) #each decrypt fix here
    ebx = (xmm7[0] | (xmm7[1]<<8) | (xmm7[2]<<16) | (xmm7[3]<<24)) & 0xFFFF
    if ebx != 0:
        ax ^= dx
        ax ^= ebx & 0xFFFF
        ax = (ax*0xa) & 0xFFFF #each decrypt fix here
    eax = (ax & 0x1FF) + 0x100


    rdi = 0
    rdi += eax
    rsi = rdi + 0x150
    ecx = 0x16  

 
    for _ in range(ecx):
        block = memory[rsi:rsi+16]
        block = pxor(block, xmm7)
        block = aesdec_round(block, xmm4)
        block = aesdeclast_round(block, xmm5)
        memory[rsi:rsi+16] = block
        rsi -= 0x10

    
    rsi = rdi + 0x15F
    ecx = 0x160
    rdx = 0
    decrypted = []
    for _ in range(ecx):
        al = memory[rsi]
        bl = rsp[2 + (_ % 2)]
        al ^= bl
        memory[rsi] = al
        decrypted.append(al)
        rsi -= 1
        rdx += 1
    return {
        "rsp": rsp[:0x42],
        "ax": ax,
        "eax": eax,
        "xmm4": xmm4,
        "xmm5": xmm5,
        "xmm6": xmm6,
        "xmm7": xmm7,
        "memory": memory,
        "rdi": rdi,
        "decrypted":list(reversed(decrypted))
    }



def is_ascii(b):
    return all(20 <= x <= 127 for x in b)

if __name__ =="__main__":
    charset = string.printable
    plaintext = bytes.fromhex("65 48 8B 04 25 60 00 00")  

    
    found = False
    for a, b in itertools.product(charset, repeat=2):
        memory = [] # each check fill with data from instruction lea rdx,unk.......
        rsp_input = [ord(a), ord(b), 0, 0] + [0]*0x3C
        res = emulate_full(rsp_input,memory)

        dec = res["decrypted"]
        if dec is None:
            continue

        if isinstance(dec, bytes):
            head = dec[:8]
        elif isinstance(dec, (list, tuple)):
            head = bytes(dec[:8])
        else:
            try:
                head = bytes(dec)[:8]
            except Exception:
                continue

        if len(head) < len(plaintext):
            continue

        mask = bytes([p ^ e for p, e in zip(plaintext, head)])

        if is_ascii(mask) and has_repeating_pattern(mask):
            found = True
            print("Key:", a+b)
            print("Mask:", mask.hex(' '), "ASCII:", mask.decode('ascii', 'ignore'))
            print("AX:", hex(res.get('ax', 0)))
            print("EAX:", hex(res.get('eax', 0)))
            print("RDI:", hex(res.get('rdi', 0)))
            break

    if not found:
        print("No alternating mask found.")
        
