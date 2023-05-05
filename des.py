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


def init_perm(clear_text):
	permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
	                     60, 52, 44, 36, 28, 20, 12, 4,
	                     62, 54, 46, 38, 30, 22, 14, 6,
	                     64, 56, 48, 40, 32, 24, 16, 8,
	                     57, 49, 41, 33, 25, 17, 9, 1,
	                     59, 51, 43, 35, 27, 19, 11, 3,
	                     61, 53, 45, 37, 29, 21, 13, 5,
	                     63, 55, 47, 39, 31, 23, 15, 7]

	permutation_bin = ['0' for _ in range(64)]

	# Reorder key with first permutation table
	for i, b in enumerate(permutation_table):
		permutation_bin[i] = clear_text[b - 1]

	# Make string out of permutation_bin1
	parity_string = ''.join([b for b in permutation_bin])

	return parity_string


def perm_two(binary):
	permutation_table = [14, 17, 11, 24, 1, 5,
	                     3, 28, 15, 6, 21, 10,
	                     23, 19, 12, 4, 26, 8,
	                     16, 7, 27, 20, 13, 2,
	                     41, 52, 31, 37, 47, 55,
	                     30, 40, 51, 45, 33, 48,
	                     44, 49, 39, 56, 34, 53,
	                     46, 42, 50, 36, 29, 32]

	permutation_bin = [b'0' for _ in range(56)]

	for i, b in enumerate(permutation_table):
		permutation_bin[i] = binary[b - 1]

	permutation_bin = permutation_bin[0:48]

	parity_string = ''.join([str(b) for b in permutation_bin])

	return parity_string


# This permutation takes the rl16 binary string and produces the final permutation
def final_perm(binary):
	permutation_table = [40, 8, 48, 16, 56, 24, 64, 32,
	                     39, 7, 47, 15, 55, 23, 63, 31,
	                     38, 6, 46, 14, 54, 22, 62, 30,
	                     37, 5, 45, 13, 53, 21, 61, 29,
	                     36, 4, 44, 12, 52, 20, 60, 28,
	                     35, 3, 43, 11, 51, 19, 59, 27,
	                     34, 2, 42, 10, 50, 18, 58, 26,
	                     33, 1, 41, 9, 49, 17, 57, 25, ]

	permutation_bin = ['0' for _ in range(64)]

	for i, b in enumerate(permutation_table):
		permutation_bin[i] = binary[b - 1]

	permutation_bin = permutation_bin[0:64]

	final_string = ''.join([str(b) for b in permutation_bin])

	return final_string


# Uses E bit-selection table to extend r
def expand_r(r):
	e_table = [32, 1, 2, 3, 4, 5,
	           4, 5, 6, 7, 8, 9,
	           8, 9, 10, 11, 12, 13,
	           12, 13, 14, 15, 16, 17,
	           16, 17, 18, 19, 20, 21,
	           20, 21, 22, 23, 24, 25,
	           24, 25, 26, 27, 28, 29,
	           28, 29, 30, 31, 32, 1]

	e = ['0' for _ in range(48)]

	for i, b in enumerate(e_table):
		e[i] = r[b - 1]

	e_string = ''.join([str(b) for b in e])

	return e_string


