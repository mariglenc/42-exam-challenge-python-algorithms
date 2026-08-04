def word_ladder_builder(start: str, end: str, wordlist: list[str]) -> int:

    if end not in wordlist:
        return 0

    queue = [(start,1)]
    visited = set()
    visited.add(start)


    while queue:
        word, steps = queue.pop(0)

        if word == end:
            return steps


        for next_word in wordlist:
            if next_word not in visited:
                diff = 0

                for i in range(len(word)):
                    if word[i] != next_word[i]:
                        diff += 1


                if diff == 1:
                    queue.append((next_word, steps+1))
                    visited.add(next_word)

    return 0