class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        freq = {}
        for i in range(n):
            freq.setdefault(nums[i],0)
            freq[nums[i]] += 1
        
        temp = freq.keys()
        temp.sort(key = lambda k: freq[k])
        #print temp
        return temp[-k:]
      
