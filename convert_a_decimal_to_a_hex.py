# 5 Convert a decimal to a hex

"""For this challenge, you need to write a function in Python that accepts a string of ASCII characters. 
It should return each character's value as a hexadecimal string. 
Separate each byte by a space, and return all alpha hexadecimal characters as lowercase."""


def decimal_to_hex(string1):

    hex_conversion = "Hex =  "

    for i in string1:
        ascii_string1 = ord(i.lower())
        hex_conversion += hex(int(ascii_string1))[2:] + " "

    return hex_conversion


print(decimal_to_hex("123456789"))
print(decimal_to_hex("abcdefghijklmnopqrstuvwxyz"))
print(decimal_to_hex("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
