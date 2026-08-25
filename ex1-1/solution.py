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
    run_char = text[0]   # the character we're currently counting
    run_length = 1       # how many times we've seen it in a row

    for char in text[1:]:
        if char == run_char:
            run_length += 1
        else:
            pieces.append(encode_run(run_char, run_length))
            run_char = char
            run_length = 1

    pieces.append(encode_run(run_char, run_length))  # don't forget the last run
    return "".join(pieces)


def encode_run(char: str, length: int) -> str:
    """Turn one run into text: 'a',1 -> 'a'   'a',4 -> 'a4'   'a',12 -> 'a9a3'"""
    encoded = ""
    while length > 9:            # split long runs into chunks of 9
        encoded += char + "9"
        length -= 9
    if length == 1:
        encoded += char          # single characters stay plain
    else:
        encoded += char + str(length)
    return encoded


def decompress(text: str) -> str:
    pieces = []
    position = 0

    while position < len(text):
        char = text[position]
        next_is_digit = position + 1 < len(text) and text[position + 1].isdigit()

        if next_is_digit:
            count = int(text[position + 1])
            pieces.append(char * count)
            position += 2        # we consumed the char AND the digit
        else:
            pieces.append(char)
            position += 1

    return "".join(pieces)

print(nebula_compressor("compress", "aaabbbcccc")) # "a3b3c4"
print(nebula_compressor("compress", "abc")) # "abc"
print(nebula_compressor("compress", "aaaaaaaaaaaa")) # "a9a3"
print(nebula_compressor("compress", "")) # ""
print(nebula_compressor("decompress", "a3b3c4")) # "aaabbbcccc"
print(nebula_compressor("decompress", "x")) # "x"
print(nebula_compressor("explode", "abc")) # "Error"