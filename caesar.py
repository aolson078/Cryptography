# Written by Alexander Olson
# Draft: 2

def caesar():
	clear = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the " \
	        "letters of the alphabet, that not a word could be made out. "
	shift = 12

	# Using a byte array is a more efficient way to process strings
	clear_bytes = bytearray(clear.encode())
	for i, b in enumerate(clear_bytes):
		if 65 <= b <= 90:
			clear_bytes[i] = (b - 65 + shift) % 26 + 65
		elif 97 <= b <= 122:
			clear_bytes[i] = (b - 97 + shift) % 26 + 97
	cipher = clear_bytes.decode()
	return cipher


print(caesar())
