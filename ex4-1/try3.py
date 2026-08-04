# ex4-1 - palindrome_cut
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

# shrink the text from start to end+1 and comapre with reversed one of it
def is_palindrome(text, start, end):
    shrinked_text = text[start:end+1]
    return shrinked_text == shrinked_text[::-1]


def min_cuts(text, start, end):
    # chec if start the same with end 
        # it means is one letter so is palindrome so 0 cuts
    # if start bigger than 0 cuts, means is empty
    # or if is palindrome than again 0 cuts
    if start>=end or is_palindrome(text, start, end):
        return 0
    
    # declare feuest cuts var
    feuest_cuts = float('inf')
    
    # iterate over the range from start to end of the text
    for split in range(start,end):
        # cut from start to split and from split+1 to end
        cuts = 1 + min_cuts(text, start, split) + min_cuts(text, split+1, end)
        # find the fuest cuts with min fucnt
        feuest_cuts = min(feuest_cuts, cuts)
    
    # than return this nr
    return feuest_cuts


def palindrome_cut(word: str) -> int:
    return min_cuts(word,0,len(word)+1)

