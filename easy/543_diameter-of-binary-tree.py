class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # type: ignore
        def findMax(node):
            if not node:
                return 0
            lh=findMax(node.left)
            rh=findMax(node.right)
            self.maxi=max(self.maxi,rh+lh)
            return max(rh,lh)+1
        self.maxi=0
        findMax(root)
        return self.maxi