class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: # type: ignore
        def isValid(node,minVal,maxVal):
            if not node:
                return True
            if node.val<=minVal or node.val>=maxVal:
                return False
            return isValid(node.left,minVal,node.val) and isValid(node.right,node.val,maxVal)
        return isValid(root,float('-inf'),float('inf'))