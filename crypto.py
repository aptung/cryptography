import math
import random

ASCIIA = 65
ASCIIZ = 90

# Caesar Cipher
# Arguments: string, integer
# Returns: string
# 'A' = 65
# 'Z' = 90
# Ord returns the integer representing the character
def encrypt_caesar(plaintext, offset):
    encrypted_text = ""
    for char in plaintext:
        if (ASCIIA<=ord(char)<=ASSCIIZ):
            encrypted_text = encrypted_text + shift_character(char, offset)
        else:
            encrypted_text = encrypted_text + char
    return encrypted_text

def shift_character(char, offset):
    return chr((ord(char)+offset-ASCIIA)%26 + ASCIIA)

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    return encrypt_caesar(ciphertext, (-offset)%26)


# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    encrypted_string = ""
    pos = 0
    shift = ord(keyword[pos]) - ASCIIA
    for char in plaintext:
        encrypted_string = encrypted_string + shift_character(char, shift)
        pos = (pos + 1) % len(keyword)
        shift = ord(keyword[pos]) - ASCIIA
    return encrypted_string

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypt_keyword = ""
    for char in keyword:
        if ord(char)==ASCIIA:
            decrypt_keyword = decrypt_keyword + char
        else:
            decrypt_keyword = decrypt_keyword + chr(2*ASCIIA + 26 - ord(char))
    return encrypt_vigenere(ciphertext, decrypt_keyword)

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    seq_w = generate_superincreasing_sequence(n+1)
    q = seq_w[n]
    del seq_w[n]
    print(q)
    r = generate_coprime_num(q)
    return (tuple(seq_w), q, r)


def generate_coprime_num (n):
    x=0
    while math.gcd(n, x) != 1:
        x = random.randint(2, n-1)
    return x

def generate_superincreasing_sequence (n):
    seq = [random.randint(1, 10)]
    while len(seq)<n:
        seq.append(random.randint(sum(seq)+1, 2*sum(seq)))
    return seq


# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    b = []
    w = private_key[0]
    q = private_key[1]
    r = private_key[2]
    for w in private_key[0]:
        b.append((r*w) % q)
    return tuple(b)

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    c = []
    for char in plaintext:
        bits = byte_to_bits(ord(char))
        total = 0
        index = 0
        for bit in bits:
            total = total + bit*public_key[index]
            index = index + 1
        c.append(total)
    return c

# Takes in an array of bits; returns a byte
def bits_to_byte (bits):
    total = 0
    for bit in bits:
        total = bit + 2*total
    return total

# Takes in a byte; returns an array of bits
def byte_to_bits (byte):
    bits = num_to_binary(byte)
    while len(bits)<8:
        bits.insert(0, 0)
    return bits

def num_to_binary (num):
    bits = []
    if num>1:
        bits = num_to_binary(num//2)
    bits.append(num%2)
    return bits

# Arguments: list of integers, private key (W, Q, R) with W a tuple
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    private = generate_private_key(8)
    print(private)
    public = create_public_key(private)
    print(public)
    print(encrypt_mhkc('ATTACKATDWAN', public))

if __name__ == "__main__":
    main()
