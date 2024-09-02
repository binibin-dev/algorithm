# 문제
# 정수 배열 nums 가 주어짐
# 반환할 배열을 answer 라고 하면
# answer.length == nums.length
# answer[i] = |leftSum[i] - rightSum[i]|
# leftSum[i] 는 i 의 왼쪽에 있는 요소의 합이며, 왼쪽에 요소가 없는 경우 0
# rightSum[i] 는 i 의 오른쪽에 있는 요소의 합이며, 왼쪽에 요소가 없는 경우 0

# 풀이
# nums 에서 인덱스 i 의 왼쪽이란 nums [0:i]
# nums 에서 인덱스 i 의 오른쪽이란 nums [i+1:]


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(abs(sum(nums[0:i]) - sum(nums[i+1:])))
        return answer