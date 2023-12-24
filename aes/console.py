# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
from encrypt import encrypt, decrypt
from block_mode import ecb
import ast
import re

KEY = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]

# Checks if value is in hex
def is_hexadecimal(s):
	return bool(re.fullmatch(r'[0-9a-fA-F]+', s))


# Takes 16 bytes of string input, returns it as a 4x4 2d list
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


# Takes 2d list of cipher as input, outputs string of hex values
def format_output(cipher):
	output = ""
	for i in cipher:
		for j in i:
			if len(hex(j)) == 4:
				output += (hex(j)[2:])
			else:
				output += "0"
				output += (hex(j)[2:])
	return output


def normalize_input_for_decrypt(cipher):
	if type(cipher) == str and len(cipher) == 32:
		cipher = [[int(cipher[i:i + 2], 16) for i in range(0, 32, 2)][j:j + 4] for j in range(0, 16, 4)]
	elif type(cipher) == str and len(cipher) > 32:
		cipher_list = ast.literal_eval(cipher)
		if type(cipher_list) == tuple:
			cipher_list = list(cipher_list)
			return cipher_list
		cipher = [[], [], [], []]
		for i in range(4):
			cipher[0].append(cipher_list[i])
		for i in range(4, 8):
			cipher[1].append(cipher_list[i])
		for i in range(8, 12):
			cipher[2].append(cipher_list[i])
		for i in range(12, 16):
			cipher[3].append(cipher_list[i])
		return cipher
	elif type(cipher) == list and len(cipher) == 16:
		cipher = [cipher[i:i + 4] for i in range(0, 16, 4)]
	else:
		raise TypeError("Invalid input for decryption")
	return cipher


def main():
	print(("Please choose from the following menu: \n"
	       + "1: Run AES128 Encryption\n"
	       + "2: Run AES128 Decryption\n"
	       + "3: Exit Program\n"))

	choice = int(input())

	if choice == 1:
		block_choice = int(input("Which block mode would you like to use? \n " + " 1: ECB Mode "))
		if block_choice == 1:
			plaintext = format_input(input("Please enter a 16 byte plaintext as string to encrypt: "))
			ecb(plaintext, KEY)

	if choice == 2:
		# Decrypt takes a 2d list 4x4
		block_choice = int(input("Which block mode would you like to use? \n " + " 1: ECB Mode "))
		if block_choice == 1:
			cipher = input("Please enter ciphertext to decrypt (Either list of 16 values, or 1D string of list len 16): ")
			cipher = normalize_input_for_decrypt(cipher)
			ecb(cipher, KEY, enc=False)
			print(format_output(decrypt(cipher, KEY)))

	elif choice == 3:
		exit()


main()
