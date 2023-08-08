"""initialize_state takes clear text in creates a 2d list of strings of individual hex values"""
def initialize_state(clear_text):
    return [['0x00', '0x01', '0x02', '0x03'],
             ['0x04', '0x05', '0x06', '0x07'],
             ['0x08', '0x09', '0x0A', '0x0B'],
             ['0x0C', '0x0D', '0x0E', '0x0F']]


def add_round_key(state, key):
    string = convert_to_string(state)
    result = int(string,16) ^ int(key[0], 16)
    hex_string = hex(result)[2:].zfill(32)
    result = convert_to_matrix(hex_string)
    return result


def convert_to_string(matrix):
    # Flatten the matrix and remove '0x' from each element
    hex_values = [value[2:] for sublist in matrix for value in sublist]
    # Join all hex values into a single string
    result = ''.join(hex_values)
    return result

def convert_to_matrix(hex_string):
    # Split the string into two-character chunks
    hex_values = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    # Add '0x' prefix to each element and group them into 4-element sublists
    matrix = [['0x' + hex_values[i+j] for j in range(4)] for i in range(0, len(hex_values), 4)]
    return matrix


"""sbox performs a byte substitution on the current state using the sbox lookup table specified in the AES algorithm.
https://en.wikipedia.org/wiki/Rijndael_S-box"""
def sbox(state):

    # Sbox for byte substitution
    sboxes = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
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
              0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0xd1, 0x9e,
              0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
              0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

    output_state = []

    for i in range(4):
        for j in range(4):
            output_state.append("0x" + str(sboxes[int(state[i][j], 16)]))

    return [output_state[i:i + 4] for i in range(0, len(output_state), 4)]

"""round_layers performs Byte Substitution, ShiftRow, MixColum, and KeyAddition layers for all rounds but the final round.
Takes current state as 2d list, outputs updated current state as 2d list."""
def round_layers(state):
    # Byte Substitution layer
    state = sbox(state)
    # Shift left second row once, third row twice, fourth row three times
    state = shift_rows(state)
    # Mix columns with galois multiplication specified in AES algorithm
    state = mix_columns(state)

    return state


"""last_round performs Byte Substitution, ShiftRow, and KeyAddition layers on last round of encryption"""
def last_round(state):
    return state


"""shift_rows takes state as a 2d list, and shifts left second row once, third row twice, fourth row 3 times, 
outputs the new current state as a 2d list """
def shift_rows(state):
    col0 = [state[0][0], state[1][1], state[2][2], state[3][3]]
    col1 = [state[1][0], state[2][1], state[3][2], state[0][3]]
    col2 = [state[2][0], state[3][1], state[0][2], state[1][3]]
    col3 = [state[3][0], state[0][1], state[1][2], state[2][3]]
    output = [col0, col1, col2, col3]
    return output


"""mix_columns takes the current state as input as a 2d list, calling mix_column with each list. Outputs the 
new current state as a 2d list. """
def mix_columns(state):
    new_state = [[],[],[],[]]
    for i in range(4):
        new_state[i] = mix_column(state[i])
    return new_state


"""mix_column takes a list of integers as an input, and performs galois multiplication on each item according to the 
table specified in the AES algorithm. Outputs new mixed column as a list of integers"""
def mix_column(column):
    # Compute the output column elements using the Galois multiplication and XOR
    r00 = galois_mult(int(column[0], 16), 2)
    r01 = galois_mult(int(column[1], 16), 3)
    r02 = int(column[2], 16)
    r03 = int(column[3], 16)

    r0 = (r00 ^ r01 ^ r02 ^ r03) # r0 is the first value of the column

    r10 = int(column[0], 16)
    r11 = galois_mult(int(column[1], 16), 2)
    r12 = galois_mult(int(column[2], 16), 3)
    r13 = int(column[3], 16)

    r1 = (r10 ^ r11 ^ r12 ^ r13)  # r1 is the second value of the column

    r20 = int(column[0], 16)
    r21 = int(column[1], 16)
    r22 = galois_mult(int(column[2], 16), 2)
    r23 = galois_mult(int(column[3], 16), 3)

    r2 = (r20 ^ r21 ^ r22 ^ r23)  # r1 is the second value of the column

    r30 = galois_mult(int(column[0], 16), 3)
    r31 = int(column[1], 16)
    r32 = int(column[2], 16)
    r33 = galois_mult(int(column[3], 16), 2)

    r3 = (r30 ^ r31 ^ r32 ^ r33)  # r1 is the second value of the column
    return [r0, r1, r2, r3]


