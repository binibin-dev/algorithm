# 문제
# 주어진 정수가 한 자리 수가 될 때까지 각 자리 수를 모두 더하는 과정을 반복

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = str(num)
            num = sum(map(int, num))
        return num