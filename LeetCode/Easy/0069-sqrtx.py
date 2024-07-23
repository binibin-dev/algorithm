# 문제
# 음수가 아닌 정수 x 가 주어짐
# 가까운 정수로 반올림한 x 의 제곱근을 구해야 함
# python 의 경우 x ** 0.5 를 사용하지 않을 것

# 풀이
# 이진탐색을 활용
# left 가 right 보다 작거나 같을 때까지만 반복
# mid 의 제곱이 x 와 같으면 mid 를 반환
# mid 의 제곱이 x 보다 크면 구해야 하는 값이 mid 의 왼쪽에 있다는 의미이므로 right=mid-1
# mid 의 제곱이 x 보다 작으면 구해야 하는 값이 mid 의 오른쪽에 있다는 의미이므로 left=mid-1

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left+right) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right