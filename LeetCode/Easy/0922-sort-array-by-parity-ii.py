# 문제
# 반은 홀수고, 반은 짝수인 정수 배열 nums 가 주어짐
# i 가 홀수이면 nums[i] 도 홀수이고, i 가 짝수이면 nums[i] 도 짝수가 되도록 정렬

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        result = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])
        return result