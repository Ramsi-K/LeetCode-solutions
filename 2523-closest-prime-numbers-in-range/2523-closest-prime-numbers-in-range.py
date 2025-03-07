class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1, -1]
        
        # Miller-Rabin primality test
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
                if n % p == 0:
                    return n == p
            d = n - 1
            s = 0
            while d % 2 == 0:
                d //= 2
                s += 1
            for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
                if a >= n:
                    continue
                x = pow(a, d, n)
                if x == 1 or x == n - 1:
                    continue
                for _ in range(s - 1):
                    x = pow(x, 2, n)
                    if x == n - 1:
                        break
                else:
                    return False
            return True
        
        # Handle the case where left <= 2
        if left <= 2:
            if right >= 3 and is_prime(3):
                return [2, 3]
            else:
                return [-1, -1]
        
        # Start from the first odd number >= left
        if left % 2 == 0:
            left += 1
        
        prev_prime = -1
        min_diff = float('inf')
        res = [-1, -1]
        
        for num in range(left, right + 1, 2):
            if is_prime(num):
                if prev_prime != -1:
                    diff = num - prev_prime
                    if diff < min_diff:
                        min_diff = diff
                        res = [prev_prime, num]
                prev_prime = num
        
        return res