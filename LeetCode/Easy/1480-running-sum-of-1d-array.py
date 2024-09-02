# 문제
# 배열 nums 가 주어짐
# runningSum[i] = sum(nums[0]…nums[i])
# nums 의 running sum 을 반환

# 풀이
# result 는 [0] 으로 초기화
# result 의 가장 마지막 값과 nums[i] 를 더하는 과정을 반복
# 초기값을 제외하기 위해 result[1:] 을 반환


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0]
        for n in nums:
            result.append(result[-1] + n)
        return result[1:]