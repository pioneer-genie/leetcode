import heapq
class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        if (len(self.min_h) + len(self.max_h) < 2):
            heapq.heappush(self.min_h, num)
        
        else:
            if (self.min_h[0] <= num):
                heapq.heappush(self.min_h, num)
            else:
                heapq.heappush(self.max_h, -num)
        
        if (len(self.min_h) > len(self.max_h) + 1):
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
        elif (len(self.max_h) > len(self.min_h) + 1):
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
        
    def findMedian(self) -> float:
        if (len(self.max_h) > len(self.min_h)):
            return -self.max_h[0]
        elif (len(self.max_h) < len(self.min_h)):
            return self.min_h[0]
        else:
            return (self.min_h[0] - self.max_h[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()