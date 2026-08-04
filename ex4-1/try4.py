# ex4-1 - palindrome_cut
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

# check if this text from taht start to end is palindrome
def is_palindrome(text, start, end):
    shrinked_text = text[start:end + 1] # question: why we do + 1 here is it because slicing does does not incude end ?
    
    return shrinked_text == shrinked_text[::-1]


def min_cuts(text, start, end): # find the min cuts nr
    if start >= end or is_palindrome(text, start, end): # if start eq end - one word is palindroem
        return 0    # if start bg than end is empty, if is palindorme again return 0 cuts
   
    feuest_cuts = float('inf')  # decalre feuest cuts with float inf
    
    for split in range(start, end):
        cuts = 1 + min_cuts(text, start, split) + min_cuts(text, split+1, end) # why we do that one time at end one time at start + 1 
        # another question why cuts has 1 + 
        # what happens if a word is palindrome already 
        # so how can i undertsnad or visuallize better this exercise ?
        feuest_cuts = min(cuts, feuest_cuts)
        
    return feuest_cuts


def palindrome_cut(word: str) -> int:
    return min_cuts(word, 0, len(word))
