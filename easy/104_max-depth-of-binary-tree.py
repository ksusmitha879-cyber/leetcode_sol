from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # type: ignore
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return max(left,right)+1