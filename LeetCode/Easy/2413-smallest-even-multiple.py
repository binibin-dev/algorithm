# 문제
# 양의 점수 n이 주어지면 2와 n 의 곱 중 가장 작은 수(최소공배수)를 반환

# 풀이
# a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), 
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 나머지가 0이 될 때까지 위의 과정을 반복하고 나누는 수가 최대공약수가 됨

# 최소공배수는 두 수의 곱을 최대공약수로 나눈 몫

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        a, b = 2, n
        while b > 0:
            a, b = b, a % b
        
        # a 는 최대공약수
        return 2 * n // a