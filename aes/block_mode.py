# DO NOT USE FOR ACTUAL SECURITY/PRODUCTION, NOT CRYPTOGRAPHICALLY SECURE!!!!!!!!!!!!!!!!
# Written by Alex Olson
# This file contains the block modes of operation to run aes128

from encrypt import encrypt, decrypt
from util import to_hex


# ECB block cipher mode. enc=True to encrypt, enc=False to decrypt. Takes list of blocks and key as input
def ecb(blocks, key, enc=True):
    # Run aes128 on each block
    full_output = [to_hex(encrypt([block[i:i + 4] for i in range(0, 16, 4)], key)) if enc
                   else to_hex(decrypt([block[i:i + 4] for i in range(0, 16, 4)], key)) for block in blocks]
    return full_output


# CBC block cipher mode. enc=True to encrypt, enc=False to decrypt. Takes list of blocks and key as input
# Encrypts the IV with the key, then xors the result with the block of plaintext, giving us the ciphertext block.
def cbc(blocks, key, enc=True, IV=0):
    # Run aes128 on each block
    full_output = []
    if not enc:
        IV = len(blocks)

    # Initialize a 2D list with zeros
    IV_list = [[0 for _ in range(4)] for _ in range(4)]

    # Replace the last element of the last block with the IV
    IV_list[-1][-1] = IV

    for block in blocks:
        text = [block[i:i + 4] for i in range(0, 16, 4)]
        if enc:
            encrypted_IV = encrypt(IV_list, key)

            # XOR the encrypted IV with the plaintext block
            result = [[elem1 ^ elem2 for elem1, elem2 in zip(encrypted_IV, text)]
                      for encrypted_IV, text in zip(encrypted_IV, text)]
        else:
            result = decrypt(IV_list, key) ^ text # NOT GOING TO WORK CURRENTLY
        cipher_hex_output = to_hex(result)
        full_output.append(cipher_hex_output)
    return full_output
