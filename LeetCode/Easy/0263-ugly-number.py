# 문제
# 소인수가 2, 3, 5 로 구성된 ugly number 라면 True 를 반환

# 풀이
# 소인수란 약수 중 소수인 수를 말함
# 약수는 어떤 수로 나눴을 때 나머지가 0, 소수는 2 이상의 수로 나눠지지 않음
# 정수 n 의 모든 약수는 쌍을 이루며, 약수 쌍 중 하나는 반드시 루트 n 보다 작음
# 

# 에라토스테네의 체
# 1. 2부터 n까지 존재하는 모든 자연수를 나열
# 2. 가장 작은 수를 x 로 지정
# 3. x 의 배수를 모두 제거 (x는 그대로 둠)
# 4. 2와 3을 반복

import math

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: 
            return False
        for i in [2,3,5]:
            while n % i == 0:
                n = n // i
        return n == 1 # 2, 3, 5 만으로 나눠져 1이 되면 True