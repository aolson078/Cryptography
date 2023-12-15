from rich import print
from rich.console import Console
from rich.theme import Theme
from aes128 import AES

"""Console and Theme settings"""
custom_theme = Theme({"info": "bold cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)


def main():
	console.print(("Please choose from the following menu: \n"
	               + "1: Run AES128\n"
	               + "2: Exit Program\n"), style="info")

	# choice = int(input())
	choice = 1

	print()

	if choice == 1:
		# Take user input in clear text for state
		aes = AES(
			[[0x0F, 0x0E, 0x0D, 0x0C], [0x0B, 0x0A, 0x09, 0x08], [0x07, 0x06, 0x05, 0x04], [0x03, 0x02, 0x01, 0x00]])
		key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
		subkeys = aes.generate_subkeys(key)

		# Initial key addition
		aes.state = aes.add_round_key(subkeys[0])

		for i in range(9):
			# Byte Substitution layer
			aes.sbox()
			# Shift left second row once, third row twice, fourth row three times
			aes.shift_rows()
			# Mix columns with galois multiplication specified in AES algorithm
			aes.mix_columns()
			# aes.inv_mix_columns()

			aes.state = aes.add_round_key(subkeys[i + 1])

		# replaces each byte in state with a corresponding byte from a nonlinear substitution table (S-box).
		# This step introduces non-linearity into the encryption process
		aes.sbox()
		aes.shift_rows()
		aes.state = aes.add_round_key(subkeys[-1])


		return aes.state

	elif choice == 2:
		exit()


print(main())
