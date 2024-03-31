class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        res = []

        for size in range(n, 1, -1):
            max_index = A.index(size)
            if max_index != size - 1:
                A[:max_index + 1] = reversed(A[:max_index + 1])
                res.append(max_index + 1)
                A[:size] = reversed(A[:size])
                res.append(size)
        return res
