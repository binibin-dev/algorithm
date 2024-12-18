# 문제
# 주어진 정수 n 이 4의 거듭 제곱이면 True, 아니면 False 를 반환

# 풀이
# n 이 1이거나 4로 나눈 나머지가 0이면 True


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4
        return True