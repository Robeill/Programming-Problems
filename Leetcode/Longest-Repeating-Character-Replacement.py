class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        windowStart = 0
        maxV = 0
        for windowEnd in range(len(s)):
            count[s[windowEnd]] = 1 + count.get(s[windowEnd] , 0)
            maxV = max(maxV, count[s[windowEnd]])
            if (windowEnd - windowStart+ 1) - maxV > k:
                count[s[windowStart]] -= 1
                windowStart += 1
            res = max(res , windowEnd - windowStart + 1)
        return res