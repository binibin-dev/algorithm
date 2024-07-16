# 문제
# array 에서 과반수[사이즈/2]를 차지하는 요소를 반환
# 배열에 항상 과반수를 차지하고 있는 요소가 존재한다고 가정한다.

# 풀이
# 요소의 개수를 카운팅하여 nums 의 절반길이보다 크면 return

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {n: 0 for n in nums}
        half = len(nums)//2

        for n in nums:
            d[n] += 1
            if d[n] > half:
                return n