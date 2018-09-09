def helper(preorder,start,end):
    if end==start:
        return [True,preorder[start],preorder[start]]
    root = preorder[start]
    idx = bs(preorder,start+1,end,root)
    #print start+1,end,root,idx
    
    if idx ==start+1 and preorder[idx]>root:
        res1 = helper(preorder,idx,end)
        return [res1[0] and root<res1[2],\
                max(root,res1[1]),\
                min(root,res1[2])]
    elif idx ==start+1 and preorder[idx]<root:
        res1 = helper(preorder,idx,end)
        return [res1[0] and root>res1[1],\
                max(root,res1[1]),\
                min(root,res1[2])]
    else:
        res1 = helper(preorder,start+1,idx-1)
        res2 = helper(preorder,idx,end)
        #print root,res1,res2
        return [res1[0] and res2[0] and root>res1[1] and root<res2[2],\
                max(root,res1[1],res2[1]),\
                min(root,res1[2],res1[2])]

def bs(preorder,start,end,root):
    l = start
    r = end
    while l<=r:
        mid = (l+r)/2
        if mid>start and (preorder[mid-1]<root and preorder[mid]>root):
            return mid
        elif preorder[mid] <root:
            l = mid+1
        else:
            r = mid -1
    return start
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder) == 0:
            return True
        #print bs(preorder,2,3,2)
        res = helper(preorder,0,len(preorder)-1)
        
        return res[0]
   
