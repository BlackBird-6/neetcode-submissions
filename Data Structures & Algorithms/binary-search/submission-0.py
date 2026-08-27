class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        while l <= r:
            par = (l+r) // 2

            if nums[par] == target:
                return par
            
            if nums[par] < target:
                l = par + 1
            
            if nums[par] > target:
                r = par - 1
        
        return -1

        