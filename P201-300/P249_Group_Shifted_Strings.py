from collections import defaultdict

def posList(string,dic):
    n = len(string)
    res = []
    for i in range(n-1):
        res.append( (dic[string[i+1]]-dic[string[i]])%26 )
        
    return tuple(res)

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        dic = {}
        for i in range(26):
            dic[alpha[i]] = i
        
        res_dic = defaultdict(list)
        
        for string in strings:
            temp = posList(string,dic)
            res_dic[temp].append(string)
            
        return res_dic.values()
   
