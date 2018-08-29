class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        permitted = set('01689')
        invariant = set('018')
        
        n = len(num)
        if n%2 == 1 and num[n/2] not in invariant:
            return False
        
        for i in range(n/2):
            if not(num[i] in invariant and num[n-1-i]==num[i]) \
            and not(num[i]=='6' and num[n-i-1]=='9')\
            and not(num[i]=='9' and num[n-i-1]=='6'):
                return False
        
        return True
        
