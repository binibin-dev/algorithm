# 문제
# 상대방이 1부터 n 사이에서 숫자를 고름
# 고른 숫자가 어떤 숫자인지 맞춰야 함
# 유추한 숫자가 고른 숫자보다 크면 1, 작으면 -1, 같으면 0을 반환하는 API guess 가 제공됨

# 풀이
# 이진 탐색으로 해결
# guess(mid) 가 1 이면 mid 보다 큰 값이므로 left 를 조정
# guess(mid) 가 -1 이면 mid 보다 작은 값이므로 right 를 조정
# guess(mid) 가 0 이면 mid 와 값이 같으므로 mid 를 반환

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            g = guess(mid)
            if g == 1: # mid 보다 큼
                left = mid + 1
            elif g == -1: # mid 보다 작음
                right = mid
            else:
                return mid
        
        return right