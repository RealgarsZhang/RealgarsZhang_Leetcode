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
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        dp = [nums[0]]
        for i in range(1,n):
            num = nums[i]
            if num>dp[-1]:
                dp.append(num)
            elif num<dp[0]:
                dp[0] = num
            else:
                dp[bs(dp,num)] = num
        #print dp
        return len(dp)
                
