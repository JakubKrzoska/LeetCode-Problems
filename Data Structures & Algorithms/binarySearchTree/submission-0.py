class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        curr = self.root
        while True:
            if key > curr.key:
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
            elif key < curr.key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr != None:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1 

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr, key):
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderHelper(self.root, res)
        return res

    def inorderHelper(self, root, res):
        if not root:
            return None
        self.inorderHelper(root.left, res)
        res.append(root.key)
        self.inorderHelper(root.right, res)
        



