# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def dfs(self,root,a):
        if (root == None):
            return
        if root.left != None:
            self.dfs(root.left,a)
        a.append(root.val)
        if root.right != None:
            self.dfs(root.right,a)
       
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a=[]
        
        self.dfs(root,a)
        flag = True
        for i in range(0,len(a)-1):
            if(a[i] >= a[i+1]):
                flag = False
        return flag
        
