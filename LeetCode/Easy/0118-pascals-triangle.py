class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = []
            for j in range(i+1): # 열의 길이는 행 인덱스 + 1
                if j == 0 or j == i: # 끝에 있는 경우
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j]) # 이전 행의 이전열 값과 이전 행의 같은 열을 더함
            result.append(row)

        return result