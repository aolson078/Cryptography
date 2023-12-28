# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson

import ast  # Provides function to parse string to produce list object
from block_mode import ecb


class Console:

	def __init__(self, encryption_key=None, input_text=""):
		# If no key is provided, a default key is used
		if encryption_key is None:
			self.encryption_key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
		# Holds preprocessed plain or cipher input_text
		self.input_text = input_text
		# Container for individual cipher_blocks
		self.cipher_blocks = []

	def change_key(self):
		self.encryption_key = input("Please enter a new 16 hex digit key: ")

	def change_input_text(self):
		self.input_text = input("Please enter plaininput_text or cipherinput_text: ")

	# format_input takes arbitrary input as a string and outputs a 1d list of decimal values
	def format_input(self):
		# Check if the input string is a list of integers
		if self.input_text.startswith('[') and self.input_text.endswith(']'):
			try:
				# If the input is a list, it is parsed into a list object
				self.input_text = ast.literal_eval(self.input_text)
			except (SyntaxError, ValueError):
				print("Invalid format! Please enter new input_text: ")
				self.change_input_text()
				self.format_input()
		else:
			# Convert the string to ASCII values
			self.input_text = [ord(char) for char in self.input_text]

	# Converts input_text to 2d list of cipher_blocks, 16 values each, and pads the last block if needed
	def convert_to_cipher_blocks(self):
		self.cipher_blocks = [self.input_text[i:i + 16] for i in range(0, len(self.input_text), 16)]

		# Pad cipher_blocks with Ansi X9.23 padding (Pad will all 0s then w/ num_padding in last position
		num_padding = 16 - len(self.input_text) % 16
		is_padding_added = False
		while len(self.cipher_blocks[-1]) < 16:
			is_padding_added = True

			self.cipher_blocks[-1].append(0)  # If the last block is less than 16 characters, it is padded with 0s
		if is_padding_added:
			self.cipher_blocks[-1][-1] = num_padding  # Last char of the block is replaced with the number of padding chars

	def run(self):
		print(("Please choose from the following menu: \n"
		       + "1: Run AES128 Encryption\n"
		       + "2: Run AES128 Decryption\n"
		       + "3: Exit Program\n"))

		menu_choice = int(input())

		if self.input_text == "":
			self.change_input_text()

		self.format_input()

		self.convert_to_cipher_blocks()

		if menu_choice == 1:
			block_mode_choice = int(input("Which block mode would you like to use? \n " + " 1: ECB Mode "))
			if block_mode_choice == 1:
				ecb(self.cipher_blocks, self.encryption_key)

		if menu_choice == 2:
			block_mode_choice = int(input("Which block mode would you like to use? \n " + " 1: ECB Mode "))
			if block_mode_choice == 1:
				ecb(self.cipher_blocks, self.encryption_key, enc=False)

		elif menu_choice == 3:
			exit()


if __name__ == "__main__":
	c = Console()
	c.run()
