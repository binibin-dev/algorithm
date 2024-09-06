# 문제
# run-length encoding 으로 압축된 리스트를 나타내는 정수 배열 nums 가 주어짐
# 각 인접된 요소들의 쌍은 [freq, val] = [nums[2*i], nums[2*i+1]] 라고 가정
# 그러한 각 쌍에 대해 val 값을 가지는 freq 개의 요소가 있음
# 만들어진 서브 리스트를 모두 합하여 압축이 해제된 리스트를 반환

# 풀이
# 두 쌍이 [freq, val] 이라면 압축을 해제할 때는 val 이 freq 개 있는 리스트를 만들면 됨


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)-1, 2):
            freq, val = nums[i], nums[i+1]
            result.extend([val] * freq)
        return result