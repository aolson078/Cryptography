# Written by Alexander Olson

# def shift_left(binary, n):
# 	first_half = binary[n::]
# 	second_half = binary[:n]
# 	result = first_half + second_half
# 	return result
#
#
# def shift_right(binary, n):
# 	first_half = binary[len(binary) - n:]
# 	second_half = binary[:len(binary) - n]
# 	result = first_half + second_half
# 	return result
#
#
# def init_perm(clear_text):
# 	permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
# 	                     60, 52, 44, 36, 28, 20, 12, 4,
# 	                     62, 54, 46, 38, 30, 22, 14, 6,
# 	                     64, 56, 48, 40, 32, 24, 16, 8,
# 	                     57, 49, 41, 33, 25, 17, 9, 1,
# 	                     59, 51, 43, 35, 27, 19, 11, 3,
# 	                     61, 53, 45, 37, 29, 21, 13, 5,
# 	                     63, 55, 47, 39, 31, 23, 15, 7]
#
# 	permutation_bin = ['0' for _ in range(64)]
#
# 	# Reorder key with first permutation table
# 	for i, b in enumerate(permutation_table):
# 		permutation_bin[i] = clear_text[b - 1]
#
# 	# Make string out of permutation_bin1
# 	parity_string = ''.join([b for b in permutation_bin])
#
# 	return parity_string


# Uses E bit-selection table to extend r
# def expand_r(r):
# 	e_table = [32, 1, 2, 3, 4, 5,
# 	           4, 5, 6, 7, 8, 9,
# 	           8, 9, 10, 11, 12, 13,
# 	           12, 13, 14, 15, 16, 17,
# 	           16, 17, 18, 19, 20, 21,
# 	           20, 21, 22, 23, 24, 25,
# 	           24, 25, 26, 27, 28, 29,
# 	           28, 29, 30, 31, 32, 1]
#
# 	e = ['0' for _ in range(48)]
#
# 	for i, b in enumerate(e_table):
# 		e[i] = r[b - 1]
#
# 	e_string = ''.join([str(b) for b in e])
#
# 	return e_string


def xor(bin1, bin2):
	ret = ""
	for i in range(len(bin1)):
		if bin1[i] != bin2[i]:
			ret += '1'
		else:
			ret += '0'
	return ret


#
#
# # Changes a string of 1's and 0's into a decimal
# def binstr_to_dec(binary_string):
# 	decimal = 0
# 	length = len(binary_string)
#
# 	for i, digit in enumerate(binary_string):
# 		decimal += int(digit) * (2 ** (length - i - 1))
#
# 	return decimal
#
#
# # Changes a decimal into a binary string
# def decimal_to_binary(decimal):
# 	binary_string = ""
#
# 	while decimal > 0:
# 		remainder = decimal % 2
# 		decimal = decimal // 2
# 		binary_string = str(remainder) + binary_string
#
# 	return binary_string
#
#
# def binary_to_hex(binary_string):
# 	# Pad the binary with 0s to make multiple of 4
# 	binary_string = binary_string.zfill(len(binary_string) + (4 - len(binary_string) % 4) % 4)
#
# 	# Create a dictionary to map binary values to their corresponding hex values
# 	hex_map = {
# 		"0000": "0", "0001": "1", "0010": "2", "0011": "3",
# 		"0100": "4", "0101": "5", "0110": "6", "0111": "7",
# 		"1000": "8", "1001": "9", "1010": "A", "1011": "B",
# 		"1100": "C", "1101": "D", "1110": "E", "1111": "F"
# 	}
#
# 	hex_string = ""
# 	for i in range(0, len(binary_string), 4):
# 		# Get the 4-bit binary substring
# 		binary_substring = binary_string[i:i + 4]
# 		hex_string += hex_map[binary_substring]
#
# 	return hex_string
#
#
# def encrypt(clear_text, key):
# 	return 0
#
#
# def sbox(bin_list):
# 	sboxs = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
# 	          0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
# 	          4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
# 	          15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
# 	         [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
# 	          3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
# 	          0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
# 	          13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
# 	         [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
# 	          13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
# 	          13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
# 	          1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
# 	         [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
# 	          13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
# 	          10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
# 	          3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
# 	         [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
# 	          14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
# 	          4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
# 	          11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
# 	         [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
# 	          10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
# 	          9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
# 	          4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
# 	         [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
# 	          13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
# 	          1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
# 	          6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
# 	         [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
# 	          1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
# 	          7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
# 	          2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
#
# 	four_bit_blocks = []
#
# 	for i in range(8):
# 		j = bin_list[i][0] + bin_list[i][-1]
# 		j = binstr_to_dec(j)
# 		k = bin_list[i][1:-1]
# 		k = binstr_to_dec(k)
#
# 		# Use j, k to look up jth row and kth column in sbox[i]
#
# 		s_permutation = sboxs[i][(j * 16) + k]
#
# 		s_permutation = decimal_to_binary(s_permutation)
#
# 		while len(s_permutation) != 4:
# 			s_permutation = '0' + s_permutation
# 		four_bit_blocks.append(s_permutation)
# 	return four_bit_blocks

