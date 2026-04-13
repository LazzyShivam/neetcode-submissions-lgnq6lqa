import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        ans = []
        for num in nums:
            mp[num] = mp.get(num,0)+1


        for ke,v in mp.items():
            heapq.heappush(ans,(-1*v,ke))
        res = []    
        while k > 0:
            if ans:
                res.append(ans[0][1])
                heapq.heappop(ans)
            k-=1
        return res    





        