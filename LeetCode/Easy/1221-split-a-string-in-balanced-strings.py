# 문제
# 균형있는 문자열인 s 가 주어짐
# 균형있는 문자열이란 문자 L 과 R 의 양이 같은 문자열을 말함
# 주어진 s 에서 문자열을 균형있는 문자열이 되도록 분리
# 분리하여 만들어지는 균형있는 문자열의 최대 개수를 반환

# 풀이
# L 과 R 이 같은 횟수만큼 나왔는지 확인하기 위해 balanced 변수를 사용
# s 의 문자를 순서대로 확인하면서
# 1. L 이 나올 때마다 balanced 를 1 증가, R 이라면 1 감소
# 2. balanced 가 0이 되었다면 L 과 R 이 같은 횟수만큼 나온 것이므로 count 를 1 증가 


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced, count = 0, 0
        for c in s:
            balanced += 1 if c == 'L' else -1
            if balanced == 0: count += 1 # 균형있는 문자열이 만들어진 경우
        return count