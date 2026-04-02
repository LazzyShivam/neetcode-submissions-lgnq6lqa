class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n > 0:
            if n % 2!=0:
                c+=1
            n = n >> 1
        return c    


        