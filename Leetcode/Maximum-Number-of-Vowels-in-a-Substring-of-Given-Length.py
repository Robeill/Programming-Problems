class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        check = ('a', 'e', 'i', 'o', 'u')
        res = 0
        max_vowels = 0
        for i in range(k):
            if s[i] in check:
                res += 1
        max_vowels = res
        for i in range(k, len(s)):
            if s[i] in check:
                res += 1
            if s[i - k] in check:
                res -= 1
            max_vowels = max(max_vowels, res)
        return max_vowels
