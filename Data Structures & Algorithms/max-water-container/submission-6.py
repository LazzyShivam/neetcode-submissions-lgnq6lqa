class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j = 0,n-1

        wmax = 0

        while i < j:
            w = min(heights[j],heights[i])*(j-i)
            wmax = max(w,wmax)
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j-=1      
        return wmax


        