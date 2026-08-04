def nebula_compressor(operation: str, data: str) -> str:
    if operation not in ("compress", "decompress"):
        return "Error"

    if not data:
        return ""

    if operation == "compress":
        result = []

        current = data[0]
        count = 1

        for ch in data[1:]:
            if ch == current:
                count += 1
            else:
                while count > 9:
                    result.append(f"{current}9")
                    count -= 9

                if count == 1:
                    result.append(current)
                else:
                    result.append(f"{current}{count}")

                current = ch
                count = 1

        # Process the final run
        while count > 9:
            result.append(f"{current}9")
            count -= 9

        if count == 1:
            result.append(current)
        else:
            result.append(f"{current}{count}")

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


print(nebula_compressor("decompress", "hel24o"))