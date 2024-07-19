# 문제
# 2n 개의 정수로 구성된 배열 nums 가 주어짐
# 2개씩 n 개의 쌍으로 묶어야 하고, 각 쌍의 최솟값을 모두 더한 값이 최대화 되어야 함
# 합의 최대를 반환

# 풀이
# 총합이 최대가 되려면 하나의 쌍은 최대한 차이가 나지 않는 숫자끼리 묶여야 함
# 따라서 정렬 후 순서대로 묶기
# 쌍의 최솟값을 구하여 누적합을 구함

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s = 0
        for i in range(0, len(nums), 2):
            s += min(nums[i:i+1])
        return s