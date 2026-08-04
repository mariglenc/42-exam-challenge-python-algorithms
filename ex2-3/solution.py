def nebula_compressor(operation: str, data: str) -> str:
    if operation not in ("compress", "decompress"):
        return "Error"

    if not data:
        return ""

    if operation == "compress":
        result = []
        current = data[0]
        count = 1

        def flush(ch, n):
            while n > 9:
                result.append(f"{ch}9")
                n -= 9
            result.append(ch if n == 1 else f"{ch}{n}")

        for ch in data[1:]:
            if ch == current:
                count += 1
            else:
                flush(current, count)
                current = ch
                count = 1

        flush(current, count)
        return "".join(result)

    # decompress
    result = []
    i = 0
    while i < len(data):
        ch = data[i]
        if i + 1 < len(data) and data[i + 1].isdigit():
            result.append(ch * int(data[i + 1]))
            i += 2
        else:
            result.append(ch)
            i += 1

    return "".join(result)


if __name__ == "__main__":
    print(nebula_compressor("compress", "aaabbc"))     # a3b2c
    print(nebula_compressor("decompress", "hel2o"))    # hello
    print(nebula_compressor("explode", "abc"))         # Error
