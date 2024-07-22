# 문제
# 정수 rowIndex 가 주어졌을 때 파스칼의 삼각형의 rowIndex 번째 행을 반환
# 인덱스는 0부터 시작

# 풀이
# 한 행에는 행의 인덱스 + 1 개수만큼의 요소가 있음
# 한 행의 맨 앞이나 맨 뒤는 1임
# 현재 위치를 i행 j 열이라고 했을 때 중간에 있는 요소는 i-1행 j-1열 요소와 i-1행 j열 요소를 더한 값


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i-1][j-1] + result[i-1][j])
            result.append(row)
        return result[-1]