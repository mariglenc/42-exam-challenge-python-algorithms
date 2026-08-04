# ex4-1 - palindrome_cut
# attempt: try5.py
# (signature pre-filled from the .en; write your solution below)

def is_palindrome(text, start, end):
    shrinked_word=text[start:end+1]
    return shrinked_word==shrinked_word[::-1]

def small_cut(text,start,end):
    if start >= end or is_palindrome(text,start,end):
        return 0

    few_cuts = float('inf')

    for split in range(start,end):
        cuts = 1 + small_cut(text,start,split) + small_cut(text,split+1,end)
        few_cuts = min(cuts,few_cuts)

    return few_cuts

def palindrome_cut(word: str) -> int:
    return small_cut(word,0,len(word))

