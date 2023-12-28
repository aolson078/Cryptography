# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
# This file contains the encrypt/decrypt functions
# Imported by block_mode | Imports aes128
from aes128 import AES


# Encrypt takes plaintext input as a length 4 2d list with 4 bytes each
def encrypt(plaintext, key):

	aes = AES(plaintext)  # Initialize the AES object with the clear text

	subkeys = aes.generate_subkeys(key)  # Generate subkeys for each round from original key

	# Initial key addition
	aes.state = aes.add_round_key(subkeys[0])

	for i in range(9):
		aes.sbox()  # replaces each byte in state with a corresponding byte from a nonlinear substitution table (S-box).
		aes.shift_rows()  # Shift rows to the left. Second row shifts once, third row twice, and fourth row three times
		aes.mix_columns()  # Mix columns with galois multiplication specified in AES algorithm

		aes.state = aes.add_round_key(subkeys[i + 1]) # Add the round key for the current round to the state

	aes.sbox()
	aes.shift_rows()
	aes.state = aes.add_round_key(subkeys[-1])

	return aes.state


def decrypt(ciphertext, key):
	aes = AES(ciphertext)   # Initialize the AES object with the ciphertext

	subkeys = aes.generate_subkeys(key)  # Generate subkeys for each round from original key
	aes.state = aes.add_round_key(subkeys[-1])
	aes.inv_shift_rows()
	aes.inv_sbox()

	for i in range(9, 0, -1):
		aes.state = aes.add_round_key(subkeys[i])
		aes.inv_mix_columns()
		aes.inv_shift_rows()
		aes.inv_sbox()

	aes.state = aes.add_round_key(subkeys[0])  # Add the first round key to the state

	return aes.state
