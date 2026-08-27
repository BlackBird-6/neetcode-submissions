class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(amount+1):
            for value in coins:
                if i-value < 0:
                    continue
                dp[i] = min(dp[i], dp[i-value] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

        # dp[i] where i is the minimum number of coins to reach X

        # [0, 1, 2, 3, 4, 1, ...]

        # 