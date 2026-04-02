class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        n = len(prices)
        j = 1
        m_p = 0
        while j < n:
            if prices[j] >  prices[i]:
                m_p = max(prices[j] - prices[i],m_p)       
            else:
                i = j
            j+=1
        return m_p        

        