class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos = 0
        l = 0
        while l <= maxPos and l < len(nums):
            maxPos = max(maxPos, l+nums[l])
            l += 1
        return maxPos >= len(nums)-1
        