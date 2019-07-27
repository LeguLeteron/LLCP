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
    pass