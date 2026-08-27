class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = []
        def dfs(i):
            visited.append(i)

            for k in range(nums[i]+1):
                next_l, next_r = i-k,i+k

                if next_l >= 0 and next_l not in visited:
                    dfs(next_l)
                if next_r < len(nums) and next_r not in visited:
                    dfs(next_r)
        
        dfs(0)

        return len(nums)-1 in visited
        