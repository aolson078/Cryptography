# Written by Alexander Olson
# Draft: 2

def caesar():
	clear = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the " \
	        "letters of the alphabet, that not a word could be made out. "
	shift = 12
	cipher = "".join([
		chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper()
		else chr((ord(c) - 97 + shift) % 26 + 97) if c.islower()
		else c for c in clear
	])
	return cipher


print(caesar())
