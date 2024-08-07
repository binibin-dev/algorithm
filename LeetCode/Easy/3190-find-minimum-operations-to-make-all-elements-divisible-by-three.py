# 문제
# 정수 배열 nums 가 주어짐
# 한 번의 연산마다 nums 의 요소 하나에 1을 더하거나 뺄 수 있음
# 모든 요소가 3으로 나눠지도록 하는 가장 적은 연산 횟수를 반환

# 풀이
# 모든 수는 3으로 나눈 나머지가 0, 1, 2 중 하나임
# 나머지가 0인 경우 3으로 나눠지므로 연산 불필요
# 최대한 적게 연산하려면 나머지가 1인 경우 1을 빼고, 2인 경우 1을 더하여 3의 배수로 만들어야 함

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for n in nums:
            r = n % 3
            if r == 1 or r == 2:
                cnt += 1
        return cnt