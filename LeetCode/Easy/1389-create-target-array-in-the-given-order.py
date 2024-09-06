# 문제
# 정수 배열 nums 와 index 가 주어짐
# 아래의 규칙을 만족하는 array 를 반환해야 함
# 1. target array 를 초기화
# 2. nums[i] 의 인덱스 index[i] 에 nums[i] 를 삽입


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target