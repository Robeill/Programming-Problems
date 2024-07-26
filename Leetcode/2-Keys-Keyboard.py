class Solution:
  def minSteps(self, n: int) -> int:
    curr = 1 
    copied = 0 
    res = 0
    while curr < n:
        if n % curr == 0:
            copied = curr
            res += 1
        curr += copied
        res += 1
    return res
