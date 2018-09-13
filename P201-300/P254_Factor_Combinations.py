from math import sqrt
def helper(res,item,target,factor):
    #print item, target

    for i in range(factor,int(sqrt(target))+1):
        #print i, target
        if target%i == 0 and target/i>=i:
            res.append(item+[i]+[target/i])
            helper(res,item+[i],target/i,i)
    

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        item = []
        res = []
        helper(res,item,n,2)
        
        return res
