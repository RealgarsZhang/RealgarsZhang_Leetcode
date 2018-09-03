def bs(dp,num):
    l = 0
    r = len(dp)-1
    
    while l<=r:
        mid = (l+r)/2
        if dp[mid] == num:
            return mid
        elif dp[mid]>num:
            r = mid-1
        else:
            l = mid+1
    
    return l
  


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
        l = 0
        r = 0
        while l<n and r<n:
            while r<n and envelopes[r][0] == envelopes[l][0]:
                r+=1
            envelopes[l:r] = sorted(envelopes[l:r],key = lambda e:e[1],reverse = True)
            l = r
        
       
        dp = [envelopes[0][1]]
        for i in range(1,n):
            num = envelopes[i][1]
            if num>dp[-1]:
                dp.append(num)
            elif num<dp[0]:
                dp[0] = num
            else:
                dp[bs(dp,num)] = num
        #print dp
        return len(dp)

