class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <=1:
            return 0
        level = -1
        start = 0
        end = 0
        next_end = 0
        while end<n-1:
            level += 1
            for i in range(start,end+1):
                next_end = max(next_end,i+nums[i])
            start = end + 1
            end = next_end
            
        return level+1
        
            
