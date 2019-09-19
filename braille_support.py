'''
O O | 1 2
O O | 3 4
O O | 5 6
'''

ON = 1
OFF = 0


class HangulCharts:
    initial = {
        "ㄱ": (OFF, ON, OFF, OFF, OFF, OFF),
        "ㄴ": (ON, ON, OFF, OFF, OFF, OFF),
        "ㄷ": (OFF, ON, ON, OFF, OFF, OFF),
        "ㄹ": (OFF, OFF, OFF, ON, OFF, OFF),
        "ㅁ": (ON, OFF, OFF, ON, OFF, OFF),
        "ㅂ": (OFF, ON, OFF, ON, OFF, OFF),
        "ㅅ": (OFF, OFF, OFF, OFF, OFF, ON),
        "ㅇ": (ON, ON, ON, ON, OFF, OFF),
        "ㅈ": (OFF, ON, OFF, OFF, OFF, ON),
        "ㅊ": (OFF, OFF, OFF, ON, OFF, ON),
        "ㅋ": (ON, ON, ON, OFF, OFF, OFF),
        "ㅌ": (ON, OFF, ON, ON, OFF, OFF),
        "ㅍ": (ON, ON, OFF, ON, OFF, OFF),
        "ㅎ": (OFF, ON, ON, ON, OFF, OFF),
    }
    vowel = {
        "ㅏ": (ON, OFF, ON, OFF, OFF, ON),
        "ㅑ": (OFF, ON, OFF, ON, ON, OFF),
        "ㅓ": (OFF, ON, ON, OFF, ON, OFF),
        "ㅕ": (ON, OFF, OFF, ON, OFF, ON),
        "ㅗ": (ON, OFF, OFF, OFF, ON, ON),
        "ㅛ": (OFF, ON, OFF, OFF, ON, ON),
        "ㅜ": (ON, ON, OFF, OFF, ON, OFF),
        "ㅠ": (ON, ON, OFF, OFF, OFF, ON),
        "ㅡ": (OFF, ON, ON, OFF, OFF, ON),
        "ㅣ": (ON, OFF, OFF, ON, ON, OFF),
        "ㅐ": (ON, OFF, ON, ON, ON, OFF),
        "ㅔ": (ON, ON, OFF, ON, ON, OFF),
        "ㅒ": ((OFF, ON, OFF, ON, ON, OFF), (ON, OFF, ON, ON, ON, OFF)),
        "ㅖ": (OFF, ON, OFF, OFF, ON, OFF),
        "ㅘ": (ON, OFF, ON, OFF, ON, ON),
        "ㅙ": ((ON, OFF, ON, OFF, ON, ON), (ON, OFF, ON, ON, ON, OFF)),
        "ㅚ": (ON, ON, OFF, ON, ON, ON),
        "ㅝ": (ON, ON, ON, OFF, ON, OFF),
        "ㅞ": ((ON, ON, ON, OFF, ON, OFF), (ON, OFF, ON, ON, ON, OFF)),
        "ㅟ": ((ON, ON, OFF, OFF, ON, OFF), (ON, OFF, ON, ON, ON, OFF)),
        "ㅢ": (OFF, ON, ON, ON, OFF, ON)
    }
    final = {
        "ㄱ": (ON, OFF, OFF, OFF, OFF, OFF),
        "ㄴ": (OFF, OFF, ON, ON, OFF, OFF),
        "ㄷ": (OFF, OFF, OFF, ON, ON, OFF),
        "ㄹ": (OFF, OFF, ON, OFF, OFF, OFF),
        "ㅁ": (OFF, OFF, ON, OFF, OFF, ON),
        "ㅂ": (ON, OFF, ON, OFF, OFF, OFF),
        "ㅅ": (OFF, OFF, OFF, OFF, ON, OFF),
        "ㅇ": (OFF, OFF, ON, ON, ON, ON),
        "ㅈ": (ON, OFF, OFF, OFF, ON, OFF),
        "ㅊ": (OFF, OFF, ON, OFF, ON, OFF),
        "ㅋ": (OFF, OFF, ON, ON, ON, OFF),
        "ㅌ": (OFF, OFF, ON, OFF, ON, ON),
        "ㅍ": (OFF, OFF, ON, ON, OFF, ON),
        "ㅎ": (OFF, OFF, OFF, ON, ON, ON),
    }


class LatinCharts:
    latin = {
        "A": (ON, OFF, OFF, OFF, OFF, OFF),
        "B": (ON, OFF, ON, OFF, OFF, OFF),
        "C": (ON, ON, OFF, OFF, OFF, OFF),
        "D": (ON, ON, OFF, ON, OFF, OFF),
        "E": (ON, OFF, OFF, ON, OFF, OFF),
        "F": (ON, ON, ON, OFF, OFF, OFF),
        "G": (ON, ON, ON, ON, OFF, OFF),
        "H": (ON, OFF, ON, ON, OFF, OFF),
        "I": (OFF, ON, ON, OFF, OFF, OFF),
        "J": (OFF, ON, ON, ON, OFF, OFF),
        "K": (ON, OFF, OFF, OFF, ON, OFF),
        "L": (ON, OFF, ON, OFF, ON, OFF),
        "M": (ON, ON, OFF, OFF, ON, OFF),
        "N": (ON, ON, OFF, ON, ON, OFF),
        "O": (ON, OFF, OFF, ON, ON, OFF),
        "P": (ON, ON, ON, ON, ON, OFF),
        "Q": (ON, ON, ON, ON, ON, OFF),
        "R": (ON, OFF, ON, ON, ON, OFF),
        "S": (OFF, ON, ON, OFF, ON, OFF),
        "T": (OFF, ON, ON, ON, ON, OFF),
        "U": (ON, OFF, OFF, OFF, ON, ON),
        "V": (ON, OFF, ON, OFF, ON, ON),
        "W": (OFF, ON, ON, ON, OFF, ON),
        "X": (ON, ON, OFF, OFF, ON, ON),
        "Y": (ON, ON, OFF, ON, ON, ON),
        "Z": (ON, OFF, OFF, ON, ON, ON),
        "#": (OFF, ON, OFF, ON, ON, ON),
        "1": ((OFF, ON, OFF, ON, ON, ON), (ON, OFF, OFF, OFF, OFF, OFF)),
        "2": ((OFF, ON, OFF, ON, ON, ON), (ON, OFF, ON, OFF, OFF, OFF)),
        "3": ((OFF, ON, OFF, ON, ON, ON), (ON, ON, OFF, OFF, OFF, OFF)),
        "4": ((OFF, ON, OFF, ON, ON, ON), (ON, ON, OFF, ON, OFF, OFF)),
        "5": ((OFF, ON, OFF, ON, ON, ON), (ON, OFF, OFF, ON, OFF, OFF)),
        "6": ((OFF, ON, OFF, ON, ON, ON), (ON, ON, ON, OFF, OFF, OFF)),
        "7": ((OFF, ON, OFF, ON, ON, ON), (ON, ON, ON, ON, OFF, OFF)),
        "8": ((OFF, ON, OFF, ON, ON, ON), (ON, OFF, ON, ON, OFF, OFF)),
        "9": ((OFF, ON, OFF, ON, ON, ON), (OFF, ON, ON, OFF, OFF, OFF)),
        "0": ((OFF, ON, OFF, ON, ON, ON), (OFF, ON, ON, ON, OFF, OFF))
    }
