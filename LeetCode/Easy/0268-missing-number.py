# 문제
# 0에서 n 까지의 범위에 있는 n 개의 수가 포함된 nums 가 주어짐
# 이 범위에서 빠져있는 하나의 숫자를 반환

# 풀이
# nums 의 길이가 nums 에서 나올 수 있는 가장 큰 값임
# 0부터 n-1까지 반복하고 만약 nums 에 포함되지 않는 수가 있으면 해당 수를 반환
# 만약 0부터 n-1까지가 nums 에 모두 있다면, 0에서 n사이에서 포함되지 않는 값은 n임!!!

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_value = len(nums)
        for i in range(max_value):
            if i not in nums:
                return i
        return max_value