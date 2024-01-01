# Written by Alexander Olson

import random


def simple_sub():
	clear = input("Please enter clear text to encrypt: \n")

	# Creates dicts of randomized alphabets for upper and lower
	cipher_lower, cipher_upper = randomize_ciphers()

	# Creates translation tables out of the dicts
	trans_lower = str.maketrans(cipher_lower)
	trans_upper = str.maketrans(cipher_upper)

	# Uses translation tables to encode clear text into cipher text
	cipher = clear.translate(trans_lower).translate(trans_upper)

	return f"Cipher code: {cipher} \nKeys: \n {cipher_lower} \n {cipher_upper}"


# randomize_ciphers loops through each alphabet dict and selects a unique letter to replace it with
def randomize_ciphers():
	lower = list(range(ord('a'), ord('z') + 1))
	upper = list(range(ord('A'), ord('Z') + 1))

	random.shuffle(lower)
	random.shuffle(upper)

	# Create dicts of randomized alphabets for upper and lower
	cipher_lower = dict(zip(map(chr, range(ord('a'), ord('z')+1)), map(chr, lower)))
	cipher_upper = dict(zip(map(chr, range(ord('A'), ord('Z') + 1)), map(chr, upper)))

	return cipher_lower, cipher_upper


print(simple_sub())
