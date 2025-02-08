class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_heap = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        if number not in self.num_to_heap:
            self.num_to_heap[number] = []
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_to_heap:
            return -1
        heap = self.num_to_heap[number]
        while heap:
            current_index = heapq.heappop(heap)
            if self.index_to_num.get(current_index, -1) == number:
                heapq.heappush(heap, current_index)
                return current_index
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)