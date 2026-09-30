class TrieNode:
    def __init__(self):
        self.children = {}
        self.isTheEnd = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isTheEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or board[r][c] not in node.children or (r, c) in visited):
                return None

            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isTheEnd:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie, "")

        return list(res)










