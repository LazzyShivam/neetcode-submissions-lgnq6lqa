class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0, n-1

        lmax,rmax = 0,0
        w = 0

        while i < j:
            if height[i] <= height[j]:
                if lmax < height[i]:
                    lmax = height[i]
                else:
                    w += lmax-height[i]
                i+=1    
            else:
                if rmax < height[j]:
                    rmax = height[j]
                else:
                    w += rmax-height[j]
                j-=1    
        return w            




        
        