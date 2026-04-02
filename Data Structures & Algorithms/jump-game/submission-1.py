class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n

        dp[0] = True

        for i in range(n):
            for j in range(i+1,i+nums[i]+1):
                if j < n:
                    dp[j] = dp[i]
        return dp[n-1]            

        