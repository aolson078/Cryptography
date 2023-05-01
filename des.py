# Written by Alexander Olson

def des():
	clear = "01234567"
	byte_clear = bytes(clear, "utf-8")
	print("Bytes: " + str(byte_clear))

	# Convert the bytes to binary representation and remove every 8th bit (parity bits)
	bin_clear = ''.join([format(b, '08b') for b in byte_clear])
	parity = [bin_clear[i] for i in range(len(bin_clear)) if (i + 1) % 8 != 0]

	bin_string = ''.join(parity)
	print("Binary string with parity bits removed: " + str(bin_string))

	permutation_table1 = [57, 49, 41, 33, 25, 17, 9,
	                      1, 58, 50, 42, 34, 26, 18,
	                      10, 2, 59, 51, 43, 35, 27,
	                      19, 11, 3, 60, 52, 44, 36,
	                      63, 55, 47, 39, 31, 23, 15,
	                      7, 62, 54, 46, 38, 30, 22,
	                      14, 6, 61, 53, 45, 37, 29,
	                      21, 13, 5, 28, 20, 12, 4]

	print(len(bin_string))

	permutation_bin1 = ['0' for i in range(64)]

	for i, b in enumerate(permutation_table1):
		permutation_bin1[i] = bin_string[b - 1]
	print(permutation_bin1)


print(des())
