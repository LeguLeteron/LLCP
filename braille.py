import hgtk
import braille_support as support

TEXT_HANGUL = 1
TEXT_LATIN = 2
TEXT_UNKNOWN = 3

hangul = support.HangulCharts()
latin = support.LatinCharts()


def check(target):
    if hgtk.checker.is_hangul(target):
        return TEXT_HANGUL
    elif hgtk.checker.is_latin1(target):
        return TEXT_LATIN
    else:
        return TEXT_UNKNOWN


def create(target):
        l, ret = list(), list()
        if check(target) is TEXT_HANGUL:
            l = hgtk.text.decompose(target).split("ᴥ")

            for i in l:
                tmp = list()
                try:
                    tmp.append(hangul.initial[i[0]])
                    tmp.append(hangul.vowel[i[1]])
                    tmp.append(hangul.final[i[2]])
                except:
                    pass
                ret.append(tuple(tmp))
        elif check(target) == TEXT_LATIN:
            pass
        elif check(target) == TEXT_UNKNOWN:
            raise ValueError
        return tuple(ret)


def show(target, mode):
    # To prevent data manipulation
    if type(target) is not tuple:
        raise RuntimeError

    if mode == TEXT_HANGUL:
        count = 0
        for i in target:
            for j in i:
                for k in j:
                    count += 1
                    if k is support.ON:
                        print("•", end=' ')
                    else:
                        print("◦", end=' ')

                    if (count % 2) is 0:
                        print("\n", end='')