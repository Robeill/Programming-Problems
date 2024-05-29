class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        required = n // 4
        if all(count[char] == required for char in 'QWER'):
            return 0
        min_len = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while all(count[char] <= required for char in 'QWER'):
                min_len = min(min_len, right - left + 1)
                count[s[left]] += 1
                left += 1
        return min_len
