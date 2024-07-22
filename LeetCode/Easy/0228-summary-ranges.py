# 문제
# 중복이 없고 정렬된 정수 배열 nums 가 주어짐
# 배열에 있는 모든 숫자를 다루는 범위를 반환해야 함
# range [a, b] 는 a 에서부터 b 까지의 모든 숫자의 집합
# nums 의 요소는 하나의 범위에만 포함되어야 함!!!!!
# range 에 포함되지만 nums 에는 포함되지 않는 정수는 없음

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        start = nums[0]
        for i in range(1, len(nums)):
            # if nums[i] != nums[i - 1] + 1:
            if nums[i] - nums[i - 1] != 1: # 범위가 끊겨야 하는 경우
                if start == nums[i - 1]: # 범위에 숫자 하나만 들어가는 경우
                    result.append(str(start))
                else: # 범위에 숫자가 하나 이상 들어가는 경우
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i] # start 업데이트
        if start == nums[-1]: # 배열의 마지막의 숫자 처리 (범위에 숫자 하나만 들어가는 경우)
            result.append(str(start))
        else: # 배열의 마지막의 숫자 처리 (범위에 숫자가 하나 이상 들어가는 경우)
            result.append(f"{start}->{nums[-1]}")
        return result