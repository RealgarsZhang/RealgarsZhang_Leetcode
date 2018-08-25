class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_pos_dict = {}
        l = 0
        r = 0
        max_len = 0
        n = len(s)
        while r<n:
            if len(last_pos_dict)<2 or s[r] in last_pos_dict:
                last_pos_dict[s[r]] = r
            else:
                max_len = max(max_len,r-l)
                letter_list = last_pos_dict.keys()
                if last_pos_dict[letter_list[0]] < last_pos_dict[letter_list[1]]:
                    l = last_pos_dict[letter_list[0]] + 1
                    del last_pos_dict[letter_list[0]]
                    last_pos_dict[s[r]] = r
                else:
                    l = last_pos_dict[letter_list[1]] + 1
                    del last_pos_dict[letter_list[1]]
                    last_pos_dict[s[r]] = r
            r += 1
        
        max_len=max(max_len,r-l)
        return max_len
