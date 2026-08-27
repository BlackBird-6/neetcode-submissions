class KthLargest:

    # [1, 2, 3, 3, 4, 5, 5, 6, 6, 7]
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



        # [10, 20, 30]
        
