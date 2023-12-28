# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
# This file contains the block modes of operation to run aes128

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
	# Blocks is 2D list that holds all encrypted blocks to process
	# Run aes128 on each block
	full_output = [to_hex(encrypt([block[i:i + 4] for i in range(0, 16, 4)], key)) if enc
	               else to_hex(decrypt([block[i:i + 4] for i in range(0, 16, 4)], key)) for block in blocks]

	# Return final value
	print(full_output)
	return full_output
