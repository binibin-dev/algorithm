# 문제
# m x n 크기의 정수 배열 accounts 가 주어짐
# accounts[i][j] 는 i 번째 고객의 j 번째 은행에 가지고 있는 돈의 양

# 풀이
# accounts[i] 의 요소들을 모두 더하면 i 번째 고객의 총 잔고가 됨

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(n) for n in accounts])