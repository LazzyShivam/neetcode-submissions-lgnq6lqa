import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            if mp.get(i) is None:
                mp[i] = 0
            mp[i]+=1    
        dt = [(-mp.get(i),i) for i in mp.keys()]
        heapq.heapify(dt)
        res = []    
        while k > 0:
            res.append(heapq.heappop(dt)[1])
            k -= 1
        return res           
