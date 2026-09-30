# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        visited, queue = set(), deque()
        queue.append(root)

        while queue:
            subArray = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                subArray.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(subArray)
        return res
            







