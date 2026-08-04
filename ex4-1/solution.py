def palindrome_cut(word: str) -> int:
    s = word.lower().replace(" ", "")
    length = len(s)

    if length <= 1:
        return 0

    # dp[i] = min cuts for s[:i+1]; expand around every palindrome centre
    dp = [i for i in range(length)]

    def expand(left, right):
        while left >= 0 and right < length and s[left] == s[right]:
            if left == 0:
                dp[right] = 0
            else:
                dp[right] = min(dp[right], dp[left - 1] + 1)
            left -= 1
            right += 1

    for i in range(length):
        expand(i, i)
        expand(i, i + 1)

    return dp[length - 1]
