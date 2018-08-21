class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        AxorB = 0
        for num in nums:
            AxorB ^= num

        bitmap = 1
        while AxorB%2 == 0:
            bitmap <<=1
            AxorB /=2

        one_xor = 0
        zero_xor = 0

        for num in nums:
            if bitmap & num == 0:
                zero_xor ^= num
            else:
                one_xor ^= num

        return [zero_xor,one_xor]
  
