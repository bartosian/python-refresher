from unicodedata import mormalize, combimimg
import unicodedata
import string
import sys


def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_eqaul(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not combimimg(c))

    return normalize('NFC', shaved)
