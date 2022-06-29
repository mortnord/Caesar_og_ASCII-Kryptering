import datetime

def Encode(text_to_encode, nr_shift):
    text_to_encode = text_to_encode.upper()
    text_to_encode = text_to_encode.strip()
    text_to_encode = text_to_encode.replace(" ", "")
    global letter_to_replace
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWYZÆØÅ"
    list_of_text_to_encode = list(text_to_encode)
    for x in range(len(list_of_text_to_encode)):
        nr_letter = alphabet.find(list_of_text_to_encode[x])
        letter_to_replace = nr_letter + int(nr_shift)

        if letter_to_replace >= (len(alphabet)):
            letter_to_replace = letter_to_replace - len(alphabet)

        list_of_text_to_encode[x] = alphabet[letter_to_replace]
    print("".join(list_of_text_to_encode))

def Manual_Mode(text_to_encode):

    print("Hvor mye skal du vri med? ")
    nr_shift = input()
    Encode(text_to_encode, nr_shift)

def Automatic_Encode(text_to_encode):
    time_seed = datetime.datetime.now()
    seed = time_seed.hour*time_seed.minute*time_seed.second + time_seed.day*time_seed.month
    modulo_seed = seed % 29
    print(modulo_seed)
    text_to_encode = text_to_encode.upper()
    text_to_encode = text_to_encode.strip()
    text_to_encode = text_to_encode.replace(" ", "")
    global letter_to_replace
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWYZÆØÅ"
    list_of_text_to_encode = list(text_to_encode)
    for x in range(len(list_of_text_to_encode)):
        nr_letter = alphabet.find(list_of_text_to_encode[x])
        letter_to_replace = nr_letter + int(modulo_seed)

        if letter_to_replace >= (len(alphabet)):
            letter_to_replace = letter_to_replace - len(alphabet)

        list_of_text_to_encode[x] = alphabet[letter_to_replace]
    print("".join(list_of_text_to_encode))