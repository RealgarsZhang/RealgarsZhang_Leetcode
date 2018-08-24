def swap(nums,i,j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<=1:
            return 
        if nums[0]>nums[1]:
            swap(nums,0,1)
        
        i = 1
        while i<n-1:
            if (i%2==1 and nums[i]<nums[i+1]) or (i%2==0 and nums[i]>nums[i+1]):
                swap(nums,i,i+1)
            i += 1
        
#At first I overcomplicate the problem trying to find median, partition
#and swap intensively. Actually, I do not have to look back once I go 
#forward. 
