class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        sum = 0
        for i in range(n):
            for j in range(n):
                if i == j or j == n - 1 - i:
                    sum += mat[i][j]

        return sum