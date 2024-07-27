# 문제
# 개발 중인 product 의 이전 버전이 quality check 에 실패함
# 각 버전은 이전 저번 기반으로 만들어지고, 이전 버전이 bad 면 다음에 만들어지는 버전도 bad 가 됨
# 1 부터 시작하는 n 개의 버전이 있고, 첫 번째 bad 버전을 찾아야 함 (다른 버전이 bad 가 되는 원인이기 때문)

# 풀이
# 이진 탐색으로 bad 버전을 찾음
# 중간에 있는 버전이 bad 가 아니라면 그 왼쪽에 bad 버전이 있을 것임
# 버전이 1부터 시작하기 때문에 left 또한 1 로 초기화


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        left, right = 1, n

        while right > left:
            mid = left + (right - left) // 2
            if isBadVersion(mid): # 탐색 범위를 줄여야 함
                right = mid
            else:
                left = mid + 1

        return right