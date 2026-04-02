class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tg = 0
        tc = 0
        s = 0
        t = 0

        for i in range(len(gas)):
            tg+=gas[i]
            tc+=cost[i]

            t = t + gas[i]-cost[i]
            if t < 0:
                s = i+1
                t = 0
        if tg < tc:
            return -1


        return s 
            

        