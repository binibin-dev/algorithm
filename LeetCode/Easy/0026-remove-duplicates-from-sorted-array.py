# 오름차순으로 정렬된 nums 가 주어짐
# 각 요소는 중복되지 않고 한 번만 나타나도록 하여 유일한 요소의 개수를 반환

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)