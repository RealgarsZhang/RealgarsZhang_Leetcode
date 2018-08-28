# O(n) Time, O(1) Space.


def swap(nums,i,j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


class Solution(object):
    def reverseWords(self, nums):
        """
        :type nums: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        n = len(nums)
        
        for i in range(n/2):
            swap(nums,i,n-i-1)
            
        word_end = 0
        word_start = 0
        
        while word_end<n:
            while word_end<n and nums[word_end]!=' ':
                word_end += 1
            word_end -= 1
            word_len = word_end - word_start + 1
            for i in range(word_len/2):
                swap(nums,word_start+i,word_end-i)
            word_end += 2
            word_start = word_end
            
   
