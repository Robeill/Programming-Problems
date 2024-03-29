class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = [set(word) for word in words]
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if res[i] == res[j]:
                    count += 1
        return count
