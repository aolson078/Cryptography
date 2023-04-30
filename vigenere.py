# Written by Alexander Olson

import random


def vigenere():
	# Take users input for clear text
	clear = input("Please enter clear text to encrypt: \n")

	cipher = ""

	# Choose a keyword
	key = input("Please enter a keyword. This should be easy to remember and not contain repeated letters \n")

	# Repeat keyword until it's the same length as the plaintext then
	# assign each letter of the repeating keyword a number from 0 to 25
	key_phrase_ord = []
	for i in range(len(clear)):
		key_phrase_ord.append(ord(key[i % len(key)]))

	# For each letter of plaintext, shift by corresponding number in repeating keyword. Follow the formula:
	# ciphertext letter = (plaintext letter + keyword letter) % 26
	for i, letter in enumerate(clear):
		if letter.isupper():
			cipher += chr(((ord(letter) - 65 + (key_phrase_ord[i % len(key_phrase_ord)] - 65)) % 26) + 65)
		elif letter.islower():
			cipher += chr(((ord(letter) - 97 + (key_phrase_ord[i % len(key_phrase_ord)] - 97)) % 26) + 97)
		else:
			cipher += letter

	return cipher


print(vigenere())
