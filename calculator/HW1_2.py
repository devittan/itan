def encrypt(plaintext, key, mod):
  """Encrypts a plaintext string using a matrix key and modular arithmetic.

  Args:
    plaintext: The string to encrypt.
    key: The matrix key to use for encryption.
    mod: The modulo to use for modular arithmetic.

  Returns:
    The encrypted ciphertext.
  """

  # Convert the plaintext characters to numbers (0-27)
  numbers = [ord(c) - ord('A') for c in plaintext] + [26, 27]

  # Encrypt the numbers using matrix multiplication and modular arithmetic
  ciphertext = []
  for i in range(0, len(numbers), len(key[0])):
    row = numbers[i:i+len(key[0])]
    encrypted_row = [(a * b) % mod for a, b in zip(row, key[0])]
    ciphertext.extend(encrypted_row)

  return ciphertext

def decrypt(ciphertext, key_inv, mod):
  """Decrypts a ciphertext using the inverse of the matrix key and modular arithmetic.

  Args:
    ciphertext: The ciphertext to decrypt.
    key_inv: The inverse of the matrix key.
    mod: The modulo to use for modular arithmetic.

  Returns:
    The decrypted plaintext.
  """

  # Decrypt the numbers using matrix multiplication and modular arithmetic
  plaintext = []
  for i in range(0, len(ciphertext), len(key_inv[0])):
    row = ciphertext[i:i+len(key_inv[0])]
    decrypted_row = [(a * b) % mod for a, b in zip(row, key_inv[0])]
    plaintext.extend(decrypted_row)

  # Convert the numbers back to characters
  return ''.join([chr(c + ord('A')) for c in plaintext])

# Input plaintext
plaintext = "CAMPBELL"

# Key and modulo
key = [[13, 24], [7, 5], [6, 8], [2, 4], [3, 5], [9, 6], [3, 1]]
mod = 29

# Encrypt the plaintext
ciphertext = encrypt(plaintext, key, mod)
print("Ciphertext:", ciphertext)

# Compute the inverse of the key
key_inv = []

# Replace this with your code to compute the inverse of the key (key_inv)

# Decrypt the ciphertext
decrypted_plaintext = decrypt(ciphertext, key_inv, mod)
print("Decrypted plaintext:", decrypted_plaintext)