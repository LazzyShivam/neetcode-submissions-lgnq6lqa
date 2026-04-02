class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i,s in enumerate(nums):
            mp[s] = i

        for i,s in enumerate(nums):
            j = mp.get(target - s)
            if j is not None and j != i:
                return  [i,mp.get(target - s)]
        return [-1,-1]        