# 문제
# 정수 배열 nums 가 주어짐
# 짝수인 경우 배열의 앞으로 옮겨야 함

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        return even + odd