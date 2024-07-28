# 문제
# 정수가 오름차순으로 정렬된 배열 nums 와 정수 target 이 주어짐
# nums 에서 target 이 존재한다면 인덱스, 없다면 -1 을 반환
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1