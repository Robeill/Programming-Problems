class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        windowStart = 0
        res = 0
        for windowEnd in range(len(s)):
            while s[windowEnd] in char:
                char.remove(s[windowStart])
                windowStart += 1
            char.add(s[windowEnd])
            res = max(res, windowEnd - windowStart + 1)
        return res