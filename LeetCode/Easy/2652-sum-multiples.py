# 문제
# 양의 정수 n 이 주어짐
# [1, n] 범위에 있는 수 중 3, 5 또는 7로 나눠지는 모든 정수의 합을 반환


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                result += i
        return result