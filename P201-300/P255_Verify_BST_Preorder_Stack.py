class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        n = len(preorder)
        stack = []
        prog = 0
        root_val = -sys.maxint-1
        
        while prog<n :
            while not stack or (prog<n and stack[-1]>preorder[prog] ):
                if preorder[prog]<root_val:
                    return False
                stack.append(preorder[prog])
                prog += 1
                #print stack
            if prog<n:
                while stack and preorder[prog] > stack[-1]:
                    root_val = max(root_val,stack[-1])
                    stack.pop()
                stack.append(preorder[prog])
                #print stack
            prog += 1
            
        
        return True
        
   
