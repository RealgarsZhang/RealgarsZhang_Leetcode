class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>= len(s):
            return s
        res = ''
        n = len(s)
        i = 0
        while i<n:
            res += s[i]
            i += 2*numRows-2
        
        for cur_row in range(1,numRows-1):
            i = cur_row
            res += s[i]
            i += 2*numRows-2
            while i<n:
                res += s[i-2*cur_row]
                res += s[i]
                i += 2*numRows-2
            if i-2*cur_row <n:
                res += s[i-2*cur_row]
        
        i = numRows-1
        while i<n:
            res += s[i]
            i += 2*numRows-2
        
        return res
  
