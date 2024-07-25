class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes=set()
        for x in nums:
            d = 2
            while d*d <= x:
                while x%d==0:
                    x //= d
                    primes.add(d)
                d+=1
            if x > 1:
                primes.add(x)
        return len(primes)                