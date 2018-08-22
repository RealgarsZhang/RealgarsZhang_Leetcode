class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(1,n+1):
            j = 1
            min_num = i
            while j*j<=i:
                min_num = min(min_num,1+dp[i-j*j])
                j+=1
            dp[i] = min_num
        return dp[-1]
#This is a lovely dp problem. However there is a 
#math theorem behind which may greatly simplify the complexity.  
