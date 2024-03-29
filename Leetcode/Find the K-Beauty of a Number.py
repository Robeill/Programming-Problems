class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        subArr = str(num)[:k]
        count = 0

        if(num % int(subArr) == 0):
            count += 1
        for i in range(1,len(str(num))-k+1):
            subArr = str(num)[i:k+i]
            if(int(subArr) != 0 and num % int(subArr) == 0):
                count += 1
        return count