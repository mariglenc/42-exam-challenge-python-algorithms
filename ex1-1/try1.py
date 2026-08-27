# ex1-1 - nebula_compressor
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def nebula_compressor(operation: str, data: str) -> str:
    if operation == "compress":
        return compress(data)
    if operation == "decompress":
        return decompress(data)
    return "Error"

def compress(text: str) -> str:
    if not text:                # If the input is empty
        return ""               # there's nothing to compress

    pieces = []                 # will hold each encoded run, e.g. ["a3", "b", "c2"]
    run_char = text[0]          # the character of the current "run"
    run_length = 1              # how long the current run is (we've seen 1 so far)

    for char in text[1:]:       # Walk through the rest of the text, starting at the 2nd character
        if char == run_char:    # Same character as before -> the run continues
            run_length += 1
        else:                   # Different character -> the run just ended.
            pieces.append(encode_run(run_char, run_length))     # Encode the finished run and save it...
            run_char = char                                     # ...then start a brand new run with this new character
            run_length = 1

    pieces.append(encode_run(run_char, run_length))     # The loop ends while we're still "inside" the last run, so we must encode and save that final run too

    return "".join(pieces)                              # Glue all encoded runs together into one string, e.g. "a3bc2"


def encode_run(char: str, length: int) -> str:
    encoded = ""
    while length > 9:
        encoded += char + "9"
        length -= 9
    if length == 1:
        encoded += char
    else:
        encoded += char + str(length)
    return encoded



def encode_run_test(char: str, length: int) -> str:
    encoded = ""            # declare an empty string for encoded char
    while length > 9: # if leng is bigger than 9 it could be 20 so with while
        encoded += char + "9" # first we add 9 to that char and it becomes char9
        length -= 9 # we make length -9
    if length == 1: #  we also check if length is 1 just do char not char1
        encoded += char
    else:
        encoded += char + str(length) # else do char number but convert the number to string
    return encoded # and return it

# delcare an empty encoded string
# whilte 
# declare encoded empty string
# while length is bigger than 9 ->
    # return char append 9
# check if len is one return just char
# else return char and nr append to it
# at the end return the encoded

def decompress(text: str) -> str:
    pieces = []
    position = 0
    
    while position < len(text):
        char = text[position]
        next_is_digit = position + 1 < len(text) and text[position+1].isdigit()
        
        if next_is_digit:
            count = int(text[position+1])
            pieces.append(char * count)
            position += 2
        else:
            pieces.append(char)
            position += 1
        
    return "".join(pieces)

# declare pieces
# declare position
# while position is less the text len
    #

print(nebula_compressor("compress", "aaabbbcccc")) # "a3b3c4"
# print(nebula_compressor("compress", "abc")) # "abc"
# print(nebula_compressor("compress", "aaaaaaaaaaaa")) # "a9a3"
# print(nebula_compressor("compress", "")) # ""
# print(nebula_compressor("decompress", "a3b3c4")) # "aaabbbcccc"
# print(nebula_compressor("decompress", "x")) # "x"
# print(nebula_compressor("explode", "abc")) # "Error"