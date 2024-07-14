# 문자
# 두 배열의 교잡합을 반환
# 순서는 상관 없음

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)