# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
# This file contains the block modes of operation to run aes128

from encrypt import encrypt, decrypt
from util import to_hex


# ECB block cipher mode. enc=True to encrypt, enc=False to decrypt. Takes list of blocks and key as input
def ecb(blocks, key, enc=True):
    # Run aes128 on each block
    full_output = [to_hex(encrypt([block[i:i + 4] for i in range(0, 16, 4)], key))if enc
                   else to_hex(decrypt([block[i:i + 4] for i in range(0, 16, 4)], key)) for block in blocks]

    # Return final value
    return full_output
