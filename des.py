# Written by Alexander Olson

def shift_left(binary, n):
	first_half = binary[n::]
	second_half = binary[:n]
	result = first_half + second_half
	return result


def shift_right(binary, n):
	first_half = binary[len(binary) - n:]
	second_half = binary[:len(binary) - n]
	result = first_half + second_half
	return result


def perm_two(binary):
	permutation_table2 = [14, 17, 11, 24, 1, 5,
	                      3, 28, 15, 6, 21, 10,
	                      23, 19, 12, 4, 26, 8,
	                      16, 7, 27, 20, 13, 2,
	                      41, 52, 31, 37, 47, 55,
	                      30, 40, 51, 45, 33, 48,
	                      44, 49, 39, 56, 34, 53,
	                      46, 42, 50, 36, 29, 32]

	permutation_bin2 = [b'0' for i in range(56)]

	for i, b in enumerate(permutation_table2):
		permutation_bin2[i] = binary[b - 1]

	permutation_bin2 = permutation_bin2[0:48]

	parity_string = ''.join([str(b) for b in permutation_bin2])

	return parity_string


def des():
	clear = "01234567"  # I Think this needs to be the key
	byte_clear = bytes(clear, "utf-8")
	print("Bytes: " + str(byte_clear))

	# Convert the bytes to binary representation and remove every 8th bit (parity bits)
	bin_clear = ''.join([format(b, '08b') for b in byte_clear])

	print(bin_clear)

	bin_string = ''.join(bin_clear)
	print("Binary string without parity bits removed: " + str(bin_string))
	print(len(bin_string))

	permutation_table1 = [57, 49, 41, 33, 25, 17, 9,
	                      1, 58, 50, 42, 34, 26, 18,
	                      10, 2, 59, 51, 43, 35, 27,
	                      19, 11, 3, 60, 52, 44, 36,
	                      63, 55, 47, 39, 31, 23, 15,
	                      7, 62, 54, 46, 38, 30, 22,
	                      14, 6, 61, 53, 45, 37, 29,
	                      21, 13, 5, 28, 20, 12, 4]

	permutation_bin1 = [b'0' for i in range(64)]

	bin_string = b"0001001100110100010101110111100110011011101111001101111111110001"  # HARD CODED FOR TESTING!!!

	for i, b in enumerate(permutation_table1):
		permutation_bin1[i] = bin_string[b - 1]

	permutation_bin1 = permutation_bin1[0:56]

	parity_string = ''.join([chr(b) for b in permutation_bin1])

	print("Parity string: " + str(parity_string))

	c0 = parity_string[:len(parity_string) // 2:]
	d0 = parity_string[(len(parity_string) // 2):]

	print("C0: " + str(c0), "D0: " + str(d0))

	c1 = shift_left(c0, 1)
	c2 = shift_left(c1, 1)
	c3 = shift_left(c2, 2)
	c4 = shift_left(c3, 2)
	c5 = shift_left(c4, 2)
	c6 = shift_left(c5, 2)
	c7 = shift_left(c6, 2)
	c8 = shift_left(c7, 2)
	c9 = shift_left(c8, 1)
	c10 = shift_left(c9, 2)
	c11 = shift_left(c10, 2)
	c12 = shift_left(c11, 2)
	c13 = shift_left(c12, 2)
	c14 = shift_left(c13, 2)
	c15 = shift_left(c14, 2)
	c16 = shift_left(c15, 1)

	d1 = shift_left(d0, 1)
	d2 = shift_left(d1, 1)
	d3 = shift_left(d2, 2)
	d4 = shift_left(d3, 2)
	d5 = shift_left(d4, 2)
	d6 = shift_left(d5, 2)
	d7 = shift_left(d6, 2)
	d8 = shift_left(d7, 2)
	d9 = shift_left(d8, 1)
	d10 = shift_left(d9, 2)
	d11 = shift_left(d10, 2)
	d12 = shift_left(d11, 2)
	d13 = shift_left(d12, 2)
	d14 = shift_left(d13, 2)
	d15 = shift_left(d14, 2)
	d16 = shift_left(d15, 1)

	k1 = perm_two(c1 + d1)
	k2 = perm_two(c2 + d2)
	k3 = perm_two(c3 + d3)
	k4 = perm_two(c4 + d4)
	k5 = perm_two(c5 + d5)
	k6 = perm_two(c6 + d6)
	k7 = perm_two(c7 + d7)
	k8 = perm_two(c8 + d8)
	k9 = perm_two(c9 + d9)
	k10 = perm_two(c10 + d10)
	k11 = perm_two(c11 + d11)
	k12 = perm_two(c12 + d12)
	k13 = perm_two(c13 + d13)
	k14 = perm_two(c14 + d14)
	k15 = perm_two(c15 + d15)
	k16 = perm_two(c16 + d16)



print(des())
