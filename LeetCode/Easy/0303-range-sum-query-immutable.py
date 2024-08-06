# 문제
# 정수 배열 nums 과 그에 대한 쿼리를 처리


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # return sum([self.nums[i] for i in range(left, right+1)])
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)