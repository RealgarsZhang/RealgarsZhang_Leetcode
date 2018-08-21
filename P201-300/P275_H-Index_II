class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        if N==0 or citations[-1]==0:
            return 0
        if N==1:
            return int(citations[0]>=1)
        if citations[0]>=N:
            return N
        
        
        l = 1
        r = N-1
        
        while l<=r:
            mid = (l+r)/2
            if citations[mid]>=N-mid and citations[mid-1]<N-(mid-1):
                return N-mid
            elif citations[mid-1]>=N-(mid-1):
                r = mid-1
            else:
                l = mid+1
        
