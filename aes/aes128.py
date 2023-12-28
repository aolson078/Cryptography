# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson

def gmult(a, b):
	p = 0
	for _ in range(8):
		if b & 1:
			p ^= a
		hi_bit_set = a & 0x80 # Check if the high bit is set
		a <<= 1
		if hi_bit_set:
			a ^= 0x1B
		b >>= 1
	return p % 256  # Add modulo operation to keep the result within 8 bits


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class AES:
	"""
            Initializes the AES class with the given state.

            Args:
            - state: The initial state for the AES encryption as a 4x4 matrix.

            Attributes:
            - SBOXES: The S-box lookup table used in the AES algorithm.
            - RCON: The round constant used in the key expansion of AES.
            - state: The current state of the AES encryption.
    """

	def __init__(self, state):

		self.SBOXES = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
		               0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
		               0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
		               0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
		               0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
		               0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
		               0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
		               0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
		               0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
		               0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
		               0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
		               0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
		               0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
		               0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
		               0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
		               0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

		# Inverse sbox
		self.INVSBOXES = []

		self.RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

		# State is the plaintext at initialization
		self.state = state

	# ------------------------------------------------------------------------------------------------------------------
	""" 
            Adds the round key to the current state.

            Args: key: The round key as a 4x4 matrix.

            Returns: The result of adding the round key to the current state as a 4x4 matrix.
    """

	def add_round_key(self, key):
		result = [[0] * 4 for _ in range(4)]
		for i in range(4):
			for j in range(4):
				result[i][j] = self.state[i][j] ^ key[i][j]
		return result

	# ------------------------------------------------------------------------------------------------------------------
	"""
            Performs a byte substitution on the current state using the S-box lookup table specified in the AES algorithm
            https://en.wikipedia.org/wiki/Rijndael_S-box

            Returns:
            - None (modifies the state in place).
    """

	def sbox(self):
		output_state = []

		for i in range(4):
			for j in range(4):
				output_state.append(self.SBOXES[int(self.state[i][j])])
		self.state = [output_state[i:i + 4] for i in range(0, len(output_state), 4)]

	# Calculates the inverted sbox and computes new state after sbox substitution
	def inv_sbox(self):
		inv_sbox = [0] * 256
		output_state = []
		for i in range(256):
			inv_sbox[self.SBOXES[i]] = i
		for i in range(4):
			for j in range(4):
				output_state.append(inv_sbox[int(self.state[i][j])])
		self.state = [output_state[i:i + 4] for i in range(0, len(output_state), 4)]

	# ------------------------------------------------------------------------------------------------------------------
	"""
           Shifts the current state as a 2D list, where the second row is shifted once, the third row is shifted twice,
           and the fourth row is shifted three times.

           Returns:
            - None (modifies the state in place).
    """

	def shift_rows(self):
		col0 = [self.state[0][0], self.state[1][1], self.state[2][2], self.state[3][3]]
		col1 = [self.state[1][0], self.state[2][1], self.state[3][2], self.state[0][3]]
		col2 = [self.state[2][0], self.state[3][1], self.state[0][2], self.state[1][3]]
		col3 = [self.state[3][0], self.state[0][1], self.state[1][2], self.state[2][3]]
		self.state = [col0, col1, col2, col3]

	# ------------------------------------------------------------------------------------------------------------------

	"""
           Undoes the shift_rows function

           Returns:
            - None (modifies the state in place).
    """

	def inv_shift_rows(self):
		col0 = [self.state[0][0], self.state[3][1], self.state[2][2], self.state[1][3]]
		col1 = [self.state[1][0], self.state[0][1], self.state[3][2], self.state[2][3]]
		col2 = [self.state[2][0], self.state[1][1], self.state[0][2], self.state[3][3]]
		col3 = [self.state[3][0], self.state[2][1], self.state[1][2], self.state[0][3]]
		self.state = [col0, col1, col2, col3]

	# ------------------------------------------------------------------------------------------------------------------
	"""
            Applies galois multiplication to each value in state, mixing the columns

            Returns:
            - None (modifies the state in place).
    """

	def mix_columns(self):
		for i in range(4):
			# Compute the new column elements using the Galois multiplication and XOR
			r00 = gmult(self.state[i][0], 2)
			r01 = gmult(self.state[i][1], 3)
			r0 = (r00 ^ r01 ^ self.state[i][2] ^ self.state[i][3])  # r0 is the first value of the new column

			r11 = gmult(self.state[i][1], 2)
			r12 = gmult(self.state[i][2], 3)
			r1 = (self.state[i][0] ^ r11 ^ r12 ^ self.state[i][3])  # r1 is the second value of the new column

			r22 = gmult(self.state[i][2], 2)
			r23 = gmult(self.state[i][3], 3)
			r2 = (self.state[i][0] ^ self.state[i][1] ^ r22 ^ r23)  # r2 is the third value of the new column

			r30 = gmult(self.state[i][0], 3)
			r33 = gmult(self.state[i][3], 2)
			r3 = (r30 ^ self.state[i][1] ^ self.state[i][2] ^ r33)  # r3 is the fourth value of the new column
			self.state[i] = [r0, r1, r2, r3]

	# ------------------------------------------------------------------------------------------------------------------
	"""
            Applies galois multiplication to each value in state with inverse matrix, unmixing the columns
            Returns:
            - None (modifies the state in place).
    """

	def inv_mix_columns(self):
		for i in range(4):
			# Compute the new column elements using the Galois multiplication and XOR
			r00 = gmult(self.state[i][0], 14)
			r01 = gmult(self.state[i][1], 11)
			r02 = gmult(self.state[i][2], 13)
			r03 = gmult(self.state[i][3], 9)
			r0 = (r00 ^ r01 ^ r02 ^ r03)  # r0 is the first value of the new column

			r11 = gmult(self.state[i][0], 9)
			r12 = gmult(self.state[i][1], 14)
			r13 = gmult(self.state[i][2], 11)
			r14 = gmult(self.state[i][3], 13)
			r1 = (r13 ^ r11 ^ r12 ^ r14)  # r1 is the second value of the new column

			r22 = gmult(self.state[i][0], 13)
			r23 = gmult(self.state[i][1], 9)
			r24 = gmult(self.state[i][2], 14)
			r25 = gmult(self.state[i][3], 11)
			r2 = (r25 ^ r24 ^ r22 ^ r23)  # r2 is the third value of the new column

			r30 = gmult(self.state[i][0], 11)
			r33 = gmult(self.state[i][1], 13)
			r31 = gmult(self.state[i][2], 9)
			r34 = gmult(self.state[i][3], 14)
			r3 = (r30 ^ r34 ^ r31 ^ r33)  # r3 is the fourth value of the new column
			self.state[i] = [r0, r1, r2, r3]

	# ------------------------------------------------------------------------------------------------------------------
	"""
            Generates subkeys using the key expansion process of the AES algorithm.

            Args:
            - key: The initial key as a list of integers.

            Returns:
            - The subkeys as a list of 4x4 matrices.
    """

	def generate_subkeys(self, key):
		# Initialize the expanded key with the cipher key
		expanded_key = []
		for i in range(4):
			expanded_key.append(key[i * 4:i * 4 + 4])

		# Generate the remaining words in the expanded key
		for i in range(4, 44):
			temp = expanded_key[i - 1]
			if i % 4 == 0:
				# Perform the key schedule core (rotate, substitute, round constant)
				temp = [self.SBOXES[temp[(j + 1) % 4]] for j in range(4)]  # Rotate and substitute
				temp[0] ^= self.RCON[i // 4 - 1]  # XOR with round constant
			expanded_key.append([expanded_key[i - 4][j] ^ temp[j] for j in range(4)])  # XOR with 4 words back

		# Group the expanded key into subkeys
		subkeys = [expanded_key[i * 4:i * 4 + 4] for i in range(11)]
		return subkeys
