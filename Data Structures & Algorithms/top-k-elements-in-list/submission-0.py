class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_tuples = [(-v, k) for k, v in Counter(nums).items()]
        heapq.heapify(freq_tuples)
        return [heapq.heappop(freq_tuples)[1] for _ in range(k)]


        