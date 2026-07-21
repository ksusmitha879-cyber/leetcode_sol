
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: # type: ignore
        self.maxPathSum=float("-inf")
        def solve(root):
            if not root:
                return 0
            left=max(0,solve(root.left))
            right=max(0,solve(root.right))
            self.maxPathSum=max(self.maxPathSum,left+right+root.val)        
            return max(left,right)+root.val
        solve(root)
        return self.maxPathSum