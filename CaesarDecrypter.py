shift = 3
text = "KHOOR ZRUOG"
converted= ""

for char in text:

    if char.isupper():

        char_unicode = ord(char)

        char_index = ord(char) - ord("A")

        new_index = (char_index - shift) % 26

        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        converted = converted + new_character

    else:
        converted += char

print("Encrypted text is:",text)

print("Decrypted text is:",converted)