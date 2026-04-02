class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        i,j = 0,n-1

        while i < j:
            t = numbers[i] + numbers[j]
            if target  == t:
                return [i+1,j+1]
            elif target > t:
                i+=1
            elif target < t:
                j-=1
        return [-1,-1]       


        

        