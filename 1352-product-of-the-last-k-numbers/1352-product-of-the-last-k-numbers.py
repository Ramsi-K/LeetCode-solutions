class ProductOfNumbers:
    def __init__(self):
        # Initialize with a dummy value (1) to simplify product calculation.
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        # If num is zero, reset the prefix product list.
        if num == 0:
            self.prefix_products = [1]
        else:
            # Multiply the last prefix product by num and append.
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is at least the length of the prefix list, then a zero was encountered in the last k elements.
        if k >= len(self.prefix_products):
            return 0
        # Otherwise, compute the product by dividing the product of all numbers so far
        # by the product of the numbers before the last k numbers.
        return self.prefix_products[-1] // self.prefix_products[-k - 1]




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)