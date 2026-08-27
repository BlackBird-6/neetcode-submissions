class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDistance(point):
            x, y = point
            return math.sqrt((x**2 + y**2))
        
        minHeap = []

        for p in points:
            heapq.heappush(minHeap, (getDistance(p), p))
        
        res = []
        for i in range(k):
            _, point = heapq.heappop(minHeap)
            res.append(point)
        
        return res