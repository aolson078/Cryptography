# Written by Alexander Olson

import random


def playfair():
	clear = input("Please enter clear text to encrypt: \n")
	cipher = ""

	# If length of clear text is odd, insert filler letter 'X'
	if len(clear) % 2 == 0:
		i = random.choice(range(len(clear)))
		clear = "".join((clear[:i], 'X', clear[i:]))

	# Divide the plaintext message into pairs of letters (digraphs).

	digraphs_clear = [clear[i:i + 2] for i in range(0, len(clear), 2)]
	print(digraphs_clear)
	# Preparing the key square: Choose a keyword or phrase and remove duplicate letters. Fill the 5x5 grid with the
	# unique letters from the keyword, followed by the remaining letters of the alphabet (excluding 'Q').

	keyword = input("Please input keyword. 25 characters max \n")
	if len(keyword) > 25:
		print("Keyword too long \n")
		keyword = input("Please input keyword. 25 characters max \n")

	# TODO remove duplicate letters in keyword!!!

	# 5x5 grid containing the keyword first, then the rest of the alphabet, excluding keyword letters and 'Q'

	cipher_grid = [[] for _ in range(5)]

	for i in range(5):
		while len(cipher_grid[i]) < 5 and len(keyword) > 0:
			cipher_grid[i].append(keyword[0])
			keyword = keyword[1:]
		offset = len(cipher_grid[i])
		for j in range(offset, 5):
			if len(cipher_grid[i]) != 5:
				ascii_value = ((i * 5) + j) + 65
				if ascii_value >= 81:
					ascii_value += 1
				cipher_grid[i].append(chr(ascii_value))

	for inner_list in cipher_grid:
		print(inner_list)

	# Encrypting the message: For each pair of letters in the plaintext, apply one of the following rules,
	# based on their positions in the key square:

	# a) If the letters are in the same row, replace each letter with the one
	# immediately to its right (wrapping around to the beginning of the row if necessary).
	same_row_rotate()
	# b) If the letters are in the same column, replace each letter with the one immediately below it
	# (wrapping around to the top of the column if necessary).
	same_column_rotate()
	# c) If the letters form the corners of a rectangle, replace each letter with the one and the same row but at the
	# opposite corner of the rectangle.
	rectangle_rotate()
	# The encrypted message consists of the substituted letters, grouped in pairs as in the original plaintext.

	# To decrypt: a) If the letters are in the same row, replace each letter with the one immediately to its left. b)
	# If the letters are in the same column, replace each letter with the one immediately above it. c) If the letters
	# form the corners of a rectangle, replace each letter with the one and the same row but at the opposite corner of
	# the rectangle.
	return cipher


def same_row_rotate():
	pass


def same_column_rotate():
	pass


def rectangle_rotate():
	pass


print(playfair())
