MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        try:
            cipher += MORSE_CODE_DICT[letter] + ' '
        except KeyError:
            print(f"\nInvalid character found: '{letter}' - refer to morse code alphabet")
            break
    return cipher

def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    try:
        for letter in message:
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ''
    except ValueError:
        print(f"\nInvalid character found")

    return decipher

def main():
    message = input("Enter word: ")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if direction == "encode":
        result = encrypt(message.upper())
        print(result)
    elif direction == "decode":
        result = decrypt(message)
        print(result)
    else:
        print(f"Invalid command: {direction}")
        main()

if __name__ == '__main__':
    main()