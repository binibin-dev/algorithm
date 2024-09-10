# 문제
# 일정하게 증가하는 정수 배열 nums 와 양의 정수 diff 가 주어짐
# (i, j, k) 는 아래의 조건을 만족하면 arithmetic triplet 이라고 함
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# 유일한 arithmetic triplet 의 개수를 반환

# 풀이
# 어떤 요소가 n 이라면, nums 에 n+diff 와 n+diff*2 가 존재하면
# (n, n+diff, n+diff*2) 즉, arithmetic triplet 이 존재함
# 이렇게 할 수 있는 이유는 nums 내에 중복된 요소가 없고 수가 일정하게 증가하기 때문


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        return sum(n+diff in nums and n+diff*2 in nums for n in nums)