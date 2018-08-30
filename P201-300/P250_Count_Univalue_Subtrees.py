# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(node,res):
    if node==None:
        return [0,0]
    list1 = helper(node.left,res)
    list2 = helper(node.right,res)
    if list1[0] == 0 and list2[0] == 0:
        res[0] += 1
        return [1,node.val]
    elif list1[0]==-1 or list2[0] == -1:
        return [-1,0]
    elif list1[0]==1 and list2[0] == 0:
        if list1[1] == node.val:
            res[0] += 1
            return [1,node.val]
        else:
            return [-1,0]
    elif list1[0]==0 and list2[0] == 1:
        if list2[1] == node.val:
            res[0] += 1
            return [1,node.val]
        else:
            return [-1,0]
    else:
        if list1[1] == node.val and list2[1] == node.val:
            res[0]+=1
            return [1,node.val]
        else:
            return [-1,0]

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        helper(root,res)
        return res[0]
        
  
