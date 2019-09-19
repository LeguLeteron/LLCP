import hgtk
import braille_support as support

HANGUL = 1
LATIN = 2
OTHERS = 3

hangul = support.HangulCharts()
latin = support.LatinCharts().latin


def remove_acl_violation(target):
    acl = list()
    acl += list(map(chr, range(ord('a'), ord('z'))))
    acl += list(map(chr, range(ord('A'), ord('Z'))))
    acl += list(map(chr, range(ord('1'), ord('9'))))
    ret = ""
    for i in target:
        if i in acl or hgtk.checker.is_hangul(i):
            ret += i
    return ret


def check(target):
    target = remove_acl_violation(target)

    if hgtk.checker.is_latin1(target):
        return LATIN
    elif hgtk.checker.is_hangul(target):
        return HANGUL
    else:
        return OTHERS


def create(target):
    target = remove_acl_violation(target)

    ret = list()
    for char in target:
        if check(char) is HANGUL:
            letter = hgtk.text.decompose(char)[:-1]
            syllable = list()
            try:
                syllable.append(hangul.initial[letter[0]])
                syllable.append(hangul.vowel[letter[1]])
                syllable.append(hangul.final[letter[2]])
            except:
                pass
            ret.append(tuple(syllable))
        elif check(char) == LATIN:
            try:
                ret.append(latin[char.upper()])
            except:
                ret.append(latin[char])
        elif check(char) == OTHERS:
            raise ValueError

    return tuple(ret)


def beautify(target):
    ret = list()
    for i in target:
        if len(i) is 6:
            ret.append(i)
        else:
            for j in i:
                if len(j) is 6:
                    ret.append(j)
                else:
                    for k in j:
                        ret.append(k)

    return tuple(ret)