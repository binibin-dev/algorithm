# 문제
# 정수 k 가 주어지며 i 가 j 보다 크면서
# 두 인덱스에 있는 값의 절대 차가 k 와 같은 (i, j) 쌍의 개수를 반환

# 풀이
# |nums[i] - nums[j]| == k 는 |nums[j] - nums[i]| == k 와 같은 의미이다.
# 즉, nums[i] - nums[j] == k 또는 nums[j] - nums[i] == -k
# 즉, nums[i] -  k == nums[j] 또는 nums[j] + k == nums[i]


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        cnt = 0
        for n in nums:
            cnt += d[n-k] + d[n+k]
            d[n] += 1
        return cnt