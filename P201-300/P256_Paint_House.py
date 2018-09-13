class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        dp = []
        dp.append([0]*n)
        dp.append([0]*n)
        dp.append([0]*n)
        
        dp[0][0] = costs[0][0]
        dp[1][0] = costs[0][1]
        dp[2][0] = costs[0][2]
        
        for i in range(1,n):
            dp[0][i] = min(dp[1][i-1],dp[2][i-1]) + costs[i][0]
            dp[1][i] = min(dp[0][i-1],dp[2][i-1]) + costs[i][1]
            dp[2][i] = min(dp[1][i-1],dp[0][i-1]) + costs[i][2]
            
        return min(dp[0][-1],dp[1][-1],dp[2][-1])
