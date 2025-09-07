class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = [0] * n
        k = 1

        for i in range(n // 2):
            arr[i] = k
            arr[n - 1 - i] = -k
            k += 1
        return arr