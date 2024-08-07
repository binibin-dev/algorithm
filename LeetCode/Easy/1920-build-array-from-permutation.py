# 문제
# 순열 nums 가 주어짐
# nums 는 0부터 (nums 의 길이 - 1) 사이에 있는 유일한 정수로 구성됨
# ans[i] = nums[nums[i]] 가 되도록 nums 와 동일한 길이의 배열을 반환

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans