class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n%2 == 1:
            res = ['1','0','8']
            if n==1:
                return res
        else:
            res = ['']
        
        for i in range(n/2-1,0,-1):
            temp_res = []
            for num in res:
                temp_res.append('6'+num+'9')
                temp_res.append('9'+num+'6')
                temp_res.append('1'+num+'1')
                temp_res.append('8'+num+'8')
                temp_res.append('0'+num+'0')
            res = temp_res
        
        temp_res = []
        for num in res:
            temp_res.append('6'+num+'9')
            temp_res.append('9'+num+'6')
            temp_res.append('1'+num+'1')
            temp_res.append('8'+num+'8')
            
        return temp_res
 
