class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                return sorted([i, seen[nums[i]]])
            else:
                seen[target-nums[i]] = i
