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
        q = deque()
        q.append(root)

        while q:
            sub_array = []
            for i in range(len(q)):
                num = q.popleft()
                sub_array.append(num.val)

                if num.left:
                    q.append(num.left)
                if num.right:
                    q.append(num.right)

            res.append(sub_array)
        return res