"""galois_mult takes 2 integers as input, num and multiplier, and performs Galois field multiplication on num by 
multiplier in GF(2^8). Outputs result as an integer """
def galois_mult(num, multiplier):
    # Perform the Galois multiplication
    temp_mul = multiplier
    result = 0
    while multiplier:
        temp_num = num
        # check if LSB is 1
        if multiplier & 1:
            # XOR
            result ^= temp_num
        # multiply by two (equal to left shift)
        temp_num <<= 1
        # if temp_num is over 255, reduce bye irreducible polynomial 0x11b
        if temp_num & 0x100:
            temp_num ^= 0x11b
        multiplier >>= 1
        result = temp_num
    if temp_mul == 3:
        return result ^ num
    return result

"""generate subkey performs the key addition step and creates an array of 44 32-bit words. 
Each round uses a subkey made of 4 of these words. The first 4 words are the initial cipher key. 
Output a list of subkeys"""
def generate_subkeys(key):
    subkeys = [[] for _ in range(11)]
    subkeys[0] = key


    # 00 04 08 0c
    # 01 05 09 0d
    # 02 06 0a 0e
    # 03 07 0b 0f I NEED TO MAKE IT LIKE THIS





    # Round constant, used to xor with each subkey. After it is multiplied by 2. Rcon[1] = 1 Rcon[2] = 2 Rcon[3] = 4
    rcon = 1

    print("Original key", key)

    # AES-128 needs 11 subkeys all together. Other key lengths will require variable number of subkeys
    for i in range(10):
        # Word rotation: Take the previous 32-bit word, rotate it to the left by one byte.
        next_key = rotate_word_left(subkeys[i])

        split_subkey = [hex(int(next_key[i:i + 2],  16)) for i in range(0, len(next_key), 2)]
        temp_output_list = [split_subkey[i:i + 4] for i in range(0, len(split_subkey), 4)]
        output_list = [[f"{int(element, 16):#04x}" for element in sublist] for sublist in temp_output_list]

        # Byte substitution
        subkey = sbox(output_list)
        print("subkey: ", subkey)
        print(hex(125))
        flat_key = []
        for row in subkey:
            for key in row:
                flat_key.append(key[2:])
        print("flat subkey: ", flat_key)

        # Rcon operation: The first byte of the resulting word is XORed with the round constant (Rcon).
        flat_key[0] = int(flat_key[0]) ^ rcon
        # Rcon changes for each round and is predefined in the AES standard
        rcon <<= 1
        print("flat key: ", flat_key[0])
        break







        # Derive the rest of the round key: The next three 4-byte words are derived by XORing
        # the previously derived word with the 4-byte word that's 4 positions back.
    print("Subkeys: ", subkeys)
    return subkeys

"""rotate word takes a list of 4 bytes, and rotates it to the left by one byte. [0a, 1b, 2c, 3d] -> [ 1b, 2c, 3d, 0a]"""
def rotate_word_left(subkey):
    return subkey[2:] + subkey[:2]


def main():
    # Take user input for clear text
    clear_text = '000102030405060708090a0b05445436c0d0e0f'
    state = initialize_state(clear_text)

    # Key will be 128 bits for AES-128
    key = "000102030405060708090a0b0c0d0e0f"
    keys = generate_subkeys(key)

    # Initial key addition
    state = add_round_key(state, keys[0])
    print("state after add_key :", state)
    # for i in range(9):
    # 	round_layers(state)
    #   add_round_key(state, keys[i+1])

    state = round_layers(state)

    # last_round(state)

    print(rotate_word_left(key))

    cipher = ''  # encrypt(clear_text, key)
    return cipher


main()
