# 문제
# road trip 서로 다른 고도에 있는 n + 1 개의 지점으로 구성되어 있음
# 바이커는 고도가 0인 포인트 0에서 여행을 시작함
# 크기가 n 인 정수 배열 gain 이 주어짐
# gain[i] 는 지점 i 와 i+1 사이의 고도에서의 순 변화량 (0 <= i < n)
# 가장 높은 고도를 반환

# 문제
# gain 을 순서대로 확인하면서
# 1. 현재 위치를 계산
# 2. 가장 높은 고도를 현재 위치와 비교하여 더 큰 값으로 업데이트


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = current
        for i in range(len(gain)):
            current += gain[i]
            highest = max(highest, current)
        return highest