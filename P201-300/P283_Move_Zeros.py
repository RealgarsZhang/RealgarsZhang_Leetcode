def swap (nums,i,j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        num_pos = 0
        for i in range(n):
            if nums[i] != 0:
                swap(nums,i,num_pos)
                num_pos += 1
        
        
