class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)

        total = 0
        for n in nums:
            if n > 0:
                total = max(n, total+n)
            else:
                total = total + n
            res = max(res, total)
        return res

        # [10,-1,-2,-3,-3,1,3,5]

        # [10,-11,8,-7,10]
        