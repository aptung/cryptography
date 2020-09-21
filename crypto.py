# Caesar Cipher
# Arguments: string, integer
# Returns: string
# 'A' = 65
# 'Z' = 90
# Ord returns the integer representing the character
def encrypt_caesar(plaintext, offset):
    encrypted_text = ""
    for char in plaintext:
        encrypted_text = encrypted_text + shift_character(char, offset)
    return encrypted_text

def shift_character(char, offset):
    return chr((ord(char)+offset-65)%26 + 65)

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    return encrypt_caesar(ciphertext, (-offset)%26)


# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    print(decrypt_caesar(encrypt_caesar("TESTTESTABCDEF", 3565), 3565))

if __name__ == "__main__":
    main()
