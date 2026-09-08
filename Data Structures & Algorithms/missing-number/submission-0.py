class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val1 = 0
        val2 = 0
        for n in nums:
            val1 ^= n
        for n in range(len(nums)+1):
            val2 ^= n
        return val1 ^ val2
        