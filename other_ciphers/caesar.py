# Written by Alexander Olson

def caesar():
	clear = input("Please enter clear text to encrypt: \n")
	shift = int(input("Please enter amount to shift: \n"))

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
