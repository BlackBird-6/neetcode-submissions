class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = Counter(nums) #3: 3, 2: 2, 1: 1
        heap = []

        for key, val in freqs.items():
            heapq.heappush(heap, (val, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [h[1] for h in heap]