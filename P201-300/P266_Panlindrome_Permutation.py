from collections import defaultdict


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = defaultdict(int)
        for letter in s:
            dic[letter] += 1
        
        odd = set()
        for key in dic:
            if dic[key]%2!=0:
                odd.add(key)
                
        return len(odd)<=1
