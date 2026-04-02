class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if m != n:
            return False
        mp = {}
        for i in s:
            if mp.get(i) is None:
                mp[i] = 0
            mp[i] = mp[i] + 1

        for i in t:
            if mp.get(i) is None:
                return False
            if mp.get(i) == 0:
                return False
            mp[i] = mp[i] - 1
        return True        

        