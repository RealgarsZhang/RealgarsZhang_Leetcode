class Solution(object):
    
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
        
        l = 0
        r = k+1
        res = []
        i = l+1
        while i<n and r<n:
            if times[l]>times[i] or times[r]>=times[i]:
                if i==r:
                    res.append(max(times[l],times[r])+1)
                l = i
                r = l+k+1
                i = l+1
            else:
                i += 1
        if res==[]:
            return -1
        return min(res)
                
     
