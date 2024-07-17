# 문제
# 정수로 이루어진 배열 nums 에서 각 요소는 두 번씩 나타나고 단 하나만 한번 나옴
# 하나만 나오는 요소를 반환
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# xor 성질
# a (XOR) 0 = a
# a (XOR) a = 0
# a (XOR) b = b (XOR) a

# 즉, 서로 같은 값끼리 xor 연산 하면 0이 됨
# 한 원소 말고는 모두 두 번씩 나오므로, 결국 남게 되는 것은 하나만 있는 원소가 될 것임.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num # 0 (XOR) N = N
        return res