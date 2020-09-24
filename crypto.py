import math
import random

ASCIIA = 65
ASCIIZ = 90

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted_text = ""
    for char in plaintext:
        if (ASCIIA<=ord(char)<=ASSCIIZ):
            encrypted_text = encrypted_text + shift_character(char, offset)
        else:
            encrypted_text = encrypted_text + char
    return encrypted_text

# Shifts one character char by an integer offset
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
    pos = 0 # Current position in the keyword which determines the shift
    shift = ord(keyword[pos]) - ASCIIA
    for char in plaintext:
        encrypted_string = encrypted_string + shift_character(char, shift)
        pos = (pos + 1) % len(keyword)
        shift = ord(keyword[pos]) - ASCIIA
    return encrypted_string

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypt_keyword = "" # Word that undoes the shifts of the original keyword
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
    r = generate_coprime_num(q)
    return (tuple(seq_w), q, r)

# Generates a number coprime to n by randomly trying numbers in [2, n-1]
def generate_coprime_num (n):
    x=0
    while math.gcd(n, x) != 1:
        x = random.randint(2, n-1)
    return x

# Generates a random superincreasing sequence
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

# Recursively converts a number to binary and returns an array of 0's and 1's
# e.g. 4 = [1, 0, 0]
# Split off from previous method because filling out 0's messes up the recursion
def num_to_binary (num):
    bits = []
    if num>1:
        bits = num_to_binary(num//2)
    bits.append(num%2)
    return bits

# Arguments: list of integers, private key (W, Q, R) with W a tuple
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    plaintext = ''
    for char in ciphertext:
        plaintext += chr(bits_to_byte(decrypt_char(char, private_key)))
    return plaintext

def decrypt_char (text, private_key):
    w_i = private_key[0]
    q = private_key[1]
    r = private_key[2]
    r_inverse = (r**(phi(q)-1)) % q # Computing the inverse using Euler's Theorem
    c_prime = text*r_inverse % q
    bits = []
    # Greedy algorithm
    # Note arraya is reversed because we pick larger values first
    for w in w_i[::-1]:
        if w<=c_prime:
            bits.append(1)
            c_prime = c_prime - w
        else:
            bits.append(0)
    # Note bits are reversed because values for larger w_i are determined first
    return bits[::-1]

# Euler totient function
def phi(n):
    result = 1
    for i in range(2,n):
        if math.gcd(i,n) == 1:
            result+=1
    return result

def main():
    # Testing code here
    private_key = generate_private_key()
    print(private_key)
    public_key = create_public_key(private_key)
    print(public_key)
    ciphertext = encrypt_mhkc('HERESASECRETMESSAGE', public_key)
    print(ciphertext)
    print(decrypt_mhkc(ciphertext, private_key))

if __name__ == "__main__":
    main()
