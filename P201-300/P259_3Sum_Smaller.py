
class Solution(object):
    def twoSumSmaller(self,nums,start,target):
        n = len(nums)
        
        l = start
        r = n-1
        res = 0
        while l<r and nums[r]+nums[l] < target:
            l += 1
        if l == r:
            return (n-start)*(n-start-1)/2
        res += l-start
        while r>=1 and l!=n:
            r -= 1
            while l<r and nums[r] + nums[l] <target:
                l += 1
            if l==r:
                return res + (r-start)*(r-start+1)/2
            res += l-start
        return res
        
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        if n<3:
            return 0
        res = 0
        for i in range(0,n-2):
            res += self.twoSumSmaller(nums,i+1,target-nums[i])
            
        return res
