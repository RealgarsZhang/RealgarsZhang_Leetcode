class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        unumbers = [1]
        i2=i3=i5=0
        while len(unumbers)<n:
            m2 = unumbers[i2]*2
            m3 = unumbers[i3]*3
            m5 = unumbers[i5]*5
            unum = min(m2,min(m3,m5))
            i2 += int(unum==m2)      # all adds needed,to avoid dup.
            i3 += int(unum==m3)
            i5 += int(unum==m5)
            unumbers.append(unum)
        
        return unumbers[-1]
        
        
