# 문제
# 정수 배열 nums 가 주어짐
# 짝수인 경우 배열의 앞으로 옮겨야 함

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: (0, x) if x % 2 == 0 else (1, x))
        return nums