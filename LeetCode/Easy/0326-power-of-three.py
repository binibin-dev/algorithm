# 문제
# 주어진 정수 n 이 3의 거듭제곱이라면 True, 아니라면 False 를 반환

# 풀이
# 양의 정수인 경우 3으로 반복해서 나눔
# 3으로 나눈 나머지가 0이 아닌 순간이 발생한다면 False

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True