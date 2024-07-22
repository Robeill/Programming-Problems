class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_count, window = {}, {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        check, need = 0, len(t_count)
        res, resLen = [-1, -1], float("inf")
        windowS = 0
        for windowE in range(len(s)):
            c = s[windowE]
            window[c] = 1 + window.get(c, 0)
            if c in t_count and window[c] == t_count[c]:
                check += 1
            while check == need:
                if (windowE - windowS + 1) < resLen:
                    res = [windowS, windowE]
                    resLen = windowE - windowS + 1
                window[s[windowS]] -= 1
                if s[windowS] in t_count and window[s[windowS]] < t_count[s[windowS]]:
                    check -= 1
                windowS += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""