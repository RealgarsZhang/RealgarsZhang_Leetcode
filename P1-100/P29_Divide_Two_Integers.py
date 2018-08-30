class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend==-2147483648 and divisor==-1:
            return 2147483647 # This is for a wrong testcase
        if dividend<0 and divisor>0 or dividend>0 and divisor<0:
            minus = -1
        else:
            minus = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        #print dividend,divisor
        res = 0
        mask = 1<<31
        shift_bit = 31
        while shift_bit>=0:
            if divisor<<shift_bit<=dividend:
                res += mask
                dividend -= divisor<<shift_bit
            mask >>=1
            shift_bit -= 1
        
        return res*minus


