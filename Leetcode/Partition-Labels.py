class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,c in enumerate(s):
            last[c] = i
        res = []
        l,r = 0,0
        for i,c in enumerate(s):
            l += 1
            r = max(r,last[c])
            if i == r:
                res.append(l)
                l = 0 
        return res
        