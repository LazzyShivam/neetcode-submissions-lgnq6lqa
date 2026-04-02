class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pf = [1]*n
        sf = [1]*n

        for i in range(n):
            if i == 0:
                pf[i] = nums[i]
                sf[n-i-1] = nums[n-i-1]
                continue
            pf[i] = nums[i]*pf[i-1]
            sf[n-i-1] = nums[n-i-1]*sf[n-i]
        
        ans = [1]*n
        for i in range(n):  
            if i == 0: 
                ans[i] = sf[i+1]
            elif i == n-1:
                ans[i] = pf[i-1]  
            else:
                ans[i] = pf[i-1]*sf[i+1]      
        return ans       

        