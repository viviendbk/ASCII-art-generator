def generate_ascii_art(text):
    characters = {
        'A': ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        'B': ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        'C': [" CCCC", "C    ", "C    ", "C    ", " CCCC"],
        'D': ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
        'E': ["EEEEE", "E    ", "EEEEE", "E    ", "EEEEE"],
        'F': ["FFFFF", "F    ", "FFFFF", "F    ", "F    "],
        'G': [" GGG ", "G    ", "G  GG", "G   G", " GGGG"],
        'H': ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
        'I': ["IIIII", "  I  ", "  I  ", "  I  ", "IIIII"],
        'J': [" JJJJ", "   J ", "   J ", "J  J ", " JJ  "],
        'K': ["K   K", "K  K ", "KK   ", "K  K ", "K   K"],
        'L': ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"],
        'N': ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
        'O': [" OOO ", "O   O", "O   O", "O   O", " OOO "],
        'P': ["PPPP ", "P   P", "PPPP ", "P    ", "P    "],
        'Q': [" QQQ ", "Q   Q", "Q Q Q", "Q  QQ", " QQQQ"],
        'R': ["RRRR ", "R   R", "RRRR ", "R R  ", "R  RR"],
        'S': [" SSS ", "S    ", " SSS ", "    S", "SSS  "],
        'T': ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
        'U': ["U   U", "U   U", "U   U", "U   U", " UUU "],
        'V': ["V   V", "V   V", "V   V", " V V ", "  V  "],
        'W': ["W   W", "W W W", "W W W", "W W W", " W W "],
        'X': ["X   X", " X X ", "  X  ", " X X ", "X   X"],
        'Y': ["Y   Y", " Y Y ", "  Y  ", "  Y  ", "  Y  "],
        'Z': ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
        ' ': ["     ", "     ", "     ", "     ", "     "],
        '0': [" OOO ", "O   O", "O  OO", "O   O", " OOO "],
        '1': ["  1  ", " 11  ", "  1  ", "  1  ", "1111"],
        '2': [" 222 ", "   2 ", "  2  ", " 2   ", "22222"],
        '3': ["3333 ", "    3", " 333 ", "    3", "3333 "],
        '4': ["   4 ", "  44 ", " 4 4 ", "44444", "   4 "],
        '5': ["55555", "5    ", "5555 ", "    5", "5555 "],
        '6': [" 666 ", "6    ", "6666 ", "6   6", " 666 "],
        '7': ["77777", "   7 ", "  7  ", " 7   ", "7    "],
        '8': [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
        '9': [" 999 ", "9   9", " 9999", "    9", " 999 "]
    }

    lines = [""] * 5  # 5 lines for each character

    for char in text.upper():
        if char in characters:
            char_lines = characters[char]
            for i in range(4):
                lines[i] += char_lines[i] + " "
        else:
            for i in range(4):
                lines[i] += " " * 6  # Default space for unknown characters

    return "\n".join(lines)

if __name__ == "__main__":
    user_input = input("Enter text to convert to ASCII art: ")
    result = generate_ascii_art(user_input)
    print(result)
