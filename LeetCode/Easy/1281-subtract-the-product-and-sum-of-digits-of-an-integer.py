# 문제
# 정수 n 이 주어짐
# 자릿수들의 곱과 합의 차를 반환


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sums = 0

        # int to str, str to int
        # for s in str(n):
        #    product *= int(s)
        #    sums += int(s)
        # return product - sums

        # 10으로 나눈 나머지로 자릿수 구하기
        while n != 0:
            last = n % 10 # 반복할수록 1의 자리부터 가장 큰 자릿수까지 구해짐
            product *= last
            sums += last
            n = n // 10 # 현재보다 큰 자릿수를 구하기 위해 10을 나눈 몫으로 업데이트
        return product - sums