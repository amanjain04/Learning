class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        while l<=r and r<len(prices):
            if (prices[l] <= prices[r]):
                res = max(res, prices[r]-prices[l])
                r+=1
            else:
                l+=1
        return res
