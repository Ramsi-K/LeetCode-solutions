class RecentCounter:

    def __init__(self):
        self.records = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.records.append(t)
        # print(self.records[self.start])
        while self.records[self.start] < t - 3000:
            self.start += 1
        
        # print(self.records[self.start])
        # print(self.start)
        # print("------------------")
        return len(self.records) - self.start
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)