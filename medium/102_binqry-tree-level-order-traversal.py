class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # type: ignore
        if not root:
            return []
        res=[]
        queue=deque([root]) # type: ignore
        while queue:
            level_size=len(queue)
            current_level=[]
            for _ in range(level_size):
                node=queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(current_level)
        return res