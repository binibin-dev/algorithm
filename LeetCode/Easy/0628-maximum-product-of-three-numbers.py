# 문제
# 배열의 세 개의 수를 곱하여 나오는 가장 큰 값을 반환

# 풀이
# 내림차순으로 정렬하여 순서대로 3 개의 값을 곱함
# 음수가 포함된 경우 주의!!
# 가장 큰 값 순서대로 곱한 것과 가장 작은 값 순서대로 곱한 것 중 큰 값을 반환
# 음수끼리 곱해져 양수가 되어 더 커지는 경우도 있기 때문

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        return max(nums[0]*nums[1]*nums[2], nums[-2]*nums[-1]*nums[0])