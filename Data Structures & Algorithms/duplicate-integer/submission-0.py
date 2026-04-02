class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in nums:
            if mp.get(i) is not None:
                return True
            mp[i] = True
        return False

