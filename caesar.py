# Written by Alexander Olson
# Draft: 1

def caesar():
    1 + 1
    clear  = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out."
    cipher = ""
    shift = 12
    for i in range(len(clear)):

        # If the char is uppercase and needs to loop back to 'A'
        if (ord(clear[i]) + shift) >= 91 and chr(ord(clear[i])).isupper():
          cipher += chr(65 + ((ord(clear[i]) + shift) - 91))

        # If the char is lowercase and needs to loop back to 'a'
        elif (ord(clear[i]) + shift) >= 123 and chr(ord(clear[i])).islower():
          cipher += chr(97 + ((ord(clear[i]) + shift) - 123))

        elif clear[i] == " ":
          cipher += " "

        else:
            cipher += chr(((ord(clear[i]) + shift)))

    return cipher


print(caesar())