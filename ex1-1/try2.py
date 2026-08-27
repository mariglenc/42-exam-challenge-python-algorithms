# ex1-1 - nebula_compressor
# attempt: try2.py
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


def encode_run(run_text, run_length) -> str:
    encoded = ""

    while run_length > 9:
        encoded += run_text + "9"
        run_length -= 9
    if run_length == 1:
        encoded += run_text
    else:
        encoded += run_text + str(run_length)

    return encoded


def decompress(text: str) -> str:
    decompressed_pieces = []
    position = 0
    while position < len(text):
        char_to_decompress = text[position]
        next_char_is_digit = position + 1 < len(text) and text[position+1].isdigit()
        if next_char_is_digit:
            count = int(text[position+1])
            decompressed_pieces.append(char_to_decompress*count)
            position += 2
        else:
            decompressed_pieces.append(char_to_decompress)
            position += 1

    return "".join(decompressed_pieces)

