# 문제
# 양의 정수 n 과 m 이 주어짐, num1 와 num2 를 정의하여 차를 반환
# num1: 1 부터 n 사이에 있는 m 으로 나눠지지 않는 정수의 합
# num2: 1 부터 n 사이에 있는 m 으로 나눌 수 있는 정수의 합

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0

        for i in range(1, n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        
        return num1 - num2