def generate_keys(key):
	# Table determining where each value of the key is inserted into the permutated binary string
	permutation_table1 = [57, 49, 41, 33, 25, 17, 9,
	                      1, 58, 50, 42, 34, 26, 18,
	                      10, 2, 59, 51, 43, 35, 27,
	                      19, 11, 3, 60, 52, 44, 36,
	                      63, 55, 47, 39, 31, 23, 15,
	                      7, 62, 54, 46, 38, 30, 22,
	                      14, 6, 61, 53, 45, 37, 29,
	                      21, 13, 5, 28, 20, 12, 4]

	# Initialize list with all binary 0's
	permutation_bin1 = [b'0' for i in range(64)]

	# Reorder key with first permutation table
	for i, b in enumerate(permutation_table1):
		permutation_bin1[i] = key[b - 1]

	# Truncate extra spaces
	permutation_bin1 = permutation_bin1[0:56]

	# Make string out of permutation_bin1
	parity_string = ''.join([chr(int(b)) for b in permutation_bin1])

	# Split key in 2
	c0 = parity_string[:len(parity_string) // 2:]
	d0 = parity_string[(len(parity_string) // 2):]

	# Shift each key left
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

	# Create key out of each c/d pair
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
	keys = [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15, k16]
	return keys


def xor(bin1, bin2):
	ret = ""
	for i in range(len(bin1)):
		if bin1[i] != bin2[i]:
			ret += '1'
		else:
			ret += '0'
	return ret


def f(r, key):
	r = expand_r(r)  # r now has a 48 bit value
	r_xor = xor(r, key)  # xor rn-1 w kn

	# sbox step, group 48 bit value of r_xor into 8 groups of 6 bits
	b0, b1, b2, b3, b4, b5, b6, b7 = r_xor[0:6], r_xor[6:12], \
	                                 r_xor[12:18], r_xor[18:24], \
	                                 r_xor[24:30], r_xor[30:36], \
	                                 r_xor[36:42], r_xor[42:48]

	b_list = [b0, b1, b2, b3, b4, b5, b6, b7]
	four_bits = sbox(b_list)

	binary_string = ""
	for i in range(len(four_bits)):
		binary_string += four_bits[i]

	permutation_table = [16, 7, 20, 21,
	                     29, 12, 28, 17,
	                     1, 15, 23, 26,
	                     5, 18, 31, 10,
	                     2, 8, 24, 14,
	                     32, 27, 3, 9,
	                     19, 13, 30, 6,
	                     22, 11, 4, 25]
	permutation_bin = ""

	# Reorder key with permutation table
	for i, b in enumerate(permutation_table):
		permutation_bin += binary_string[b - 1]
	return permutation_bin


# sbox takes 8 6 bit binary strings and reduces them into 4 bit binary strings
def sbox(bin_list):
	sboxs = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
	          0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
	          4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
	          15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
	         [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
	          3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
	          0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
	          13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
	         [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
	          13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
	          13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
	          1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
	         [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
	          13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
	          10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
	          3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
	         [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
	          14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
	          4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
	          11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
	         [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
	          10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
	          9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
	          4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
	         [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
	          13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
	          1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
	          6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
	         [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
	          1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
	          7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
	          2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

	four_bit_blocks = []

	for i in range(8):
		j = bin_list[i][0] + bin_list[i][-1]
		j = binstr_to_dec(j)
		k = bin_list[i][1:-1]
		k = binstr_to_dec(k)

		# Use j, k to look up jth row and kth column in sbox[i]

		s_permutation = sboxs[i][(j * 16) + k]

		s_permutation = decimal_to_binary(s_permutation)

		while len(s_permutation) != 4:
			s_permutation = '0' + s_permutation
		four_bit_blocks.append(s_permutation)
	return four_bit_blocks


# Changes a string of 1's and 0's into a decimal
def binstr_to_dec(binary_string):
	decimal = 0
	length = len(binary_string)

	for i, digit in enumerate(binary_string):
		decimal += int(digit) * (2 ** (length - i - 1))

	return decimal


# Changes a decimal into a binary string
def decimal_to_binary(decimal):
	binary_string = ""

	while decimal > 0:
		remainder = decimal % 2
		decimal = decimal // 2
		binary_string = str(remainder) + binary_string

	return binary_string


def binary_to_hex(binary_string):
	# Pad the binary with 0s to make multiple of 4
	binary_string = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4) % 4)

	# Create a dictionary to map binary values to their corresponding hex values
	hex_map = {
		"0000": "0", "0001": "1", "0010": "2", "0011": "3",
		"0100": "4", "0101": "5", "0110": "6", "0111": "7",
		"1000": "8", "1001": "9", "1010": "A", "1011": "B",
		"1100": "C", "1101": "D", "1110": "E", "1111": "F"
	}

	hex_string = ""
	for i in range(0, len(binary_string), 4):
		# Get the 4-bit binary substring
		binary_substring = binary_string[i:i + 4]
		hex_string += hex_map[binary_substring]

	return hex_string


def encrypt(clear_text, key):
	keys = generate_keys(key)
	initial_permutation = init_perm(clear_text)
	# Split key in 2
	l0 = initial_permutation[:len(initial_permutation) // 2:]
	r0 = initial_permutation[(len(initial_permutation) // 2):]

	l1 = r0
	r1 = xor(l0, f(r0, keys[0]))
	l2 = r1
	r2 = xor(l1, f(r1, keys[1]))
	l3 = r2
	r3 = xor(l2, f(r2, keys[2]))
	l4 = r3
	r4 = xor(l3, f(r3, keys[3]))
	l5 = r4
	r5 = xor(l4, f(r4, keys[4]))
	l6 = r5
	r6 = xor(l5, f(r5, keys[5]))
	l7 = r6
	r7 = xor(l6, f(r6, keys[6]))
	l8 = r7
	r8 = xor(l7, f(r7, keys[7]))
	l9 = r8
	r9 = xor(l8, f(r8, keys[8]))
	l10 = r9
	r10 = xor(l9, f(r9, keys[9]))
	l11 = r10
	r11 = xor(l10, f(r10, keys[10]))
	l12 = r11
	r12 = xor(l11, f(r11, keys[11]))
	l13 = r12
	r13 = xor(l12, f(r12, keys[12]))
	l14 = r13
	r14 = xor(l13, f(r13, keys[13]))
	l15 = r14
	r15 = xor(l14, f(r14, keys[14]))
	l16 = r15
	r16 = xor(l15, f(r15, keys[15]))

	rl16 = r16 + l16
	ip = final_perm(rl16)

	return binary_to_hex(ip)


def main():
	# TODO still need to write decrypt function, ECB/CFB mode, and Triple-DES

	# Convert hexadecimal clear text to binary
	clear_text = f'{0x0123456789ABCDEF:0>64b}'
	key = b"0001001100110100010101110111100110011011101111001101111111110001"
	cipher = encrypt(clear_text, key)
	print(f"Ciphertext: {cipher}")

	return cipher


main()
