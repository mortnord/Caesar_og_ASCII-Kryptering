def ASCII_Encode(text_to_encode):
    list_of_ascii = []
    list_of_hex = []
    for x in range(len(text_to_encode)):
        list_of_ascii.append(ord(text_to_encode[x]))

    for x in range(len(list_of_ascii)):
        list_of_hex.append(hex(list_of_ascii[x]).lstrip("0x"))
    result = "".join(list_of_hex)
    print(result)

def ASCII_Decode(text_to_decode):
    list_ascii = []
    for x in range(len(text_to_decode)):
        if(x % 2 == 1):

            value1 = text_to_decode[x]
            value2 = text_to_decode[x-1]

            hex_value = (str(value2) + str(value1))
            bytes_object = bytes.fromhex(hex_value)
            list_ascii.append(bytes_object.decode("ASCII"))
    print("".join(list_ascii))