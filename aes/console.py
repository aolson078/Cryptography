# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
import ast

from encrypt import encrypt, decrypt
from block_mode import ecb


class Console:

	def __init__(self, key=None, text=""):
		if key is None:
			self.key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
		# Holds preprocessed plain or cipher text
		self.text = text
		# Container for individual blocks
		self.blocks = []

	def change_key(self):
		self.key = input("Please enter a new 16 hex digit key: ")

	def change_text(self):
		self.text = input("Please enter plaintext or ciphertext: ")

	# format_input takes arbitrary input as a string and outputs a 1d list of decimal values
	def format_input(self):
		# Check if the input string is a list of integers
		if self.text.startswith('[') and self.text.endswith(']'):
			try:
				self.text = ast.literal_eval(self.text)
			except (SyntaxError, ValueError):
				print("Invalid format! Please enter new text: ")
				self.change_text()
				self.format_input()
		else:
			# Convert the string to ASCII values
			self.text = [ord(char) for char in self.text]

	# Converts text to 2d list of blocks, 16 values each, and pads the last block if needed
	def convert_to_blocks(self):
		self.blocks = [self.text[i:i + 16] for i in range(0, len(self.text), 16)]

		# Pad blocks with Ansi X9.23 padding (Pad will all 0s then w/ num_padding in last position
		num_padding = 16 - len(self.text) % 16
		padding = False
		while len(self.blocks[-1]) < 16:
			padding = True
			self.blocks[-1].append(0)  # Pad with 0s
		if padding:
			self.blocks[-1][-1] = num_padding

	def run(self):
		print(("Please choose from the following menu: \n"
		       + "1: Run AES128 Encryption\n"
		       + "2: Run AES128 Decryption\n"
		       + "3: Exit Program\n"))

		choice = int(input())

		if self.text == "":
			self.change_text()

		self.format_input()

		self.convert_to_blocks()

		if choice == 1:
			block_choice = int(input("Which block mode would you like to use? \n " + " 1: ECB Mode "))
			if block_choice == 1:
				ecb(self.blocks, self.key)

		if choice == 2:
			block_choice = int(input("Which block mode would you like to use? \n " + " 1: ECB Mode "))
			if block_choice == 1:
				ecb(self.blocks, self.key, enc=False)

		elif choice == 3:
			exit()


if __name__ == "__main__":
	c = Console()
	c.run()
