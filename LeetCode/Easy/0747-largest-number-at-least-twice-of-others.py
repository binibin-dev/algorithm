# 문제
# 가장 큰 수가 유일한 정수 배열 nums 가 주어짐
# 배열에서 가장 큰 수가 배열의 다른 모든 수보다 적어도 두 배 이상인지 확인
# 맞다면 가장 큰 수의 인덱스를 반환, 아니라면 -1 을 반환

# hint
# Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`.
# Scan through the array again.
# If we find some `x != m` with `m < 2*x`, we should return `-1`. Otherwise, we should return `maxIndex`.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        for i in range(len(nums)):
            if nums[i] == m:
                maxIndex = i
                continue
            if nums[i]*2 > m:
                return -1
        return maxIndex