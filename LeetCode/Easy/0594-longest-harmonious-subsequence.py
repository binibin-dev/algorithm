# 문제
# subsequence 는 순서를 바꾸지 않고 0개 이상의 값을 삭제해서 얻을 수 있는 sequence
# harmonious array 는 큰 값과 작은 값의 차이가 정확히 1인 배열을 의미
# 만들어질 수 있는 harmonious subsequnece 중 가장 긴 길이를 반환

# 풀이
# 각 수가 나온 횟수를 카운팅
# 딕셔너리의 키 순서대로 k와 k+1의 각 카운트 갯수를 더하고, 이 값이 가장 큰 경우 반환

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for i, n in enumerate(nums):
            d[n] = d.get(n, 0) + 1

        max_length = 0
        for k in d:
            if k + 1 in d:
                current_length = d[k] + d[k+1]
                max_length = max(max_length, current_length)
        return max_length