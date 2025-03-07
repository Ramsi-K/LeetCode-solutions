class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes to find all primes in [left, right]
        if right < 2:
            return [-1, -1]
        
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        
        # Extract primes in [left, right]
        primes = [num for num in range(left, right + 1) if is_prime[num]]
        
        # Find the pair with the smallest difference
        if len(primes) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        result = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]
        
        return result