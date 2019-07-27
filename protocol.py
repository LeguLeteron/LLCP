from tkinter import Tk
import braille as b


def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except:
        raise LookupError
    return result

