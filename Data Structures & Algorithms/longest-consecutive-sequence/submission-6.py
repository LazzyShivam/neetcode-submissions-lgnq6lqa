class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in nums: 
            if i - 1 in s:
               continue
            c = 1 
            j = i+1   
            while j in s:
                c += 1
                j+=1

            longest = max(c,longest)
        return longest        
                    



        