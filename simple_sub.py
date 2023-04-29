# Written by Alexander Olson

import random


def simple_sub():
	clear = input("Please enter clear text to encrypt: \n")
	cipher = ""

	cipher_lower = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

	cipher_upper = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}

	cipher_lower, cipher_upper = randomize_ciphers(cipher_lower, cipher_upper)

	for letter in clear:
		if letter.isupper():
			cipher += cipher_upper[letter]
		elif letter.islower():
			cipher += cipher_lower[letter]
		else:
			cipher += letter

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
