class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        ans = 0

        for correct in ["T", "F"]:
            count  = 0
            left = 0
            for right in range(n):
                if answerKey[right] != correct:
                    count += 1
                while count > k:
                    if answerKey[left] != correct:
                        count -=1
                    left += 1
                ans = max(ans, right - left + 1)
        return ans
            