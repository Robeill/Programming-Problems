class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left > right:
            return [-1, -1]
        
        def sieve(n):
            sieve = [0] * (n + 1)
            primes = []
            for x in range(2, n + 1):
                if sieve[x] == 0:
                    primes.append(x)
                    for u in range(x * x, n + 1, x):
                        if sieve[u] == 0:
                            sieve[u] = x
            return primes
        
        primes_in_range = [p for p in sieve(right) if p >= left]
        if len(primes_in_range) < 2:
            return [-1, -1]
        
        closest_pair = [primes_in_range[0], primes_in_range[1]]
        min_gap = primes_in_range[1] - primes_in_range[0]
        
        for i in range(1, len(primes_in_range) - 1):
            gap = primes_in_range[i + 1] - primes_in_range[i]
            if gap < min_gap:
                min_gap = gap
                closest_pair = [primes_in_range[i], primes_in_range[i + 1]]
        
        return closest_pair