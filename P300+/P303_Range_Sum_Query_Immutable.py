class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        n = len(nums)
        self.cum_sum = [0]*(n+1)
        
        for i in range(len(nums)):
            self.cum_sum[i+1] = nums[i]+self.cum_sum[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cum_sum[j+1]-self.cum_sum[i]
        
  
