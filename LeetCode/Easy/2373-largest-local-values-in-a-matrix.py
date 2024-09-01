# 문제
# n x n 크기의 배열 grid 가 주어짐
# (n-2) x (n-2) 크기의 정수 배열 maxLocal 을 만들어야 함
# maxLocal[i][j] 요소는 grid 의 i+1 행과 j+1 열을 중심으로 한 3 x 3 크기의 배열에서 가장 큰 값

# 문제
# maxLocal[i][j] 은 grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+1][j:j+3] 중 가장 큰 값


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(max(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]))
            result.append(row)
        return result