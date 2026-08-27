class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones] # -6 -4 -3 -2 -2
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            
            if x > y:
                heapq.heappush(max_heap, -(x-y))
            
        return 0 if len(max_heap) == 0 else -max_heap[0]
        