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

# ECB block cipher mode. enc=True to encrypt, enc=False to decrypt
def ecb(plaintext, key, enc=True):
	# Calculate number of blocks needed
	num_blocks = ceil(len(plaintext) / 16)
	num_padding = 16 - len(plaintext) % 16

	# Add padding (pad with same value as number of padding bytes)
	blocks = []
	for i in range(num_blocks):
		blocks.append([])
	print("Blocks:")
	plaintext = [item for row in plaintext for item in row]
	for block in blocks:
		while len(block) < 16 and plaintext:
			# Appends each letters ordinal ascii value
			block.append(plaintext[0])
			plaintext = plaintext[1:]


	# Pad blocks with Ansi X9.23 padding (Pad will all 0s then w/ num_padding in last position
	while len(blocks[-1]) < 16:
		blocks[-1].append(0)  # Pad with 0s
		blocks[-1][-1] = num_padding

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
	print(full_output[0])
	return full_output[0]

