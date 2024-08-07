# 문제
# 정수 배열 nums 가 주어짐
# ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n 인 새로운 배열을 만들어야 함

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2