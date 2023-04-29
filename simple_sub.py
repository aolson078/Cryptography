# Written by Alexander Olson

import random


def simple_sub():
	clear = input("Please enter clear text to encrypt: \n")
	cipher = ""

	cipher_lower = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

	cipher_upper = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

	cipher_lower, cipher_upper = randomize_ciphers(cipher_lower, cipher_upper)

	# Creates translation tables out of the dicts
	trans_lower = str.maketrans(cipher_lower)
	trans_upper = str.maketrans(cipher_upper)

	# Uses translation tables to encode clear text into cipher text
	cipher = clear.translate(trans_lower).translate(trans_upper)

	return "Cipher code: " + cipher + " \nKeys: \n" + str(cipher_lower) + " \n" + str(cipher_upper)


# randomize_ciphers loops through each alphabet dict and selects a unique letter to replace it with
def randomize_ciphers(cipher_lower, cipher_upper):
	lower = list(cipher_lower.keys())
	upper = list(cipher_upper.keys())
	for letter in cipher_lower:
		choice = random.choice(lower)
		cipher_lower[letter] = choice
		lower.remove(choice)
	for letter in cipher_upper:
		choice = random.choice(upper)
		cipher_upper[letter] = choice
		upper.remove(choice)

	return cipher_lower, cipher_upper


print(simple_sub())
