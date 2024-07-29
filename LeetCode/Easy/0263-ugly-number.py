# 문제
# 소인수가 2, 3, 5 로 구성된 ugly number 라면 True 를 반환

# 풀이
# 소인수란 약수 중 소수인 수를 말함

class Solution:
    def isUgly(self, n: int) -> bool:
        for i in range(2, n):
            if n % i == 0 and i not in [2, 3, 5]:
                return False
        return True