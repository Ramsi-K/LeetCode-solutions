class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Step 1: Start at 1
        curr = 1  
        k -= 1    # Already counted the first number

        # Step 2: Traverse until k becomes 0
        while k > 0:
            steps = self.countSteps(n, curr, curr + 1)

            if steps <= k:
                # Step 3: Skip this prefix's subtree
                curr += 1    
                k -= steps
            else:
                # Step 4: Dive deeper into this prefix
                curr *= 10   
                k -= 1

        # Step 5: Return result
        return curr  

    def countSteps(self, n: int, curr: int, next: int) -> int:
        steps = 0
        while curr <= n:
            steps += min(n + 1, next) - curr
            curr *= 10
            next *= 10
        return steps