class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        def Tree(root,result):
            if root!=None:
                result.append(root.val)
                Tree(root.left,result)
                Tree(root.right,result)
        result=[]
        Tree(root,result)
        return result