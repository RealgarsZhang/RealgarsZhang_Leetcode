class NumArray(object):
    
    def lowbit(self,num):
        return num&(-num)
    
    def change(self,idx,delta):
        
        while idx<len(self.tree_arr):
            self.tree_arr[idx] += delta
            idx += self.lowbit(idx)
            
    def comp_sum(self,idx):
        res = 0
        while idx>0:
            res += self.tree_arr[idx]
            idx -= self.lowbit(idx)
        return res
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.tree_arr = [0]+nums[:]
        for i in range(1,len(nums)+1):
            parent = i+self.lowbit(i)
            if parent<=len(nums):
                self.tree_arr[parent] += self.tree_arr[i]
            
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
       
        delta = val-self.nums[i]
        self.nums[i] = val
        self.change(i+1,delta)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum1 = self.comp_sum(j+1)
        sum2 = self.comp_sum(i)
        #print self.tree_arr
        return sum1-sum2
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
