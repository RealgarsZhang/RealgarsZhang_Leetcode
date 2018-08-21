class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        
        record = [0]*(N+1)
        for cite in citations:
            cite = min(cite,N)
            record[cite] +=1
            
        cumul_sum = 0
        for i in range(N,-1,-1):
            cumul_sum += record[i]
            if cumul_sum >= i:
                return i
        
