# 문제
# 네 자리수 양의 정수 num 이 주어짐
# num 의 자리수를 사용하여 두 개의 정수로 분할
# 분할된 두 정수의 가장 작은 합을 반환

# 풀이
# num 을 문자열로 변환하여 정렬
# 가장 작은 두 수를 두 정수의 10의 자리수,
# 가장 큰 두 수를 두 정수의 1의 자리수가 되도록 함


class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        return int(s[0] + s[2]) + int(s[1] + s[3])
        