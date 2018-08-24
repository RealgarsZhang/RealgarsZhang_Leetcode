class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = s.upper()
        
        temp_list = []
        n = len(s)
        
        unit_cnt = 0
        for i in range(n-1,-1,-1):
            if s[i]!='-':
                temp_list.append(s[i])
                unit_cnt += 1
                if unit_cnt == k :
                    unit_cnt = 0
                    temp_list.append('-')
        while len(temp_list)>0 and temp_list[-1]=='-':
            temp_list.pop()
        res = ''.join(temp_list)
        return res[::-1]
        
