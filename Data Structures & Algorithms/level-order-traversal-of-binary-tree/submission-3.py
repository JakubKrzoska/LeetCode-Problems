# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        level = []
        level.append([root.val])

        q = deque()
        q.appendleft(root)

        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    curr.append(node.left.val)
                    q.append(node.left)
                
                if node.right:
                    curr.append(node.right.val)
                    q.append(node.right)

            if len(curr):   level.append(curr)

         
        return level
