class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {i:True for i in nums}
        longest = 0
        for j in nums:
            if j-1 not in mp:
                curr = j
                l = 1 
                while curr+1 in mp:
                    curr+=1
                    l+=1
                longest = max(longest,l)
        return longest             
                


        