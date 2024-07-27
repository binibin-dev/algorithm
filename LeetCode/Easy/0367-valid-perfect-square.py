# 문제
# 주어진 양의 정수가 완전 제곱인지 여부를 반환
# 완전 제곱이란 어떤 정수의 제곱으로 표현될 수 있는 수

# 풀이
# 1부터 num 까지의 정수 배열을 만듦
# 


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True

        left, right = 1, num

        while left < right:
            mid = (left + right) // 2
            if mid*mid < num: # 오른쪽 범위를 탐색해야 함
                left = mid + 1
            elif mid*mid > num: # 왼쪽 범위를 탐색해야 함
                right = mid
            else:
                return True
        
        return False