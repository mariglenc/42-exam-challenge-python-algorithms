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
    if not text:
        return ""
    pieces = []
    run_char = text[0] # the caracter we curenlty counting
    run_length = 1 # how many times we have seen it in a row
    
    for char in text[1::]:
        if char in run_char:
            run_length += 1
        else:
            pieces.append(encode_run(run_char,run_length))
            run_char = char
            run_length = 1
    pieces.append(encode_run(run_char, run_length))
    return "".join(pieces)


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

def decompress(text: str) -> str:
    pieces = []
    

