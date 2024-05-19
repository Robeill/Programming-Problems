class Solution:
    def sortSentence(self, s: str) -> str:
        split_string = s[::-1].split()
        split_string.sort()
        res = []
        for word in split_string:
            res.append(word[1:][::-1])
        return " ".join(res)