# 문제
# 정수 num 과 t 가 주어짐
# 아래의 두 연산을 거치면 num 이 될 수 있는 수를 archievable 하다고 함.
# 1만큼 더하거나 빼면서 동시에 num 을 1만큼 더하거나 뺌
# 최대 t 번의 연산을 거쳐 나올 수 있는 가장 큰 archievable number 를 반환

# 풀이
# **maximum** archievable number 를 구해야 함
# 따라서 x 는 num 에서부터 시작
# x 는 t 번 감소 하고, num 은 t 번 증가 해야 함
# 즉, x 는 num 보다 t*2 만큼 큼 (x 는 num + t*2)


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t*2