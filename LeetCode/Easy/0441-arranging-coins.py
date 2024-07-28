# 문제
# n 개의 코인으로 계단을 만들려고 함
# 계단은 k 개의 행으로 구성되며, i 번째 행은 i 개의 코인만 가질 수 있음
# 마지막 행은 완전하지 않을 수 있음
# 만들어진 계단의 완전한 행의 수를 반환



class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1