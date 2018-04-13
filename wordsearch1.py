class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if(self.dfs(board, word, i, j)):
                    return True
        return False
    
    def dfs(self, board, word, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >=len(board[0]):
            return False
        if word[0] == board[i][j]:
            tmp = board[i][j]
            board[i][j] = "*"
            #print(mt)
            word = word[1:]    
            if word:
                if self.dfs(board, word, i+1, j) or self.dfs(board, word, i-1, j) or self.dfs(board, word, i, j+1) or self.dfs(board, word, i, j-1):
                    return True
            else:
                return True
            board[i][j] = tmp
        else:
            return False
