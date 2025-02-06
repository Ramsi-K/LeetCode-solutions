class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        n = len(nums)
        
        # Step 1: Compute all products and store frequencies
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1
        
        # Step 2: Count valid (a, b, c, d) tuples
        count = 0
        for product, freq in product_map.items():
            if freq > 1:
                count += (freq * (freq - 1) // 2) * 8  # k choose 2 * 8
        
        return count