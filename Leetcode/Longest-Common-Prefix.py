class Solution:
    def longestCommonPrefix(self, strs):
        ans = str()
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans