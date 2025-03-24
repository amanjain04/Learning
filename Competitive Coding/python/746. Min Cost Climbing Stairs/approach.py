class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0]*(len(cost)+1)
        dp[len(cost)-1] = cost[len(cost)-1]
        if (len(cost)<=1):
            return dp[len(cost)]
        for i in range(len(cost)-2,-1,-1):
            dp[i] = min(dp[i+1],dp[i+2]) + cost[i]

        return min(dp[0],dp[1])