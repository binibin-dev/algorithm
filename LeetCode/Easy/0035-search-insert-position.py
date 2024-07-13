# 문제
# 순서대로 정렬된 리스트에 target 이 들어갈 위치를 구함

# 풀이
# 이진탐색으로 범위를 좁히면서 비교
# target 과 중간값을 비교하여 target 이 크면 l 을, target 이 작으면 r 을 업데이트
# 위의 과정을 l 이 r 보다 커질 때까지(비교할 값이 없을 때까지) 반복

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l