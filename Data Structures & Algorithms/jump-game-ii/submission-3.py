class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('INF')]*n

        dp[0] = 0

        for i in range(n):
            for j in range(i+1,i+nums[i]+1):
                if j > n - 1:
                    continue
                c = min(dp[j],dp[i]+1)
                if j == n-1:
                    return c
                if j < n:
                   dp[j] = c
        return dp[n-1]           

        