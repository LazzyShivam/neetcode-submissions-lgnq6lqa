class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)

        for i in range(n):
            mp[nums[i]] = i

        for i in range(n):
            if mp.get(target - nums[i])  is not None and i != mp.get(target - nums[i]):
                return [i,mp.get(target - nums[i])] 
        return []          