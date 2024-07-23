# 문제
# n개의 계단을 오르는 방법의 개수를 반환 (n 은 1 이상, 45 이하)
# 한번에 1개 또는 2개의 계단을 오를 수 있음
# 계단을 오르는 방법의 개수를 반환

# 풀이
# n 만큼 반복하면서 2 스텝 전의 값(a)과 이전 스텝의 값(b)을 더해서 c 에 넣음
# a에 이전 값(b), b에 현재 값(c) 를 업데이트

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 0, 1, 0
        
        for i in range(n):
            c = a + b
            a, b = b, c
        
        return b