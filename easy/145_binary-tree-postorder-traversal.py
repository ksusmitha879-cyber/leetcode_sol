class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]: # type: ignore
        def Tree(root,result):
            if root!=None:
                
                Tree(root.left,result)
                Tree(root.right,result)
                result.append(root.val)
        result=[]
        Tree(root,result)
        return result