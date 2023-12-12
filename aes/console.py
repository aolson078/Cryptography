from rich import print
from rich import inspect
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import aes128

"""Console and Theme settings"""
custom_theme = Theme({"info": "bold cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)


def main():
	console.print(("Please choose from the following menu: \n"
	               + "1: Run AES128\n"
	               + "2: Exit Program\n"), style="info")

	choice = int(input())

	print()

	if choice == 1:
		# Take user input for clear text
		clear_text = [[0x0F, 0x0E, 0x0D, 0x0C], [0x0B, 0x0A, 0x09, 0x08], [0x07, 0x06, 0x05, 0x04],
		              [0x03, 0x02, 0x01, 0x00]]
		state = clear_text

		# Key will be 128 bits for AES-128
		key = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
		subkeys = aes128.generate_subkeys(key)

		# Initial key addition
		state = aes128.add_round_key(state, subkeys[0])

		for i in range(9):
			state = aes128.add_round_key(aes128.round_layers(state), subkeys[i + 1])

		state = aes128.add_round_key(aes128.last_round(state), subkeys[-1])

		return state

	elif choice == 2:
		exit()


print(main())
