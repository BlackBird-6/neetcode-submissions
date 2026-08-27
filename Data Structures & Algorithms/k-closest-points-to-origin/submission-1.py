class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def getDistance(point):
            x, y = point
            return math.sqrt((x**2 + y**2))
        
        maxHeap = []

        for p in points:
            heapq.heappush(maxHeap, (-getDistance(p), p))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [p[1] for p in maxHeap]