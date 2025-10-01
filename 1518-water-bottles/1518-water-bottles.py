class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles_drunk = bottles_emptied = 0
        while numBottles > 0:
            bottles_drunk += numBottles 
            bottles_emptied += numBottles
            numBottles = bottles_emptied // numExchange
            bottles_emptied = bottles_emptied % numExchange

        return bottles_drunk
