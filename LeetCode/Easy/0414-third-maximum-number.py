# 문제
# 주어진 nums 에서 세 번째로 큰 값을 구해야 함 (중복 제외)
# 세 번째로 큰 값이 없다면 가장 큰 값을 반환

# 풀이
# nums 에서 중복을 제거하여 순서대로 정렬
# 정렬된 상태에서 세 번째 요소를 반환

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)), reverse=True)
        return sorted_nums[2] if len(sorted_nums) >= 3 else sorted_nums[0]