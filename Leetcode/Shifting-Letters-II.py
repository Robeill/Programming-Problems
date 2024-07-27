class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        effects = [0] * (len(s) + 1)
        
        for l, r, d in shifts:
            if d == 1:
                effects[l] += 1
                if r + 1 < len(s):
                    effects[r + 1] -= 1
            else:
                effects[l] -= 1
                if r + 1 < len(s):
                    effects[r + 1] += 1
        current_shift = 0
        for i in range(len(s)):
            current_shift += effects[i]
            s[i] = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
        return "".join(s)
