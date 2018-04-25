class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root
        lleft = self.lowestCommonAncestor(root.left, p, q)
        rright = self.lowestCommonAncestor(root.right, p, q)
        if lleft == None:
            return rright
        elif rright == None:
            return lleft
        else:
            return root
     
