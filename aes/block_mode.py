# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
# This file contains the block modes of operation to run aes128
from math import ceil
from encrypt import encrypt, decrypt


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


# ECB block cipher mode. enc=True to encrypt, enc=False to decrypt. Takes list of blocks and key as input
def ecb(blocks, key, enc=True):
	# 2D list to hold all encrypted blocks
	full_output = []
	# Run aes128 on each block
	for block in blocks:
		text = [block[:4], block[4:8], block[8:12], block[12:16]]
		output = ""
		if enc:
			cipher = encrypt(text, key)
		else:
			cipher = decrypt(text, key)
		# for i in cipher:
		# 	for j in i:
		# 		output += (chr(j))
		cipher_hex_output = to_hex(cipher)
		full_output.append(cipher_hex_output)

	# Return final value
	print(full_output)
	return full_output
