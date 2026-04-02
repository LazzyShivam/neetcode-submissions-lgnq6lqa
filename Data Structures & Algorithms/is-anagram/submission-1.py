class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        for i in s:
            if mp.get(i) is None:
                mp[i] = 0
            mp[i] += 1

        for i in t:
            if mp.get(i) is None:
                return False
            mp[i] -= 1

        for k in mp.values():
            if k != 0:
                return False
        return True        

        