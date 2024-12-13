# 문제
# 주어진 배열 nums 의 각 요소를 자릿수의 합으로 바꿔야 함
# 바뀐 요소 중 가장 작은 요소를 반환

# 풀이
# 각 요소를 문자열로 바꿔 합을 구함


class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = []
        for n in nums:
            digits = [int(i) for i in str(n)]
            result.append(sum(digits))
        return min(result)