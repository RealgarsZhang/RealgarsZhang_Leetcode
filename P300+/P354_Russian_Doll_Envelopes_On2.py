class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        #bry check
        if n==0:
            return 0
        envelopes.sort(key = lambda e:e[0])
        dp = [0]*n
        dp[0] = 1
       
        for i in range(1,n):
          
            max_val = 1
            for j in range(0,i):
                if envelopes[j][1]<envelopes[i][1] and envelopes[j][0]<envelopes[i][0]:
                    max_val = max(max_val,dp[j] + 1)
          
            dp[i] = max_val
          
        return max(dp)
