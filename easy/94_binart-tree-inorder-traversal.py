class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def Tree(root,result):
            if root!=None:
                Tree(root.left,result)
                result.append(root.val)
                Tree(root.right,result)
        result=[]
        Tree(root,result)
        return result