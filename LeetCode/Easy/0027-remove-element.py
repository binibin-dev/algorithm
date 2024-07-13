# val 을 배열 nums 에서 삭제하고, 남은 개수를 반환

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)