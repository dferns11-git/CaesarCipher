def encrypter(text,shift):

    result = ""
    #traverse the list of characters
    for x in range(len(text)):
        char=text[x]

        if(char.isupper()):
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += chr((ord(char) + shift - 65) % 26 + 65)
    return result

text = "CaesAR CIPHeR METHoD"
shift = 4

print("Plain Text: " + text)
print("Shift Pattern: " + str(shift))
print("Cipher: " + encrypter(text,shift))