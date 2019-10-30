class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return

        if n % 2 == 0:
            row = n / 2
            col = n / 2
        else:
            row = n / 2
            col = n / 2 + 1

        for i in range(row):
            for j in range(col):
                x1 = i
                y1 = j
                for k in range(3):
                    x2 = n - 1 - y1
                    y2 = x1

                    matrix[x1][y1] = matrix[x1][y1] ^ matrix[x2][y2]
                    matrix[x2][y2] = matrix[x1][y1] ^ matrix[x2][y2]
                    matrix[x1][y1] = matrix[x1][y1] ^ matrix[x2][y2]

                    x1 = x2
                    y1 = y2

