# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(node,cur_list,res):
    cur_list.append(node.val)
    if node.left==node.right == None:
        res.append('->'.join(map(str,cur_list)))
    else:
        if node.left!=None:
            helper(node.left,cur_list,res)
        if node.right!=None:
            helper(node.right,cur_list,res)
    cur_list.pop()


    
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        cur_list = []
        res =[]
        helper(root,cur_list,res)
        return res
