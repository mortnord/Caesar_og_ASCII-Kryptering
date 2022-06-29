import datetime
import CaesarChiffering
import ASCII_Encoder


print("Input 1 for manual mode, eller 2 for automatisk, Input 3 for ASCII encoding, Input 4 for ASCII Decoding")
mode = input()

print("Hva skal du kode/dekode?")
text_to_encode = input()
if mode == str(1):
    CaesarChiffering.Manual_Mode(text_to_encode)
elif mode == str(2):
    CaesarChiffering.Automatic_Encode(text_to_encode)
elif mode == str(3):
    ASCII_Encoder.ASCII_Encode(text_to_encode)
elif mode == str(4):
    ASCII_Encoder.ASCII_Decode(text_to_encode)