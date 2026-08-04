def word_ladder_builder(start: str, end: str, wordlist: list[str]) -> int:
    if end not in wordlist:
        return 0

    if start not in wordlist:
        wordlist.append(start)

    lista_e_placeh = dict()

    for word in wordlist:
        for i in range(len(word)):
            placeh = word[:i]+"*"+word[i+1:]
            if placeh not in lista_e_placeh.keys():
                lista_e_placeh[placeh] = list()
            lista_e_placeh[placeh].append(word)

    queue = list([start])
    visited = list([start])

    count = 1
    while queue:
        for i in range(len(queue)):
            print("que :",queue, "\nvisited :", visited)
            check = queue.pop(0)

            if check == end:
                return count

            for j in range(len(check)):
                pattern = check[:j]+"*"+check[j+1:]
                for version in lista_e_placeh[pattern]:
                    if version not in visited:
                        queue.append(version)
                        visited.append(version)
        count += 1
        print(lista_e_placeh)

    return 0


print(word_ladder_builder("hit", "cog", ["hot","doti","dog","lot","log","cog"]))
print("\n\n")