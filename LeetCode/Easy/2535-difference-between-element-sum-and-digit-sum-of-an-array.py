# 문제
# 양의 정수 배열 nums 가 주어짐
# element sum 은 nums 의 모든 요소의 합
# digit sum 은 nums 에서 나타나는 모든 자릿수의 합
# element sum 과 digit sum 의 절대차를 반환


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ds = 0
        for n in nums:
            ds += sum([int(c) for c in str(n)])
        return abs(sum(nums) - ds)