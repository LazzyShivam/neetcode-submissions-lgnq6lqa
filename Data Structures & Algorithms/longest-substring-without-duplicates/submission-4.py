class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ind = {}
        ml = 0
        for r,v in enumerate(s):
            if v in ind and ind.get(v) >= l:
                l = ind.get(v)+1
            ind[v] = r    
            ml = max(ml,r-l+1)
        return ml        
