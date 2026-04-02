class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            print(m)
            if target >= m[0] and target <= m[-1]:
                print(m)
                l,r = 0,len(m)
                while l <= r:
                    md = int(l+(r-l)/2)
                    if m[md] == target:
                        return True
                    if m[md] < target:
                        l = md + 1
                    else:
                        r = md - 1  
        return False
                            
                      