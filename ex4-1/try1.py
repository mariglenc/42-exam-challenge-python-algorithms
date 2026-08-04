# ex4-1 - palindrome_cut
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def is_palindrome(text, start, end):
    text_s_e = text[start:end+1]
    return text_s_e == text_s_e[::-1]

def min_cuts_between(text, start, end):
    print("start,end=",start,end)
    if start >= end or is_palindrome(text, start, end):
        return 0

    fewest_cuts = float('inf')

    for split in range(start,end):
        cuts = 1 + min_cuts_between(text, start, split) + min_cuts_between(text, split+1, end) 
        fewest_cuts = min(fewest_cuts, cuts)

    return fewest_cuts


def palindrome_cut(word: str) -> int:
    return min_cuts_between(word, 0, len(word) - 1)


# check if is_palindrome with text start end
    # shrink the text to the start end
    # comapare the shrinked one with reversed shrikned one

# def min cuts 
# check if start bigger equal to end or is palindrome
    # if so return 0

# declare a feuest cuts var

# iterate over range start end
# declare cuts 1 + mincuts(text start split) + mincuts(text split+1 end)
# find the minimum of each iteration

# return mincuts

