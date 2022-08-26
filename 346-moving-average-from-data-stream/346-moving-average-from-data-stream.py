class MovingAverage:

    def __init__(self, size: int):
        self.data = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.data.append(val)
        if len(self.data) < self.size:
            return sum(self.data) / len(self.data)
        else:
            numerator = sum(self.data[len(self.data)-self.size:len(self.data)])
            denominator = min(len(self.data), self.size)
            return numerator / denominator

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)