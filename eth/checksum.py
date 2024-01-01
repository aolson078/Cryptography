from Crypto.Hash import keccak


def hash_address(address):
	address = address.lower().replace('0x', '')
	k = keccak.new(digest_bits=256)
	k.update(address.encode('utf-8'))  # encode the address as UTF-8
	return k.hexdigest()


def check_sum(address):
	lowercase_address = address.lower()
	address = address.replace('0x', '')
	digest = hash_address(lowercase_address)
	for i in range(len(address)):
		# if the ith digit of digest is 0x8 or more, if so, check if the ith digit of address is upper, if not, return False
		if int(digest[i], 16) >= 0x8 and address[i].islower():
			return False
		# if the ith digit of digest is 0x7 or less, if so, check if the ith digit of address is lower, if not, return False
		elif int(digest[i], 16) <= 0x7 and address[i].isupper():
			return False

	return True


def main():
	address = '001d3f1ef827552ae1114027bd3ecf1f086ba0F9'
	digest = hash_address(address)
	new_address = ''
	for i in range(len(address)):
		if address[i].isalpha() and int(digest[i], 16) >= 0x8:
			new_address += address[i].upper()
		else:
			new_address += address[i]

	print(check_sum('001d3F1ef827552Ae1114027BD3ECF1f086bA0E9')) # Invalid address, should return False
	print(check_sum(new_address))


main()
