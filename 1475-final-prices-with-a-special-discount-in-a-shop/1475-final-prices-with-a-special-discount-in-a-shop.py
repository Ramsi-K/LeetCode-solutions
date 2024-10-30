class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        result = prices[:]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                result[index] -= prices[i]
            
            stack.append(i)

        
        # print(result)
        return result