""""#Transformation in the Cipher and Inverse Cipher in which a Round
# Key is added to the State using an XOR operation. The length of a
# Round Key equals the size of the State (i.e., for Nb = 4, the Round
# Key length equals 128 bits/16 bytes).
# AddRoundKey()

InvMixColumns()Transformation in the Inverse Cipher that is the inverse of
MixColumns().

InvShiftRows() Transformation in the Inverse Cipher that is the inverse of
ShiftRows().

InvSubBytes()	 Transformation in the Inverse Cipher that is the inverse of
SubBytes().

K	 Cipher Key.



MixColumns()	 Transformation in the Cipher that takes all of the columns of the
State and mixes their data (independently of one another) to
produce new columns.

Nb	 Number of columns (32-bit words) comprising the State. For this
standard, Nb = 4. (Also see Sec. 6.3.)

Nk	 Number of 32-bit words comprising the Cipher Key. For this
standard, Nk = 4, 6, or 8. (Also see Sec. 6.3.)

Nr	 Number of rounds, which is a function of Nk and Nb (which is
fixed). For this standard, Nr = 10, 12, or 14. (Also see Sec. 6.3.)

Rcon[]	 The round constant word array.

RotWord()	 Function used in the Key Expansion routine that takes a four-byte
word and performs a cyclic permutation.

ShiftRows()	 Transformation in the Cipher that processes the State by cyclically
shifting the last three rows of the State by different offsets.

SubBytes()	 Transformation in the Cipher that processes the State using a nonlinear byte substitution table (S-box) that operates on each of the
State bytes independently.

SubWord()	 Function used in the Key Expansion routine that takes a four-byte
input word and applies an S-box to each of the four bytes to
produce an output word.

 XOR	 Exclusive-OR operation

Circle with diagonal hex = Multiplication of two polynomials (each with degree < 4) modulo
x^4 + 1.
 """


def binstr_to_dec(bin_str):
	return int(bin_str, 2)


def dec_to_binstr(dec, width=32):
	return format(dec, f'0{width}b')


def rotate_word_left(word, rot):
	if not (isinstance(word, int) and 0 <= word):
		raise ValueError("Invalid input: word must be a non-negative integer")

	if not (isinstance(rot, int) and 0 <= rot):
		raise ValueError("Invalid input: rot must be a non-negative integer")

	bin_str = format(word, 'b')
	word_length = len(bin_str)
	rot = rot % word_length
	rotated_bin_str = bin_str[rot:] + bin_str[:rot]
	return int(rotated_bin_str, 2)


def key_expansion(key):
	key_schedule = [key[0:32], key[32:64], key[64:96], key[96:128]]
	matrix = create_key_matrix(key_schedule)


def create_key_matrix(key_schedule):
	key_matrix = [[], [], [], []]

	for i in range(4):
		for j in range(4):
			key_matrix[i].append(key_schedule[j][(i * 8):(i + 1) * 8].decode())

	for key in key_matrix:
		print(key)

	return key_matrix


# Takes original key and XORs with binary string
def init_round(binary_string, key):
	xor(binary_string, key)


def main():
	# Convert hexadecimal clear text to binary
	clear_text = f'{0x0123456789ABCDEF:0>64b}'

	# Key will be 128 bits for AES-128
	key = b"0001001100110100010101110111100110011011101111001101111111110001" \
	      b"0001001100110100010101110111100110011011101111001101111111110001"

	cipher = ''  # encrypt(clear_text, key)
	key_expansion(key)
	print(rotate_word_left(10, 1))

	# TODO Implement SubWord sbox func

	return cipher


main()
