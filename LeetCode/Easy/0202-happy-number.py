# 문제
# happy number 여부를 반환해야 함. happy number 의 조건은 다음과 같음
# 양의 정수로 시작하면 그 자리수의 제곱의 합으로 대체 (12 + 92 = 82)
# 위의 과정을 반복하여 1이 되는 숫자가 happy number
# **happy number 가 아니라면 끝없이 반복될 것임**

# 풀이
# happy number 는 1, happy number 가 아니면 이전에 계산했던 값들이 반복하여 나오게 됨
# 따라서 결과가 1 또는 이전에 계산했던 값이 나오게 되면 반복문을 멈추고 happy number 여부를 반환

class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        numbers = []

        while True:
            num = sum([int(c)**2 for c in str(num)])
            if num in numbers:
                return False
            else:
                if num == 1:
                    return True
                else:
                    numbers.append(num)

        return False