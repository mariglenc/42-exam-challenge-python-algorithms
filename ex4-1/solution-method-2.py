def is_palindrome(text, start, end):
    text_piece = text[start:end+1]              # grab the sub-string (end+1 because slicing excludes end)
    return text_piece == text_piece[::-1]       # compare it to its reverse

def min_cuts_between(text, start, end):
    if start >= end or is_palindrome(text, start, end):
        return 0

    best = float('inf')

    for split in range(start, end):
        cuts = 1 + min_cuts_between(text, start, split) + min_cuts_between(text, split + 1, end)
        best = min(best, cuts)

    return best

def palindrome_cut(word: str) -> int:
    return min_cuts_between(word, 0, len(word) - 1)

print(palindrome_cut("aab"))      # 1  -> aa | b


# "aab" is not a palindrome → try splits:

# split=0:  "a" | "ab"
#           "a"  = 0 cuts
#           "ab" = not palindrome → recurses → 1 cut
#           total = 1 + 0 + 1 = 2

# split=1:  "aa" | "b"
#           "aa" = 0 cuts (palindrome)
#           "b"  = 0 cuts
#           total = 1 + 0 + 0 = 1   ← smaller!

# best = min(2, 1) = 1
