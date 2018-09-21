from collections import defaultdict

def helper(res,partial_str,residue,dest_len,mid):
    if len(partial_str) == dest_len:
        res.append(partial_str+mid+partial_str[::-1])
        return
    for key in residue:
        next_residue = residue.copy()
        next_residue[key] -= 2
        if next_residue[key] ==0:
            del next_residue[key]
        helper(res,partial_str+key,next_residue,dest_len,mid)
            


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = defaultdict(int)
        
        for letter in s:
            dic[letter] += 1
            
        odd = [key for key in dic if dic[key]%2==1]
        if len(odd)>1:
            return []
        elif len(odd)==1:
            mid = odd[0]
            dic[mid] -= 1
            if dic[mid] == 0:
                del dic[mid]
        else:
            mid = ''
        res = []
        
        helper(res,"",dic,len(s)/2,mid)
        
        return res
        
