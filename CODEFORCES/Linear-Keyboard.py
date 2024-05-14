t = int(input())
for _ in range(t):
    idx = {}
    letters = input()
    for i in range(26):
        idx[letters[i]] = i
    s = input()
    res = 0
    for i in range(1, len(s)):
        res += abs(idx[s[i]] - idx[s[i - 1]])
    print(res)