class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         n = len(nums)
         l_p = [1] * n
         r_p = [1] * n
         l_p[0] = nums[0]
         r_p[n-1] = nums[n-1]
         for i in range(1, n):
            l_p[i] = l_p[i-1] * nums[i]
         for i in range(n-2, -1, -1):
            r_p[i] = r_p[i+1] * nums[i]
         op = []
         for i in range(n):  
            if i == 0:
                op.append(r_p[i+1])
            elif i == n-1:
                op.append(l_p[i-1]) 
            else:    
                op.append(l_p[i-1]*r_p[i+1])       
         return op