class Solution(object):
    def minSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n==0:
            return []
        res = []
        stack = collections.deque()
        
        for i in range(min(k,n)):
            while len(stack)!=0 and nums[stack[-1]]>nums[i]:
                stack.pop()
            stack.append(i)
        
        res.append(nums[stack[0]])
        
        for prog in range(k,n):
            if prog-k==stack[0]:
                stack.popleft()
            while len(stack)>0 and nums[stack[-1]]>nums[prog]:
                stack.pop()
            stack.append(prog)
            res.append(nums[stack[0]])
        
        return res
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        if k>n-2:
            return -1
        
        times = [0]*n
        
        
        for i in range(n):
            times[flowers[i]-1] = i
        
        if k==0:
            res = []
            for i in range(n-1):
                res.append(max(times[i],times[i+1])+1)
            return min(res)
            
        window_min = self.minSlidingWindow(times,k)
        l = 0
        r = k+1
        win = 1
        res = []
        while r<n:
            temp = max(times[r],times[l])
            if window_min[win]>temp:
                res.append(temp+1)
            r += 1
            l += 1
            win += 1
        ''' 
        #print times
        min_val = n+1
        min_idx = -1
        for i in range(1,k+1):
            if min_val>times[i]:
                min_val = times[i]
                min_idx = i
                
        l = 0
        r = k+1
        res = []
        while r<n:
            #print l,r,min_idx
            if min_val>max(times[l],times[r]):
                res.append(max(times[l],times[r])+1)              
            
            l = min_idx
            min_idx = r
            min_val = times[r]
            while r-l<=k and r<n:
                if min_val>times[r]:
                    min_val = times[r]
                    min_idx = r
                r += 1
        '''
        print res
        if len(res)>0:
            return min(res)
        return -1
