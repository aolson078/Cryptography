import ast

def format_input(string):
    if len(string) != 16:
        raise ValueError("String must be exactly 16 bytes/chars")
    output = [[], [], [], []]
    for i in range(4):
        output[0].append(ord(string[i]))
    for i in range(4, 8):
        output[1].append(ord(string[i]))
    for i in range(8, 12):
        output[2].append(ord(string[i]))
    for i in range(12, 16):
        output[3].append(ord(string[i]))
    return output


def format_output(cipher):
    output = ""
    for i in cipher:
        for j in i:
            if len(hex(j)) == 4:
                output += (hex(j)[2:])
            else:
                output += "0"
                output += (hex(j)[2:])
    return output


def normalize_input_for_decrypt(cipher):
    if type(cipher) == str and len(cipher) == 32:
        cipher = [[int(cipher[i:i + 2], 16) for i in range(0, 32, 2)][j:j + 4] for j in range(0, 16, 4)]
    elif type(cipher) == str and len(cipher) > 32:
        cipher_list = ast.literal_eval(cipher)
        if type(cipher_list) == tuple:
            cipher_list = list(cipher_list)
            return cipher_list
        cipher = [[], [], [], []]
        for i in range(4):
            cipher[0].append(cipher_list[i])
        for i in range(4, 8):
            cipher[1].append(cipher_list[i])
        for i in range(8, 12):
            cipher[2].append(cipher_list[i])
        for i in range(12, 16):
            cipher[3].append(cipher_list[i])
        return cipher
    elif type(cipher) == list and len(cipher) == 16:
        cipher = [cipher[i:i + 4] for i in range(0, 16, 4)]
    else:
        raise TypeError("Invalid input for decryption")
    return cipher


# Function takes 2d list (of size 1) as input and outputs string of hex values
def to_hex(string):
    output = ''.join(['0' + hex(j)[2:] if len(hex(j)[2:]) == 1 else hex(j)[2:] for i in string for j in i])
    return output