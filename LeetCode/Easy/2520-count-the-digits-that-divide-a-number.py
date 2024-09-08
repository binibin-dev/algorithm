# 문제
# 정수 num 이 주어짐
# num 을 나눌 수 있는 num 의 자릿수의 개수를 반환
# 나눌 수 있다는 것은 나눠서 나머지가 0이 된다는 의미


class Solution:
    def countDigits(self, num: int) -> int:
        digits = [num % int(d) == 0 for d in str(num)]
        return sum(digits)