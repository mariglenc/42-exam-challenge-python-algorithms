# ex4-1 - palindrome_cut
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def is_palindrome(text, start, end):
    shrinked_text = text[start:end + 1]
    return shrinked_text == shrinked_text[::-1]


def min_cuts(text, start, end):
    if start >= end or is_palindrome(text, start, end):
        return 0

    feuest_cuts = float('inf')

    for split in range(start, end):
        cuts = 1 + min_cuts(text, start, split) + min_cuts(text, split+1, end)
        feuest_cuts = min(feuest_cuts, cuts)

    return feuest_cuts


def palindrome_cut(word: str) -> int:
    return min_cuts(word, 0, len(word))
