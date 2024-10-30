class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        curr = 0

        for i in range(len(prices)-1):
            curr = prices[i]
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    stack.append((curr - prices[j]))
                    break
                
            else:
                stack.append(curr)
        
        stack.append(prices[-1])
        # print(stack)
        return stack
