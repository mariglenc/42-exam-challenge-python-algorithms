# ex1-1 - nebula_compressor
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def nebula_compressor(operation: str, data: str) -> str:
    if operation == "compress":
        return compress(data)
    if operation == "decompress":
        return decompress(data)
    return "Error"

def compress(text: str) -> str:
    if not text:
        return ""
    encoded_pieces = []
    run_char = text[0]
    run_len = 1
    for char in text[1:]:
        if char in run_char:
            run_len += 1
        else:
            encoded_pieces.append(encode_run(run_char, run_len))
            run_char = char
            run_len = 1
    encoded_pieces.append(encode_run(run_char, run_len))
    return "".join(encoded_pieces)

#if not text retunr empty string
# delcare the encoded_pieces and empty list 
# declare the curent run char and curent run length
# iterate over chars of text from index 1
# if char is on run char increase the run len
# else 
    # first append the current char and length
    # set the new run char and length to 1
    # continue iteration at the end we append againb 
#return the string with "".join encoded peices

def encode_run(text: str, length: int) -> str:
    encoded = ""
    while length > 9:
        encoded += text + "9"
        length -= 9
    if length == 1:
        encoded += text
    else:
        encoded += text + str(length)

    return encoded

# declare the encoded string
# iterate over the length while it is bigger than 9
# append to encoded the text and 9 and minus 9 on each iteration
# if length is one append onlt text
# else append text and lebght
# return the encoded

def decompress(text: str) -> str:
    decoded_pieces = []
    position = 0
    while position < len(text):
        char_to_explode = text[position]
        is_next_digit = position+1 < len(text) and text[position+1].isdigit()
        if is_next_digit:
            count = int(text[position+1])
            decoded_pieces.append(char_to_explode * count)
            position += 2
        else:
            decoded_pieces.append(char_to_explode)
            position += 1
    return "".join(decoded_pieces)

# declare a list for decoded_pieces and position
# iterate while position is less the length of text
# declare char_to_explode with text[position]
        