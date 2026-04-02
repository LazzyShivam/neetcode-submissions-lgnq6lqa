class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        i,j = 0,1
        res = [0]*len(nums)
        for v in nums:
            if v > 0:
                res[i] = v
                i+=2
            else:
                res[j] = v
                j+=2 
        return res                


                       
