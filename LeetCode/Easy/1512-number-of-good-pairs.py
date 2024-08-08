# 문제
# 정수 배열 nums 가 주어지며 good pair 의 개수를 반환
# good pair 란 nums[i] == nums[j] and i < j 인 (i, j) 쌍을 말함


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
        return cnt