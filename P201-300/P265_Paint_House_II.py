class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
       
        n = len(costs)
        
        if n == 0:
            return 0
        k = len(costs[0])
        dp = []
        for i in range(n):
            dp.append([0]*k)
        dp[0] = costs[0] # costs read only
        
        
       
        
        for i in range(1,n):
            for j in range(k):
                dp[i][j] = min(dp[i-1][:j]+dp[i-1][j+1:])  + costs[i][j]
            
            
        return min(dp[-1])
