# 문제
# 정수 배열 nums 가 주어짐
# 짝수인 경우 배열의 앞으로 옮겨야 함

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
                continue
            
            if nums[right] % 2 != 0:
                right -= 1
                continue
            
            # left 에 있는 수가 홀수이고 right 에 있는 수가 짝수인 경우
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums