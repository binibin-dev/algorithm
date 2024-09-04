# 문제
# 정수 배열 nums 와 정수 k 가 주어짐
# 한 번의 연산에서는 nums 에서 가장 작은 요소 하나를 제거할 수 있음
# 연산 후 모든 요소가 k 보다 크거나 같아지는 가장 적은 연산 횟수

# 풀이
# nums 를 한번씩 돌면서
# nums 에서 가장 작은 값을 제거, count 1 증가

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for n in nums:
            if n < k:
                count += 1
        return count