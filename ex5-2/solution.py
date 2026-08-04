from collections import deque


def word_ladder_builder(start: str, end: str, wordlist: list[str]) -> int:
    if end not in wordlist:
        return 0

    queue = deque([(start, 1)])
    visited = {start}

    while queue:
        word, steps = queue.popleft()

        if word == end:
            return steps

        for candidate in wordlist:
            if candidate in visited or len(candidate) != len(word):
                continue

            diff = 0
            for i in range(len(word)):
                if word[i] != candidate[i]:
                    diff += 1

            if diff == 1:
                queue.append((candidate, steps + 1))
                visited.add(candidate)

    return 0


if __name__ == "__main__":
    print(word_ladder_builder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(word_ladder_builder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))         # 0
