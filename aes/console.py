# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
from rich import print
from rich.console import Console
from rich.theme import Theme
from aes128 import AES

"""Console and Theme settings"""
custom_theme = Theme({"info": "bold cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)

KEY = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]


# Function takes 2d list (of size 1) as input and outputs string of hex values
def to_hex(string):
	output = ""
	for i in string:
		for j in i:
			if len(hex(j)[2::]) == 1:
				output += "0"
				output += (hex(j)[2::])
			else:
				output += (hex(j)[2::])
	return output


# Encrypt takes plaintext input as a length 4 2d list with 4 bytes each
def encrypt(plaintext):
	flat_plaintext = [item for row in plaintext for item in row]
	print("-------------------------------------------------------------------------------")
	print("Plaintext to encrypt:")
	print(flat_plaintext)
	print("-------------------------------------------------------------------------------")

	# Take user input in clear text for state
	aes = AES(plaintext)

	subkeys = aes.generate_subkeys(KEY)

	# Initial key addition
	aes.state = aes.add_round_key(subkeys[0])

	for i in range(9):
		# Byte Substitution layer
		aes.sbox()
		# Shift left second row once, third row twice, fourth row three times
		aes.shift_rows()
		# Mix columns with galois multiplication specified in AES algorithm
		aes.mix_columns()

		aes.state = aes.add_round_key(subkeys[i + 1])

	# replaces each byte in state with a corresponding byte from a nonlinear substitution table (S-box).
	# This step introduces non-linearity into the encryption process
	aes.sbox()
	aes.shift_rows()
	aes.state = aes.add_round_key(subkeys[-1])

	# Flatten 2d list to 1d
	flat_state = [item for row in aes.state for item in row]
	print("-------------------------------------------------------------------------------")
	print("Encrypted:")
	print(flat_state)
	print("-------------------------------------------------------------------------------")
	return aes.state


def decrypt(ciphertext):
	aes = AES(ciphertext)

	subkeys = aes.generate_subkeys(KEY)
	aes.state = aes.add_round_key(subkeys[-1])
	aes.inv_shift_rows()
	aes.inv_sbox()

	for i in range(9, 0, -1):
		aes.state = aes.add_round_key(subkeys[i])
		aes.inv_mix_columns()
		aes.inv_shift_rows()
		aes.inv_sbox()

	aes.state = aes.add_round_key(subkeys[0])
	flat_plaintext = [item for row in aes.state for item in row]
	print("-------------------------------------------------------------------------------")
	print("Decrypted:")
	print(flat_plaintext)
	print("-------------------------------------------------------------------------------")
	return aes.state


# Takes 2d list of cipher as input, outputs 1d list of hex values
def output_hex(cipher):
	output = []
	for i in cipher:
		for j in i:
			output.append(hex(j)[2:])
	return output


# Takes 16 bytes of input, returns it as a 4x4 2d list
def format_input(string):
	if len(string) != 16:
		raise ValueError("String must be exactly 16 bytes/chars")

	output = [[], [], [], []]
	for i in range(4):
		output[0].append(ord(string[i]))
	for i in range(4, 8):
		output[1].append(ord(string[i]))
	for i in range(8, 12):
		output[2].append(ord(string[i]))
	for i in range(12, 16):
		output[3].append(ord(string[i]))
	return output

def main():
	Console.print(("Please choose from the following menu: \n"
	               + "1: Run AES128 Encryption\n"
	               + "2: Run AES128 Decryption\n"
	               + "3: Exit Program\n"), style="info")

	choice = int(input())

	if choice == 1:
		print("!!!!!!!!!!")
		plaintext = console.format_input(input("Please enter a 16 byte plaintext as string to encrypt: "))
		console.encrypt(plaintext)

	if choice == 2:
		plaintext = input("Please enter ciphertext to decrypt: ")
		encrypted = console.encrypt(plaintext)
		print(to_hex(encrypted))
		print(to_hex(console.decrypt(encrypted)))


	elif choice == 3:
		exit()
