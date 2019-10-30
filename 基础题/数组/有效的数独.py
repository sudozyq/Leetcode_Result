class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def search(self, row_start, row_end, col_start, col_end):
            nums = set()
            for i in range(row_start, row_end):
                for j in range(col_start, col_end):
                    if board[i][j] in nums:
                        return False
                    if board[i][j] != '.':
                        nums.add(board[i][j])

            return True

        for i in range(len(board)):
            nums = set()
            for j in range(len(board[i])):
                if board[i][j] in nums:
                    return False
                if board[i][j] != '.':
                    nums.add(board[i][j])

        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] in nums:
                    return False
                if board[j][i] != '.':
                    nums.add(board[j][i])

        if search(self, 0, 3, 0, 3) == False or \
           search(self, 0, 3, 3, 6) == False or \
           search(self, 0, 3, 6, 9) == False or \
           search(self, 3, 6, 0, 3) == False or \
           search(self, 3, 6, 3, 6) == False or \
           search(self, 3, 6, 6, 9) == False or \
           search(self, 6, 9, 0, 3) == False or \
           search(self, 6, 9, 3, 6) == False or \
           search(self, 6, 9, 6, 9) == False:
            return False

        return True

